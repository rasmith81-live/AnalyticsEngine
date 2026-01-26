"""
Pydantic models for PostgreSQL MCP Server.
"""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class MCPToolRequest(BaseModel):
    """Base request model for MCP tool calls."""
    tool_name: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    correlation_id: Optional[str] = None


class MCPToolResponse(BaseModel):
    """Base response model for MCP tool results."""
    success: bool
    data: Dict[str, Any] = Field(default_factory=dict)
    error: Optional[str] = None
    execution_time_ms: float = 0.0
    correlation_id: Optional[str] = None


class SchemaInfo(BaseModel):
    """Information about a database schema."""
    schema_name: str
    owner: Optional[str] = None
    table_count: int = 0
    description: Optional[str] = None


class ColumnInfo(BaseModel):
    """Information about a table column."""
    column_name: str
    data_type: str
    is_nullable: bool = True
    column_default: Optional[str] = None
    character_maximum_length: Optional[int] = None
    numeric_precision: Optional[int] = None
    numeric_scale: Optional[int] = None
    is_primary_key: bool = False
    is_foreign_key: bool = False
    foreign_key_reference: Optional[str] = None
    description: Optional[str] = None


class IndexInfo(BaseModel):
    """Information about a table index."""
    index_name: str
    columns: List[str]
    is_unique: bool = False
    is_primary: bool = False
    index_type: str = "btree"


class ConstraintInfo(BaseModel):
    """Information about a table constraint."""
    constraint_name: str
    constraint_type: str  # PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK
    columns: List[str]
    reference_table: Optional[str] = None
    reference_columns: Optional[List[str]] = None


class TableInfo(BaseModel):
    """Information about a database table."""
    table_name: str
    schema_name: str
    table_type: str = "BASE TABLE"  # BASE TABLE, VIEW, FOREIGN TABLE
    is_hypertable: bool = False
    row_count_estimate: Optional[int] = None
    total_size_bytes: Optional[int] = None
    description: Optional[str] = None
    columns: List[ColumnInfo] = Field(default_factory=list)
    indexes: List[IndexInfo] = Field(default_factory=list)
    constraints: List[ConstraintInfo] = Field(default_factory=list)


class HypertableInfo(BaseModel):
    """Information about a TimescaleDB hypertable."""
    hypertable_name: str
    schema_name: str
    time_column: str
    chunk_interval: Optional[str] = None
    num_chunks: int = 0
    total_size_bytes: Optional[int] = None
    compressed_size_bytes: Optional[int] = None
    compression_enabled: bool = False
    retention_policy: Optional[str] = None


class ContinuousAggregateInfo(BaseModel):
    """Information about a TimescaleDB continuous aggregate."""
    view_name: str
    schema_name: str
    source_hypertable: str
    refresh_interval: Optional[str] = None
    materialized: bool = True
    last_refresh: Optional[datetime] = None


class TableStatsInfo(BaseModel):
    """Statistics about a table."""
    table_name: str
    schema_name: str
    row_count: int = 0
    total_size_bytes: int = 0
    table_size_bytes: int = 0
    index_size_bytes: int = 0
    toast_size_bytes: int = 0
    last_vacuum: Optional[datetime] = None
    last_analyze: Optional[datetime] = None
    dead_tuples: int = 0
    live_tuples: int = 0


class QueryExplainResult(BaseModel):
    """Result of EXPLAIN ANALYZE."""
    query: str
    plan: List[Dict[str, Any]]
    execution_time_ms: float = 0.0
    planning_time_ms: float = 0.0
    total_cost: float = 0.0
    rows_estimate: int = 0
    rows_actual: Optional[int] = None


class SampleQueryResult(BaseModel):
    """Result of a sample query."""
    table_name: str
    columns: List[str]
    rows: List[Dict[str, Any]]
    row_count: int = 0
    truncated: bool = False


# Tool-specific request models

class ListSchemasRequest(BaseModel):
    """Request to list schemas."""
    include_system: bool = False


class ListTablesRequest(BaseModel):
    """Request to list tables."""
    schema_name: str = "public"
    include_views: bool = True
    table_pattern: Optional[str] = None


class DescribeTableRequest(BaseModel):
    """Request to describe a table."""
    table_name: str
    schema_name: str = "public"
    include_indexes: bool = True
    include_constraints: bool = True


class ListHypertablesRequest(BaseModel):
    """Request to list hypertables."""
    schema_name: Optional[str] = None


class ListContinuousAggregatesRequest(BaseModel):
    """Request to list continuous aggregates."""
    schema_name: Optional[str] = None


class QuerySampleRequest(BaseModel):
    """Request for sample data."""
    table_name: str
    schema_name: str = "public"
    limit: int = Field(default=10, le=100)
    columns: Optional[List[str]] = None
    where_clause: Optional[str] = None
    order_by: Optional[str] = None


class ExplainQueryRequest(BaseModel):
    """Request for query explanation."""
    query: str
    analyze: bool = True
    buffers: bool = False
    format: str = "json"


class GetTableStatsRequest(BaseModel):
    """Request for table statistics."""
    table_name: str
    schema_name: str = "public"
