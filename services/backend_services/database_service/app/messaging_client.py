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
from redis.exceptions import BusyLoadingError

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
        self._callbacks: Dict[str, Callable] = {}
        self._dispatcher_task: Optional[asyncio.Task] = None
        self._subscribed_event = asyncio.Event()

    async def connect(self):
        """Connect to Redis with retry logic and start the message dispatcher."""
        if self.is_connected():
            return

        max_retries = 5
        retry_delay = 1  # initial delay in seconds
        for attempt in range(max_retries):
            try:
                self._redis = redis.Redis.from_url(
                    self.redis_url,
                    decode_responses=True,
                    max_connections=self.pool_size
                )
                self._pubsub = self._redis.pubsub()

                await self._redis.ping()
                self._running = True

                # Start the single message dispatcher task
                self._dispatcher_task = asyncio.create_task(self._main_message_dispatcher())
                logger.info(f"Connected to Redis at {self.redis_url} and started message dispatcher.")
                return  # Exit on successful connection
            except BusyLoadingError:
                logger.warning(f"Redis is loading data. Retrying in {retry_delay}s... (Attempt {attempt + 1}/{max_retries})")
                await asyncio.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            except Exception as e:
                logger.error(f"Failed to connect to Redis during attempt {attempt + 1}: {e}", exc_info=True)
                raise
        
        logger.error("Failed to connect to Redis after multiple retries.")
        raise ConnectionError("Failed to connect to Redis after multiple retries.")

    async def disconnect(self):
        """Disconnect from Redis and stop the message dispatcher."""
        if not self.is_connected():
            return

        self._running = False

        # Cancel the dispatcher task
        if self._dispatcher_task:
            self._dispatcher_task.cancel()
            try:
                await self._dispatcher_task
            except asyncio.CancelledError:
                pass  # Expected cancellation
            self._dispatcher_task = None

        # Close pubsub and redis connections
        if self._pubsub:
            await self._pubsub.close()
        
        if self._redis:
            await self._redis.close()
        
        self._redis = None
        self._pubsub = None
        logger.info("Disconnected from Redis")

    def is_connected(self) -> bool:
        """Check if connected to Redis."""
        return self._redis is not None and self._running

    async def publish_event(
        self,
        topic: str,
        event_type: str,
        payload: Dict[str, Any],
        service_name: Optional[str] = None
    ) -> bool:
        """Publish an event to a topic."""
        if not self.is_connected():
            await self.connect()

        try:
            message = {
                "event_id": str(uuid.uuid4()),
                "event_type": event_type,
                "service_name": service_name or self.service_name,
                "timestamp": datetime.utcnow().isoformat(),
                "payload": payload
            }
            await self._redis.publish(topic, json.dumps(message))
            return True
        except Exception as e:
            logger.error(f"Failed to publish event to {topic}: {e}", exc_info=True)
            return False

    async def publish_message(
        self,
        channel: str,
        message: Dict[str, Any],
        message_type: str = "message"
    ) -> bool:
        """
        Publish a generic message to a channel.
        
        Args:
            channel: Redis channel to publish to
            message: Message content (will be JSON encoded)
            message_type: Type of message
            
        Returns:
            True if successful, False otherwise
        """
        # Reuse publish_event logic or simple publish
        # StreamPublisher expects specific format possibly? 
        # Looking at StreamPublisher code, it just sends the message dict directly 
        # inside publish_message call, but wrapping it might be safer for consistency.
        # However, StreamPublisher code:
        # await self.messaging_client.publish_message(
        #     channel=channel,
        #     message=message,
        #     message_type="kpi_stream_update"
        # )
        
        return await self.publish_event(
            topic=channel,
            event_type=message_type,
            payload=message
        )

    async def subscribe(
        self,
        topic: str,
        callback: Callable[[Dict[str, Any]], Any]
    ):
        """Subscribe to a topic."""
        if not self.is_connected():
            await self.connect()

        self._callbacks[topic] = callback
        await self._pubsub.subscribe(topic)
        self._subscribed_event.set()
        logger.info(f"Subscribed to topic: {topic}")

    async def unsubscribe(self, topic: str):
        """Unsubscribe from a topic."""
        if not self.is_connected() or topic not in self._callbacks:
            return

        await self._pubsub.unsubscribe(topic)
        del self._callbacks[topic]
        if not self._callbacks:
            self._subscribed_event.clear()
        logger.info(f"Unsubscribed from topic: {topic}")

    async def _main_message_dispatcher(self):
        """A single, centralized listener for all subscribed topics."""
        logger.info("Main message dispatcher started.")
        try:
            await self._subscribed_event.wait()
            while self._running:
                message = await self._pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                if message is None:
                    await asyncio.sleep(0.01) # Prevent busy-waiting
                    continue

                if message["type"] == "message":
                    topic = message["channel"]
                    if topic in self._callbacks:
                        try:
                            data = json.loads(message["data"])
                            payload = data.get("payload", data)
                            # Schedule callback to run concurrently
                            asyncio.create_task(self._callbacks[topic](payload))
                        except json.JSONDecodeError:
                            logger.warning(f"Received invalid JSON on topic {topic}")
                        except Exception as e:
                            logger.error(f"Error processing message on topic {topic}: {e}", exc_info=True)
        except asyncio.CancelledError:
            logger.info("Main message dispatcher cancelled.")
        except Exception as e:
            # This may catch redis.exceptions.ConnectionError during shutdown
            if self._running:
                logger.error(f"Main message dispatcher error: {e}", exc_info=True)
        finally:
            logger.info("Main message dispatcher stopped.")

    async def get_active_subscriptions(self) -> List[str]:
        """Get list of active subscriptions."""
        return list(self._callbacks.keys())
