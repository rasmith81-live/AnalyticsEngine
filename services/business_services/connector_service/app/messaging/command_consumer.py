# =============================================================================
# Connector Command Consumer
# Processes data commands from multi_agent_service via Redis Streams
# =============================================================================
"""
Command consumer for connector_service.

Handles:
- Data fetching from sources
- Connection testing
- Source listing
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add shared path for imports
shared_path = Path(__file__).parent.parent.parent.parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from events.schemas import ServiceCommand, CommandType, ResponseType
from events.consumer import BaseCommandConsumer

logger = logging.getLogger(__name__)


class ConnectorCommandConsumer(BaseCommandConsumer):
    """
    Command consumer for connector_service.
    
    Processes data fetch commands from other services via Redis Streams.
    """
    
    def __init__(
        self,
        connector_manager,
        redis_url: Optional[str] = None
    ):
        """
        Initialize consumer.
        
        Args:
            connector_manager: The connector manager instance
            redis_url: Redis connection URL
        """
        super().__init__(
            service_name="connector",
            redis_url=redis_url
        )
        self.connector_manager = connector_manager
    
    async def _register_handlers(self) -> None:
        """Register command handlers."""
        self.register_handler(CommandType.FETCH_DATA, self._handle_fetch_data)
        self.register_handler(CommandType.TEST_CONNECTION, self._handle_test_connection)
        self.register_handler(CommandType.LIST_SOURCES, self._handle_list_sources)
        self.register_handler(CommandType.HEALTH_CHECK, self._handle_health_check)
        
        logger.info("Registered connector command handlers")
    
    async def _handle_fetch_data(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle data fetch request."""
        payload = command.payload
        source_code = payload.get("source_code")
        query = payload.get("query")
        parameters = payload.get("parameters", {})
        time_range = payload.get("time_range")
        limit = payload.get("limit", 1000)
        
        logger.info(f"Fetching data from source: {source_code}")
        
        try:
            result = await self.connector_manager.fetch_data(
                source_code=source_code,
                query=query,
                parameters=parameters,
                time_range=time_range,
                limit=limit
            )
            
            return {
                "source_code": source_code,
                "rows": result.get("rows", []),
                "columns": result.get("columns", []),
                "row_count": result.get("row_count", 0),
                "metadata": result.get("metadata", {})
            }
        except Exception as e:
            logger.error(f"Data fetch failed for {source_code}: {e}")
            raise
    
    async def _handle_test_connection(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle connection test request."""
        payload = command.payload
        source_code = payload.get("source_code")
        
        logger.info(f"Testing connection to source: {source_code}")
        
        try:
            result = await self.connector_manager.test_connection(source_code)
            
            return {
                "source_code": source_code,
                "connected": result.get("connected", False),
                "latency_ms": result.get("latency_ms"),
                "error": result.get("error")
            }
        except Exception as e:
            logger.error(f"Connection test failed for {source_code}: {e}")
            return {
                "source_code": source_code,
                "connected": False,
                "error": str(e)
            }
    
    async def _handle_list_sources(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle list sources request."""
        payload = command.payload
        source_type = payload.get("source_type")
        
        try:
            sources = await self.connector_manager.list_sources(source_type=source_type)
            
            return {
                "sources": [
                    {
                        "code": s.code,
                        "name": s.name,
                        "type": s.source_type,
                        "status": s.status
                    }
                    for s in sources
                ],
                "count": len(sources)
            }
        except Exception as e:
            logger.error(f"Failed to list sources: {e}")
            return {"sources": [], "count": 0, "error": str(e)}
    
    async def _handle_health_check(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle health check."""
        return {
            "service": "connector_service",
            "status": "healthy",
            "consumer": self.consumer_name
        }
