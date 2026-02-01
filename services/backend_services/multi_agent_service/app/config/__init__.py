# =============================================================================
# Multi-Agent Service Configuration Package
# =============================================================================
"""
Configuration modules for multi_agent_service.

Components:
- Settings, get_settings: Core service settings
- ClientFramework: Industry-agnostic client framework configuration
- FrameworkLoader: Loads client config from metadata service
"""

from pydantic_settings import BaseSettings
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Service settings
    SERVICE_NAME: str = "multi_agent_service"
    SERVICE_VERSION: str = "0.1.0"
    DEBUG: bool = False
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8090
    
    # Redis settings (for blackboard persistence)
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 1
    REDIS_PASSWORD: Optional[str] = None
    
    # Database settings (for audit log - TimescaleDB)
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/analyticsengine"
    
    # Anthropic API settings
    ANTHROPIC_API_KEY: Optional[str] = None
    DEFAULT_MODEL: str = "claude-sonnet-4-20250514"
    
    # Contract settings
    MAX_CONTEXT_TOKENS: int = 200000
    TOKEN_WARNING_THRESHOLD: float = 0.70
    TOKEN_CRITICAL_THRESHOLD: float = 0.85
    
    # Agent settings
    MAX_TOOL_CALLS_PER_TASK: int = 10
    MAX_CONSULTATION_DEPTH: int = 2
    STRUGGLE_SIGNAL_AFTER_ATTEMPTS: int = 2
    
    # Peer review settings
    TWO_FAILURES_ESCALATION: bool = True
    TARGET_REJECTION_RATE_MIN: float = 0.20
    TARGET_REJECTION_RATE_MAX: float = 0.40
    
    class Config:
        env_file = ".env"
        env_prefix = "MULTI_AGENT_"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


from .client_framework import (
    ClientConfiguration,
    ClientFramework,
    FrameworkLoader,
    FrameworkType,
    KPITemplate,
    ModuleDefinition,
    RelationshipDefinition,
)

__all__ = [
    "Settings",
    "get_settings",
    "ClientConfiguration",
    "ClientFramework",
    "FrameworkLoader",
    "FrameworkType",
    "KPITemplate",
    "ModuleDefinition",
    "RelationshipDefinition",
]
