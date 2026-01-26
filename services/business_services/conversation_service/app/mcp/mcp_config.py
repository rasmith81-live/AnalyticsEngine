"""
Configuration for MCP clients.
"""

import os
from typing import Optional
from pydantic import BaseModel, Field


class MCPConfig(BaseModel):
    """Configuration for MCP client connections."""
    
    # Database Service MCP (PostgreSQL + Knowledge Graph)
    database_service_url: str = Field(
        default="http://database_service:8000",
        description="URL of the database service"
    )
    postgres_mcp_enabled: bool = Field(
        default=True,
        description="Enable PostgreSQL MCP client"
    )
    knowledge_mcp_enabled: bool = Field(
        default=True,
        description="Enable Knowledge Graph MCP client"
    )
    
    # Exa Web Search
    web_search_enabled: bool = Field(
        default=True,
        description="Enable web search MCP client"
    )
    web_search_provider: str = Field(
        default="exa",
        description="Web search provider (exa, brave, tavily)"
    )
    exa_api_key: Optional[str] = Field(
        default=None,
        description="Exa API key"
    )
    web_search_rate_limit: int = Field(
        default=10,
        description="Max requests per minute"
    )
    web_search_cache_ttl: int = Field(
        default=3600,
        description="Cache TTL in seconds"
    )
    
    # General settings
    request_timeout: float = Field(
        default=30.0,
        description="Request timeout in seconds"
    )
    max_retries: int = Field(
        default=3,
        description="Maximum retry attempts"
    )
    
    @classmethod
    def from_env(cls) -> "MCPConfig":
        """Create config from environment variables."""
        return cls(
            database_service_url=os.getenv(
                "DATABASE_SERVICE_URL", 
                "http://database_service:8000"
            ),
            postgres_mcp_enabled=os.getenv(
                "POSTGRES_MCP_ENABLED", 
                "true"
            ).lower() == "true",
            knowledge_mcp_enabled=os.getenv(
                "KNOWLEDGE_MCP_ENABLED", 
                "true"
            ).lower() == "true",
            web_search_enabled=os.getenv(
                "WEB_SEARCH_ENABLED", 
                "true"
            ).lower() == "true",
            web_search_provider=os.getenv(
                "WEB_SEARCH_PROVIDER", 
                "exa"
            ),
            exa_api_key=os.getenv("EXA_API_KEY"),
            web_search_rate_limit=int(os.getenv(
                "WEB_SEARCH_RATE_LIMIT", 
                "10"
            )),
            web_search_cache_ttl=int(os.getenv(
                "WEB_SEARCH_CACHE_TTL", 
                "3600"
            )),
            request_timeout=float(os.getenv(
                "MCP_REQUEST_TIMEOUT", 
                "30.0"
            )),
            max_retries=int(os.getenv(
                "MCP_MAX_RETRIES", 
                "3"
            )),
        )
