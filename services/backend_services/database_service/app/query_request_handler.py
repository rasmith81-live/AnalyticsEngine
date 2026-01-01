"""
Query Request Handler for Database Service.

Handles database query and command requests received via pub/sub messaging,
enabling event-driven database access for other services.
"""

import logging
from typing import Any, Dict

from .database_manager import DatabaseManager
from .request_reply import RequestReplyServer

logger = logging.getLogger(__name__)

# Request channels
CHANNEL_DATABASE_QUERY = "database.query"
CHANNEL_DATABASE_COMMAND = "database.command"


class QueryRequestHandler:
    """
    Handles database query/command requests via pub/sub.
    
    Enables services to execute database operations without direct HTTP calls,
    maintaining the event-driven architecture.
    """
    
    def __init__(
        self,
        database_manager: DatabaseManager,
        redis_url: str
    ):
        self.database_manager = database_manager
        self.server = RequestReplyServer(
            redis_url=redis_url,
            service_name="database_service"
        )
    
    async def start(self) -> None:
        """Start handling query requests."""
        await self.server.connect()
        
        # Register handlers
        await self.server.register_handler(
            CHANNEL_DATABASE_QUERY,
            self._handle_query_request
        )
        await self.server.register_handler(
            CHANNEL_DATABASE_COMMAND,
            self._handle_command_request
        )
        
        logger.info("QueryRequestHandler started")
    
    async def stop(self) -> None:
        """Stop handling query requests."""
        await self.server.disconnect()
        logger.info("QueryRequestHandler stopped")
    
    async def _handle_query_request(
        self,
        request_type: str,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Handle a database query request.
        
        Request types:
        - execute_query: Execute a read query
        - get_entity: Get entity by ID
        - list_entities: List entities with filters
        """
        try:
            if request_type == "execute_query":
                return await self._execute_query(payload)
            elif request_type == "get_entity":
                return await self._get_entity(payload)
            elif request_type == "list_entities":
                return await self._list_entities(payload)
            else:
                raise ValueError(f"Unknown query request type: {request_type}")
                
        except Exception as e:
            logger.error(f"Query request failed: {e}")
            raise
    
    async def _handle_command_request(
        self,
        request_type: str,
        payload: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Handle a database command request.
        
        Request types:
        - execute_command: Execute a write command
        - insert_record: Insert a record
        - update_record: Update a record
        - delete_record: Delete a record
        """
        try:
            if request_type == "execute_command":
                return await self._execute_command(payload)
            elif request_type == "insert_record":
                return await self._insert_record(payload)
            elif request_type == "update_record":
                return await self._update_record(payload)
            elif request_type == "delete_record":
                return await self._delete_record(payload)
            else:
                raise ValueError(f"Unknown command request type: {request_type}")
                
        except Exception as e:
            logger.error(f"Command request failed: {e}")
            raise
    
    async def _execute_query(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a read query."""
        query = payload.get("query")
        parameters = payload.get("parameters", {})
        
        if not query:
            raise ValueError("Query is required")
        
        result = await self.database_manager.execute_query(query, parameters)
        return {"rows": result, "row_count": len(result) if result else 0}
    
    async def _get_entity(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Get entity by ID."""
        table_name = payload.get("table_name")
        entity_id = payload.get("entity_id")
        
        if not table_name or not entity_id:
            raise ValueError("table_name and entity_id are required")
        
        result = await self.database_manager.get_by_id(table_name, entity_id)
        return {"entity": result}
    
    async def _list_entities(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """List entities with filters."""
        table_name = payload.get("table_name")
        filters = payload.get("filters", {})
        limit = payload.get("limit", 100)
        offset = payload.get("offset", 0)
        
        if not table_name:
            raise ValueError("table_name is required")
        
        result = await self.database_manager.list_records(
            table_name, filters, limit, offset
        )
        return {"entities": result, "count": len(result) if result else 0}
    
    async def _execute_command(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a write command."""
        command = payload.get("command")
        parameters = payload.get("parameters", {})
        
        if not command:
            raise ValueError("Command is required")
        
        result = await self.database_manager.execute_command(command, parameters)
        return {"result": result}
    
    async def _insert_record(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Insert a record."""
        table_name = payload.get("table_name")
        record = payload.get("record")
        
        if not table_name or not record:
            raise ValueError("table_name and record are required")
        
        result = await self.database_manager.insert_record(table_name, record)
        return {"inserted": True, "result": result}
    
    async def _update_record(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Update a record."""
        table_name = payload.get("table_name")
        entity_id = payload.get("entity_id")
        updates = payload.get("updates")
        
        if not table_name or not entity_id or not updates:
            raise ValueError("table_name, entity_id, and updates are required")
        
        result = await self.database_manager.update_record(
            table_name, entity_id, updates
        )
        return {"updated": True, "result": result}
    
    async def _delete_record(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Delete a record."""
        table_name = payload.get("table_name")
        entity_id = payload.get("entity_id")
        
        if not table_name or not entity_id:
            raise ValueError("table_name and entity_id are required")
        
        result = await self.database_manager.delete_record(table_name, entity_id)
        return {"deleted": True, "result": result}
