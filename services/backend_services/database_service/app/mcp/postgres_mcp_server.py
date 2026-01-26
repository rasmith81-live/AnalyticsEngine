"""
PostgreSQL MCP Server for Database Service.

Provides MCP-compatible endpoints for database introspection and queries,
enabling AI agents to explore and query the TimescaleDB schema.
"""

from __future__ import annotations

import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field

from .postgres_mcp_models import MCPToolRequest, MCPToolResponse
from .postgres_mcp_tools import (
    BaseMCPTool,
    ListSchemasTool,
    ListTablesTool,
    DescribeTableTool,
    ListHypertablesTool,
    ListContinuousAggregatesTool,
    QuerySampleTool,
    ExplainQueryTool,
    GetTableStatsTool,
    ALL_POSTGRES_TOOLS,
)

if TYPE_CHECKING:
    from ..database_manager import DatabaseManager

logger = logging.getLogger(__name__)


class MCPServerInfo(BaseModel):
    """Information about the MCP server."""
    name: str = "postgres-mcp"
    version: str = "1.0.0"
    description: str = "PostgreSQL/TimescaleDB MCP Server for database introspection"
    tools: List[Dict[str, Any]] = Field(default_factory=list)


class MCPToolListResponse(BaseModel):
    """Response listing available tools."""
    tools: List[Dict[str, Any]]


class MCPHealthResponse(BaseModel):
    """Health check response."""
    status: str
    timestamp: datetime
    database_connected: bool


class PostgresMCPServer:
    """
    MCP Server for PostgreSQL/TimescaleDB.
    
    Provides read-only access to database schema information
    for use by AI agents in the multi-agent system.
    """
    
    def __init__(self, database_manager: "DatabaseManager"):
        """
        Initialize the MCP server.
        
        Args:
            database_manager: Database manager instance
        """
        self.db_manager = database_manager
        self.router = APIRouter(prefix="/mcp/postgres", tags=["MCP - PostgreSQL"])
        self._tools: Dict[str, BaseMCPTool] = {}
        self._setup_routes()
        self._register_tools()
    
    def _register_tools(self) -> None:
        """Register all PostgreSQL MCP tools."""
        for tool_class in ALL_POSTGRES_TOOLS:
            tool = tool_class(self.db_manager)
            self._tools[tool.name] = tool
            logger.info(f"Registered MCP tool: {tool.name}")
    
    def _setup_routes(self) -> None:
        """Set up FastAPI routes for MCP protocol."""
        
        @self.router.get("/info", response_model=MCPServerInfo)
        async def get_server_info():
            """Get MCP server information and available tools."""
            return MCPServerInfo(
                tools=[tool.get_schema() for tool in self._tools.values()]
            )
        
        @self.router.get("/tools", response_model=MCPToolListResponse)
        async def list_tools():
            """List all available MCP tools."""
            return MCPToolListResponse(
                tools=[tool.get_schema() for tool in self._tools.values()]
            )
        
        @self.router.get("/tools/{tool_name}")
        async def get_tool_schema(tool_name: str):
            """Get schema for a specific tool."""
            tool = self._tools.get(tool_name)
            if not tool:
                raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
            return tool.get_schema()
        
        @self.router.post("/tools/{tool_name}/execute", response_model=MCPToolResponse)
        async def execute_tool(tool_name: str, request: MCPToolRequest):
            """Execute an MCP tool."""
            tool = self._tools.get(tool_name)
            if not tool:
                raise HTTPException(status_code=404, detail=f"Tool '{tool_name}' not found")
            
            correlation_id = request.correlation_id or str(uuid.uuid4())
            logger.info(f"Executing MCP tool '{tool_name}' [correlation_id={correlation_id}]")
            
            try:
                response = await tool.execute(request.parameters)
                response.correlation_id = correlation_id
                return response
            except Exception as e:
                logger.error(f"MCP tool '{tool_name}' failed: {e}")
                return MCPToolResponse(
                    success=False,
                    error=str(e),
                    correlation_id=correlation_id
                )
        
        @self.router.post("/execute", response_model=MCPToolResponse)
        async def execute_tool_generic(request: MCPToolRequest):
            """Execute an MCP tool by name in request body."""
            tool = self._tools.get(request.tool_name)
            if not tool:
                raise HTTPException(
                    status_code=404, 
                    detail=f"Tool '{request.tool_name}' not found"
                )
            
            correlation_id = request.correlation_id or str(uuid.uuid4())
            logger.info(f"Executing MCP tool '{request.tool_name}' [correlation_id={correlation_id}]")
            
            try:
                response = await tool.execute(request.parameters)
                response.correlation_id = correlation_id
                return response
            except Exception as e:
                logger.error(f"MCP tool '{request.tool_name}' failed: {e}")
                return MCPToolResponse(
                    success=False,
                    error=str(e),
                    correlation_id=correlation_id
                )
        
        @self.router.get("/health", response_model=MCPHealthResponse)
        async def health_check():
            """Check MCP server health."""
            try:
                # Quick database connectivity check
                await self.db_manager.check_database_connection()
                return MCPHealthResponse(
                    status="healthy",
                    timestamp=datetime.utcnow(),
                    database_connected=True
                )
            except Exception as e:
                logger.error(f"MCP health check failed: {e}")
                return MCPHealthResponse(
                    status="unhealthy",
                    timestamp=datetime.utcnow(),
                    database_connected=False
                )
    
    def get_tool(self, tool_name: str) -> Optional[BaseMCPTool]:
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
    ) -> MCPToolResponse:
        """
        Execute a tool directly (for programmatic access).
        
        Args:
            tool_name: Name of the tool to execute
            params: Tool parameters
            correlation_id: Optional correlation ID for tracing
            
        Returns:
            MCPToolResponse with results
        """
        tool = self._tools.get(tool_name)
        if not tool:
            return MCPToolResponse(
                success=False,
                error=f"Tool '{tool_name}' not found",
                correlation_id=correlation_id
            )
        
        try:
            response = await tool.execute(params)
            response.correlation_id = correlation_id
            return response
        except Exception as e:
            logger.error(f"MCP tool '{tool_name}' failed: {e}")
            return MCPToolResponse(
                success=False,
                error=str(e),
                correlation_id=correlation_id
            )


# Singleton instance holder
_postgres_mcp_server: Optional[PostgresMCPServer] = None


def get_postgres_mcp_server(db_manager: "DatabaseManager") -> PostgresMCPServer:
    """Get or create the PostgreSQL MCP server instance."""
    global _postgres_mcp_server
    
    if _postgres_mcp_server is None:
        _postgres_mcp_server = PostgresMCPServer(db_manager)
    
    return _postgres_mcp_server


def create_postgres_mcp_router(db_manager: "DatabaseManager") -> APIRouter:
    """Create and return the MCP router for inclusion in the main app."""
    server = get_postgres_mcp_server(db_manager)
    return server.router
