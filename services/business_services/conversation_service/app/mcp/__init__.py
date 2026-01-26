"""
MCP (Model Context Protocol) Clients for Conversation Service.

This module provides MCP client implementations for agents to interact with:
- PostgreSQL MCP Server (database introspection)
- Knowledge Graph MCP Server (ontology management)
- Exa Web Search (external research)
"""

from .mcp_client_manager import MCPClientManager, MCPConfig
from .postgres_mcp_client import PostgresMCPClient
from .knowledge_graph_mcp_client import KnowledgeGraphMCPClient
from .exa_search_client import ExaSearchClient

__all__ = [
    "MCPClientManager",
    "MCPConfig",
    "PostgresMCPClient",
    "KnowledgeGraphMCPClient",
    "ExaSearchClient",
]
