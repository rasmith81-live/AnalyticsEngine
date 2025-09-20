"""
Messaging Client for Redis pub/sub communication.

This module provides functionality to interact with Redis for pub/sub messaging
between microservices.
"""
import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Dict, Any, Callable, Optional, List

import redis.asyncio as redis

from .telemetry import trace_method, add_span_attributes, traced_span, inject_trace_context, extract_trace_context

logger = logging.getLogger(__name__)

class MessagingClient:
    """Client for interacting with Redis pub/sub messaging."""
    
    def __init__(
        self,
        redis_url: str,
        service_name: str,
        pool_size: int = 10
    ):
        """Initialize the messaging client.
        
        Args:
            redis_url: Redis connection URL
            service_name: Name of this service
            pool_size: Redis connection pool size
        """
        self.redis_url = redis_url
        self.service_name = service_name
        self.pool_size = pool_size
        self._redis = None
        self._pubsub = None
        self._running = False
        self._subscription_tasks = {}
        self._callbacks = {}
    
    @trace_method(name="MessagingClient.connect", kind="CLIENT")
    async def connect(self):
        """Connect to Redis."""
        if self._redis is not None:
            return
        
        # Add span attributes for Redis connection
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.url": self.redis_url,
            "messaging.operation": "connect",
            "service.name": self.service_name
        })
        
        try:
            self._redis = redis.Redis.from_url(
                self.redis_url,
                decode_responses=True,
                max_connections=self.pool_size
            )
            self._pubsub = self._redis.pubsub()
            
            # Test connection
            await self._redis.ping()
            
            self._running = True
            logger.info(f"Connected to Redis at {self.redis_url}")
        except Exception as e:
            logger.error(f"Failed to connect to Redis: {e}", exc_info=True)
            raise
    
    @trace_method(name="MessagingClient.disconnect", kind="CLIENT")
    async def disconnect(self):
        """Disconnect from Redis."""
        if self._redis is None:
            return
        
        # Add span attributes for Redis disconnection
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.operation": "disconnect",
            "service.name": self.service_name,
            "active_subscriptions": len(self._subscription_tasks)
        })
        
        self._running = False
        
        # Cancel all subscription tasks
        for task in self._subscription_tasks.values():
            task.cancel()
        
        # Wait for tasks to complete
        if self._subscription_tasks:
            await asyncio.gather(*self._subscription_tasks.values(), return_exceptions=True)
        
        # Close pubsub and redis connections
        if self._pubsub:
            await self._pubsub.close()
        
        await self._redis.close()
        self._redis = None
        self._pubsub = None
        logger.info("Disconnected from Redis")
    
    @trace_method(name="MessagingClient.ping", kind="CLIENT")
    async def ping(self):
        """Ping Redis to check connection health."""
        if not self.is_connected():
            await self.connect()
        
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.operation": "ping",
            "service.name": self.service_name
        })
        
        try:
            await self._redis.ping()
        except Exception as e:
            logger.error(f"Redis ping failed: {e}", exc_info=True)
            self._running = False
            raise

    def is_connected(self) -> bool:
        """Check if connected to Redis.
        
        Returns:
            True if connected, False otherwise
        """
        return self._redis is not None and self._running
    
    @trace_method(name="MessagingClient.publish_event", kind="PRODUCER")
    async def publish_event(
        self,
        topic: str,
        event_type: str,
        payload: Dict[str, Any],
        service_name: Optional[str] = None,
        correlation_id: Optional[str] = None
    ) -> bool:
        """Publish an event to a topic.
        
        Args:
            topic: Topic to publish to
            event_type: Type of event
            payload: Event payload
            service_name: Optional service name, defaults to self.service_name
            correlation_id: Optional correlation ID for distributed tracing
            
        Returns:
            True if publish was successful, False otherwise
        """
        if not self.is_connected():
            await self.connect()
        
        # Generate event ID and correlation ID if not provided
        event_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add span attributes for messaging context
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.destination": topic,
            "messaging.destination_kind": "topic",
            "messaging.operation": "publish",
            "messaging.message_id": event_id,
            "event_type": event_type,
            "correlation_id": correlation_id,
            "service.name": service_name or self.service_name
        })
        
        try:
            # Create the message
            message = {
                "event_id": event_id,
                "event_type": event_type,
                "service_name": service_name or self.service_name,
                "timestamp": datetime.utcnow().isoformat(),
                "correlation_id": correlation_id,
                "payload": payload
            }
            
            # Add trace context to message headers
            headers = {}
            inject_trace_context(headers)
            if headers:
                message["trace_context"] = headers
            
            # Publish to Redis
            await self._redis.publish(topic, json.dumps(message))
            return True
        except Exception as e:
            logger.error(f"Failed to publish event to {topic}: {e}", exc_info=True)
            return False
    
    @trace_method(name="MessagingClient.subscribe", kind="CONSUMER")
    async def subscribe(
        self,
        topic: str,
        callback: Callable[[Dict[str, Any]], None],
        service_name: Optional[str] = None
    ):
        """Subscribe to a topic.
        
        Args:
            topic: Topic to subscribe to
            callback: Function to call when a message is received
            service_name: Optional service name for logging
        """
        if not self.is_connected():
            await self.connect()
        
        # Add span attributes for subscription context
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.destination": topic,
            "messaging.destination_kind": "topic",
            "messaging.operation": "subscribe",
            "service.name": service_name or self.service_name
        })
        
        # Store the callback
        self._callbacks[topic] = callback
        
        # Subscribe to the topic
        await self._pubsub.subscribe(topic)
        
        # Start the listener task if not already running
        if topic not in self._subscription_tasks or self._subscription_tasks[topic].done():
            self._subscription_tasks[topic] = asyncio.create_task(
                self._message_listener(topic, service_name or self.service_name)
            )
        
        logger.info(f"Subscribed to topic: {topic}")
    
    @trace_method(name="MessagingClient.unsubscribe", kind="CONSUMER")
    async def unsubscribe(
        self,
        topic: str,
        service_name: Optional[str] = None
    ):
        """Unsubscribe from a topic.
        
        Args:
            topic: Topic to unsubscribe from
            service_name: Optional service name for logging
        """
        if not self.is_connected():
            return
        
        # Add span attributes for unsubscription context
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.destination": topic,
            "messaging.destination_kind": "topic",
            "messaging.operation": "unsubscribe",
            "service.name": service_name or self.service_name
        })
        
        # Unsubscribe from the topic
        await self._pubsub.unsubscribe(topic)
        
        # Cancel the listener task
        if topic in self._subscription_tasks:
            self._subscription_tasks[topic].cancel()
            try:
                await self._subscription_tasks[topic]
            except asyncio.CancelledError:
                pass
            del self._subscription_tasks[topic]
        
        # Remove the callback
        if topic in self._callbacks:
            del self._callbacks[topic]
        
        logger.info(f"Unsubscribed from topic: {topic}")
    
    async def _message_listener(self, topic: str, service_name: str):
        """Listen for messages on a topic.
        
        Args:
            topic: Topic to listen on
            service_name: Service name for logging
        """
        try:
            while self._running:
                message = await self._pubsub.get_message(ignore_subscribe_messages=True)
                if message is not None and message["type"] == "message":
                    # Parse the message
                    try:
                        data = json.loads(message["data"])
                        
                        # Extract correlation ID and trace context
                        correlation_id = data.get("correlation_id", "unknown")
                        trace_context = data.get("trace_context", {})
                        
                        # Process message with tracing context
                        async with traced_span(
                            name=f"process_message_{topic}",
                            kind="CONSUMER",
                            attributes={
                                "messaging.system": "redis",
                                "messaging.destination": topic,
                                "messaging.destination_kind": "topic",
                                "messaging.operation": "receive",
                                "messaging.message_id": data.get("event_id", "unknown"),
                                "event_type": data.get("event_type", "unknown"),
                                "correlation_id": correlation_id,
                                "service.name": service_name
                            }
                        ) as span:
                            # Extract trace context if available
                            if trace_context:
                                extracted_context = extract_trace_context(trace_context)
                            
                            # Call the callback
                            if topic in self._callbacks:
                                callback = self._callbacks[topic]
                                
                                # Extract payload if it exists
                                payload = data.get("payload", data)
                                
                                # Add original message metadata to payload for context
                                if isinstance(payload, dict):
                                    if "correlation_id" not in payload and correlation_id != "unknown":
                                        payload["correlation_id"] = correlation_id
                                    if "event_id" not in payload and "event_id" in data:
                                        payload["event_id"] = data["event_id"]
                                
                                # Call the callback with the payload
                                await callback(payload)
                    except json.JSONDecodeError:
                        logger.warning(f"Received invalid JSON message on topic {topic}")
                    except Exception as e:
                        logger.error(f"Error processing message on topic {topic}: {e}", exc_info=True)
                
                # Small sleep to avoid high CPU usage
                await asyncio.sleep(0.01)
        except asyncio.CancelledError:
            # Task was cancelled, exit gracefully
            logger.info(f"Message listener for topic {topic} cancelled")
        except Exception as e:
            logger.error(f"Error in message listener for topic {topic}: {e}", exc_info=True)
    
    @trace_method(name="MessagingClient.get_active_subscriptions", kind="INTERNAL")
    async def get_active_subscriptions(self) -> List[str]:
        """Get list of active subscriptions.
        
        Returns:
            List of topics this client is subscribed to
        """
        # Add span attributes for subscription context
        add_span_attributes({
            "messaging.system": "redis",
            "messaging.operation": "list_subscriptions",
            "service.name": self.service_name,
            "subscription_count": len(self._subscription_tasks)
        })
        
        return list(self._subscription_tasks.keys())
