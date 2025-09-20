"""
Database Service Configuration
"""

import os
from typing import Optional, List
from pydantic import Field
from pydantic_settings import BaseSettings

class DatabaseServiceSettings(BaseSettings):
    """Database service configuration settings."""
    
    # Service Configuration
    service_name: str = Field(default="database_service", description="Service name")
    version: str = Field(default="1.0.0", description="Service version")
    environment: str = Field(default="development", description="Deployment environment (development, staging, production)")
    
    # Database Configuration
    database_url: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/database_service",
        description="Database connection URL (must use asyncpg for async operations)"
    )
    
    # Redis Configuration
    redis_url: str = Field(default="redis://localhost:6379", description="Redis connection URL")
    redis_pool_size: int = Field(default=10, description="Redis connection pool size")
    redis_channel_prefix: str = Field(default="database", description="Redis channel prefix")
    
    # Migration Configuration
    run_migrations_on_startup: bool = Field(default=True, description="Run migrations on startup")
    schema_evolution_enabled: bool = Field(default=True, description="Enable schema evolution")
    schema_validation_level: str = Field(default="basic", description="Schema validation level")
    auto_rollback_on_failure: bool = Field(default=False, description="Auto rollback on failure")
    monitoring_enabled: bool = Field(default=True, description="Enable monitoring")
    
    # TimescaleDB Configuration
    timescale_chunk_interval: str = Field(default="7 days", description="Default chunk interval")
    metrics_retention_period: str = Field(default="365 days", description="Metrics retention period")
    enforce_timescaledb: bool = Field(default=True, description="Enforce TimescaleDB usage")
    disable_sqlite_fallback: bool = Field(default=True, description="Disable SQLite fallback")
    
    # TimescaleDB Compression Configuration
    enable_compression: bool = Field(default=True, description="Enable TimescaleDB compression")
    compression_after: str = Field(default="7 days", description="Compress chunks older than this interval")
    compression_segment_by: Optional[str] = Field(default=None, description="Column to segment compressed chunks by")
    compression_orderby: str = Field(default="time DESC", description="Order by expression for compression")
    
    # TimescaleDB Retention Configuration
    enable_retention: bool = Field(default=True, description="Enable automatic data retention policies")
    
    # Data Retention and Archival Configuration
    retention_period_days: int = Field(default=730, description="Data retention period in days (2 years)")
    retention_check_interval_hours: int = Field(default=24, description="Interval between retention checks in hours")
    archival_service_url: str = Field(default="http://localhost:8003", description="URL for the backend_services/archival_service")
    archival_timeout: int = Field(default=300, description="Archival operation timeout in seconds")
    archival_batch_size: int = Field(default=10, description="Number of chunks to archive in a batch")
    lakehouse_enabled: bool = Field(default=True, description="Enable lakehouse archival")
    lakehouse_storage_account: str = Field(default="devstoreaccount1", description="Azure Storage account for lakehouse")
    lakehouse_container: str = Field(default="timescaledb-archive", description="Azure Storage container for lakehouse")
    
    # Connection Pool Configuration
    connection_pool_size: int = Field(default=10, description="Connection pool size")
    connection_pool_max_overflow: int = Field(default=20, description="Connection pool max overflow")
    connection_pool_timeout: int = Field(default=30, description="Connection pool timeout")
    connection_pool_recycle: int = Field(default=3600, description="Connection pool recycle time")
    
    # Performance Configuration
    query_timeout: int = Field(default=30, description="Default query timeout in seconds")
    command_timeout: int = Field(default=30, description="Default command timeout in seconds")
    enable_query_cache: bool = Field(default=True, description="Enable query result caching")
    cache_ttl: int = Field(default=300, description="Cache TTL in seconds")
    
    # Logging Configuration
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: str = Field(default="json", description="Log format")
    log_sql_queries: bool = Field(default=False, description="Log SQL queries")
    
    # Security Configuration
    secret_key: str = Field(default="your-secret-key", description="Secret key for encryption")
    algorithm: str = Field(default="HS256", description="JWT algorithm")
    
    # Rate Limiting
    rate_limit_per_minute: int = Field(default=1000, description="Rate limit per minute")
    
    # CORS Configuration
    allowed_origins: str = Field(default="*", description="Allowed CORS origins")
    allowed_methods: str = Field(default="*", description="Allowed CORS methods")
    allowed_headers: str = Field(default="*", description="Allowed CORS headers")
    
    # Metrics Configuration
    observability_service_url: str = Field(
        default="http://observability_service:8000",
        description="Observability service URL for metrics export"
    )
    enable_prometheus_metrics: bool = Field(
        default=True,
        description="Enable Prometheus metrics collection"
    )
    prometheus_push_gateway: str = Field(
        default="http://prometheus-pushgateway:9091",
        description="Prometheus push gateway URL"
    )
    metrics_push_interval: int = Field(
        default=15,
        description="Metrics push interval in seconds"
    )
    metrics_export_job_name: str = Field(
        default="database_service",
        description="Job name for metrics export"
    )
    
    # Distributed Tracing Configuration
    enable_distributed_tracing: bool = Field(
        default=True,
        env="ENABLE_DISTRIBUTED_TRACING",
        description="Enable OpenTelemetry distributed tracing"
    )
    otlp_endpoint: str = Field(
        default="http://observability_service:4317",
        env="OTLP_ENDPOINT",
        description="OpenTelemetry collector endpoint for trace export"
    )
    trace_sample_rate: float = Field(
        default=1.0,
        env="TRACE_SAMPLE_RATE",
        description="Trace sampling rate (0.0 to 1.0)"
    )
    propagate_correlation_id: bool = Field(
        default=True,
        env="PROPAGATE_CORRELATION_ID",
        description="Propagate correlation ID across service boundaries"
    )
    
    model_config = {
        "env_file": ".env",
        "case_sensitive": False,
        "extra": "allow"  # Allow extra fields from environment variables
    }

# Global settings instance
_settings: Optional[DatabaseServiceSettings] = None

def get_settings() -> DatabaseServiceSettings:
    """Get application settings singleton."""
    global _settings
    if _settings is None:
        _settings = DatabaseServiceSettings()
    return _settings
