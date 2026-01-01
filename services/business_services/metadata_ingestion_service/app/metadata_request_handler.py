"""
Metadata Request Handler for Metadata Ingestion Service.

Handles metadata lookup requests received via pub/sub messaging,
enabling event-driven metadata access for other services.
"""

import logging
from typing import Any, Dict, Optional
import json

import redis.asyncio as redis

logger = logging.getLogger(__name__)

# Request channel
CHANNEL_METADATA_LOOKUP = "metadata.lookup"


class MetadataRequestHandler:
    """
    Handles metadata lookup requests via pub/sub.
    
    Enables services to fetch KPI definitions, entity definitions, etc.
    without direct HTTP calls, maintaining the event-driven architecture.
    """
    
    def __init__(
        self,
        redis_url: str,
        metadata_store: Any  # Reference to the metadata storage
    ):
        self.redis_url = redis_url
        self.metadata_store = metadata_store
        self._redis: Optional[redis.Redis] = None
        self._pubsub: Optional[redis.client.PubSub] = None
        self._running = False
        self._listener_task = None
    
    async def start(self) -> None:
        """Start handling metadata requests."""
        if self._running:
            return
        
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        await self._redis.ping()
        
        self._pubsub = self._redis.pubsub()
        await self._pubsub.subscribe(CHANNEL_METADATA_LOOKUP)
        
        self._running = True
        self._listener_task = asyncio.create_task(self._handle_requests())
        
        logger.info("MetadataRequestHandler started")
    
    async def stop(self) -> None:
        """Stop handling metadata requests."""
        self._running = False
        
        if self._listener_task:
            self._listener_task.cancel()
            try:
                await self._listener_task
            except asyncio.CancelledError:
                pass
        
        if self._pubsub:
            await self._pubsub.close()
        
        if self._redis:
            await self._redis.close()
        
        logger.info("MetadataRequestHandler stopped")
    
    async def _handle_requests(self) -> None:
        """Listen for and handle metadata requests."""
        import asyncio
        
        try:
            while self._running:
                message = await self._pubsub.get_message(
                    ignore_subscribe_messages=True,
                    timeout=1.0
                )
                
                if message and message["type"] == "message":
                    asyncio.create_task(self._process_request(message["data"]))
                
                if not message:
                    await asyncio.sleep(0.01)
                    
        except asyncio.CancelledError:
            pass
        except Exception as e:
            if self._running:
                logger.error(f"Request handler error: {e}")
    
    async def _process_request(self, data: str) -> None:
        """Process a single metadata request."""
        try:
            request = json.loads(data)
            correlation_id = request.get("correlation_id")
            reply_to = request.get("reply_to")
            request_type = request.get("request_type")
            payload = request.get("payload", {})
            
            if not correlation_id or not reply_to:
                logger.warning("Invalid request: missing correlation_id or reply_to")
                return
            
            try:
                result = await self._handle_lookup(request_type, payload)
                await self._send_response(reply_to, correlation_id, result)
            except Exception as e:
                logger.error(f"Handler error for {request_type}: {e}")
                await self._send_error(reply_to, correlation_id, str(e))
                
        except json.JSONDecodeError:
            logger.warning("Invalid JSON in metadata request")
        except Exception as e:
            logger.error(f"Error processing request: {e}")
    
    async def _handle_lookup(
        self,
        request_type: str,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Handle a metadata lookup request.
        
        Request types:
        - get_metric_definition: Get a KPI/metric definition
        - get_entity_definition: Get an entity definition
        - list_definitions: List definitions by kind
        - search_definitions: Search definitions
        """
        if request_type == "get_metric_definition":
            return await self._get_metric_definition(payload)
        elif request_type == "get_entity_definition":
            return await self._get_entity_definition(payload)
        elif request_type == "list_definitions":
            return await self._list_definitions(payload)
        elif request_type == "search_definitions":
            return await self._search_definitions(payload)
        else:
            raise ValueError(f"Unknown request type: {request_type}")
    
    async def _get_metric_definition(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Get a metric/KPI definition by code."""
        code = payload.get("code")
        if not code:
            raise ValueError("code is required")
        
        # Use metadata store to fetch definition
        definition = await self.metadata_store.get_definition(
            kind="metric_definition",
            code=code
        )
        return {"definition": definition}
    
    async def _get_entity_definition(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Get an entity definition by code."""
        code = payload.get("code")
        if not code:
            raise ValueError("code is required")
        
        definition = await self.metadata_store.get_definition(
            kind="entity_definition",
            code=code
        )
        return {"definition": definition}
    
    async def _list_definitions(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """List definitions by kind."""
        kind = payload.get("kind")
        limit = payload.get("limit", 100)
        offset = payload.get("offset", 0)
        
        definitions = await self.metadata_store.list_definitions(
            kind=kind,
            limit=limit,
            offset=offset
        )
        return {"definitions": definitions, "count": len(definitions)}
    
    async def _search_definitions(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Search definitions."""
        query = payload.get("query", "")
        kind = payload.get("kind")
        limit = payload.get("limit", 100)
        
        definitions = await self.metadata_store.search_definitions(
            query=query,
            kind=kind,
            limit=limit
        )
        return {"definitions": definitions, "count": len(definitions)}
    
    async def _send_response(
        self,
        reply_to: str,
        correlation_id: str,
        payload: Any
    ) -> None:
        """Send a success response."""
        from datetime import datetime
        response = {
            "correlation_id": correlation_id,
            "source": "metadata_service",
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
        from datetime import datetime
        response = {
            "correlation_id": correlation_id,
            "source": "metadata_service",
            "timestamp": datetime.utcnow().isoformat(),
            "error": error
        }
        await self._redis.publish(reply_to, json.dumps(response))


# Import asyncio at module level
import asyncio
