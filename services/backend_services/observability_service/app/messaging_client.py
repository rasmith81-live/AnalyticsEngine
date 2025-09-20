"""
Messaging Client for Observability Service

This module provides a client for interacting with the Messaging Service.
It handles event publishing and subscription through HTTP API calls to the Messaging Service.
"""

import aiohttp
from .logging import get_logger
import json
import time
import asyncio
import uuid
from typing import Dict, List, Any, Optional, Union, Callable, Awaitable
from datetime import datetime

from .config import get_settings
from .telemetry import trace_method, add_span_attributes, extract_correlation_id_from_headers

logger = get_logger(__name__)

# Type for event handlers
EventHandlerType = Callable[[Dict[str, Any], Optional[str]], Awaitable[bool]]

class MessagingClient:
    """
    Client for interacting with the Messaging Service.
    
    This client handles event publishing and subscription through HTTP API calls
    to the Messaging Service. It provides methods for publishing events, subscribing
    to events, and managing subscriptions.
    """
    
    def __init__(
        self,
        base_url: str,
        service_name: str,
        timeout: int = 30,
        retries: int = 3
    ):
        """
        Initialize the Messaging Client.
        
        Args:
            base_url: Base URL of the Messaging Service
            service_name: Name of the service using this client
            timeout: Request timeout in seconds
            retries: Number of retries for failed requests
        """
        self.base_url = base_url.rstrip('/')
        self.service_name = service_name
        self.timeout = timeout
        self.retries = retries
        self.session: Optional[aiohttp.ClientSession] = None
        self._initialized = False
        self._subscriptions: Dict[str, Dict[str, Any]] = {}
        self._event_handlers: Dict[str, EventHandlerType] = {}
        
        # Get settings
        self.settings = get_settings()
    
    @trace_method(name="messaging_client.initialize", kind="CLIENT")
    async def initialize(self) -> bool:
        """
        Initialize the client and establish a connection to the Messaging Service.
        
        Returns:
            bool: True if initialization was successful, False otherwise
        """
        try:
            # Create HTTP session
            if self.session is None or self.session.closed:
                self.session = aiohttp.ClientSession(
                    timeout=aiohttp.ClientTimeout(total=self.timeout),
                    headers={
                        "User-Agent": f"{self.service_name}-messaging-client/1.0",
                        "Content-Type": "application/json",
                        "Accept": "application/json"
                    }
                )
            
            # Check connection to Messaging Service
            health_check = await self.check_health()
            if not health_check:
                logger.error("Failed to connect to Messaging Service during initialization")
                return False
            
            self._initialized = True
            logger.info("Messaging Client initialized successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize Messaging Client: {str(e)}")
            return False
    
    async def close(self):
        """Close the client session and unsubscribe from all events."""
        try:
            # Unsubscribe from all events
            for subscription_id in list(self._subscriptions.keys()):
                await self.unsubscribe(subscription_id)
            
            # Close HTTP session
            if self.session and not self.session.closed:
                await self.session.close()
                logger.info("Messaging Client session closed")
                
        except Exception as e:
            logger.error(f"Error closing Messaging Client: {str(e)}")
    
    @trace_method(name="messaging_client.make_request", kind="CLIENT")
    async def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Make a request to the Messaging Service with retry logic.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Request data
            params: Query parameters
            headers: Additional headers
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            Dict[str, Any]: Response data
            
        Raises:
            Exception: If the request fails after all retries
        """
        if not self.session or self.session.closed:
            await self.initialize()
        
        url = f"{self.base_url}{endpoint}"
        
        # Add correlation ID to headers for distributed tracing
        request_headers = headers or {}
        if correlation_id:
            request_headers["X-Correlation-ID"] = correlation_id
        
        # Add span attributes for telemetry
        add_span_attributes({
            "messaging.operation": method,
            "messaging.url": url,
            "messaging.service": "messaging_service",
            "correlation_id": correlation_id
        })
        
        # Retry logic
        retries_left = self.retries
        last_exception = None
        
        while retries_left > 0:
            try:
                start_time = time.time()
                
                async with self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    headers=request_headers
                ) as response:
                    elapsed_time = time.time() - start_time
                    
                    # Add response attributes to span
                    add_span_attributes({
                        "messaging.response.status_code": response.status,
                        "messaging.response.time_ms": elapsed_time * 1000
                    })
                    
                    # Log request details
                    logger.debug(
                        f"Messaging request: {method} {url} - "
                        f"Status: {response.status} - "
                        f"Time: {elapsed_time:.3f}s"
                    )
                    
                    # Handle response
                    if response.status in (200, 201, 204):
                        if response.status == 204:
                            return {}
                        
                        try:
                            return await response.json()
                        except Exception as e:
                            logger.warning(f"Failed to parse response as JSON: {str(e)}")
                            return {"content": await response.text()}
                    
                    # Handle error responses
                    error_text = await response.text()
                    try:
                        error_json = json.loads(error_text)
                        error_message = error_json.get("detail", error_text)
                    except:
                        error_message = error_text
                    
                    # Add error details to span
                    add_span_attributes({
                        "error": True,
                        "error.message": error_message
                    })
                    
                    # Log error details
                    logger.error(
                        f"Messaging request failed: {method} {url} - "
                        f"Status: {response.status} - "
                        f"Error: {error_message}"
                    )
                    
                    # Raise exception for retry
                    raise Exception(f"Messaging request failed with status {response.status}: {error_message}")
                    
            except Exception as e:
                last_exception = e
                retries_left -= 1
                
                if retries_left > 0:
                    # Exponential backoff
                    wait_time = 0.5 * (2 ** (self.retries - retries_left))
                    logger.warning(
                        f"Messaging request failed, retrying in {wait_time:.2f}s "
                        f"({retries_left} retries left): {str(e)}"
                    )
                    await asyncio.sleep(wait_time)
                else:
                    # Add error details to span
                    add_span_attributes({
                        "error": True,
                        "error.message": str(e)
                    })
                    
                    logger.error(f"Messaging request failed after {self.retries} retries: {str(e)}")
                    raise
        
        # This should not be reached, but just in case
        if last_exception:
            raise last_exception
        else:
            raise Exception("Unknown error in messaging request")
    
    @trace_method(name="messaging_client.publish_event", kind="PRODUCER")
    async def publish_event(
        self,
        event_type: str,
        event_data: Dict[str, Any],
        channel: str = "default",
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Publish an event to the Messaging Service.
        
        Args:
            event_type: Type of the event
            event_data: Event data
            channel: Channel to publish the event to
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            Dict[str, Any]: Publication result
        """
        # Generate a correlation ID if not provided
        if not correlation_id:
            correlation_id = str(uuid.uuid4())
        
        # Ensure event_data is a dict
        if not isinstance(event_data, dict):
            event_data = {"data": event_data}
        
        # Add correlation ID to event data for tracing
        if "correlation_id" not in event_data:
            event_data["correlation_id"] = correlation_id
        
        # Add span attributes for telemetry
        add_span_attributes({
            "messaging.event_type": event_type,
            "messaging.channel": channel,
            "messaging.operation": "publish",
            "correlation_id": correlation_id
        })
        
        data = {
            "event_type": event_type,
            "source_service": self.service_name,
            "event_data": event_data,
            "correlation_id": correlation_id,
            "metadata": {
                "channel": channel,
                "timestamp": datetime.utcnow().isoformat()
            }
        }
        
        try:
            result = await self._make_request(
                method="POST",
                endpoint="/api/v1/events/publish",
                data=data,
                correlation_id=correlation_id
            )
            
            logger.info(f"Published event {event_type} to channel {channel}")
            return result
            
        except Exception as e:
            logger.error(f"Failed to publish event {event_type}: {str(e)}")
            raise
    
    @trace_method(name="messaging_client.subscribe", kind="CONSUMER")
    async def subscribe(
        self,
        event_types: List[str],
        callback_url: str,
        channel: str = "default",
        filters: Optional[Dict[str, Any]] = None,
        correlation_id: Optional[str] = None
    ) -> str:
        """
        Subscribe to events from the Messaging Service.
        
        Args:
            event_types: Types of events to subscribe to
            callback_url: URL to receive event callbacks
            channel: Channel to subscribe to
            filters: Filters to apply to events
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            str: Subscription ID
        """
        # Add span attributes for telemetry
        add_span_attributes({
            "messaging.channel": channel,
            "messaging.operation": "subscribe",
            "correlation_id": correlation_id
        })

        # The channel is the event_type for observability
        # We subscribe to each event type as a channel
        data = {
            "service_name": self.service_name,
            "callback_url": callback_url,
            "channel_pattern": channel, # event_types are treated as channels
            "filter_criteria": filters or {}
        }

        try:
            result = await self._make_request(
                method="POST",
                endpoint="/messaging/subscriptions",
                data=data,
                correlation_id=correlation_id
            )
            
            subscription_id = result.get("subscription_id")
            if not subscription_id:
                raise Exception("No subscription ID returned")
            
            # Store subscription details
            self._subscriptions[subscription_id] = {
                "event_types": event_types,
                "channel": channel,
                "callback_url": callback_url
            }
            
            logger.info(f"Subscribed to events {event_types} on channel {channel}")
            return subscription_id
            
        except Exception as e:
            logger.error(f"Failed to subscribe to events {event_types}: {str(e)}")
            raise
    
    @trace_method(name="messaging_client.unsubscribe", kind="CONSUMER")
    async def unsubscribe(
        self,
        subscription_id: str,
        correlation_id: Optional[str] = None
    ) -> bool:
        """
        Unsubscribe from events.
        
        Args:
            subscription_id: Subscription ID to unsubscribe
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            bool: True if unsubscription was successful, False otherwise
        """
        # Add span attributes for telemetry
        add_span_attributes({
            "messaging.subscription_id": subscription_id,
            "messaging.operation": "unsubscribe",
            "correlation_id": correlation_id
        })
        
        try:
            await self._make_request(
                method="DELETE",
                endpoint=f"/messaging/subscriptions/{subscription_id}",
                correlation_id=correlation_id
            )
            
            # Remove subscription from local storage
            if subscription_id in self._subscriptions:
                del self._subscriptions[subscription_id]
            
            logger.info(f"Unsubscribed from subscription {subscription_id}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to unsubscribe from subscription {subscription_id}: {str(e)}")
            return False
    
    @trace_method(name="messaging_client.register_event_handler", kind="CONSUMER")
    def register_event_handler(
        self,
        event_type: str,
        handler: EventHandlerType
    ) -> None:
        """
        Register a handler for a specific event type.
        
        Args:
            event_type: Type of event to handle
            handler: Async function to handle the event
        """
        self._event_handlers[event_type] = handler
        logger.info(f"Registered handler for event type {event_type}")
    
    @trace_method(name="messaging_client.process_event", kind="CONSUMER")
    async def process_event(
        self,
        event: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> bool:
        """
        Process an incoming event.
        
        Args:
            event: Event data
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            bool: True if the event was processed successfully, False otherwise
        """
        event_type = event.get("event_type")
        if not event_type:
            logger.warning("Received event with no event_type")
            return False
        
        # Extract correlation ID from event if not provided
        if not correlation_id and "correlation_id" in event:
            correlation_id = event["correlation_id"]
        
        # Add span attributes for telemetry
        add_span_attributes({
            "messaging.event_type": event_type,
            "messaging.operation": "process",
            "correlation_id": correlation_id
        })
        
        # Find handler for this event type
        handler = self._event_handlers.get(event_type)
        if not handler:
            # Try wildcard handlers
            for pattern, h in self._event_handlers.items():
                if pattern.endswith("*") and event_type.startswith(pattern[:-1]):
                    handler = h
                    break
        
        if handler:
            try:
                logger.info(f"Processing event {event_type}")
                return await handler(event, correlation_id)
            except Exception as e:
                logger.error(f"Error processing event {event_type}: {str(e)}")
                return False
        else:
            logger.warning(f"No handler registered for event type {event_type}")
            return False
    
    @trace_method(name="messaging_client.check_health", kind="CLIENT")
    async def check_health(self, correlation_id: Optional[str] = None) -> bool:
        """
        Check the health of the Messaging Service.
        
        Args:
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            bool: True if the Messaging Service is healthy, False otherwise
        """
        try:
            result = await self._make_request(
                method="GET",
                endpoint="/health",
                correlation_id=correlation_id
            )
            
            status = result.get("status", "").lower()
            return status == "healthy"
            
        except Exception as e:
            logger.error(f"Messaging Service health check failed: {str(e)}")
            return False
    
    @trace_method(name="messaging_client.get_subscriptions", kind="CLIENT")
    async def get_subscriptions(self, correlation_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get all subscriptions for this service.
        
        Args:
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            List[Dict[str, Any]]: List of subscriptions
        """
        try:
            params = {
                "subscriber": self.service_name
            }
            
            result = await self._make_request(
                method="GET",
                endpoint="/messaging/subscriptions",
                params=params,
                correlation_id=correlation_id
            )
            
            subscriptions = result.get("subscriptions", [])
            
            # Update local subscription cache
            self._subscriptions = {
                sub["subscription_id"]: {
                    "event_types": sub["event_types"],
                    "channel": sub["channel"],
                    "callback_url": sub["callback_url"]
                }
                for sub in subscriptions
            }
            
            return subscriptions
            
        except Exception as e:
            logger.error(f"Failed to get subscriptions: {str(e)}")
            return []
    
    @trace_method(name="messaging_client.get_channels", kind="CLIENT")
    async def get_channels(self, correlation_id: Optional[str] = None) -> List[str]:
        """
        Get all available channels from the Messaging Service.
        
        Args:
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            List[str]: List of channel names
        """
        # This endpoint does not exist on the messaging service, returning empty list
        logger.warning("Attempted to call get_channels, which is not implemented in the messaging service.")
        return []
    
    @trace_method(name="messaging_client.get_event_types", kind="CLIENT")
    async def get_event_types(self, correlation_id: Optional[str] = None) -> List[str]:
        """
        Get all available event types from the Messaging Service.
        
        Args:
            correlation_id: Correlation ID for distributed tracing
            
        Returns:
            List[str]: List of event types
        """
        # This endpoint does not exist on the messaging service, returning empty list
        logger.warning("Attempted to call get_event_types, which is not implemented in the messaging service.")
        return []
