"""
Initialize the service registry with all downstream services.
This script is run during API Gateway startup to ensure all services are registered.
"""
import asyncio
from typing import Dict, Any, List

from app.core.config import settings
from app.core.logging import get_logger
from app.services.registry import service_registry, ServiceInfo

logger = get_logger(__name__)

async def initialize_service_registry() -> List[ServiceInfo]:
    """
    Initialize the service registry with all configured services.
    
    Returns:
        List of registered ServiceInfo objects
    """
    logger.info("Initializing service registry")
    
    registered_services = []
    
    # Register all services from settings
    for service_name, service_config in settings.SERVICE_REGISTRY.items():
        service_url = service_config.get("url")
        if not service_url:
            logger.warning(f"Skipping registration for service '{service_name}' as its URL is not configured.")
            continue

        # Create ServiceInfo object
        service_info = ServiceInfo(
            name=service_name,
            url=service_url,
            is_active=True,  # Initially set to active, health check will update
            health_endpoint=service_config.get("health_endpoint", "/health"),
            timeout=service_config.get("timeout", 30.0)
        )
        
        # Register service
        try:
            await service_registry.register_service(service_info)
            registered_services.append(service_info)
            logger.info(f"Registered service: {service_name} at {service_info.url}")
        except Exception as e:
            logger.error(f"Failed to register service {service_name}: {str(e)}")
    
    # Check health of all services - DISABLED: Blocking startup
    # logger.info("Checking health of all registered services")
    # await service_registry.check_all_services_health()
    
    return registered_services

async def main():
    """Main function for standalone execution."""
    try:
        services = await initialize_service_registry()
        logger.info(f"Registered {len(services)} services")
        
        # Get all services with health status
        all_services = await service_registry.get_all_services()
        
        # Print service status
        for service in all_services:
            status = "ACTIVE" if service.is_active else "INACTIVE"
            logger.info(f"Service {service.name}: {status} - {service.url}")
        
    except Exception as e:
        logger.error(f"Error initializing service registry: {str(e)}")
    finally:
        # Close Redis connections
        await service_registry.close()

if __name__ == "__main__":
    asyncio.run(main())
