"""
Observability Service Models

This module contains all Pydantic models used by the Observability Service API.
"""

from typing import Dict, List, Optional, Any, Union
from datetime import datetime
from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

# Common Models
class ErrorResponse(BaseModel):
    """Standard error response model."""
    status_code: int = Field(..., description="HTTP status code")
    detail: str = Field(..., description="Error detail message")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the error")
    path: Optional[str] = Field(None, description="Request path that caused the error")
    trace_id: Optional[str] = Field(None, description="Trace ID for correlation")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status_code": 400,
                "detail": "Invalid request parameters",
                "timestamp": "2023-01-01T00:00:00Z",
                "path": "/api/v1/traces",
                "trace_id": "1234567890abcdef1234567890abcdef"
            }
        }
    )


# Health Models
class HealthStatus(str, Enum):
    """Health status enum for service health checks."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


class HealthData(BaseModel):
    """Model for health check data ingestion."""
    service: str = Field(..., description="Name of the service")
    status: HealthStatus = Field(..., description="Health status of the service")
    timestamp: Optional[datetime] = Field(None, description="Timestamp of the health check")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional health details")
    latency_ms: Optional[float] = Field(None, description="Response latency in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "api_service",
                "status": "healthy",
                "timestamp": "2023-01-01T00:00:00Z",
                "details": {
                    "database": "connected",
                    "redis": "connected"
                },
                "latency_ms": 45.2
            }
        }
    )


class HealthDataBatch(BaseModel):
    """Model for batch health data ingestion."""
    health_data: List[HealthData] = Field(..., description="List of health data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "health_data": [
                    {
                        "service": "api_service",
                        "status": "healthy",
                        "timestamp": "2023-01-01T00:00:00Z",
                        "details": {"database": "connected"},
                        "latency_ms": 45.2
                    }
                ]
            }
        }
    )


class HealthQuery(BaseModel):
    """Model for health data queries."""
    service: Optional[str] = Field(None, description="Filter by service name")
    status: Optional[HealthStatus] = Field(None, description="Filter by health status")
    start_time: Optional[datetime] = Field(None, description="Start time for query")
    end_time: Optional[datetime] = Field(None, description="End time for query")
    limit: int = Field(100, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "api_service",
                "status": "healthy",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T23:59:59Z",
                "limit": 100,
                "offset": 0
            }
        }
    )


class HealthResponse(BaseModel):
    """Response model for health operations."""
    service: str = Field(..., description="Service name")
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Response message")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "api_service",
                "status": "success",
                "message": "Health data ingested successfully"
            }
        }
    )


class HealthStatistics(BaseModel):
    """Health statistics model."""
    total_checks: int = Field(..., description="Total number of health checks")
    healthy_count: int = Field(..., description="Number of healthy checks")
    degraded_count: int = Field(..., description="Number of degraded checks")
    unhealthy_count: int = Field(..., description="Number of unhealthy checks")
    avg_latency_ms: float = Field(..., description="Average latency in milliseconds")
    service_count: int = Field(..., description="Number of unique services")
    services: List[str] = Field(..., description="List of services")
    start_time: datetime = Field(..., description="Start time of statistics")
    end_time: datetime = Field(..., description="End time of statistics")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_checks": 1000,
                "healthy_count": 950,
                "degraded_count": 30,
                "unhealthy_count": 20,
                "avg_latency_ms": 45.2,
                "service_count": 5,
                "services": ["api_service", "auth_service"],
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T23:59:59Z"
            }
        }
    )


class ComponentHealth(BaseModel):
    """Component health model for service health checks."""
    status: HealthStatus = Field(..., description="Health status of the component")
    details: Dict[str, Any] = Field(default_factory=dict, description="Component health details")
    last_check: datetime = Field(default_factory=datetime.now, description="Last health check timestamp")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "healthy",
                "details": {"connection": "established", "latency_ms": 45.2},
                "last_check": "2023-01-01T00:00:00Z"
            }
        }
    )


class ServiceHealthResponse(BaseModel):
    """Service health response model."""
    service: str = Field(..., description="Service name")
    status: HealthStatus = Field(..., description="Overall service health status")
    version: str = Field(..., description="Service version")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
    components: Dict[str, ComponentHealth] = Field(..., description="Component health status")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "observability_service",
                "status": "healthy",
                "version": "1.0.0",
                "uptime_seconds": 3600.0,
                "components": {
                    "database": {
                        "status": "healthy",
                        "details": {"connection": "established"},
                        "last_check": "2023-01-01T00:00:00Z"
                    }
                }
            }
        }
    )


# Dependency Models
class DependencyStatus(str, Enum):
    """Dependency status enum."""
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    DEGRADED = "degraded"


class DependencyData(BaseModel):
    """Model for dependency check data ingestion."""
    service: str = Field(..., description="Name of the service")
    name: str = Field(..., description="Name of the dependency")
    type: str = Field(..., description="Type of dependency (database, api, cache, etc.)")
    status: DependencyStatus = Field(..., description="Status of the dependency")
    timestamp: Optional[datetime] = Field(None, description="Timestamp of the dependency check")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional dependency details")
    latency_ms: Optional[float] = Field(None, description="Response latency in milliseconds")


class DependencyDataBatch(BaseModel):
    """Model for batch dependency data ingestion."""
    dependency_data: List[DependencyData] = Field(..., description="List of dependency data")


class DependencyQuery(BaseModel):
    """Model for dependency data queries."""
    service: Optional[str] = Field(None, description="Filter by service name")
    name: Optional[str] = Field(None, description="Filter by dependency name")
    type: Optional[str] = Field(None, description="Filter by dependency type")
    status: Optional[DependencyStatus] = Field(None, description="Filter by dependency status")
    start_time: Optional[datetime] = Field(None, description="Start time for query")
    end_time: Optional[datetime] = Field(None, description="End time for query")
    limit: int = Field(100, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")


class DependencyResponse(BaseModel):
    """Response model for dependency operations."""
    name: str = Field(..., description="Dependency name")
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Response message")


class DependencyStatistics(BaseModel):
    """Dependency statistics model."""
    total_checks: int = Field(..., description="Total number of dependency checks")
    available_count: int = Field(..., description="Number of available dependencies")
    unavailable_count: int = Field(..., description="Number of unavailable dependencies")
    degraded_count: int = Field(..., description="Number of degraded dependencies")
    avg_latency_ms: float = Field(..., description="Average latency in milliseconds")
    dependency_count: int = Field(..., description="Number of unique dependencies")
    service_count: int = Field(..., description="Number of unique services")
    dependencies: List[str] = Field(..., description="List of dependency names")
    services: List[str] = Field(..., description="List of services")
    start_time: datetime = Field(..., description="Start time of statistics")
    end_time: datetime = Field(..., description="End time of statistics")


# Event Models
class EventSeverity(str, Enum):
    """Event severity enum."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class EventData(BaseModel):
    """Model for event data ingestion."""
    event_type: str = Field(..., description="Type of the event")
    source_service: str = Field(..., description="Service that generated the event")
    event_data: Dict[str, Any] = Field(..., description="Event data payload")
    timestamp: Optional[datetime] = Field(None, description="Timestamp of the event")
    correlation_id: Optional[str] = Field(None, description="Correlation ID for tracing")
    severity: EventSeverity = Field(EventSeverity.INFO, description="Event severity level")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional event metadata")


class EventDataBatch(BaseModel):
    """Model for batch event data ingestion."""
    events: List[EventData] = Field(..., description="List of event data")


class EventQuery(BaseModel):
    """Model for event data queries."""
    event_type: Optional[str] = Field(None, description="Filter by event type")
    source_service: Optional[str] = Field(None, description="Filter by source service")
    severity: Optional[EventSeverity] = Field(None, description="Filter by event severity")
    correlation_id: Optional[str] = Field(None, description="Filter by correlation ID")
    start_time: Optional[datetime] = Field(None, description="Start time for query")
    end_time: Optional[datetime] = Field(None, description="End time for query")
    limit: int = Field(100, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")


class EventResponse(BaseModel):
    """Response model for event operations."""
    event_type: str = Field(..., description="Event type")
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Response message")


class EventStatistics(BaseModel):
    """Event statistics model."""
    total_events: int = Field(..., description="Total number of events")
    info_count: int = Field(..., description="Number of info events")
    warning_count: int = Field(..., description="Number of warning events")
    error_count: int = Field(..., description="Number of error events")
    critical_count: int = Field(..., description="Number of critical events")
    event_type_count: int = Field(..., description="Number of unique event types")
    service_count: int = Field(..., description="Number of unique services")
    event_types: List[str] = Field(..., description="List of event types")
    services: List[str] = Field(..., description="List of services")
    start_time: datetime = Field(..., description="Start time of statistics")
    end_time: datetime = Field(..., description="End time of statistics")


class EventRequest(BaseModel):
    """Model for event publishing requests."""
    event_type: str = Field(..., description="Type of the event")
    source_service: str = Field(..., description="Service that generated the event")
    event_data: Dict[str, Any] = Field(..., description="Event data payload")
    correlation_id: Optional[str] = Field(None, description="Correlation ID for tracing")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional event metadata")
    channel: Optional[str] = Field(None, description="Target channel for event publishing")
    headers: Dict[str, str] = Field(default_factory=dict, description="Event headers")


class EventPublishResponse(BaseModel):
    """Response model for event publishing."""
    event_id: str = Field(..., description="Generated event ID")
    status: str = Field(..., description="Publishing status")
    message: str = Field(..., description="Response message")
    channel: Optional[str] = Field(None, description="Channel where event was published")


# Metric Models
class MetricType(str, Enum):
    """Metric type enum."""
    GAUGE = "gauge"
    COUNTER = "counter"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"


class MetricData(BaseModel):
    """Model for metric data ingestion."""
    name: str = Field(..., description="Metric name")
    value: float = Field(..., description="Metric value")
    timestamp: Optional[datetime] = Field(None, description="Timestamp when the metric was recorded")
    service_name: str = Field(..., description="Name of the service that generated the metric")
    aggregation: str = Field("gauge", description="Aggregation type (gauge, counter, histogram, etc.)")
    labels: Dict[str, str] = Field(default_factory=dict, description="Additional metric labels")


class MetricDataBatch(BaseModel):
    """Model for batch metric data ingestion."""
    metrics: List[MetricData] = Field(..., description="List of metric data")


class MetricQuery(BaseModel):
    """Model for metric data queries."""
    name: Optional[str] = Field(None, description="Filter by metric name")
    service_name: Optional[str] = Field(None, description="Filter by service name")
    aggregation: Optional[str] = Field(None, description="Filter by aggregation type")
    labels: Dict[str, str] = Field(default_factory=dict, description="Filter by labels")
    start_time: Optional[datetime] = Field(None, description="Start time for query")
    end_time: Optional[datetime] = Field(None, description="End time for query")
    limit: int = Field(100, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")


class MetricResponse(BaseModel):
    """Response model for metric operations."""
    name: str = Field(..., description="Metric name")
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Response message")


class MetricStatistics(BaseModel):
    """Metric statistics model."""
    total_metrics: int = Field(..., description="Total number of metrics")
    gauge_count: int = Field(..., description="Number of gauge metrics")
    counter_count: int = Field(..., description="Number of counter metrics")
    histogram_count: int = Field(..., description="Number of histogram metrics")
    summary_count: int = Field(..., description="Number of summary metrics")
    metric_name_count: int = Field(..., description="Number of unique metric names")
    service_count: int = Field(..., description="Number of unique services")
    metric_names: List[str] = Field(..., description="List of metric names")
    services: List[str] = Field(..., description="List of services")
    start_time: datetime = Field(..., description="Start time of statistics")
    end_time: datetime = Field(..., description="End time of statistics")


# Trace Models
class TraceData(BaseModel):
    """Model for trace data ingestion."""
    service: str = Field(..., description="Name of the service generating the trace")
    trace_id: str = Field(..., description="Unique trace identifier")
    span_id: str = Field(..., description="Unique span identifier")
    parent_span_id: Optional[str] = Field(None, description="Parent span identifier")
    name: str = Field(..., description="Name of the span")
    kind: str = Field(..., description="Kind of span (server, client, etc.)")
    timestamp: Optional[datetime] = Field(None, description="Start time of the span")
    duration_ms: Optional[float] = Field(None, description="Duration of the span in milliseconds")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Span attributes")
    events: List[Dict[str, Any]] = Field(default_factory=list, description="Span events")
    status_code: str = Field(..., description="Status code of the span")
    status_message: Optional[str] = Field(None, description="Status message")


class TraceDataBatch(BaseModel):
    """Model for batch trace data ingestion."""
    traces: List[TraceData] = Field(..., description="List of trace data")


class TraceQuery(BaseModel):
    """Model for trace data queries."""
    service: Optional[str] = Field(None, description="Filter by service name")
    trace_id: Optional[str] = Field(None, description="Filter by trace ID")
    span_id: Optional[str] = Field(None, description="Filter by span ID")
    parent_span_id: Optional[str] = Field(None, description="Filter by parent span ID")
    name: Optional[str] = Field(None, description="Filter by span name")
    kind: Optional[str] = Field(None, description="Filter by span kind")
    status_code: Optional[str] = Field(None, description="Filter by status code")
    start_time: Optional[datetime] = Field(None, description="Start time for query")
    end_time: Optional[datetime] = Field(None, description="End time for query")
    min_duration_ms: Optional[float] = Field(None, description="Minimum duration filter")
    max_duration_ms: Optional[float] = Field(None, description="Maximum duration filter")
    limit: int = Field(100, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")


class TraceResponse(BaseModel):
    """Response model for trace operations."""
    trace_id: str = Field(..., description="Trace ID")
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Response message")


class TraceStatistics(BaseModel):
    """Trace statistics model."""
    total_traces: int = Field(..., description="Total number of traces")
    error_count: int = Field(..., description="Number of traces with errors")
    error_rate: float = Field(..., description="Error rate (0.0 to 1.0)")
    avg_duration_ms: float = Field(..., description="Average trace duration in milliseconds")
    service_count: int = Field(..., description="Number of unique services")
    services: List[str] = Field(..., description="List of services")
    start_time: datetime = Field(..., description="Start time of statistics")
    end_time: datetime = Field(..., description="End time of statistics")


# Query Models (for advanced querying across data types)
class QueryData(BaseModel):
    """Model for advanced query data."""
    query_id: str = Field(..., description="Unique query identifier")
    query_type: str = Field(..., description="Type of query")
    parameters: Dict[str, Any] = Field(..., description="Query parameters")
    timestamp: Optional[datetime] = Field(None, description="Query timestamp")


class QueryDataBatch(BaseModel):
    """Model for batch query data."""
    queries: List[QueryData] = Field(..., description="List of query data")


class QueryQuery(BaseModel):
    """Model for advanced query parameters."""
    data_types: List[str] = Field(..., description="Types of data to query (trace, metric, event, health, dependency)")
    service: Optional[str] = Field(None, description="Filter by service name")
    start_time: Optional[datetime] = Field(None, description="Start time for query")
    end_time: Optional[datetime] = Field(None, description="End time for query")
    correlation_id: Optional[str] = Field(None, description="Filter by correlation ID")
    trace_id: Optional[str] = Field(None, description="Filter by trace ID")
    span_id: Optional[str] = Field(None, description="Filter by span ID")
    parent_span_id: Optional[str] = Field(None, description="Filter by parent span ID")
    metric_name: Optional[str] = Field(None, description="Filter by metric name")
    event_type: Optional[str] = Field(None, description="Filter by event type")
    limit: int = Field(100, description="Maximum number of results")
    offset: int = Field(0, description="Offset for pagination")
    order_by: Optional[str] = Field(None, description="Field to order by")
    order_direction: Optional[str] = Field("desc", description="Order direction (asc, desc)")


class QueryResponse(BaseModel):
    """Response model for query operations."""
    query_id: str = Field(..., description="Query ID")
    status: str = Field(..., description="Query status")
    message: str = Field(..., description="Response message")
    results: Dict[str, List[Dict[str, Any]]] = Field(..., description="Query results by data type")
    execution_time_ms: float = Field(..., description="Query execution time in milliseconds")


class QueryStatistics(BaseModel):
    """Query statistics model."""
    total_queries: int = Field(..., description="Total number of queries executed")
    avg_execution_time_ms: float = Field(..., description="Average execution time in milliseconds")
    data_type_counts: Dict[str, int] = Field(..., description="Count of queries by data type")
    service_counts: Dict[str, int] = Field(..., description="Count of queries by service")
    start_time: datetime = Field(..., description="Start time of statistics")
    end_time: datetime = Field(..., description="End time of statistics")


# Metrics Ingestion Models
class MetricsIngestRequest(BaseModel):
    """Model for metrics ingestion requests."""
    service: str = Field(..., description="Service name that is sending metrics")
    timestamp: datetime = Field(..., description="Timestamp when metrics were collected")
    metrics: str = Field(..., description="Prometheus formatted metrics data")
    format: str = Field(default="prometheus", description="Format of the metrics data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "api_service",
                "timestamp": "2023-01-01T12:00:00Z",
                "metrics": "# HELP http_requests_total Total HTTP requests\n# TYPE http_requests_total counter\nhttp_requests_total{method=\"GET\",status=\"200\"} 1000\n",
                "format": "prometheus"
            }
        }
    )


class MetricsIngestResponse(BaseModel):
    """Model for metrics ingestion responses."""
    success: bool = Field(..., description="Whether the metrics ingestion was successful")
    message: str = Field(..., description="Response message")
    metrics_count: Optional[int] = Field(None, description="Number of metrics ingested")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Metrics ingested successfully",
                "metrics_count": 15
            }
        }
    )


# Incoming Event Model (for callback)
class IncomingEvent(BaseModel):
    """Generic model for an event received from the messaging service callback."""
    event_type: str = Field(..., description="The type of the event.")
    event_data: Dict[str, Any] = Field(..., description="The payload of the event.")
    source_service: str = Field(..., description="The service that originally published the event.")
    timestamp: datetime = Field(..., description="The timestamp of when the event was published.")
    correlation_id: Optional[str] = Field(None, description="Correlation ID for tracing the event across services.")
    message_id: Optional[str] = Field(None, description="Unique ID of the message from the messaging system.")

