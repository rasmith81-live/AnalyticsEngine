"""
Health check service for the API Gateway service.
Provides health check endpoints and monitoring of downstream services.
"""
from typing import Dict, Any, List
from datetime import datetime
from pydantic import BaseModel, Field

from app.core.config import settings
from app.core.logging import get_logger
from app.services.registry import service_registry
from app.core.redis_client import redis_client_context

logger = get_logger(__name__)

class HealthStatus(BaseModel):
    """Health status model using Pydantic v2."""
    status: str = Field(..., description="Overall health status")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Health check timestamp")
    version: str = Field("1.0.0", description="API version")
    service_name: str = Field(settings.SERVICE_NAME, description="Service name")
    dependencies: Dict[str, Any] = Field(default_factory=dict, description="Dependencies health status")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional health details")

class HealthService:
    """
    Service that provides health check functionality.
    Monitors the health of the API Gateway and its dependencies.
    """
    
    @staticmethod
    async def check_redis_health() -> Dict[str, Any]:
        """
        Check Redis health.
        
        Returns:
            Health status of Redis
        """
        try:
            async with redis_client_context() as redis:
                ping_result = await redis.ping()
                return {
                    "status": "healthy" if ping_result else "unhealthy",
                    "latency_ms": 0,  # Could implement actual latency measurement
                    "details": {
                        "ping": ping_result,
                        "connection": "connected"
                    }
                }
        except Exception as e:
            logger.error(f"Redis health check failed: {str(e)}")
            return {
                "status": "unhealthy",
                "error": str(e),
                "details": {
                    "connection": "failed"
                }
            }
    
    @staticmethod
    async def check_services_health() -> Dict[str, Dict[str, Any]]:
        """
        Check the health of all downstream services.
        
        Returns:
            Health status of all services
        """
        services_health = {}
        
        # Get health status from service registry
        health_results = await service_registry.check_all_services_health()
        
        # Get all services
        services = await service_registry.get_all_services()
        
        # Format health status
        for service in services:
            is_healthy = health_results.get(service.name, False)
            services_health[service.name] = {
                "status": "healthy" if is_healthy else "unhealthy",
                "url": service.url,
                "last_check": service.last_health_check.isoformat() if service.last_health_check else None,
            }
        
        return services_health
    
    @staticmethod
    async def get_health_status(include_details: bool = False) -> HealthStatus:
        """
        Get the overall health status of the API Gateway.
        
        Args:
            include_details: Whether to include detailed health information
            
        Returns:
            Health status object
        """
        # Check Redis health
        redis_health = await HealthService.check_redis_health()
        
        # Check services health if details requested
        services_health = {}
        if include_details:
            services_health = await HealthService.check_services_health()
        
        # Determine overall status
        overall_status = "healthy"
        if redis_health["status"] != "healthy":
            overall_status = "degraded"
        
        # If any critical service is unhealthy, mark as degraded
        if services_health:
            critical_services = ["operations", "governance", "ingestion"]
            for service_name in critical_services:
                if service_name in services_health and services_health[service_name]["status"] != "healthy":
                    overall_status = "degraded"
        
        # Create health status object
        health_status = HealthStatus(
            status=overall_status,
            dependencies={
                "redis": redis_health,
                "services": services_health if include_details else {"status": "checked" if services_health else "not_checked"}
            },
            details={
                "uptime": "unknown",  # Could implement actual uptime tracking
                "memory_usage": "unknown",  # Could implement memory usage tracking
                "cpu_usage": "unknown",  # Could implement CPU usage tracking
            } if include_details else {}
        )
        
        return health_status
