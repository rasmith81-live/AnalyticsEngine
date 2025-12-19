"""
Messaging Client - HTTP client for communicating with the Messaging Service.
"""

import asyncio
import logging
from typing import Any, Dict, List, Optional, Union
import aiohttp
import json
from datetime import datetime

from .models import ItemEvent
from .telemetry_utils import inject_trace_context, trace_method, add_span_attributes

logger = logging.getLogger(__name__)


class MessagingClient:
    """HTTP client for Messaging Service communication."""
    
    def __init__(
        self,
        base_url: str,
        service_name: str = "systems_monitor",
        timeout: int = 30,
        retries: int = 3
    ):
        self.base_url = base_url.rstrip('/')
        self.service_name = service_name
        self.timeout = timeout
        self.retries = retries
        self.session: Optional[aiohttp.ClientSession] = None
        self.active_subscriptions: Dict[str, str] = {}  # pattern -> subscription_id
        
    async def initialize(self):
        """Initialize the messaging client."""
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={"Content-Type": "application/json"}
        )
        logger.info(f"Messaging client initialized for {self.base_url}")
    
    async def close(self):
        """Close the messaging client."""
        # Cancel all subscriptions
        for subscription_id in list(self.active_subscriptions.values()):
            try:
                await self.cancel_subscription(subscription_id)
            except Exception as e:
                logger.error(f"Failed to cancel subscription {subscription_id}: {e}")
        
        if self.session:
            await self.session.close()
        logger.info("Messaging client closed")
    
    @trace_method(name="messaging_client_request", kind="CLIENT")
    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Make HTTP request with retry logic."""
        if not self.session:
            raise RuntimeError("Messaging client not initialized")
        
        url = f"{self.base_url}{endpoint}"
        
        # Add span attributes for the request
        add_span_attributes({
            "messaging.system": "http",
            "messaging.operation": method,
            "messaging.url": url,
            "service.name": self.service_name
        })
        
        # Create headers with trace context
        headers = {"Content-Type": "application/json"}
        if correlation_id:
            headers["X-Correlation-ID"] = correlation_id
        
        # Inject trace context into headers
        headers = inject_trace_context(headers)
        
        for attempt in range(self.retries):
            try:
                async with self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    headers=headers
                ) as response:
                    if response.status in [200, 201]:
                        return await response.json()
                    else:
                        error_text = await response.text()
                        logger.error(f"Messaging service error {response.status}: {error_text}")
                        
                        if response.status >= 500 and attempt < self.retries - 1:
                            # Retry on server errors
                            await asyncio.sleep(2 ** attempt)
                            continue
                        
                        raise aiohttp.ClientResponseError(
                            request_info=response.request_info,
                            history=response.history,
                            status=response.status,
                            message=error_text
                        )
                        
            except aiohttp.ClientError as e:
                logger.error(f"Messaging client error (attempt {attempt + 1}): {e}")
                if attempt < self.retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                raise
        
        raise RuntimeError(f"Failed to complete request after {self.retries} attempts")
    
    # Message Publishing Methods
    @trace_method(name="publish_message", kind="PRODUCER")
    async def publish_message(
        self,
        channel: str,
        payload: Union[Dict[str, Any], str],
        metadata: Optional[Dict[str, Any]] = None,
        persistent: bool = True,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publish a message to a channel."""
        # Add span attributes for message publishing
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.operation": "publish",
            "messaging.channel": channel,
            "correlation_id": correlation_id
        })
        
        message_data = {
            "channel": channel,
            "payload": payload,
            "metadata": metadata or {},
            "service_name": self.service_name,
            "persistent": persistent
        }
        
        # Add correlation ID to metadata if provided
        if correlation_id:
            if not message_data["metadata"]:
                message_data["metadata"] = {}
            message_data["metadata"]["correlation_id"] = correlation_id
        
        return await self._make_request(
            method="POST",
            endpoint="/messaging/publish",
            data=message_data,
            correlation_id=correlation_id
        )
    
    async def publish_bulk_messages(
        self,
        messages: List[Dict[str, Any]],
        fail_on_error: bool = False
    ) -> Dict[str, Any]:
        """Publish multiple messages in bulk."""
        # Convert messages to proper format
        formatted_messages = []
        for msg in messages:
            formatted_messages.append({
                "channel": msg["channel"],
                "payload": msg["payload"],
                "metadata": msg.get("metadata"),
                "service_name": self.service_name,
                "persistent": msg.get("persistent", True)
            })
        
        bulk_data = {
            "messages": formatted_messages,
            "service_name": self.service_name,
            "fail_on_error": fail_on_error
        }
        
        return await self._make_request(
            method="POST",
            endpoint="/messaging/publish-bulk",
            data=bulk_data
        )
    
    # Command Publishing Methods
    @trace_method(name="publish_command", kind="PRODUCER")
    async def publish_command(
        self,
        command_type: str,
        payload: Dict[str, Any],
        correlation_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Publish a command to the messaging service."""
        add_span_attributes({
            "messaging.system": "command",
            "messaging.operation": "publish",
            "messaging.command_type": command_type,
            "correlation_id": correlation_id
        })

        command_data = {
            "command_type": command_type,
            "source_service": self.service_name,
            "payload": payload,
            "correlation_id": correlation_id,
            "metadata": metadata or {}
        }

        return await self._make_request(
            method="POST",
            endpoint="/messaging/commands/publish",
            data=command_data,
            correlation_id=correlation_id
        )

    # Event Publishing Methods
    @trace_method(name="publish_event", kind="PRODUCER")
    async def publish_event(
        self,
        event_type: str,
        event_data: Dict[str, Any],
        correlation_id: Optional[str] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Publish a structured event."""
        # Add span attributes for event publishing
        add_span_attributes({
            "messaging.system": "event",
            "messaging.operation": "publish",
            "messaging.event_type": event_type,
            "correlation_id": correlation_id
        })
        
        event_request = {
            "event_type": event_type,
            "source_service": self.service_name,
            "event_data": event_data,
            "correlation_id": correlation_id,
            "metadata": metadata or {}
        }
        
        return await self._make_request(
            method="POST",
            endpoint="/messaging/events/publish",
            data=event_request,
            correlation_id=correlation_id
        )
    
    @trace_method(name="publish_item_event", kind="PRODUCER")
    async def publish_item_event(self, item_event: ItemEvent) -> Dict[str, Any]:
        """Publish an item domain event."""
        # Add span attributes for item event
        add_span_attributes({
            "messaging.event_type": item_event.event_type,
            "messaging.item.id": item_event.item_id,
            "messaging.item.uuid": item_event.item_uuid,
            "correlation_id": item_event.correlation_id
        })
        
        return await self.publish_event(
            event_type=item_event.event_type,
            event_data={
                "item_id": item_event.item_id,
                "item_uuid": item_event.item_uuid,
                **item_event.event_data
            },
            correlation_id=item_event.correlation_id,
            metadata=item_event.metadata
        )
    
    # Subscription Management Methods
    @trace_method(name="create_subscription", kind="CLIENT")
    async def create_subscription(
        self,
        channel_pattern: str,
        callback_url: Optional[str] = None,
        webhook_headers: Optional[Dict[str, str]] = None,
        max_delivery_attempts: int = 3,
        ack_timeout: int = 30,
        batch_size: int = 1,
        auto_ack: bool = False,
        correlation_id: Optional[str] = None
    ) -> str:
        """Create a new subscription."""
        # Add span attributes for subscription creation
        add_span_attributes({
            "messaging.operation": "subscribe",
            "messaging.channel_pattern": channel_pattern,
            "messaging.auto_ack": auto_ack,
            "correlation_id": correlation_id
        })
        
        # Prepare webhook headers with trace context if callback URL is provided
        prepared_webhook_headers = webhook_headers or {}
        if callback_url:
            # Ensure trace context is propagated in webhook callbacks
            prepared_webhook_headers = inject_trace_context(prepared_webhook_headers)
            # Add correlation ID header if provided
            if correlation_id:
                prepared_webhook_headers["X-Correlation-ID"] = correlation_id
        
        subscription_data = {
            "channel_pattern": channel_pattern,
            "service_name": self.service_name,
            "callback_url": callback_url,
            "webhook_headers": prepared_webhook_headers,
            "max_delivery_attempts": max_delivery_attempts,
            "ack_timeout": ack_timeout,
            "batch_size": batch_size,
            "auto_ack": auto_ack
        }
        
        response = await self._make_request(
            method="POST",
            endpoint="/messaging/subscriptions",
            data=subscription_data,
            correlation_id=correlation_id
        )
        
        subscription_id = response["subscription_id"]
        self.active_subscriptions[channel_pattern] = subscription_id
        
        logger.info(f"Created subscription {subscription_id} for pattern {channel_pattern}")
        return subscription_id
    
    @trace_method(name="cancel_subscription", kind="CLIENT")
    async def cancel_subscription(self, subscription_id: str, correlation_id: Optional[str] = None) -> bool:
        """Cancel a subscription."""
        try:
            # Add span attributes for subscription cancellation
            add_span_attributes({
                "messaging.operation": "unsubscribe",
                "messaging.subscription_id": subscription_id,
                "correlation_id": correlation_id
            })
            
            await self._make_request(
                method="DELETE",
                endpoint=f"/messaging/subscriptions/{subscription_id}",
                correlation_id=correlation_id
            )
            
            # Remove from active subscriptions
            pattern_to_remove = None
            for pattern, sub_id in self.active_subscriptions.items():
                if sub_id == subscription_id:
                    pattern_to_remove = pattern
                    break
            
            if pattern_to_remove:
                del self.active_subscriptions[pattern_to_remove]
            
            logger.info(f"Cancelled subscription {subscription_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to cancel subscription {subscription_id}: {e}")
            return False
    
    async def get_subscription_info(self, subscription_id: str) -> Dict[str, Any]:
        """Get subscription information."""
        return await self._make_request(
            method="GET",
            endpoint=f"/messaging/subscriptions/{subscription_id}"
        )
    
    async def list_subscriptions(self) -> List[Dict[str, Any]]:
        """List all subscriptions for this service."""
        return await self._make_request(
            method="GET",
            endpoint="/messaging/subscriptions",
            params={"service_name": self.service_name}
        )
    
    # Message Acknowledgment Methods
    @trace_method(name="acknowledge_message", kind="CLIENT")
    async def acknowledge_message(
        self,
        subscription_id: str,
        message_id: str,
        success: bool = True,
        error: Optional[str] = None,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Acknowledge message processing."""
        # Add span attributes for message acknowledgment
        add_span_attributes({
            "messaging.operation": "acknowledge",
            "messaging.subscription_id": subscription_id,
            "messaging.message_id": message_id,
            "messaging.success": success,
            "correlation_id": correlation_id
        })
        
        if error:
            add_span_attributes({
                "error": True,
                "error.message": error
            })
        
        ack_data = {
            "message_id": message_id,
            "subscription_id": subscription_id,
            "success": success,
            "error": error
        }
        
        return await self._make_request(
            method="POST",
            endpoint="/messaging/acknowledge",
            data=ack_data,
            correlation_id=correlation_id
        )
    
    # Channel Information Methods
    async def get_channel_info(self, channel_name: str) -> Dict[str, Any]:
        """Get information about a channel."""
        return await self._make_request(
            method="GET",
            endpoint=f"/messaging/channels/{channel_name}"
        )
    
    # Health and Monitoring Methods
    async def check_health(self) -> Dict[str, Any]:
        """Check messaging service health."""
        return await self._make_request(
            method="GET",
            endpoint="/health"
        )
    
    async def get_metrics(self) -> Dict[str, Any]:
        """Get messaging service metrics."""
        return await self._make_request(
            method="GET",
            endpoint="/messaging/metrics"
        )
    
    async def get_performance_stats(self) -> Dict[str, Any]:
        """Get detailed performance statistics."""
        return await self._make_request(
            method="GET",
            endpoint="/messaging/performance/stats"
        )
    
    # Convenience Methods for Common Event Patterns
    async def subscribe_to_item_events(self, callback_url: Optional[str] = None, correlation_id: Optional[str] = None) -> str:
        """Subscribe to all item-related events."""
        return await self.create_subscription(
            channel_pattern="events.item.*",
            callback_url=callback_url,
            auto_ack=False,  # Manual acknowledgment for reliability
            correlation_id=correlation_id
        )
    
    async def subscribe_to_service_events(self, target_service: str, callback_url: Optional[str] = None, correlation_id: Optional[str] = None) -> str:
        """Subscribe to events from a specific service."""
        return await self.create_subscription(
            channel_pattern=f"events.{target_service}.*",
            callback_url=callback_url,
            auto_ack=False,
            correlation_id=correlation_id
        )
    
    async def subscribe_to_all_events(self, callback_url: Optional[str] = None, correlation_id: Optional[str] = None) -> str:
        """Subscribe to all events."""
        return await self.create_subscription(
            channel_pattern="events.*",
            callback_url=callback_url,
            auto_ack=False,
            correlation_id=correlation_id
        )
    
    @trace_method(name="publish_item_created_event", kind="PRODUCER")
    async def publish_item_created_event(
        self,
        item_id: int,
        item_uuid: str,
        item_data: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publish item created event."""
        # Add span attributes for item created event
        add_span_attributes({
            "messaging.event_type": "item.created",
            "messaging.item.id": item_id,
            "messaging.item.uuid": item_uuid,
            "correlation_id": correlation_id
        })
        
        return await self.publish_event(
            event_type="item.created",
            event_data={
                "item_id": item_id,
                "item_uuid": item_uuid,
                "item_data": item_data
            },
            correlation_id=correlation_id
        )
    
    @trace_method(name="publish_item_updated_event", kind="PRODUCER")
    async def publish_item_updated_event(
        self,
        item_id: int,
        item_uuid: str,
        changes: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publish item updated event."""
        # Add span attributes for item updated event
        add_span_attributes({
            "messaging.event_type": "item.updated",
            "messaging.item.id": item_id,
            "messaging.item.uuid": item_uuid,
            "correlation_id": correlation_id
        })
        
        return await self.publish_event(
            event_type="item.updated",
            event_data={
                "item_id": item_id,
                "item_uuid": item_uuid,
                "changes": changes
            },
            correlation_id=correlation_id
        )
    
    @trace_method(name="publish_item_deleted_event", kind="PRODUCER")
    async def publish_item_deleted_event(
        self,
        item_id: int,
        item_uuid: str,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publish item deleted event."""
        # Add span attributes for item deleted event
        add_span_attributes({
            "messaging.event_type": "item.deleted",
            "messaging.item.id": item_id,
            "messaging.item.uuid": item_uuid,
            "correlation_id": correlation_id
        })
        
        return await self.publish_event(
            event_type="item.deleted",
            event_data={
                "item_id": item_id,
                "item_uuid": item_uuid
            },
            correlation_id=correlation_id
        )
    
    @trace_method(name="publish_item_status_changed_event", kind="PRODUCER")
    async def publish_item_status_changed_event(
        self,
        item_id: int,
        item_uuid: str,
        old_status: str,
        new_status: str,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Publish item status changed event."""
        # Add span attributes for item status changed event
        add_span_attributes({
            "messaging.event_type": "item.status_changed",
            "messaging.item.id": item_id,
            "messaging.item.uuid": item_uuid,
            "messaging.item.old_status": old_status,
            "messaging.item.new_status": new_status,
            "correlation_id": correlation_id
        })
        
        return await self.publish_event(
            event_type="item.status_changed",
            event_data={
                "item_id": item_id,
                "item_uuid": item_uuid,
                "old_status": old_status,
                "new_status": new_status
            },
            correlation_id=correlation_id
        )
