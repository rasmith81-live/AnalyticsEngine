"""
MCP Client Manager for the Agent System.

Manages connections to all MCP servers and provides tools to agents
based on their roles.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from .mcp_config import MCPConfig
from .postgres_mcp_client import PostgresMCPClient
from .knowledge_graph_mcp_client import KnowledgeGraphMCPClient
from .exa_search_client import ExaSearchClient

if TYPE_CHECKING:
    from ..agents.base_agent import AgentRole

logger = logging.getLogger(__name__)


# Agent role to MCP tool mapping
# NOTE: Tool names use underscores (not periods) to comply with Anthropic's naming pattern
AGENT_MCP_ACCESS = {
    "coordinator": [
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
        "knowledge_open_nodes",
    ],
    "architect": [
        "postgres_list_schemas",
        "postgres_list_tables",
        "postgres_describe_table",
        "postgres_get_table_stats",
        "postgres_list_hypertables",
        "knowledge_search_nodes",
        "knowledge_get_lineage",
        "knowledge_get_entity_context",
    ],
    "developer": [
        "postgres_list_tables",
        "postgres_describe_table",
        "postgres_list_hypertables",
        "postgres_list_continuous_aggregates",
        "knowledge_get_entity_context",
        "knowledge_search_nodes",
    ],
    "data_analyst": [
        "postgres_query_sample",
        "postgres_explain_query",
        "postgres_list_continuous_aggregates",
        "postgres_list_hypertables",
        "postgres_describe_table",
        "knowledge_get_lineage",
        "knowledge_search_nodes",
    ],
    "tester": [
        "postgres_query_sample",
        "postgres_describe_table",
        "postgres_get_table_stats",
    ],
    "business_analyst": [
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
        "knowledge_create_entity",
        "knowledge_create_relation",
        "knowledge_add_observations",
    ],
    "business_strategist": [
        "knowledge_create_entity",
        "knowledge_create_relation",
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
        "web_search_search_web",
        "web_search_search_companies",
    ],
    "competitive_analyst": [
        "web_search_search_web",
        "web_search_search_companies",
        "web_search_search_news",
        "web_search_find_similar",
        "web_search_get_contents",
        "knowledge_search_nodes",
    ],
    "marketing_manager": [
        "web_search_search_web",
        "web_search_search_news",
        "web_search_search_companies",
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
    ],
    "project_manager": [
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
    ],
    "documenter": [
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
        "knowledge_get_lineage",
        "postgres_describe_table",
    ],
    "deployment_specialist": [
        "postgres_list_schemas",
        "postgres_list_tables",
        "postgres_list_hypertables",
    ],
    "librarian_curator": [
        "knowledge_create_entity",
        "knowledge_create_relation",
        "knowledge_search_nodes",
        "knowledge_get_entity_context",
        "knowledge_get_lineage",
        "knowledge_open_nodes",
        "knowledge_add_observations",
        "postgres_list_schemas",
        "postgres_list_tables",
        "postgres_describe_table",
        "web_search_search_web",
        "web_search_get_contents",
    ],
}


class MCPToolDefinition:
    """Definition of an MCP tool for agent use."""
    
    def __init__(
        self,
        name: str,
        description: str,
        input_schema: Dict[str, Any],
        client_name: str,
        tool_name: str
    ):
        self.name = name
        self.description = description
        self.input_schema = input_schema
        self.client_name = client_name
        self.tool_name = tool_name
    
    def get_schema(self) -> Dict[str, Any]:
        """Get schema for Claude tool registration."""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.input_schema
        }


class MCPClientManager:
    """
    Manages MCP client connections for the agent system.
    
    Provides a unified interface for agents to access MCP tools
    based on their roles.
    """
    
    def __init__(self, config: Optional[MCPConfig] = None):
        """
        Initialize the MCP client manager.
        
        Args:
            config: MCP configuration (defaults to env-based config)
        """
        self.config = config or MCPConfig.from_env()
        self._clients: Dict[str, Any] = {}
        self._tools: Dict[str, MCPToolDefinition] = {}
        self._initialized = False
    
    async def initialize(self) -> None:
        """Initialize all MCP clients."""
        if self._initialized:
            return
        
        logger.info("Initializing MCP Client Manager...")
        
        # Initialize PostgreSQL MCP client
        if self.config.postgres_mcp_enabled:
            try:
                self._clients["postgres"] = PostgresMCPClient(
                    base_url=self.config.database_service_url,
                    timeout=self.config.request_timeout
                )
                connected = await self._clients["postgres"].connect()
                if connected:
                    await self._register_postgres_tools()
                    logger.info("PostgreSQL MCP client connected")
                else:
                    logger.warning("PostgreSQL MCP client failed to connect")
            except Exception as e:
                logger.error(f"Failed to initialize PostgreSQL MCP client: {e}")
        
        # Initialize Knowledge Graph MCP client
        if self.config.knowledge_mcp_enabled:
            try:
                self._clients["knowledge"] = KnowledgeGraphMCPClient(
                    base_url=self.config.database_service_url,
                    timeout=self.config.request_timeout
                )
                connected = await self._clients["knowledge"].connect()
                if connected:
                    await self._register_knowledge_tools()
                    logger.info("Knowledge Graph MCP client connected")
                else:
                    logger.warning("Knowledge Graph MCP client failed to connect")
            except Exception as e:
                logger.error(f"Failed to initialize Knowledge Graph MCP client: {e}")
        
        # Initialize Exa Web Search client
        if self.config.web_search_enabled and self.config.exa_api_key:
            try:
                self._clients["web_search"] = ExaSearchClient(
                    api_key=self.config.exa_api_key,
                    rate_limit=self.config.web_search_rate_limit,
                    cache_ttl=self.config.web_search_cache_ttl,
                    timeout=self.config.request_timeout
                )
                await self._register_web_search_tools()
                logger.info("Exa Web Search client initialized")
            except Exception as e:
                logger.error(f"Failed to initialize Exa Web Search client: {e}")
        elif self.config.web_search_enabled and not self.config.exa_api_key:
            logger.warning("Web search enabled but EXA_API_KEY not set")
        
        self._initialized = True
        logger.info(f"MCP Client Manager initialized with {len(self._tools)} tools")
    
    async def _register_postgres_tools(self) -> None:
        """Register PostgreSQL MCP tools."""
        client = self._clients.get("postgres")
        if not client:
            return
        
        tools = await client.get_tools()
        for tool in tools:
            tool_def = MCPToolDefinition(
                name=f"postgres_{tool['name']}",
                description=tool.get("description", ""),
                input_schema=tool.get("input_schema", {}),
                client_name="postgres",
                tool_name=tool["name"]
            )
            self._tools[tool_def.name] = tool_def
    
    async def _register_knowledge_tools(self) -> None:
        """Register Knowledge Graph MCP tools."""
        client = self._clients.get("knowledge")
        if not client:
            return
        
        tools = await client.get_tools()
        for tool in tools:
            tool_def = MCPToolDefinition(
                name=f"knowledge_{tool['name']}",
                description=tool.get("description", ""),
                input_schema=tool.get("input_schema", {}),
                client_name="knowledge",
                tool_name=tool["name"]
            )
            self._tools[tool_def.name] = tool_def
    
    async def _register_web_search_tools(self) -> None:
        """Register Exa Web Search tools."""
        client = self._clients.get("web_search")
        if not client:
            return
        
        tools = client.get_tools()
        for tool in tools:
            tool_def = MCPToolDefinition(
                name=f"web_search_{tool['name']}",
                description=tool.get("description", ""),
                input_schema=tool.get("input_schema", {}),
                client_name="web_search",
                tool_name=tool["name"]
            )
            self._tools[tool_def.name] = tool_def
    
    def get_tools_for_agent(self, agent_role: str) -> List[MCPToolDefinition]:
        """
        Get MCP tools available to a specific agent role.
        
        Args:
            agent_role: The agent's role (e.g., 'architect', 'developer')
            
        Returns:
            List of tool definitions available to the agent
        """
        # Normalize role name
        role = agent_role.lower().replace(" ", "_")
        
        # Get allowed tools for this role
        allowed_tools = AGENT_MCP_ACCESS.get(role, [])
        
        # Return matching tool definitions
        return [
            self._tools[name]
            for name in allowed_tools
            if name in self._tools
        ]
    
    def get_tool_schemas_for_agent(self, agent_role: str) -> List[Dict[str, Any]]:
        """
        Get tool schemas formatted for Claude tool registration.
        
        Args:
            agent_role: The agent's role
            
        Returns:
            List of tool schemas for Claude
        """
        tools = self.get_tools_for_agent(agent_role)
        return [tool.get_schema() for tool in tools]
    
    async def execute_tool(
        self,
        tool_name: str,
        params: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Execute an MCP tool.
        
        Args:
            tool_name: Full tool name (e.g., 'postgres.list_tables')
            params: Tool parameters
            correlation_id: Optional correlation ID for tracing
            
        Returns:
            Tool execution result
        """
        if not self._initialized:
            await self.initialize()
        
        tool_def = self._tools.get(tool_name)
        if not tool_def:
            return {
                "success": False,
                "error": f"Tool '{tool_name}' not found"
            }
        
        client = self._clients.get(tool_def.client_name)
        if not client:
            return {
                "success": False,
                "error": f"Client '{tool_def.client_name}' not available"
            }
        
        try:
            if tool_def.client_name == "web_search":
                # Exa client uses different signature
                return await client.execute(tool_def.tool_name, params)
            else:
                # PostgreSQL and Knowledge Graph clients
                return await client.execute(
                    tool_def.tool_name,
                    params,
                    correlation_id=correlation_id
                )
        except Exception as e:
            logger.error(f"Tool execution failed: {tool_name} - {e}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_client(self, name: str) -> Optional[Any]:
        """Get a specific MCP client."""
        return self._clients.get(name)
    
    def list_all_tools(self) -> List[str]:
        """List all available tool names."""
        return list(self._tools.keys())
    
    def list_clients(self) -> List[str]:
        """List all connected clients."""
        return list(self._clients.keys())
    
    async def close(self) -> None:
        """Close all client connections."""
        for name, client in self._clients.items():
            try:
                if hasattr(client, "close"):
                    await client.close()
                logger.debug(f"Closed MCP client: {name}")
            except Exception as e:
                logger.warning(f"Error closing MCP client {name}: {e}")
        
        self._clients.clear()
        self._tools.clear()
        self._initialized = False
        logger.info("MCP Client Manager closed")


# Global instance
_mcp_manager: Optional[MCPClientManager] = None


async def get_mcp_manager(config: Optional[MCPConfig] = None) -> MCPClientManager:
    """Get or create the global MCP client manager."""
    global _mcp_manager
    
    if _mcp_manager is None:
        _mcp_manager = MCPClientManager(config)
        await _mcp_manager.initialize()
    
    return _mcp_manager
