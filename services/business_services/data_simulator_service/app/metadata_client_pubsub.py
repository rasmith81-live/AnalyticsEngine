"""
Metadata Client using Pub/Sub for Data Simulator Service.

Provides metadata access via Redis pub/sub request/reply pattern,
maintaining the event-driven architecture.
"""

import asyncio
import json
import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)

CHANNEL_METADATA_LOOKUP = "metadata.lookup"


class MetadataClientPubSub:
    """
    Metadata client using pub/sub for event-driven metadata access.
    
    Uses request/reply pattern over Redis pub/sub instead of HTTP.
    """
    
    def __init__(
        self,
        redis_url: str,
        service_name: str = "data_simulator",
        default_timeout: float = 10.0
    ):
        self.redis_url = redis_url
        self.service_name = service_name
        self.default_timeout = default_timeout
        self._redis: Optional[redis.Redis] = None
        self._pubsub: Optional[redis.client.PubSub] = None
        self._pending_requests: Dict[str, asyncio.Future] = {}
        self._reply_channel: str = f"reply.{service_name}.metadata.{uuid.uuid4().hex[:8]}"
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
        
        logger.info(f"MetadataClientPubSub connected")
    
    async def close(self) -> None:
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
        
        for future in self._pending_requests.values():
            if not future.done():
                future.set_exception(asyncio.CancelledError("Client disconnected"))
        self._pending_requests.clear()
        
        logger.info("MetadataClientPubSub disconnected")
    
    async def _request(
        self,
        request_type: str,
        payload: Dict[str, Any],
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """Send a request and wait for reply."""
        if not self._running:
            await self.connect()
        
        correlation_id = str(uuid.uuid4())
        timeout = timeout or self.default_timeout
        
        future: asyncio.Future = asyncio.get_event_loop().create_future()
        self._pending_requests[correlation_id] = future
        
        try:
            message = {
                "correlation_id": correlation_id,
                "reply_to": self._reply_channel,
                "request_type": request_type,
                "source": self.service_name,
                "timestamp": datetime.utcnow().isoformat(),
                "payload": payload
            }
            
            await self._redis.publish(CHANNEL_METADATA_LOOKUP, json.dumps(message))
            response = await asyncio.wait_for(future, timeout=timeout)
            
            if response.get("error"):
                raise Exception(response["error"])
            
            return response.get("payload", response)
            
        except asyncio.TimeoutError:
            logger.error(f"Metadata request timeout: {request_type}")
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
                        pass
                    except Exception as e:
                        logger.error(f"Error processing reply: {e}")
                
                if not message:
                    await asyncio.sleep(0.01)
                    
        except asyncio.CancelledError:
            pass
        except Exception as e:
            if self._running:
                logger.error(f"Reply listener error: {e}")
    
    async def get_metric_definition(
        self,
        code: str,
        timeout: Optional[float] = None
    ) -> Optional[Dict[str, Any]]:
        """Get a metric/KPI definition by code."""
        try:
            result = await self._request(
                request_type="get_metric_definition",
                payload={"code": code},
                timeout=timeout
            )
            return result.get("definition")
        except Exception as e:
            logger.warning(f"Failed to get metric definition {code}: {e}")
            return None
    
    async def get_entity_definition(
        self,
        code: str,
        timeout: Optional[float] = None
    ) -> Optional[Dict[str, Any]]:
        """Get an entity definition by code."""
        try:
            result = await self._request(
                request_type="get_entity_definition",
                payload={"code": code},
                timeout=timeout
            )
            return result.get("definition")
        except Exception as e:
            logger.warning(f"Failed to get entity definition {code}: {e}")
            return None
    
    async def list_definitions(
        self,
        kind: Optional[str] = None,
        limit: int = 100,
        offset: int = 0,
        timeout: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """List definitions by kind."""
        try:
            result = await self._request(
                request_type="list_definitions",
                payload={
                    "kind": kind,
                    "limit": limit,
                    "offset": offset
                },
                timeout=timeout
            )
            return result.get("definitions", [])
        except Exception as e:
            logger.warning(f"Failed to list definitions: {e}")
            return []
