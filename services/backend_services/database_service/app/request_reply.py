"""
Request/Reply Pattern over Redis Pub/Sub.

Implements a request/reply messaging pattern for synchronous-style
communication over the event-driven pub/sub infrastructure.

Pattern:
1. Requester publishes to request channel with a unique correlation_id and reply_to channel
2. Responder subscribes to request channel, processes, publishes response to reply_to channel
3. Requester subscribes to reply_to channel, waits for response with matching correlation_id
"""

import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Any, Callable, Dict, Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)


class RequestReplyClient:
    """
    Client for making request/reply calls over Redis pub/sub.
    
    Used by services to make synchronous-style requests to other services
    while maintaining the event-driven architecture.
    """
    
    def __init__(
        self,
        redis_url: str,
        service_name: str,
        default_timeout: float = 30.0
    ):
        self.redis_url = redis_url
        self.service_name = service_name
        self.default_timeout = default_timeout
        self._redis: Optional[redis.Redis] = None
        self._pubsub: Optional[redis.client.PubSub] = None
        self._pending_requests: Dict[str, asyncio.Future] = {}
        self._reply_channel: str = f"reply.{service_name}.{uuid.uuid4().hex[:8]}"
        self._listener_task: Optional[asyncio.Task] = None
        self._running = False
    
    async def connect(self) -> None:
        """Connect to Redis and start reply listener."""
        if self._running:
            return
        
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        await self._redis.ping()
        
        self._pubsub = self._redis.pubsub()
        await self._pubsub.subscribe(self._reply_channel)
        
        self._running = True
        self._listener_task = asyncio.create_task(self._listen_for_replies())
        
        logger.info(f"RequestReplyClient connected, reply channel: {self._reply_channel}")
    
    async def disconnect(self) -> None:
        """Disconnect from Redis."""
        self._running = False
        
        if self._listener_task:
            self._listener_task.cancel()
            try:
                await self._listener_task
            except asyncio.CancelledError:
                pass
        
        if self._pubsub:
            await self._pubsub.unsubscribe(self._reply_channel)
            await self._pubsub.close()
        
        if self._redis:
            await self._redis.close()
        
        # Cancel any pending requests
        for future in self._pending_requests.values():
            if not future.done():
                future.set_exception(asyncio.CancelledError("Client disconnected"))
        self._pending_requests.clear()
        
        logger.info("RequestReplyClient disconnected")
    
    async def request(
        self,
        channel: str,
        request_type: str,
        payload: Dict[str, Any],
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Send a request and wait for reply.
        
        Args:
            channel: Request channel (e.g., "database.query", "metadata.lookup")
            request_type: Type of request
            payload: Request payload
            timeout: Timeout in seconds (uses default if not specified)
            
        Returns:
            Response payload
            
        Raises:
            asyncio.TimeoutError: If no response within timeout
            Exception: If response contains an error
        """
        if not self._running:
            await self.connect()
        
        correlation_id = str(uuid.uuid4())
        timeout = timeout or self.default_timeout
        
        # Create future for response
        future: asyncio.Future = asyncio.get_event_loop().create_future()
        self._pending_requests[correlation_id] = future
        
        try:
            # Build request message
            message = {
                "correlation_id": correlation_id,
                "reply_to": self._reply_channel,
                "request_type": request_type,
                "source": self.service_name,
                "timestamp": datetime.utcnow().isoformat(),
                "payload": payload
            }
            
            # Publish request
            await self._redis.publish(channel, json.dumps(message))
            
            # Wait for response
            response = await asyncio.wait_for(future, timeout=timeout)
            
            # Check for error in response
            if response.get("error"):
                raise Exception(response["error"])
            
            return response.get("payload", response)
            
        except asyncio.TimeoutError:
            logger.error(f"Request timeout: {channel}/{request_type}")
            raise
        finally:
            self._pending_requests.pop(correlation_id, None)
    
    async def _listen_for_replies(self) -> None:
        """Listen for reply messages."""
        try:
            while self._running:
                message = await self._pubsub.get_message(
                    ignore_subscribe_messages=True,
                    timeout=1.0
                )
                
                if message and message["type"] == "message":
                    try:
                        data = json.loads(message["data"])
                        correlation_id = data.get("correlation_id")
                        
                        if correlation_id and correlation_id in self._pending_requests:
                            future = self._pending_requests[correlation_id]
                            if not future.done():
                                future.set_result(data)
                    except json.JSONDecodeError:
                        logger.warning("Invalid JSON in reply message")
                    except Exception as e:
                        logger.error(f"Error processing reply: {e}")
                
                if not message:
                    await asyncio.sleep(0.01)
                    
        except asyncio.CancelledError:
            pass
        except Exception as e:
            if self._running:
                logger.error(f"Reply listener error: {e}")


class RequestReplyServer:
    """
    Server for handling request/reply calls over Redis pub/sub.
    
    Used by services to handle incoming requests and send responses.
    """
    
    def __init__(
        self,
        redis_url: str,
        service_name: str
    ):
        self.redis_url = redis_url
        self.service_name = service_name
        self._redis: Optional[redis.Redis] = None
        self._pubsub: Optional[redis.client.PubSub] = None
        self._handlers: Dict[str, Callable] = {}
        self._listener_tasks: Dict[str, asyncio.Task] = {}
        self._running = False
    
    async def connect(self) -> None:
        """Connect to Redis."""
        if self._running:
            return
        
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        await self._redis.ping()
        self._pubsub = self._redis.pubsub()
        self._running = True
        
        logger.info(f"RequestReplyServer connected for {self.service_name}")
    
    async def disconnect(self) -> None:
        """Disconnect from Redis."""
        self._running = False
        
        for task in self._listener_tasks.values():
            task.cancel()
        
        if self._listener_tasks:
            await asyncio.gather(*self._listener_tasks.values(), return_exceptions=True)
        
        if self._pubsub:
            await self._pubsub.close()
        
        if self._redis:
            await self._redis.close()
        
        logger.info(f"RequestReplyServer disconnected for {self.service_name}")
    
    async def register_handler(
        self,
        channel: str,
        handler: Callable[[str, Dict[str, Any]], Any]
    ) -> None:
        """
        Register a handler for a request channel.
        
        Args:
            channel: Request channel to handle
            handler: Async function(request_type, payload) -> response_payload
        """
        self._handlers[channel] = handler
        await self._pubsub.subscribe(channel)
        
        # Start listener for this channel
        task = asyncio.create_task(self._handle_requests(channel))
        self._listener_tasks[channel] = task
        
        logger.info(f"Registered handler for channel: {channel}")
    
    async def _handle_requests(self, channel: str) -> None:
        """Handle incoming requests on a channel."""
        try:
            while self._running:
                message = await self._pubsub.get_message(
                    ignore_subscribe_messages=True,
                    timeout=1.0
                )
                
                if message and message["type"] == "message" and message["channel"] == channel:
                    asyncio.create_task(self._process_request(channel, message["data"]))
                
                if not message:
                    await asyncio.sleep(0.01)
                    
        except asyncio.CancelledError:
            pass
        except Exception as e:
            if self._running:
                logger.error(f"Request handler error for {channel}: {e}")
    
    async def _process_request(self, channel: str, data: str) -> None:
        """Process a single request."""
        try:
            request = json.loads(data)
            correlation_id = request.get("correlation_id")
            reply_to = request.get("reply_to")
            request_type = request.get("request_type")
            payload = request.get("payload", {})
            
            if not correlation_id or not reply_to:
                logger.warning(f"Invalid request on {channel}: missing correlation_id or reply_to")
                return
            
            handler = self._handlers.get(channel)
            if not handler:
                await self._send_error(reply_to, correlation_id, f"No handler for {channel}")
                return
            
            try:
                # Call handler
                if asyncio.iscoroutinefunction(handler):
                    result = await handler(request_type, payload)
                else:
                    result = handler(request_type, payload)
                
                # Send response
                await self._send_response(reply_to, correlation_id, result)
                
            except Exception as e:
                logger.error(f"Handler error for {channel}/{request_type}: {e}")
                await self._send_error(reply_to, correlation_id, str(e))
                
        except json.JSONDecodeError:
            logger.warning(f"Invalid JSON in request on {channel}")
        except Exception as e:
            logger.error(f"Error processing request on {channel}: {e}")
    
    async def _send_response(
        self,
        reply_to: str,
        correlation_id: str,
        payload: Any
    ) -> None:
        """Send a success response."""
        response = {
            "correlation_id": correlation_id,
            "source": self.service_name,
            "timestamp": datetime.utcnow().isoformat(),
            "payload": payload
        }
        await self._redis.publish(reply_to, json.dumps(response))
    
    async def _send_error(
        self,
        reply_to: str,
        correlation_id: str,
        error: str
    ) -> None:
        """Send an error response."""
        response = {
            "correlation_id": correlation_id,
            "source": self.service_name,
            "timestamp": datetime.utcnow().isoformat(),
            "error": error
        }
        await self._redis.publish(reply_to, json.dumps(response))
