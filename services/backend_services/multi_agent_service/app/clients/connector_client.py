# =============================================================================
# Connector Event Client for Multi-Agent Service
# Redis-based client for connector_service communication
# =============================================================================
"""
Event client for agents to interact with connector_service.

Replaces HTTP calls with Redis Streams for:
- Data fetching from sources
- Connection testing
- Source listing
"""

import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add shared path for imports
shared_path = Path(__file__).parent.parent.parent.parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from events.schemas import CommandType
from events.redis_client import BaseEventClient

logger = logging.getLogger(__name__)


class ConnectorEventClient(BaseEventClient):
    """
    Redis-based client for connector_service.
    
    Used by agents to fetch data from external sources via Redis Streams.
    """
    
    def __init__(self, redis_url: Optional[str] = None, timeout: float = 60.0):
        super().__init__(
            service_name="multi_agent_service",
            target_service="connector_service",
            redis_url=redis_url,
            timeout=timeout
        )
    
    async def fetch_data(
        self,
        source_code: str,
        query: Optional[str] = None,
        parameters: Optional[Dict[str, Any]] = None,
        time_range: Optional[Dict[str, str]] = None,
        limit: int = 1000,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Fetch data from a configured source.
        
        Args:
            source_code: Code of the data source
            query: Optional query string
            parameters: Query parameters
            time_range: Optional time range
            limit: Maximum rows to return
            session_id: Session ID for tracing
            
        Returns:
            Data result with rows and metadata
        """
        return await self.send_command(
            CommandType.FETCH_DATA,
            {
                "source_code": source_code,
                "query": query,
                "parameters": parameters or {},
                "time_range": time_range,
                "limit": limit
            },
            session_id=session_id,
            timeout=60.0
        )
    
    async def test_connection(
        self,
        source_code: str,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Test connection to a data source.
        
        Args:
            source_code: Code of the data source to test
            session_id: Session ID for tracing
            
        Returns:
            Connection status
        """
        return await self.send_command(
            CommandType.TEST_CONNECTION,
            {"source_code": source_code},
            session_id=session_id,
            timeout=30.0
        )
    
    async def list_sources(
        self,
        source_type: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        List available data sources.
        
        Args:
            source_type: Optional filter by type
            session_id: Session ID for tracing
            
        Returns:
            List of data sources
        """
        try:
            result = await self.send_command(
                CommandType.LIST_SOURCES,
                {"source_type": source_type},
                session_id=session_id
            )
            return result.get("sources", [])
        except Exception as e:
            logger.warning(f"Failed to list sources: {e}")
            return []
    
    async def fetch_data_with_fallback(
        self,
        source_code: str,
        query: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Fetch data with fallback on failure."""
        return await self.send_command_with_fallback(
            CommandType.FETCH_DATA,
            {"source_code": source_code, "query": query},
            fallback={
                "source_code": source_code,
                "rows": [],
                "error": "Connector service unavailable"
            },
            session_id=session_id
        )


# Singleton instance
_connector_client: Optional[ConnectorEventClient] = None


def get_connector_client() -> ConnectorEventClient:
    """Get singleton connector client."""
    global _connector_client
    if _connector_client is None:
        _connector_client = ConnectorEventClient()
    return _connector_client
