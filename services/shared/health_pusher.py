"""
Health Pusher Utility for Services.

Provides a background task that periodically pushes health status
to the Observability Service for centralized health monitoring.
"""

import asyncio
import logging
from typing import Dict, Any, Optional, Callable, Awaitable
import httpx

logger = logging.getLogger(__name__)

DEFAULT_PUSH_INTERVAL = 30  # seconds
DEFAULT_OBSERVABILITY_URL = "http://observability_service:8000"


class HealthPusher:
    """
    Pushes service health status to the Observability Service periodically.
    
    Usage:
        health_pusher = HealthPusher(
            service_name="my_service",
            service_url="http://my_service:8000",
            health_check_fn=my_health_check_function
        )
        await health_pusher.start()
        # ... service runs ...
        await health_pusher.stop()
    """
    
    def __init__(
        self,
        service_name: str,
        service_url: str,
        health_check_fn: Callable[[], Awaitable[Dict[str, Any]]],
        observability_url: str = DEFAULT_OBSERVABILITY_URL,
        push_interval: int = DEFAULT_PUSH_INTERVAL
    ):
        """
        Initialize the health pusher.
        
        Args:
            service_name: Name of this service
            service_url: URL of this service
            health_check_fn: Async function that returns health status dict
            observability_url: URL of the observability service
            push_interval: Interval in seconds between health pushes
        """
        self.service_name = service_name
        self.service_url = service_url
        self.health_check_fn = health_check_fn
        self.observability_url = observability_url
        self.push_interval = push_interval
        self._task: Optional[asyncio.Task] = None
        self._running = False
    
    async def start(self):
        """Start the health pusher background task."""
        if self._running:
            return
        
        self._running = True
        self._task = asyncio.create_task(self._push_loop())
        logger.info(f"Health pusher started for {self.service_name}")
    
    async def stop(self):
        """Stop the health pusher background task."""
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        logger.info(f"Health pusher stopped for {self.service_name}")
    
    async def _push_loop(self):
        """Background loop that pushes health status periodically."""
        while self._running:
            try:
                await self._push_health()
            except Exception as e:
                logger.error(f"Error pushing health status: {e}")
            
            await asyncio.sleep(self.push_interval)
    
    async def _push_health(self):
        """Push current health status to the observability service."""
        try:
            # Get current health status from the service
            health_data = await self.health_check_fn()
            
            # Determine status string
            status = health_data.get("status", "unknown")
            if isinstance(status, bool):
                status = "healthy" if status else "unhealthy"
            
            # Build payload
            payload = {
                "status": status,
                "url": self.service_url,
                "details": health_data
            }
            
            # Push to observability service
            url = f"{self.observability_url}/health/services/{self.service_name}"
            
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.post(url, json=payload)
                
                if response.status_code == 200:
                    logger.debug(f"Successfully pushed health status for {self.service_name}")
                else:
                    logger.warning(
                        f"Failed to push health status: {response.status_code} - {response.text}"
                    )
                    
        except httpx.ConnectError:
            logger.debug(f"Could not connect to observability service at {self.observability_url}")
        except Exception as e:
            logger.error(f"Error pushing health status: {e}")


async def create_health_pusher(
    service_name: str,
    service_url: str,
    health_check_fn: Callable[[], Awaitable[Dict[str, Any]]],
    observability_url: Optional[str] = None,
    push_interval: int = DEFAULT_PUSH_INTERVAL,
    auto_start: bool = True
) -> HealthPusher:
    """
    Factory function to create and optionally start a health pusher.
    
    Args:
        service_name: Name of this service
        service_url: URL of this service
        health_check_fn: Async function that returns health status dict
        observability_url: URL of the observability service (optional)
        push_interval: Interval in seconds between health pushes
        auto_start: Whether to start the pusher immediately
        
    Returns:
        HealthPusher instance
    """
    pusher = HealthPusher(
        service_name=service_name,
        service_url=service_url,
        health_check_fn=health_check_fn,
        observability_url=observability_url or DEFAULT_OBSERVABILITY_URL,
        push_interval=push_interval
    )
    
    if auto_start:
        await pusher.start()
    
    return pusher
