
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Conversation Service"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8004
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://postgres:postgres@timescaledb:5432/analytics_engine"
    )
    
    # LLM Provider
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY", "")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT", "")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "openai")  # openai or azure
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    
    # Anthropic (Multi-Agent System)
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    ANTHROPIC_COORDINATOR_MODEL: str = os.getenv("ANTHROPIC_COORDINATOR_MODEL", "claude-opus-4-20250514")
    ANTHROPIC_SUBAGENT_MODEL: str = os.getenv("ANTHROPIC_SUBAGENT_MODEL", "claude-sonnet-4-20250514")
    
    # Database Service (for secure storage)
    DATABASE_SERVICE_URL: str = os.getenv("DATABASE_SERVICE_URL", "http://database_service:8025")
    
    # Messaging
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://redis:6379/0")
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
