"""
Configuration settings for the API Gateway service.
"""
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings
from typing import Dict, Any, Optional
import os

class Settings(BaseSettings):
    """API Gateway configuration settings using Pydantic v2 style."""
    
    # Service information
    SERVICE_NAME: str = Field("api_gateway", description="Service name for schema naming")
    PROJECT_NAME: str = Field("Supply Chain Analytics API Gateway", description="Project name")
    API_V1_STR: str = Field("/api/v1", description="API version string")
    
    # Security
    SECRET_KEY: str = Field(default_factory=lambda: os.getenv("SECRET_KEY", "your-secret-key-here"))
    JWT_SECRET_KEY: str = Field(default_factory=lambda: os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key-here"))
    JWT_ALGORITHM: str = Field(default_factory=lambda: os.getenv("JWT_ALGORITHM", "HS256"))
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(60 * 24 * 8, description="Token expiry in minutes (8 days)")
    
    # Redis - use the same connection settings as other services
    REDIS_URL: str = Field(
        default_factory=lambda: os.getenv(
            "REDIS_URL", 
            f"redis://{os.getenv('REDIS_HOST', 'redis')}:{os.getenv('REDIS_PORT', '6379')}/0"
        )
    )
    
    # Rate Limiting
    RATE_LIMIT: int = Field(100, description="Default requests per minute limit")
    RATE_LIMIT_WINDOW: int = Field(60, description="Time window in seconds for rate limiting")
    
    # Circuit Breaker
    CIRCUIT_BREAKER_THRESHOLD: int = Field(5, description="Failures before circuit opens")
    CIRCUIT_BREAKER_RECOVERY_TIME: int = Field(30, description="Seconds before attempting recovery")
    
    # Caching
    CACHE_ENABLED: bool = Field(True, description="Enable response caching")
    CACHE_TTL: int = Field(300, description="Cache TTL in seconds")
    
    # Health check settings
    HEALTH_CHECK_INTERVAL: int = Field(30, description="Health check interval in seconds")
    
    # Messaging service settings
    MESSAGING_SERVICE_URL: str = Field(
        default_factory=lambda: os.getenv("MESSAGING_SERVICE_URL", "http://messaging_service:8000")
    )
    QUERY_TIMEOUT: int = Field(10, description="Timeout for query responses in seconds")
    
    # Service Registry
    SERVICE_REGISTRY: Dict[str, Dict[str, Any]] = Field(default_factory=lambda: {
        # Business Services
        "business_service_a": {
            "url": os.getenv("BUSINESS_SERVICE_A_URL"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "business_service_b": {
            "url": os.getenv("BUSINESS_SERVICE_B_URL"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        
        # Backend Services
        "messaging_service": {
            "url": os.getenv("MESSAGING_SERVICE_URL"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "database_service": {
            "url": os.getenv("DATABASE_SERVICE_URL"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "archival_service": {
            "url": os.getenv("ARCHIVAL_SERVICE_URL"),
            "timeout": 60.0,
            "health_endpoint": "/health",
        },
        "observability_service": {
            "url": os.getenv("OBSERVABILITY_SERVICE_URL"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
    })
    
    # Database settings for any local storage needs
    DATABASE_URL: str = Field(
        default_factory=lambda: os.getenv(
            "DATABASE_URL",
            "postgresql+asyncpg://postgres:postgres@timescaledb:5432/api_gateway"
        )
    )
    
    # Logging
    LOG_LEVEL: str = Field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))

    # Tracing
    OTLP_ENDPOINT: Optional[str] = Field(
        default_factory=lambda: os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", os.getenv("OTLP_ENDPOINT"))
    )
    
    # CORS settings
    CORS_ORIGINS: list = Field(
        default_factory=lambda: [
            origin.strip()
            for origin in os.getenv("CORS_ORIGINS", "*").split(",")
        ]
    )
    
    @field_validator('REDIS_URL')
    @classmethod
    def validate_redis_url(cls, v):
        if not v.startswith('redis://') and not v.startswith('rediss://'):
            raise ValueError("Redis URL must start with redis:// or rediss://")
        return v
    
    model_config = {
        "case_sensitive": True,
        "env_file": ".env",
        "extra": "ignore"
    }

settings = Settings()
