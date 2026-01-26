"""
PostgreSQL MCP Client for connecting to the database service's PostgreSQL MCP Server.

This client provides agents with access to database introspection tools.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

import httpx
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class PostgresMCPClient:
    """
    Client for PostgreSQL MCP Server.
    
    Provides access to database introspection tools for AI agents.
    """
    
    def __init__(
        self,
        base_url: str = "http://database_service:8000",
        timeout: float = 30.0
    ):
        """
        Initialize the PostgreSQL MCP client.
        
        Args:
            base_url: Base URL of the database service
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")
        self.mcp_url = f"{self.base_url}/mcp/postgres"
        self.timeout = timeout
        self._client: Optional[httpx.AsyncClient] = None
        self._tools_cache: Optional[List[Dict[str, Any]]] = None
    
    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the HTTP client."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=self.timeout,
                headers={"Content-Type": "application/json"}
            )
        return self._client
    
    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client and not self._client.is_closed:
            await self._client.aclose()
    
    async def connect(self) -> bool:
        """Test connection to the MCP server."""
        try:
            client = await self._get_client()
            response = await client.get(f"{self.mcp_url}/health")
            response.raise_for_status()
            data = response.json()
            return data.get("status") == "healthy"
        except Exception as e:
            logger.error(f"PostgreSQL MCP connection failed: {e}")
            return False
    
    async def get_tools(self) -> List[Dict[str, Any]]:
        """Get available tools from the MCP server."""
        if self._tools_cache:
            return self._tools_cache
        
        try:
            client = await self._get_client()
            response = await client.get(f"{self.mcp_url}/tools")
            response.raise_for_status()
            data = response.json()
            self._tools_cache = data.get("tools", [])
            return self._tools_cache
        except Exception as e:
            logger.error(f"Failed to get PostgreSQL MCP tools: {e}")
            return []
    
    async def execute(
        self,
        tool_name: str,
        params: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute a PostgreSQL MCP tool.
        
        Args:
            tool_name: Name of the tool to execute
            params: Tool parameters
            correlation_id: Optional correlation ID for tracing
            
        Returns:
            Tool execution result
        """
        try:
            client = await self._get_client()
            response = await client.post(
                f"{self.mcp_url}/tools/{tool_name}/execute",
                json={
                    "tool_name": tool_name,
                    "parameters": params,
                    "correlation_id": correlation_id
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"PostgreSQL MCP tool '{tool_name}' failed: {e.response.status_code}")
            return {
                "success": False,
                "error": f"HTTP {e.response.status_code}: {e.response.text}",
                "correlation_id": correlation_id
            }
        except Exception as e:
            logger.error(f"PostgreSQL MCP tool '{tool_name}' failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "correlation_id": correlation_id
            }
    
    # Convenience methods for common operations
    
    async def list_schemas(self, include_system: bool = False) -> Dict[str, Any]:
        """List database schemas."""
        return await self.execute("list_schemas", {"include_system": include_system})
    
    async def list_tables(
        self,
        schema_name: str = "public",
        include_views: bool = True,
        table_pattern: Optional[str] = None
    ) -> Dict[str, Any]:
        """List tables in a schema."""
        params = {
            "schema_name": schema_name,
            "include_views": include_views
        }
        if table_pattern:
            params["table_pattern"] = table_pattern
        return await self.execute("list_tables", params)
    
    async def describe_table(
        self,
        table_name: str,
        schema_name: str = "public",
        include_indexes: bool = True,
        include_constraints: bool = True
    ) -> Dict[str, Any]:
        """Get detailed table information."""
        return await self.execute("describe_table", {
            "table_name": table_name,
            "schema_name": schema_name,
            "include_indexes": include_indexes,
            "include_constraints": include_constraints
        })
    
    async def list_hypertables(self, schema_name: Optional[str] = None) -> Dict[str, Any]:
        """List TimescaleDB hypertables."""
        params = {}
        if schema_name:
            params["schema_name"] = schema_name
        return await self.execute("list_hypertables", params)
    
    async def query_sample(
        self,
        table_name: str,
        schema_name: str = "public",
        limit: int = 10,
        columns: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Get sample data from a table."""
        params = {
            "table_name": table_name,
            "schema_name": schema_name,
            "limit": limit
        }
        if columns:
            params["columns"] = columns
        return await self.execute("query_sample", params)
    
    async def explain_query(
        self,
        query: str,
        analyze: bool = True
    ) -> Dict[str, Any]:
        """Explain a query execution plan."""
        return await self.execute("explain_query", {
            "query": query,
            "analyze": analyze
        })
    
    async def get_table_stats(
        self,
        table_name: str,
        schema_name: str = "public"
    ) -> Dict[str, Any]:
        """Get table statistics."""
        return await self.execute("get_table_stats", {
            "table_name": table_name,
            "schema_name": schema_name
        })
