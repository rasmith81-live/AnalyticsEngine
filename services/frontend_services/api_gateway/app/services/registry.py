"""
Service registry for the API Gateway service.
Manages the registry of downstream services and their configurations.
"""
from typing import Dict, Any, Optional, List
import httpx
import asyncio
from pydantic import BaseModel, Field
from datetime import datetime

from app.core.config import settings
from app.core.logging import get_logger
from app.core.cache import CacheService

logger = get_logger(__name__)

class ServiceInfo(BaseModel):
    """Service information model using Pydantic v2."""
    name: str = Field(..., description="Service name")
    url: str = Field(..., description="Service base URL")
    timeout: float = Field(30.0, description="Request timeout in seconds")
    health_endpoint: str = Field("/health", description="Health check endpoint")
    is_active: bool = Field(True, description="Whether the service is active")
    last_health_check: Optional[datetime] = Field(None, description="Last health check timestamp")
    health_status: Optional[bool] = Field(None, description="Last health check status")

class ServiceRegistry:
    """
    Service registry that manages the configuration and health of downstream services.
    Uses Redis for caching service information across instances.
    """
    
    def __init__(self):
        """Initialize the service registry."""
        self._services: Dict[str, ServiceInfo] = {}
        self._initialize_from_config()
    
    def _initialize_from_config(self) -> None:
        """Initialize services from configuration."""
        for name, config in settings.SERVICE_REGISTRY.items():
            # Convert hyphenated service names to underscore format for consistency
            normalized_name = name.replace("-", "_")
            
            self._services[normalized_name] = ServiceInfo(
                name=normalized_name,
                url=config["url"],
                timeout=config.get("timeout", 30.0),
                health_endpoint=config.get("health_endpoint", "/health"),
                is_active=True
            )
            
            logger.info(f"Registered service: {normalized_name} at {config['url']}")
    
    async def get_service(self, name: str) -> Optional[ServiceInfo]:
        """
        Get service information by name.
        
        Args:
            name: Service name
            
        Returns:
            Service information or None if not found
        """
        # First check cache
        cache_key = f"service_registry:{name}"
        cached_service = await CacheService.get(cache_key)
        if cached_service:
            return ServiceInfo(**cached_service)
        
        # Convert hyphenated service names to underscore format
        normalized_name = name.replace("-", "_")
        
        # Get from registry
        service = self._services.get(normalized_name)
        
        # Cache if found
        if service:
            await CacheService.set(cache_key, service.model_dump(mode='json'), 300)  # Cache for 5 minutes
            
        return service
    
    async def get_all_services(self) -> List[ServiceInfo]:
        """
        Get all registered services.
        
        Returns:
            List of all service information
        """
        return list(self._services.values())
    
    async def register_service(self, service: ServiceInfo) -> None:
        """
        Register a new service or update an existing one.
        
        Args:
            service: Service information
        """
        # Convert hyphenated service names to underscore format
        normalized_name = service.name.replace("-", "_")
        service.name = normalized_name
        
        self._services[normalized_name] = service
        
        # Update cache
        cache_key = f"service_registry:{normalized_name}"
        await CacheService.set(cache_key, service.model_dump(), 300)
        
        logger.info(f"Service {normalized_name} registered/updated")
    
    async def deregister_service(self, name: str) -> bool:
        """
        Deregister a service.
        
        Args:
            name: Service name
            
        Returns:
            True if service was deregistered, False otherwise
        """
        # Convert hyphenated service names to underscore format
        normalized_name = name.replace("-", "_")
        
        if normalized_name in self._services:
            del self._services[normalized_name]
            
            # Remove from cache
            cache_key = f"service_registry:{normalized_name}"
            await CacheService.delete(cache_key)
            
            logger.info(f"Service {normalized_name} deregistered")
            return True
        
        return False
    
    async def check_service_health(self, name: str) -> bool:
        """
        Check the health of a service.

        Args:
            name: Service name

        Returns:
            True if service is healthy, False otherwise
        """
        normalized_name = name.replace("-", "_")
        service = self._services.get(normalized_name)
        if not service:
            return False

        is_healthy = False
        try:
            async with httpx.AsyncClient() as client:
                health_url = f"{service.url.rstrip('/')}{service.health_endpoint}"
                response = await client.get(health_url, timeout=5.0)
                is_healthy = response.status_code == 200
        except Exception as e:
            logger.error(f"Health check failed for service {normalized_name}: {str(e)}")
        finally:
            service.last_health_check = datetime.utcnow()
            service.health_status = is_healthy
            self._services[normalized_name] = service
            cache_key = f"service_registry:{normalized_name}"
            await CacheService.set(cache_key, service.model_dump(mode='json'), 300)

        return is_healthy
    
    async def check_all_services_health(self) -> Dict[str, bool]:
        """
        Check the health of all services.
        
        Returns:
            Dictionary mapping service names to health status
        """
        tasks = [self.check_service_health(name) for name in self._services.keys()]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return {
            name: (result if not isinstance(result, Exception) else False)
            for name, result in zip(self._services.keys(), results)
        }

# Create a singleton instance
service_registry = ServiceRegistry()
