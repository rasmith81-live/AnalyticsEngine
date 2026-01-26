"""
MCP (Model Context Protocol) Servers for Database Service.

This module provides MCP server implementations for:
- PostgreSQL/TimescaleDB introspection and queries
- Knowledge Graph management
"""

from .postgres_mcp_server import PostgresMCPServer, create_postgres_mcp_router
from .postgres_mcp_tools import (
    ListSchemasTool,
    ListTablesTool,
    DescribeTableTool,
    ListHypertablesTool,
    ListContinuousAggregatesTool,
    QuerySampleTool,
    ExplainQueryTool,
    GetTableStatsTool,
)
from .knowledge_graph_mcp_server import (
    KnowledgeGraphMCPServer,
    create_knowledge_graph_mcp_router,
)
from .knowledge_graph_manager import KnowledgeGraphManager
from .knowledge_graph_mcp_tools import (
    CreateEntityTool,
    CreateRelationTool,
    SearchNodesTool,
    GetEntityContextTool,
    GetLineageTool,
    OpenNodesTool,
    AddObservationsTool,
)

__all__ = [
    # PostgreSQL MCP
    "PostgresMCPServer",
    "create_postgres_mcp_router",
    "ListSchemasTool",
    "ListTablesTool",
    "DescribeTableTool",
    "ListHypertablesTool",
    "ListContinuousAggregatesTool",
    "QuerySampleTool",
    "ExplainQueryTool",
    "GetTableStatsTool",
    # Knowledge Graph MCP
    "KnowledgeGraphMCPServer",
    "create_knowledge_graph_mcp_router",
    "KnowledgeGraphManager",
    "CreateEntityTool",
    "CreateRelationTool",
    "SearchNodesTool",
    "GetEntityContextTool",
    "GetLineageTool",
    "OpenNodesTool",
    "AddObservationsTool",
]
