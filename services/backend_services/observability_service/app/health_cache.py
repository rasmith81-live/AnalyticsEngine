"""
Health Cache Manager for Observability Service.

Provides Redis-based caching for real-time service health status.
Services push their health data here, and the SystemMonitorPage queries
the aggregated status.
"""

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import redis.asyncio as redis

from .config import get_settings

logger = logging.getLogger(__name__)

HEALTH_CACHE_PREFIX = "health:service:"
HEALTH_CACHE_TTL = 120  # Health data expires after 2 minutes if not refreshed


class HealthCacheManager:
    """
    Manages real-time health status caching in Redis.
    
    Services push their health status periodically, and this cache
    provides fast access to aggregated health data.
    """
    
    def __init__(self):
        self._redis: Optional[redis.Redis] = None
        self._connected = False
    
    async def initialize(self) -> bool:
        """Initialize Redis connection."""
        try:
            settings = get_settings()
            self._redis = redis.from_url(
                settings.redis_url,
                encoding="utf-8",
                decode_responses=True
            )
            # Test connection
            await self._redis.ping()
            self._connected = True
            logger.info("Health cache Redis connection established")
            return True
        except Exception as e:
            logger.error(f"Failed to connect to Redis for health cache: {e}")
            self._connected = False
            return False
    
    async def close(self):
        """Close Redis connection."""
        if self._redis:
            await self._redis.close()
            self._connected = False
    
    async def update_service_health(
        self,
        service_name: str,
        status: str,
        details: Optional[Dict[str, Any]] = None,
        url: Optional[str] = None
    ) -> bool:
        """
        Update health status for a service.
        
        Args:
            service_name: Name of the service
            status: Health status ('healthy', 'unhealthy', 'degraded')
            details: Optional health details
            url: Optional service URL
            
        Returns:
            True if successful
        """
        if not self._connected or not self._redis:
            logger.warning("Redis not connected, cannot update health cache")
            return False
        
        try:
            health_data = {
                "service": service_name,
                "status": status,
                "timestamp": datetime.utcnow().isoformat(),
                "url": url or f"http://{service_name}:8000",
                "details": details or {}
            }
            
            key = f"{HEALTH_CACHE_PREFIX}{service_name}"
            await self._redis.setex(
                key,
                HEALTH_CACHE_TTL,
                json.dumps(health_data)
            )
            
            logger.debug(f"Updated health cache for {service_name}: {status}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to update health cache for {service_name}: {e}")
            return False
    
    async def get_service_health(self, service_name: str) -> Optional[Dict[str, Any]]:
        """
        Get health status for a specific service.
        
        Args:
            service_name: Name of the service
            
        Returns:
            Health data or None if not found
        """
        if not self._connected or not self._redis:
            return None
        
        try:
            key = f"{HEALTH_CACHE_PREFIX}{service_name}"
            data = await self._redis.get(key)
            
            if data:
                return json.loads(data)
            return None
            
        except Exception as e:
            logger.error(f"Failed to get health cache for {service_name}: {e}")
            return None
    
    async def get_all_services_health(self) -> List[Dict[str, Any]]:
        """
        Get health status for all services.
        
        Returns:
            List of health data for all services
        """
        if not self._connected or not self._redis:
            return []
        
        try:
            # Get all health keys
            pattern = f"{HEALTH_CACHE_PREFIX}*"
            keys = []
            async for key in self._redis.scan_iter(match=pattern):
                keys.append(key)
            
            if not keys:
                return []
            
            # Get all values
            results = []
            for key in keys:
                data = await self._redis.get(key)
                if data:
                    health_data = json.loads(data)
                    # Check if data is stale (older than TTL)
                    timestamp = datetime.fromisoformat(health_data["timestamp"])
                    age = datetime.utcnow() - timestamp
                    if age > timedelta(seconds=HEALTH_CACHE_TTL):
                        health_data["status"] = "unknown"
                        health_data["details"]["stale"] = True
                    results.append(health_data)
            
            return results
            
        except Exception as e:
            logger.error(f"Failed to get all services health: {e}")
            return []
    
    async def remove_service_health(self, service_name: str) -> bool:
        """
        Remove health status for a service.
        
        Args:
            service_name: Name of the service
            
        Returns:
            True if successful
        """
        if not self._connected or not self._redis:
            return False
        
        try:
            key = f"{HEALTH_CACHE_PREFIX}{service_name}"
            await self._redis.delete(key)
            return True
        except Exception as e:
            logger.error(f"Failed to remove health cache for {service_name}: {e}")
            return False


# Global instance
health_cache = HealthCacheManager()
