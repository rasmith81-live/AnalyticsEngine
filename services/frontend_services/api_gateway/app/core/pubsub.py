"""
Redis Pub/Sub implementation for the API Gateway service.
Provides functionality for publishing and subscribing to Redis channels.
"""
import asyncio
import json
from typing import Any, Callable, Dict, Optional, Set
import uuid

from app.core.logging import get_logger
from app.core.redis_client import redis_client_context

logger = get_logger(__name__)

# Type for message handlers
MessageHandler = Callable[[str, Any], None]

class PubSubService:
    """
    Service that provides Redis Pub/Sub functionality.
    Manages subscriptions and message handlers.
    """
    
    def __init__(self):
        """Initialize the Pub/Sub service."""
        self._handlers: Dict[str, Set[MessageHandler]] = {}
        self._pattern_handlers: Dict[str, Set[MessageHandler]] = {}
        self._subscriber_task: Optional[asyncio.Task] = None
        self._running = False
    
    async def start(self) -> None:
        """Start the Pub/Sub service."""
        if self._running:
            logger.warning("PubSubService is already running")
            return
        
        self._running = True
        self._subscriber_task = asyncio.create_task(self._subscriber_loop())
        logger.info("PubSubService started")
    
    async def stop(self) -> None:
        """Stop the Pub/Sub service."""
        if not self._running:
            logger.warning("PubSubService is not running")
            return
        
        self._running = False
        if self._subscriber_task:
            self._subscriber_task.cancel()
            try:
                await self._subscriber_task
            except asyncio.CancelledError:
                pass
            self._subscriber_task = None
        
        logger.info("PubSubService stopped")
    
    async def publish(self, channel: str, message: Any) -> bool:
        """
        Publish a message to a channel.
        
        Args:
            channel: Channel to publish to
            message: Message to publish
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Serialize message to JSON if it's not a string
            if not isinstance(message, str):
                message = json.dumps(message)
            
            async with redis_client_context() as redis:
                await redis.publish(channel, message)
                logger.debug(f"Published message to channel {channel}")
                return True
        except Exception as e:
            logger.error(f"Failed to publish message to channel {channel}: {str(e)}")
            return False
    
    def subscribe(self, channel: str, handler: MessageHandler) -> str:
        """
        Subscribe to a channel.
        
        Args:
            channel: Channel to subscribe to
            handler: Message handler function
            
        Returns:
            Subscription ID
        """
        if channel not in self._handlers:
            self._handlers[channel] = set()
        
        self._handlers[channel].add(handler)
        subscription_id = str(uuid.uuid4())
        
        logger.debug(f"Subscribed to channel {channel} with ID {subscription_id}")
        
        return subscription_id
    
    def unsubscribe(self, channel: str, handler: MessageHandler) -> bool:
        """
        Unsubscribe from a channel.
        
        Args:
            channel: Channel to unsubscribe from
            handler: Message handler function
            
        Returns:
            True if successful, False otherwise
        """
        if channel not in self._handlers:
            logger.warning(f"No subscriptions for channel {channel}")
            return False
        
        try:
            self._handlers[channel].remove(handler)
            
            # Remove channel if no handlers left
            if not self._handlers[channel]:
                del self._handlers[channel]
            
            logger.debug(f"Unsubscribed from channel {channel}")
            return True
        except KeyError:
            logger.warning(f"Handler not found for channel {channel}")
            return False
            
    def psubscribe(self, pattern: str, handler: MessageHandler) -> str:
        """
        Subscribe to a channel pattern.
        
        Args:
            pattern: Channel pattern to subscribe to (e.g., "responses.*")
            handler: Message handler function
            
        Returns:
            Subscription ID
        """
        if pattern not in self._pattern_handlers:
            self._pattern_handlers[pattern] = set()
        
        self._pattern_handlers[pattern].add(handler)
        subscription_id = str(uuid.uuid4())
        
        logger.debug(f"Pattern subscribed to {pattern} with ID {subscription_id}")
        
        return subscription_id
        
    def punsubscribe(self, pattern: str, handler: MessageHandler) -> bool:
        """
        Unsubscribe from a channel pattern.
        
        Args:
            pattern: Channel pattern to unsubscribe from
            handler: Message handler function
            
        Returns:
            True if successful, False otherwise
        """
        if pattern not in self._pattern_handlers:
            logger.warning(f"No pattern subscriptions for {pattern}")
            return False
        
        try:
            self._pattern_handlers[pattern].remove(handler)
            
            # Remove pattern if no handlers left
            if not self._pattern_handlers[pattern]:
                del self._pattern_handlers[pattern]
            
            logger.debug(f"Unsubscribed from pattern {pattern}")
            return True
        except KeyError:
            logger.warning(f"Handler not found for pattern {pattern}")
            return False
    
    async def _subscriber_loop(self) -> None:
        """
        Main subscriber loop.
        Listens for messages on subscribed channels and patterns.
        """
        while self._running:
            try:
                # Get all channels and patterns with handlers
                channels = list(self._handlers.keys())
                patterns = list(self._pattern_handlers.keys())
                
                if not channels and not patterns:
                    # No subscriptions, wait and try again
                    await asyncio.sleep(1)
                    continue
                
                async with redis_client_context() as redis:
                    # Create a pubsub instance
                    pubsub = redis.pubsub()
                    
                    # Subscribe to channels and patterns
                    if channels:
                        await pubsub.subscribe(*channels)
                        logger.debug(f"Subscribed to {len(channels)} channels")
                    
                    if patterns:
                        await pubsub.psubscribe(*patterns)
                        logger.debug(f"Pattern subscribed to {len(patterns)} patterns")
                    
                    # Listen for messages
                    while self._running:
                        message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=1.0)
                        
                        if message is None:
                            # No message, continue
                            continue
                        
                        # Process message
                        await self._process_message(message)
                    
                    # Unsubscribe when stopping
                    if channels:
                        await pubsub.unsubscribe()
                    if patterns:
                        await pubsub.punsubscribe()
                    
            except asyncio.CancelledError:
                logger.info("Subscriber loop cancelled")
                break
            except Exception as e:
                logger.error(f"Error in subscriber loop: {str(e)}")
                # Wait before reconnecting
                await asyncio.sleep(1)
    
    async def _process_message(self, message: Dict[str, Any]) -> None:
        """
        Process a received message.
        
        Args:
            message: Redis message
        """
        try:
            message_type = message.get("type", "")
            data = message.get("data")

            # Data is already decoded by aioredis (decode_responses=True)
            # Parse data if it's a JSON string
            if isinstance(data, str):
                try:
                    data = json.loads(data)
                except json.JSONDecodeError:
                    pass  # Not a JSON string, use as is

            if message_type == "message":
                channel = message.get("channel", "")
                if not channel:
                    return
                
                handlers = self._handlers.get(channel, set())
                for handler in handlers:
                    try:
                        if asyncio.iscoroutinefunction(handler):
                            await handler(channel, data)
                        else:
                            handler(channel, data)
                    except Exception as e:
                        logger.error(f"Error in message handler for channel {channel}: {e}")

            elif message_type == "pmessage":
                pattern = message.get("pattern", "")
                channel = message.get("channel", "")
                if not pattern or not channel:
                    return

                handlers = self._pattern_handlers.get(pattern, set())
                for handler in handlers:
                    try:
                        if asyncio.iscoroutinefunction(handler):
                            await handler(channel, data)
                        else:
                            handler(channel, data)
                    except Exception as e:
                        logger.error(f"Error in pattern handler for {pattern} on channel {channel}: {e}")

        except Exception as e:
            logger.error(f"Error processing message: {e}")

# Create a singleton instance
pubsub_service = PubSubService()
