"""
Database Client using Pub/Sub for Calculation Engine Service.

Provides database access via Redis pub/sub request/reply pattern,
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

# Request channels (must match database service handlers)
CHANNEL_DATABASE_QUERY = "database.query"
CHANNEL_DATABASE_COMMAND = "database.command"


class DatabaseClientPubSub:
    """
    Database client using pub/sub for event-driven database access.
    
    Uses request/reply pattern over Redis pub/sub instead of HTTP.
    """
    
    def __init__(
        self,
        redis_url: str,
        service_name: str = "calculation_engine",
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
        
        logger.info(f"DatabaseClientPubSub connected, reply channel: {self._reply_channel}")
    
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
        
        logger.info("DatabaseClientPubSub disconnected")
    
    async def _request(
        self,
        channel: str,
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
            
            await self._redis.publish(channel, json.dumps(message))
            response = await asyncio.wait_for(future, timeout=timeout)
            
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
    
    async def execute_query(
        self,
        query: str,
        parameters: Optional[Dict[str, Any]] = None,
        use_cache: bool = True,
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Execute a read query against the database.
        
        Args:
            query: SQL query to execute
            parameters: Query parameters
            use_cache: Use query result caching
            timeout: Query timeout
            
        Returns:
            Query result with rows and row_count
        """
        return await self._request(
            channel=CHANNEL_DATABASE_QUERY,
            request_type="execute_query",
            payload={
                "query": query,
                "parameters": parameters or {},
                "use_cache": use_cache
            },
            timeout=timeout
        )
    
    async def execute_command(
        self,
        command: str,
        parameters: Optional[Dict[str, Any]] = None,
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Execute a write command against the database.
        
        Args:
            command: SQL command to execute
            parameters: Command parameters
            timeout: Command timeout
            
        Returns:
            Command execution result
        """
        return await self._request(
            channel=CHANNEL_DATABASE_COMMAND,
            request_type="execute_command",
            payload={
                "command": command,
                "parameters": parameters or {}
            },
            timeout=timeout
        )
    
    async def insert_record(
        self,
        table_name: str,
        record: Dict[str, Any],
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """Insert a record into a table."""
        return await self._request(
            channel=CHANNEL_DATABASE_COMMAND,
            request_type="insert_record",
            payload={
                "table_name": table_name,
                "record": record
            },
            timeout=timeout
        )
    
    async def update_record(
        self,
        table_name: str,
        entity_id: str,
        updates: Dict[str, Any],
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """Update a record in a table."""
        return await self._request(
            channel=CHANNEL_DATABASE_COMMAND,
            request_type="update_record",
            payload={
                "table_name": table_name,
                "entity_id": entity_id,
                "updates": updates
            },
            timeout=timeout
        )
    
    async def get_entity(
        self,
        table_name: str,
        entity_id: str,
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """Get an entity by ID."""
        return await self._request(
            channel=CHANNEL_DATABASE_QUERY,
            request_type="get_entity",
            payload={
                "table_name": table_name,
                "entity_id": entity_id
            },
            timeout=timeout
        )
    
    async def list_entities(
        self,
        table_name: str,
        filters: Optional[Dict[str, Any]] = None,
        limit: int = 100,
        offset: int = 0,
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """List entities with optional filters."""
        return await self._request(
            channel=CHANNEL_DATABASE_QUERY,
            request_type="list_entities",
            payload={
                "table_name": table_name,
                "filters": filters or {},
                "limit": limit,
                "offset": offset
            },
            timeout=timeout
        )
