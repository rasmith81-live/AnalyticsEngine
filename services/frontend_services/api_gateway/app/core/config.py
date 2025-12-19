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
    
    # OIDC / Azure AD Settings
    AUTH_METHOD: str = Field(default_factory=lambda: os.getenv("AUTH_METHOD", "oidc"), description="Auth method: 'secret' (HS256) or 'oidc' (RS256)")
    OIDC_ISSUER: Optional[str] = Field(default_factory=lambda: os.getenv("OIDC_ISSUER"))
    OIDC_JWKS_URI: Optional[str] = Field(default_factory=lambda: os.getenv("OIDC_JWKS_URI"))
    OIDC_CLIENT_ID: Optional[str] = Field(default_factory=lambda: os.getenv("OIDC_CLIENT_ID"))
    OIDC_AUDIENCE: Optional[str] = Field(default_factory=lambda: os.getenv("OIDC_AUDIENCE"))
    
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
        # Backend Services
        "messaging_service": {
            "url": os.getenv("MESSAGING_SERVICE_URL", "http://messaging_service:8001"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "database_service": {
            "url": os.getenv("DATABASE_SERVICE_URL", "http://database_service:8002"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "archival_service": {
            "url": os.getenv("ARCHIVAL_SERVICE_URL", "http://archival_service:8003"),
            "timeout": 60.0,
            "health_endpoint": "/health",
        },
        "observability_service": {
            "url": os.getenv("OBSERVABILITY_SERVICE_URL", "http://observability_service:8000"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        # Business Services
        "business_metadata_service": {
            "url": os.getenv("BUSINESS_METADATA_SERVICE_URL", "http://analytics_metadata_service:8023"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "calculation_engine_service": {
            "url": os.getenv("CALCULATION_ENGINE_SERVICE_URL", "http://calculation_engine_service:8000"),
            "timeout": 60.0,
            "health_endpoint": "/health",
        },
        "conversation_service": {
            "url": os.getenv("CONVERSATION_SERVICE_URL", "http://conversation_service:8004"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "demo_config_service": {
            "url": os.getenv("DEMO_CONFIG_SERVICE_URL", "http://demo_config_service:8000"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "connector_service": {
            "url": os.getenv("CONNECTOR_SERVICE_URL", "http://connector_service:8000"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "ingestion_service": {
            "url": os.getenv("INGESTION_SERVICE_URL", "http://ingestion_service:8000"),
            "timeout": 30.0,
            "health_endpoint": "/health",
        },
        "entity_resolution_service": {
            "url": os.getenv("ENTITY_RESOLUTION_SERVICE_URL", "http://entity_resolution_service:8000"),
            "timeout": 60.0,
            "health_endpoint": "/health",
        },
        "metadata_ingestion_service": {
            "url": os.getenv("METADATA_INGESTION_SERVICE_URL", "http://metadata_ingestion_service:8000"),
            "timeout": 60.0,
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
