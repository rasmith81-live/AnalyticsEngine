"""
Knowledge Graph MCP Server for Database Service.

Provides MCP-compatible endpoints for knowledge graph operations,
enabling AI agents to manage ontology entities and relationships.
"""

from __future__ import annotations

import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from .knowledge_graph_models import KGToolResponse, EntityType, RelationType
from .knowledge_graph_manager import KnowledgeGraphManager
from .knowledge_graph_mcp_tools import (
    BaseKGTool,
    CreateEntityTool,
    CreateRelationTool,
    SearchNodesTool,
    GetEntityContextTool,
    GetLineageTool,
    OpenNodesTool,
    AddObservationsTool,
    ALL_KNOWLEDGE_GRAPH_TOOLS,
)

if TYPE_CHECKING:
    from ..database_manager import DatabaseManager
    from ..messaging_client import MessagingClient

logger = logging.getLogger(__name__)


class KGToolRequest(BaseModel):
    """Request model for Knowledge Graph MCP tool calls."""
    tool_name: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    correlation_id: Optional[str] = None


class KGServerInfo(BaseModel):
    """Information about the Knowledge Graph MCP server."""
    name: str = "knowledge-graph-mcp"
    version: str = "1.0.0"
    description: str = "Knowledge Graph MCP Server for ontology and relationship management"
    tools: List[Dict[str, Any]] = Field(default_factory=list)
    entity_types: List[str] = Field(default_factory=list)
    relation_types: List[str] = Field(default_factory=list)


class KGToolListResponse(BaseModel):
    """Response listing available tools."""
    tools: List[Dict[str, Any]]


class KGHealthResponse(BaseModel):
    """Health check response."""
    status: str
    timestamp: datetime
    database_connected: bool
    tables_initialized: bool


class KnowledgeGraphMCPServer:
    """
    MCP Server for Knowledge Graph operations.
    
    Provides tools for managing ontology entities (value chains, modules,
    KPIs, entities) and their relationships for use by AI agents.
    """
    
    def __init__(
        self,
        database_manager: "DatabaseManager",
        messaging_client: Optional["MessagingClient"] = None
    ):
        """
        Initialize the Knowledge Graph MCP server.
        
        Args:
            database_manager: Database manager instance
            messaging_client: Optional messaging client for event publishing
        """
        self.db_manager = database_manager
        self.messaging_client = messaging_client
        self.kg_manager = KnowledgeGraphManager(database_manager)
        self.router = APIRouter(prefix="/mcp/knowledge", tags=["MCP - Knowledge Graph"])
        self._tools: Dict[str, BaseKGTool] = {}
        self._setup_routes()
        self._initialized = False
    
    async def initialize(self) -> None:
        """Initialize the knowledge graph tables and tools."""
        if self._initialized:
            return
        
        await self.kg_manager.initialize()
        self._register_tools()
        self._initialized = True
        logger.info("Knowledge Graph MCP Server initialized")
    
    def _register_tools(self) -> None:
        """Register all Knowledge Graph MCP tools."""
        for tool_class in ALL_KNOWLEDGE_GRAPH_TOOLS:
            tool = tool_class(self.kg_manager)
            self._tools[tool.name] = tool
            logger.info(f"Registered KG MCP tool: {tool.name}")
    
    def _setup_routes(self) -> None:
        """Set up FastAPI routes for MCP protocol."""
        
        @self.router.get("/info", response_model=KGServerInfo)
        async def get_server_info():
            """Get MCP server information and available tools."""
            await self.initialize()
            return KGServerInfo(
                tools=[tool.get_schema() for tool in self._tools.values()],
                entity_types=[e.value for e in EntityType],
                relation_types=[r.value for r in RelationType]
            )
        
        @self.router.get("/tools", response_model=KGToolListResponse)
        async def list_tools():
            """List all available MCP tools."""
            await self.initialize()
            return KGToolListResponse(
                tools=[tool.get_schema() for tool in self._tools.values()]
            )
        
        @self.router.get("/tools/{tool_name}")
        async def get_tool_schema(tool_name: str):
            """Get schema for a specific tool."""
            await self.initialize()
            tool = self._tools.get(tool_name)
            if not tool:
                raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
            return tool.get_schema()
        
        @self.router.post("/tools/{tool_name}/execute", response_model=KGToolResponse)
        async def execute_tool(tool_name: str, request: KGToolRequest):
            """Execute a Knowledge Graph MCP tool."""
            await self.initialize()
            
            tool = self._tools.get(tool_name)
            if not tool:
                raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
            
            correlation_id = request.correlation_id or str(uuid.uuid4())
            logger.info(f"Executing KG MCP tool '{tool_name}' [correlation_id={correlation_id}]")
            
            try:
                response = await tool.execute(request.parameters)
                response.correlation_id = correlation_id
                
                # Publish event for write operations
                if self.messaging_client and tool_name in ["create_entity", "create_relation", "add_observations"]:
                    await self._publish_change_event(tool_name, request.parameters, response)
                
                return response
            except Exception as e:
                logger.error(f"KG MCP tool '{tool_name}' failed: {e}")
                return KGToolResponse(
                    success=False,
                    error=str(e),
                    correlation_id=correlation_id
                )
        
        @self.router.post("/execute", response_model=KGToolResponse)
        async def execute_tool_generic(request: KGToolRequest):
            """Execute a Knowledge Graph MCP tool by name in request body."""
            await self.initialize()
            
            tool = self._tools.get(request.tool_name)
            if not tool:
                raise HTTPException(
                    status_code=404,
                    detail=f"Tool '{request.tool_name}' not found"
                )
            
            correlation_id = request.correlation_id or str(uuid.uuid4())
            logger.info(f"Executing KG MCP tool '{request.tool_name}' [correlation_id={correlation_id}]")
            
            try:
                response = await tool.execute(request.parameters)
                response.correlation_id = correlation_id
                
                # Publish event for write operations
                if self.messaging_client and request.tool_name in ["create_entity", "create_relation", "add_observations"]:
                    await self._publish_change_event(request.tool_name, request.parameters, response)
                
                return response
            except Exception as e:
                logger.error(f"KG MCP tool '{request.tool_name}' failed: {e}")
                return KGToolResponse(
                    success=False,
                    error=str(e),
                    correlation_id=correlation_id
                )
        
        @self.router.get("/health", response_model=KGHealthResponse)
        async def health_check():
            """Check Knowledge Graph MCP server health."""
            try:
                await self.initialize()
                return KGHealthResponse(
                    status="healthy",
                    timestamp=datetime.utcnow(),
                    database_connected=True,
                    tables_initialized=self._initialized
                )
            except Exception as e:
                logger.error(f"KG MCP health check failed: {e}")
                return KGHealthResponse(
                    status="unhealthy",
                    timestamp=datetime.utcnow(),
                    database_connected=False,
                    tables_initialized=False
                )
        
        @self.router.get("/entity-types")
        async def list_entity_types():
            """List all supported entity types."""
            return {"entity_types": [e.value for e in EntityType]}
        
        @self.router.get("/relation-types")
        async def list_relation_types():
            """List all supported relation types."""
            return {"relation_types": [r.value for r in RelationType]}
    
    async def _publish_change_event(
        self,
        tool_name: str,
        params: Dict[str, Any],
        response: KGToolResponse
    ) -> None:
        """Publish a change event to the messaging service."""
        if not self.messaging_client or not response.success:
            return
        
        try:
            event_type_map = {
                "create_entity": "knowledge.entity_created",
                "create_relation": "knowledge.relation_created",
                "add_observations": "knowledge.observation_added",
            }
            
            event_type = event_type_map.get(tool_name)
            if not event_type:
                return
            
            await self.messaging_client.publish(
                channel=event_type,
                message={
                    "event_type": event_type,
                    "tool": tool_name,
                    "parameters": params,
                    "result": response.data,
                    "timestamp": datetime.utcnow().isoformat(),
                    "correlation_id": response.correlation_id
                }
            )
            logger.debug(f"Published {event_type} event")
            
        except Exception as e:
            logger.warning(f"Failed to publish change event: {e}")
    
    def get_tool(self, tool_name: str) -> Optional[BaseKGTool]:
        """Get a tool by name."""
        return self._tools.get(tool_name)
    
    def list_tools(self) -> List[str]:
        """List all available tool names."""
        return list(self._tools.keys())
    
    async def execute_tool(
        self,
        tool_name: str,
        params: Dict[str, Any],
        correlation_id: Optional[str] = None
    ) -> KGToolResponse:
        """
        Execute a tool directly (for programmatic access).
        
        Args:
            tool_name: Name of the tool to execute
            params: Tool parameters
            correlation_id: Optional correlation ID for tracing
            
        Returns:
            KGToolResponse with results
        """
        await self.initialize()
        
        tool = self._tools.get(tool_name)
        if not tool:
            return KGToolResponse(
                success=False,
                error=f"Tool '{tool_name}' not found",
                correlation_id=correlation_id
            )
        
        try:
            response = await tool.execute(params)
            response.correlation_id = correlation_id
            
            # Publish event for write operations
            if self.messaging_client and tool_name in ["create_entity", "create_relation", "add_observations"]:
                await self._publish_change_event(tool_name, params, response)
            
            return response
        except Exception as e:
            logger.error(f"KG MCP tool '{tool_name}' failed: {e}")
            return KGToolResponse(
                success=False,
                error=str(e),
                correlation_id=correlation_id
            )


# Singleton instance holder
_knowledge_graph_mcp_server: Optional[KnowledgeGraphMCPServer] = None


def get_knowledge_graph_mcp_server(
    db_manager: "DatabaseManager",
    messaging_client: Optional["MessagingClient"] = None
) -> KnowledgeGraphMCPServer:
    """Get or create the Knowledge Graph MCP server instance."""
    global _knowledge_graph_mcp_server
    
    if _knowledge_graph_mcp_server is None:
        _knowledge_graph_mcp_server = KnowledgeGraphMCPServer(db_manager, messaging_client)
    
    return _knowledge_graph_mcp_server


def create_knowledge_graph_mcp_router(
    db_manager: "DatabaseManager",
    messaging_client: Optional["MessagingClient"] = None
) -> APIRouter:
    """Create and return the Knowledge Graph MCP router for inclusion in the main app."""
    server = get_knowledge_graph_mcp_server(db_manager, messaging_client)
    return server.router
