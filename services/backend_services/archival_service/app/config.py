"""
Configuration settings for the Archival Service.
"""
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Application settings."""
    
    # Service configuration
    service_name: str = "archival_service"
    host: str = "0.0.0.0"
    port: int = 8003
    debug: bool = False
    version: str = "1.0.0"
    environment: str = Field(default="development", description="Deployment environment (development, staging, production)")
    
    # Redis configuration
    redis_url: str = Field(default="redis://redis:6379/0", description="Redis connection URL")
    redis_pool_size: int = 10
    
    # Azure Data Lake Storage configuration
    storage_account: str = Field(default="devstoreaccount1", description="Azure Storage account name")
    container_name: str = Field(default="timescaledb-archive", description="Container name for data lake storage")
    storage_connection_string: str = Field(
        default="DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://azurite:10000/devstoreaccount1;", 
        description="Azure Storage connection string"
    )
    
    # Lakehouse configuration
    default_format: str = "parquet"  # Options: parquet, delta, json
    
    # CORS configuration
    cors_origins: list[str] = ["*"]
    
    # Database Service configuration
    database_service_url: str = Field(default="http://database_service:8000", description="Database service URL")
    
    # Archival configuration
    max_concurrent_archival_tasks: int = 5
    chunk_batch_size: int = 10  # Number of chunks to process in a single batch
    auto_archival_enabled: bool = True  # Enable automatic archival operations
    
    # Monitoring and metrics
    enable_metrics: bool = True
    metrics_port: int = 8053
    
    # Prometheus metrics configuration
    enable_prometheus_metrics: bool = True
    observability_service_url: str = Field(default="http://observability_service:8000/metrics/ingest", description="URL for the Observability Service metrics ingestion endpoint")
    prometheus_push_gateway: str = Field(default="", description="Optional Prometheus Pushgateway URL")
    metrics_push_interval: int = Field(default=15, description="Interval in seconds for pushing metrics to Observability Service")
    metrics_update_interval: int = Field(default=60, description="Interval in seconds for updating system metrics")
    metrics_export_job_name: str = Field(default="archival_service", description="Job name for metrics export")
    
    # Security
    enable_auth: bool = False
    jwt_secret: str = ""
    jwt_algorithm: str = "HS256"
    
    # Logging
    log_level: str = "INFO"
    
    # Distributed Tracing
    enable_distributed_tracing: bool = Field(default=True, description="Enable OpenTelemetry distributed tracing")
    otlp_endpoint: str = Field(default="http://observability_service:4317", description="OpenTelemetry collector endpoint")
    trace_sample_rate: float = Field(default=1.0, description="Trace sampling rate (0.0 to 1.0)")
    propagate_correlation_id: bool = Field(default=True, description="Propagate correlation IDs across service boundaries")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="ARCHIVAL_",
        case_sensitive=False,
        env_nested_delimiter="__",
        extra="ignore"
    )

# Create settings instance
settings = Settings()
