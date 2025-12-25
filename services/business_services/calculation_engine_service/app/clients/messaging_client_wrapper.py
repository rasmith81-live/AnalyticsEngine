"""
Messaging Client Wrapper for Calculation Engine Service.

Provides standardized interface to Messaging Service.
"""

import sys
from pathlib import Path
import logging
from typing import Dict, Any, Optional

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient

logger = logging.getLogger(__name__)


class MessagingClientWrapper:
    """Wrapper for MessagingClient to provide consistent interface."""
    
    def __init__(self, redis_url: str, service_name: str = "calculation_engine"):
        """
        Initialize Messaging Client Wrapper.
        
        Args:
            redis_url: Redis connection URL
            service_name: Name of this service
        """
        self.redis_url = redis_url
        self.service_name = service_name
        self.client: Optional[MessagingClient] = None
    
    async def connect(self):
        """Connect to messaging service."""
        self.client = MessagingClient(
            redis_url=self.redis_url,
            service_name=self.service_name,
            pool_size=5
        )
        await self.client.connect()
        logger.info(f"MessagingClient connected for {self.service_name}")
    
    async def publish_event(
        self,
        event_type: str,
        payload: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> bool:
        """
        Publish an event to the messaging service.
        
        Args:
            event_type: Type of event
            payload: Event payload
            correlation_id: Optional correlation ID
            
        Returns:
            Success status
        """
        if not self.client:
            logger.error("MessagingClient not connected")
            return False
        
        try:
            await self.client.publish_event(
                event_type=event_type,
                payload=payload,
                correlation_id=correlation_id
            )
            return True
        except Exception as e:
            logger.error(f"Failed to publish event: {e}")
            return False
    
    async def subscribe(self, channel: str, callback):
        """Subscribe to a channel."""
        if self.client:
            await self.client.subscribe(channel, callback)
    
    async def disconnect(self):
        """Disconnect from messaging service."""
        if self.client:
            await self.client.disconnect()
            logger.info(f"MessagingClient disconnected for {self.service_name}")
