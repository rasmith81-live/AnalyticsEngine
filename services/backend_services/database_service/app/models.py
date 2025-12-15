"""
Database Service Models - Pydantic models for API requests and responses.
"""

from pydantic import BaseModel, Field
from typing import Dict, List, Any, Optional
from datetime import datetime
from enum import Enum

class ArchivalStatus(str, Enum):
    """Archival status enum."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

# Request Models
class QueryRequest(BaseModel):
    """Request model for database queries."""
    query: str = Field(..., description="SQL query to execute")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="Query parameters")
    service_name: str = Field(..., description="Name of the requesting service")
    timeout: Optional[int] = Field(default=30, description="Query timeout in seconds")
    use_cache: bool = Field(default=True, description="Use query result caching")
    query_type: str = Field(default="read", description="Type of query (read/write)")

class AdHocQueryRequest(BaseModel):
    """Request model for ad-hoc structured queries."""
    table_name: str = Field(..., description="Table to query")
    columns: Optional[List[str]] = Field(default=None, description="Columns to select")
    filters: Optional[List[Dict[str, Any]]] = Field(default=None, description="List of filters")
    time_range: Optional[Dict[str, Any]] = Field(default=None, description="Time range filter")
    group_by: Optional[List[str]] = Field(default=None, description="Group by columns")
    order_by: Optional[str] = Field(default=None, description="Order by column")
    order_direction: str = Field(default="DESC", description="Order direction (ASC/DESC)")
    limit: int = Field(default=100, description="Row limit")
    offset: int = Field(default=0, description="Row offset")
    service_name: str = Field(..., description="Name of the requesting service")
    use_cache: bool = Field(default=True, description="Use query result caching")

class CommandRequest(BaseModel):
    """Request model for database commands."""
    command: str = Field(..., description="SQL command to execute")
    parameters: Optional[Dict[str, Any]] = Field(default=None, description="Command parameters")
    service_name: str = Field(..., description="Name of the requesting service")
    transaction_id: Optional[str] = Field(default=None, description="Transaction ID for command grouping")
    timeout: Optional[int] = Field(default=30, description="Command timeout in seconds")

class MigrationRequest(BaseModel):
    """Request model for migration execution."""
    service_name: str = Field(..., description="Name of the service to migrate")
    target_revision: Optional[str] = Field(default="head", description="Target migration revision")
    auto_rollback: bool = Field(default=False, description="Enable automatic rollback on failure")
    validation_level: str = Field(default="basic", description="Validation level: basic, strict")
    run_in_background: bool = Field(default=False, description="Run migration in background")

class HypertableRequest(BaseModel):
    """Request model for TimescaleDB hypertable creation."""
    table_name: str = Field(..., description="Name of the table to convert to hypertable")
    time_column: str = Field(..., description="Name of the time column for partitioning")
    chunk_interval: Optional[str] = Field(default="7 days", description="Chunk interval for partitioning")
    compression_enabled: bool = Field(default=True, description="Enable compression")
    retention_period: Optional[str] = Field(default="365 days", description="Data retention period")

class ModelRegistrationRequest(BaseModel):
    """Request model for model registration."""
    service_name: str = Field(..., description="Name of the service")
    models: List[Dict[str, Any]] = Field(..., description="List of model definitions")
    auto_create_tables: bool = Field(default=True, description="Automatically create tables")

# Response Models
class QueryResponse(BaseModel):
    """Response model for database queries."""
    success: bool
    data: Optional[Dict[str, Any]] = None
    execution_time: float
    row_count: int
    cache_hit: bool = False
    error_message: Optional[str] = None

class CommandResponse(BaseModel):
    """Response model for database commands."""
    success: bool
    transaction_id: Optional[str] = None
    affected_rows: int
    execution_time: float
    error_message: Optional[str] = None

class ValidationIssue(BaseModel):
    """Validation issue model."""
    severity: str
    category: str
    description: str
    location: str
    suggestion: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class MigrationResponse(BaseModel):
    """Response model for migration execution."""
    success: bool
    service_name: str
    phases_completed: List[str]
    hypertables_created: List[str] = Field(default_factory=list)
    validation_issues: List[Dict[str, Any]] = Field(default_factory=list)
    error_message: Optional[str] = None
    rollback_performed: bool = False
    execution_time: Optional[float] = None
    message: Optional[str] = None

class HypertableResponse(BaseModel):
    """Response model for hypertable operations."""
    success: bool
    table_name: str
    hypertable_created: bool
    chunk_interval: Optional[str] = None
    compression_policy: Optional[Dict[str, Any]] = None
    retention_policy: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None

class ModelInfo(BaseModel):
    """Model information."""
    name: str
    table_name: str
    fields: Dict[str, str]
    relationships: List[str]
    is_hypertable: bool = False
    time_column: Optional[str] = None
    source_file: str = ""

class ModelDiscoveryResponse(BaseModel):
    """Response model for model discovery."""
    service_name: str
    models: List[ModelInfo]
    discovery_time: datetime

class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    database_connected: bool
    timescaledb_available: bool
    connection_pool_status: Dict[str, Any]
    active_connections: int
    timestamp: datetime

# Database Entity Models
class DatabaseConnection(BaseModel):
    """Database connection configuration."""
    service_name: str
    database_url: str
    pool_size: int = 10
    max_overflow: int = 20
    pool_timeout: int = 30
    pool_recycle: int = 3600

class TransactionContext(BaseModel):
    """Transaction context for command execution."""
    transaction_id: str
    service_name: str
    started_at: datetime
    commands_executed: int = 0
    is_active: bool = True

# CQRS Models
class CommandBase(BaseModel):
    """Base class for CQRS commands."""
    command_id: str
    service_name: str
    timestamp: datetime
    correlation_id: Optional[str] = None

class QueryBase(BaseModel):
    """Base class for CQRS queries."""
    query_id: str
    service_name: str
    timestamp: datetime
    correlation_id: Optional[str] = None

class ReadModelBase(BaseModel):
    """Base class for CQRS read models."""
    id: int
    uuid: str
    created_at: datetime
    updated_at: datetime
    version: int = 1

# TimescaleDB Specific Models
class RetentionPolicy(BaseModel):
    """TimescaleDB retention policy."""
    enabled: bool = True
    retention_period_days: int = 730  # Default 2 years

class ArchivalEvent(BaseModel):
    """Event model for data archival requests."""
    event_id: str
    table_name: str
    chunks: List[Dict[str, Any]]
    status: ArchivalStatus
    created_at: datetime
    error_message: Optional[str] = None

class ArchivalConfirmation(BaseModel):
    """Confirmation model for completed archival operations."""
    event_id: str
    status: ArchivalStatus
    completed_at: datetime
    lakehouse_path: Optional[str] = None
    error_message: Optional[str] = None

class HypertableInfo(BaseModel):
    """TimescaleDB hypertable information."""
    table_name: str
    time_column: str
    chunk_interval: str
    compression_enabled: bool
    retention_period: Optional[str] = None
    created_at: datetime
    last_chunk_created: Optional[datetime] = None

class ChunkInfo(BaseModel):
    """TimescaleDB chunk information."""
    chunk_name: str
    table_name: str
    range_start: datetime
    range_end: datetime
    compressed: bool
    size_bytes: int

class ContinuousAggregateInfo(BaseModel):
    """TimescaleDB continuous aggregate information."""
    view_name: str
    source_table: str
    refresh_policy: Optional[Dict[str, Any]] = None
    materialized: bool
    created_at: datetime

# Migration Models
class MigrationInfo(BaseModel):
    """Migration information."""
    revision: str
    service_name: str
    description: str
    applied_at: Optional[datetime] = None
    is_current: bool = False

class SchemaValidationResult(BaseModel):
    """Schema validation result."""
    is_valid: bool
    issues: List[ValidationIssue]
    validated_at: datetime
    validation_level: str

# Performance Models
class PerformanceStats(BaseModel):
    """Database performance statistics."""
    total_queries: int
    total_commands: int
    avg_query_time: float
    avg_command_time: float
    cache_hit_rate: float
    active_connections: int
    total_connections: int
    timestamp: datetime

class ConnectionPoolStatus(BaseModel):
    """Connection pool status."""
    size: int
    checked_in: int
    checked_out: int
    overflow: int
    invalid: int
    total_created: int

# Secure Storage Models
class SecureArtifactRequest(BaseModel):
    """Request model for storing a secure artifact."""
    key: str = Field(..., description="Unique key for the artifact")
    value: str = Field(..., description="Sensitive value to store")
    description: Optional[str] = Field(None, description="Description of the artifact")
    category: str = Field(default="general", description="Category (e.g., 'api_key', 'credential')")

class SecureArtifactResponse(BaseModel):
    """Response model for secure artifact metadata."""
    key: str
    description: Optional[str]
    category: str
    created_at: datetime
    updated_at: datetime
    
    model_config = {"from_attributes": True}

class SecureArtifactValueResponse(SecureArtifactResponse):
    """Response model for secure artifact with decrypted value."""
    value: str
    
    model_config = {"from_attributes": True}
