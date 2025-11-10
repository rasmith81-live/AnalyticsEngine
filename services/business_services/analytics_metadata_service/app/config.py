"""
Analytics Metadata Service Configuration
"""

import os
from typing import Optional
from pydantic import Field
from pydantic_settings import BaseSettings


class MetadataServiceSettings(BaseSettings):
    """Metadata service configuration settings."""
    
    # Service Configuration
    service_name: str = Field(
        default="analytics_metadata_service",
        description="Service name"
    )
    version: str = Field(default="1.0.0", description="Service version")
    environment: str = Field(
        default="development",
        description="Deployment environment"
    )
    
    # Server Configuration
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")
    
    # Database Service Configuration
    database_service_url: str = Field(
        default="http://database_service:8000",
        description="Database service URL"
    )
    
    # Messaging Service Configuration
    messaging_service_url: str = Field(
        default="http://messaging_service:8000",
        description="Messaging service URL"
    )
    
    # Observability Configuration
    observability_service_url: str = Field(
        default="http://observability_service:8000",
        description="Observability service URL"
    )
    
    # Distributed Tracing Configuration
    enable_distributed_tracing: bool = Field(
        default=True,
        description="Enable OpenTelemetry distributed tracing"
    )
    otlp_endpoint: str = Field(
        default="http://observability_service:4317",
        description="OpenTelemetry collector endpoint"
    )
    
    # Metrics Configuration
    enable_prometheus_metrics: bool = Field(
        default=True,
        description="Enable Prometheus metrics"
    )
    prometheus_push_gateway: str = Field(
        default="http://prometheus-pushgateway:9091",
        description="Prometheus push gateway URL"
    )
    metrics_push_interval: int = Field(
        default=15,
        description="Metrics push interval in seconds"
    )
    
    # Cache Configuration
    enable_cache: bool = Field(
        default=True,
        description="Enable definition caching"
    )
    cache_ttl: int = Field(
        default=3600,
        description="Cache TTL in seconds (1 hour)"
    )
    
    # CORS Configuration
    allowed_origins: str = Field(
        default="*",
        description="Allowed CORS origins"
    )
    
    # Logging Configuration
    log_level: str = Field(default="INFO", description="Logging level")
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "allow"
    }


# Global settings instance
_settings: Optional[MetadataServiceSettings] = None


def get_settings() -> MetadataServiceSettings:
    """Get application settings singleton."""
    global _settings
    if _settings is None:
        _settings = MetadataServiceSettings()
    return _settings
