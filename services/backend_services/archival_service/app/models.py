"""
Archival Service Models - Pydantic models for API requests and responses.
"""
from datetime import datetime
from enum import Enum
from typing import Dict, List, Any, Optional

from pydantic import BaseModel, Field

class ArchivalStatus(str, Enum):
    """Archival status enum."""
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

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

class ChunkInfo(BaseModel):
    """TimescaleDB chunk information."""
    chunk_name: str
    chunk_id: int
    range_start: Optional[datetime] = None
    range_end: Optional[datetime] = None

class ArchivalMetrics(BaseModel):
    """Metrics for archival operations."""
    total_events: int
    completed_events: int
    failed_events: int
    processing_events: int
    average_processing_time_seconds: float
    total_chunks_archived: int
    total_bytes_archived: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class HealthResponse(BaseModel):
    """Health check response model."""
    status: str
    messaging_connected: bool
    lakehouse_connected: bool
    active_archival_events: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    monitoring_health: Optional[Dict[str, Any]] = None
    management_health: Optional[Dict[str, Any]] = None

class ArchivalQuery(BaseModel):
    """Query model for archived data."""
    table_name: str
    time_range_start: Optional[datetime] = None
    time_range_end: Optional[datetime] = None
    filters: Optional[Dict[str, Any]] = None
    limit: int = 1000

class ArchivalQueryResult(BaseModel):
    """Result model for archived data queries."""
    query: ArchivalQuery
    data_paths: List[str]
    record_count: int
    execution_time_seconds: float
    timestamp: datetime = Field(default_factory=datetime.utcnow)
