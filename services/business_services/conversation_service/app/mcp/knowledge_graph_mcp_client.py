"""
Knowledge Graph MCP Client for connecting to the database service's Knowledge Graph MCP Server.

This client provides agents with access to ontology and relationship management tools.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional

import httpx

logger = logging.getLogger(__name__)


class KnowledgeGraphMCPClient:
    """
    Client for Knowledge Graph MCP Server.
    
    Provides access to ontology management tools for AI agents.
    """
    
    def __init__(
        self,
        base_url: str = "http://database_service:8000",
        timeout: float = 30.0
    ):
        """
        Initialize the Knowledge Graph MCP client.
        
        Args:
            base_url: Base URL of the database service
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip("/")
        self.mcp_url = f"{self.base_url}/mcp/knowledge"
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
            logger.error(f"Knowledge Graph MCP connection failed: {e}")
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
            logger.error(f"Failed to get Knowledge Graph MCP tools: {e}")
            return []
    
    async def execute(
        self,
        tool_name: str,
        params: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute a Knowledge Graph MCP tool.
        
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
            logger.error(f"Knowledge Graph MCP tool '{tool_name}' failed: {e.response.status_code}")
            return {
                "success": False,
                "error": f"HTTP {e.response.status_code}: {e.response.text}",
                "correlation_id": correlation_id
            }
        except Exception as e:
            logger.error(f"Knowledge Graph MCP tool '{tool_name}' failed: {e}")
            return {
                "success": False,
                "error": str(e),
                "correlation_id": correlation_id
            }
    
    # Convenience methods for common operations
    
    async def create_entity(
        self,
        name: str,
        entity_type: str,
        observations: List[str] = None,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Create a new entity in the knowledge graph."""
        params = {
            "name": name,
            "entity_type": entity_type
        }
        if observations:
            params["observations"] = observations
        if metadata:
            params["metadata"] = metadata
        return await self.execute("create_entity", params)
    
    async def create_relation(
        self,
        from_entity: str,
        to_entity: str,
        relation_type: str,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Create a relationship between entities."""
        params = {
            "from_entity": from_entity,
            "to_entity": to_entity,
            "relation_type": relation_type
        }
        if metadata:
            params["metadata"] = metadata
        return await self.execute("create_relation", params)
    
    async def search_nodes(
        self,
        query: str,
        entity_types: List[str] = None,
        limit: int = 20
    ) -> Dict[str, Any]:
        """Search for entities in the knowledge graph."""
        params = {"query": query, "limit": limit}
        if entity_types:
            params["entity_types"] = entity_types
        return await self.execute("search_nodes", params)
    
    async def get_entity_context(
        self,
        name: str,
        depth: int = 1,
        include_observations: bool = True
    ) -> Dict[str, Any]:
        """Get an entity with its relationships."""
        return await self.execute("get_entity_context", {
            "name": name,
            "depth": depth,
            "include_observations": include_observations
        })
    
    async def get_lineage(
        self,
        entity_name: str,
        direction: str = "upstream",
        max_depth: int = 5,
        relation_types: List[str] = None
    ) -> Dict[str, Any]:
        """Get lineage (dependency chain) for an entity."""
        params = {
            "entity_name": entity_name,
            "direction": direction,
            "max_depth": max_depth
        }
        if relation_types:
            params["relation_types"] = relation_types
        return await self.execute("get_lineage", params)
    
    async def open_nodes(self, names: List[str]) -> Dict[str, Any]:
        """Get multiple entities by name."""
        return await self.execute("open_nodes", {"names": names})
    
    async def add_observations(
        self,
        entity_name: str,
        observations: List[str]
    ) -> Dict[str, Any]:
        """Add observations to an entity."""
        return await self.execute("add_observations", {
            "entity_name": entity_name,
            "observations": observations
        })
