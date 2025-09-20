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


class ComponentHealth(BaseModel):
    """Health status of a specific component."""
    status: HealthStatus = Field(..., description="Health status of the component")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional health details")
    last_check: datetime = Field(default_factory=datetime.now, description="Timestamp of the last health check")
    latency_ms: Optional[float] = Field(None, description="Latency of the health check in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "healthy",
                "details": {"connection": "established", "version": "1.0.0"},
                "last_check": "2023-01-01T00:00:00Z",
                "latency_ms": 5.2
            }
        }
    )


class HealthCheck(BaseModel):
    """Health check model for services."""
    service: str = Field(..., description="Service name")
    status: HealthStatus = Field(..., description="Health status")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the health check")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional health details")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "observability_service",
                "status": "healthy",
                "timestamp": "2023-01-01T00:00:00Z",
                "details": {"message": "Service is healthy"}
            }
        }
    )


class DependencyCheck(BaseModel):
    """Dependency check model for service dependencies."""
    name: str = Field(..., description="Dependency name")
    type: str = Field(..., description="Dependency type (database, service, etc.)")
    status: HealthStatus = Field(..., description="Dependency health status")
    latency_ms: float = Field(..., description="Latency in milliseconds")
    last_check: datetime = Field(default_factory=datetime.now, description="Last check timestamp")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional dependency details")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "database",
                "type": "postgresql",
                "status": "healthy",
                "latency_ms": 5.2,
                "last_check": "2023-01-01T00:00:00Z",
                "details": {"connection": "established", "version": "14.0"}
            }
        }
    )


class ServiceHealthResponse(BaseModel):
    """Overall health status of the service and its dependencies."""
    service: str = Field(..., description="Service name")
    status: HealthStatus = Field(..., description="Overall health status")
    version: str = Field(..., description="Service version")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
    components: Dict[str, ComponentHealth] = Field(
        default_factory=dict, 
        description="Health status of individual components"
    )
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the health check")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service": "observability_service",
                "status": "healthy",
                "version": "1.0.0",
                "uptime_seconds": 3600,
                "components": {
                    "database": {
                        "status": "healthy",
                        "details": {"connection": "established"},
                        "last_check": "2023-01-01T00:00:00Z",
                        "latency_ms": 5.2
                    },
                    "redis": {
                        "status": "healthy",
                        "details": {"connection": "established"},
                        "last_check": "2023-01-01T00:00:00Z",
                        "latency_ms": 2.1
                    }
                },
                "timestamp": "2023-01-01T00:00:00Z"
            }
        }
    )


# Trace Models
class SpanStatus(str, Enum):
    """Status of a span in a trace."""
    OK = "ok"
    ERROR = "error"
    UNSET = "unset"


class SpanResponse(BaseModel):
    """Response model for a span in a distributed trace."""
    span_id: str = Field(..., description="Unique identifier for the span")
    trace_id: str = Field(..., description="Trace ID this span belongs to")
    parent_span_id: Optional[str] = Field(None, description="Parent span ID if applicable")
    name: str = Field(..., description="Name of the span")
    kind: str = Field(..., description="Kind of span (server, client, producer, consumer)")
    start_time: datetime = Field(..., description="Start time of the span")
    end_time: Optional[datetime] = Field(None, description="End time of the span")
    duration_ms: float = Field(..., description="Duration of the span in milliseconds")
    status: SpanStatus = Field(..., description="Status of the span")
    service_name: str = Field(..., description="Name of the service that generated the span")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Span attributes")
    events: List[Dict[str, Any]] = Field(default_factory=list, description="Events associated with the span")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "span_id": "1234567890abcdef",
                "trace_id": "abcdef1234567890abcdef1234567890",
                "parent_span_id": "0987654321fedcba",
                "name": "process_request",
                "kind": "server",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T00:00:01Z",
                "duration_ms": 1000.0,
                "status": "ok",
                "service_name": "api_service",
                "attributes": {
                    "http.method": "GET",
                    "http.url": "/api/v1/items",
                    "http.status_code": 200
                },
                "events": [
                    {
                        "name": "exception",
                        "timestamp": "2023-01-01T00:00:00.500Z",
                        "attributes": {
                            "exception.type": "ValueError",
                            "exception.message": "Invalid input"
                        }
                    }
                ]
            }
        }
    )


class TraceResponse(BaseModel):
    """Response model for a complete distributed trace."""
    trace_id: str = Field(..., description="Unique identifier for the trace")
    root_span_id: str = Field(..., description="ID of the root span")
    start_time: datetime = Field(..., description="Start time of the trace")
    end_time: Optional[datetime] = Field(None, description="End time of the trace")
    duration_ms: float = Field(..., description="Total duration of the trace in milliseconds")
    status: SpanStatus = Field(..., description="Overall status of the trace")
    service_count: int = Field(..., description="Number of services involved in the trace")
    span_count: int = Field(..., description="Total number of spans in the trace")
    error_count: int = Field(..., description="Number of spans with errors")
    root_service: str = Field(..., description="Name of the service that initiated the trace")
    spans: List[SpanResponse] = Field(..., description="List of spans in the trace")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "trace_id": "abcdef1234567890abcdef1234567890",
                "root_span_id": "1234567890abcdef",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T00:00:02Z",
                "duration_ms": 2000.0,
                "status": "ok",
                "service_count": 3,
                "span_count": 10,
                "error_count": 0,
                "root_service": "api_gateway",
                "spans": []  # Truncated for brevity
            }
        }
    )


class TraceSearchResponse(BaseModel):
    """Response model for trace search results."""
    traces: List[TraceResponse] = Field(..., description="List of traces matching the search criteria")
    total_count: int = Field(..., description="Total number of traces matching the search criteria")
    page: int = Field(1, description="Current page number")
    page_size: int = Field(..., description="Number of traces per page")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "traces": [],  # Truncated for brevity
                "total_count": 100,
                "page": 1,
                "page_size": 10
            }
        }
    )


class ServiceDependencyResponse(BaseModel):
    """Response model for service dependency information."""
    source_service: str = Field(..., description="Source service name")
    target_service: str = Field(..., description="Target service name")
    call_count: int = Field(..., description="Number of calls between services")
    average_latency_ms: float = Field(..., description="Average latency in milliseconds")
    error_rate: float = Field(..., description="Error rate as a percentage")
    last_seen: datetime = Field(..., description="Timestamp of the last call")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source_service": "api_gateway",
                "target_service": "user_service",
                "call_count": 1000,
                "average_latency_ms": 50.5,
                "error_rate": 0.2,
                "last_seen": "2023-01-01T00:00:00Z"
            }
        }
    )


class TracePathNode(BaseModel):
    """Node in a trace path."""
    service_name: str = Field(..., description="Service name")
    span_id: str = Field(..., description="Span ID")
    operation_name: str = Field(..., description="Operation name")
    duration_ms: float = Field(..., description="Duration in milliseconds")
    status: SpanStatus = Field(..., description="Status of the span")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "span_id": "1234567890abcdef",
                "operation_name": "process_request",
                "duration_ms": 100.5,
                "status": "ok"
            }
        }
    )


class TracePathResponse(BaseModel):
    """Response model for a trace path."""
    trace_id: str = Field(..., description="Trace ID")
    path: List[TracePathNode] = Field(..., description="Path of spans through services")
    total_duration_ms: float = Field(..., description="Total duration of the path in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "trace_id": "abcdef1234567890abcdef1234567890",
                "path": [],  # Truncated for brevity
                "total_duration_ms": 500.5
            }
        }
    )


# Metrics Models
class MetricType(str, Enum):
    """Types of metrics."""
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"


class MetricResponse(BaseModel):
    """Response model for a metric."""
    name: str = Field(..., description="Metric name")
    description: str = Field(..., description="Metric description")
    type: MetricType = Field(..., description="Metric type")
    value: float = Field(..., description="Current metric value")
    timestamp: datetime = Field(..., description="Timestamp when the metric was recorded")
    labels: Dict[str, str] = Field(default_factory=dict, description="Metric labels")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "http_requests_total",
                "description": "Total number of HTTP requests",
                "type": "counter",
                "value": 1000.0,
                "timestamp": "2023-01-01T00:00:00Z",
                "labels": {
                    "method": "GET",
                    "endpoint": "/api/v1/items",
                    "status": "200"
                }
            }
        }
    )


class MetricTimeSeriesPoint(BaseModel):
    """A single point in a metric time series."""
    timestamp: datetime = Field(..., description="Timestamp of the data point")
    value: float = Field(..., description="Metric value at this timestamp")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "timestamp": "2023-01-01T00:00:00Z",
                "value": 42.0
            }
        }
    )


class MetricTimeSeriesResponse(BaseModel):
    """Response model for a metric time series."""
    name: str = Field(..., description="Metric name")
    description: str = Field(..., description="Metric description")
    type: MetricType = Field(..., description="Metric type")
    labels: Dict[str, str] = Field(default_factory=dict, description="Metric labels")
    start_time: datetime = Field(..., description="Start time of the time series")
    end_time: datetime = Field(..., description="End time of the time series")
    interval_seconds: int = Field(..., description="Interval between data points in seconds")
    data_points: List[MetricTimeSeriesPoint] = Field(..., description="Time series data points")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "http_requests_total",
                "description": "Total number of HTTP requests",
                "type": "counter",
                "labels": {
                    "method": "GET",
                    "endpoint": "/api/v1/items",
                    "status": "200"
                },
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "interval_seconds": 60,
                "data_points": [
                    {"timestamp": "2023-01-01T00:00:00Z", "value": 10.0},
                    {"timestamp": "2023-01-01T00:01:00Z", "value": 15.0}
                ]
            }
        }
    )


class MetricAggregation(str, Enum):
    """Types of metric aggregations."""
    SUM = "sum"
    AVG = "avg"
    MIN = "min"
    MAX = "max"
    COUNT = "count"
    P50 = "p50"
    P90 = "p90"
    P95 = "p95"
    P99 = "p99"


class MetricAggregationResponse(BaseModel):
    """Response model for metric aggregations."""
    name: str = Field(..., description="Metric name")
    aggregation: MetricAggregation = Field(..., description="Aggregation type")
    value: float = Field(..., description="Aggregated value")
    start_time: datetime = Field(..., description="Start time of the aggregation period")
    end_time: datetime = Field(..., description="End time of the aggregation period")
    labels: Dict[str, str] = Field(default_factory=dict, description="Metric labels")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "http_request_duration_seconds",
                "aggregation": "avg",
                "value": 0.25,
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "labels": {
                    "method": "GET",
                    "endpoint": "/api/v1/items"
                }
            }
        }
    )


class ServiceMetric(BaseModel):
    """Metrics for a specific service."""
    service_name: str = Field(..., description="Service name")
    request_rate: float = Field(..., description="Requests per second")
    error_rate: float = Field(..., description="Error rate as a percentage")
    average_latency_ms: float = Field(..., description="Average latency in milliseconds")
    p95_latency_ms: float = Field(..., description="95th percentile latency in milliseconds")
    cpu_usage_percent: float = Field(..., description="CPU usage percentage")
    memory_usage_mb: float = Field(..., description="Memory usage in MB")
    uptime_seconds: float = Field(..., description="Service uptime in seconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "request_rate": 50.5,
                "error_rate": 0.2,
                "average_latency_ms": 25.5,
                "p95_latency_ms": 75.0,
                "cpu_usage_percent": 15.5,
                "memory_usage_mb": 256.0,
                "uptime_seconds": 3600.0
            }
        }
    )


class ServiceMetricsResponse(BaseModel):
    """Response model for service metrics."""
    services: List[ServiceMetric] = Field(..., description="List of service metrics")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the metrics")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "services": [],  # Truncated for brevity
                "timestamp": "2023-01-01T00:00:00Z"
            }
        }
    )


# Trace Models
class TraceData(BaseModel):
    """Model for trace data."""
    trace_id: str = Field(..., description="Unique trace identifier")
    span_id: str = Field(..., description="Unique span identifier")
    parent_span_id: Optional[str] = Field(None, description="Parent span identifier")
    name: str = Field(..., description="Name of the span")
    kind: str = Field(..., description="Kind of span (SERVER, CLIENT, etc.)")
    start_time: datetime = Field(..., description="Start time of the span")
    end_time: datetime = Field(..., description="End time of the span")
    duration_ms: float = Field(..., description="Duration of the span in milliseconds")
    service_name: str = Field(..., description="Name of the service that generated the span")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Additional span attributes")
    status_code: str = Field("OK", description="Status code of the span")
    status_message: Optional[str] = Field(None, description="Status message of the span")
    events: List[Dict[str, Any]] = Field(default_factory=list, description="Events associated with the span")
    links: List[Dict[str, Any]] = Field(default_factory=list, description="Links to other spans")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "trace_id": "1234567890abcdef1234567890abcdef",
                "span_id": "1234567890abcdef",
                "parent_span_id": "0987654321fedcba",
                "name": "GET /api/v1/items",
                "kind": "SERVER",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T00:00:00.100Z",
                "duration_ms": 100.0,
                "service_name": "api_gateway",
                "attributes": {
                    "http.method": "GET",
                    "http.url": "/api/v1/items",
                    "http.status_code": 200
                },
                "status_code": "OK",
                "status_message": None,
                "events": [],
                "links": []
            }
        }
    )


class TraceDataBatch(BaseModel):
    """Model for batch trace data ingestion."""
    traces: List[TraceData] = Field(..., description="List of trace data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "traces": []  # Truncated for brevity
            }
        }
    )


class TraceQuery(BaseModel):
    """Model for querying trace data."""
    trace_id: Optional[str] = Field(None, description="Filter by trace ID")
    service_name: Optional[str] = Field(None, description="Filter by service name")
    operation_name: Optional[str] = Field(None, description="Filter by operation name")
    start_time: Optional[datetime] = Field(None, description="Filter by start time (inclusive)")
    end_time: Optional[datetime] = Field(None, description="Filter by end time (inclusive)")
    min_duration_ms: Optional[float] = Field(None, description="Filter by minimum duration in milliseconds")
    max_duration_ms: Optional[float] = Field(None, description="Filter by maximum duration in milliseconds")
    status_code: Optional[str] = Field(None, description="Filter by status code")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Filter by attributes")
    limit: int = Field(100, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "min_duration_ms": 50.0,
                "attributes": {
                    "http.method": "GET"
                },
                "limit": 100,
                "offset": 0
            }
        }
    )


class TraceStatistics(BaseModel):
    """Model for trace statistics."""
    total_traces: int = Field(..., description="Total number of traces")
    average_duration_ms: float = Field(..., description="Average duration in milliseconds")
    p95_duration_ms: float = Field(..., description="95th percentile duration in milliseconds")
    p99_duration_ms: float = Field(..., description="99th percentile duration in milliseconds")
    error_count: int = Field(..., description="Number of traces with errors")
    error_rate: float = Field(..., description="Error rate as a percentage")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_traces": 1000,
                "average_duration_ms": 50.5,
                "p95_duration_ms": 150.0,
                "p99_duration_ms": 250.0,
                "error_count": 5,
                "error_rate": 0.5
            }
        }
    )


class TraceResponse(BaseModel):
    """Response model for trace queries."""
    traces: List[TraceData] = Field(..., description="List of trace data")
    total: int = Field(..., description="Total number of traces matching the query")
    statistics: Optional[TraceStatistics] = Field(None, description="Statistics about the traces")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "traces": [],  # Truncated for brevity
                "total": 1000,
                "statistics": None
            }
        }
    )


# Metric Models
class MetricType(str, Enum):
    """Metric types for monitoring."""
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"

class MetricData(BaseModel):
    """Model for metric data."""
    name: str = Field(..., description="Metric name")
    value: float = Field(..., description="Metric value")
    timestamp: datetime = Field(..., description="Timestamp when the metric was recorded")
    service_name: str = Field(..., description="Name of the service that generated the metric")
    aggregation: str = Field("gauge", description="Aggregation type (gauge, counter, histogram, etc.)")
    labels: Dict[str, str] = Field(default_factory=dict, description="Additional metric labels")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "http_request_duration_seconds",
                "value": 0.25,
                "timestamp": "2023-01-01T00:00:00Z",
                "service_name": "api_gateway",
                "aggregation": "gauge",
                "labels": {
                    "method": "GET",
                    "endpoint": "/api/v1/items"
                }
            }
        }
    )


class SingleMetric(BaseModel):
    """Model for individual metric data."""
    name: str = Field(..., description="Metric name")
    service_name: str = Field(..., description="Service that generated the metric")
    type: MetricType = Field(..., description="Type of metric")
    value: float = Field(..., description="Metric value")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the metric was recorded")
    labels: Dict[str, str] = Field(default_factory=dict, description="Metric labels")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "http_requests_total",
                "service_name": "api_service",
                "type": "counter",
                "value": 100.0,
                "timestamp": "2023-01-01T00:00:00Z",
                "labels": {
                    "method": "GET",
                    "endpoint": "/api/users"
                }
            }
        }
    )

class MetricDataBatch(BaseModel):
    """Model for batch metric data ingestion."""
    metrics: List[MetricData] = Field(..., description="List of metric data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "metrics": []  # Truncated for brevity
            }
        }
    )


class MetricQuery(BaseModel):
    """Model for querying metric data."""
    name: Optional[str] = Field(None, description="Filter by metric name")
    service_name: Optional[str] = Field(None, description="Filter by service name")
    aggregation: Optional[str] = Field(None, description="Filter by aggregation type")
    start_time: Optional[datetime] = Field(None, description="Filter by start time (inclusive)")
    end_time: Optional[datetime] = Field(None, description="Filter by end time (inclusive)")
    min_value: Optional[float] = Field(None, description="Filter by minimum value")
    max_value: Optional[float] = Field(None, description="Filter by maximum value")
    labels: Dict[str, str] = Field(default_factory=dict, description="Filter by labels")
    limit: int = Field(100, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "http_request_duration_seconds",
                "service_name": "api_gateway",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "labels": {
                    "method": "GET"
                },
                "limit": 100,
                "offset": 0
            }
        }
    )


class MetricStatistics(BaseModel):
    """Model for metric statistics."""
    total_metrics: int = Field(..., description="Total number of metrics")
    by_type: Dict[str, int] = Field(..., description="Count of metrics by type")
    by_service: Dict[str, int] = Field(..., description="Count of metrics by service")
    by_name: Dict[str, int] = Field(..., description="Count of metrics by name")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_metrics": 1000,
                "by_type": {
                    "counter": 500,
                    "gauge": 300,
                    "histogram": 150,
                    "summary": 50
                },
                "by_service": {
                    "api_gateway": 300,
                    "user_service": 400,
                    "product_service": 300
                },
                "by_name": {
                    "http_requests_total": 400,
                    "response_time": 300,
                    "error_rate": 300
                }
            }
        }
    )


class MetricResponse(BaseModel):
    """Response model for metric queries."""
    metrics: List[MetricData] = Field(..., description="List of metric data")
    total: int = Field(..., description="Total number of metrics matching the query")
    statistics: Optional[MetricStatistics] = Field(None, description="Statistics about the metrics")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "metrics": [],  # Truncated for brevity
                "total": 1000,
                "statistics": None
            }
        }
    )

class MetricQueryResponse(BaseModel):
    """Response model for metric queries."""
    metrics: List[SingleMetric] = Field(..., description="List of metric data")
    total: int = Field(..., description="Total number of metrics matching the query")
    statistics: Optional[MetricStatistics] = Field(None, description="Metric statistics")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "metrics": [],  # Truncated for brevity
                "total": 1000,
                "statistics": None
            }
        }
    )


# Health Models
class HealthData(BaseModel):
    """Model for health data."""
    service_name: str = Field(..., description="Name of the service")
    status: str = Field(..., description="Health status (healthy, degraded, unhealthy)")
    timestamp: datetime = Field(..., description="Timestamp when the health check was performed")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional health details")
    latency_ms: Optional[float] = Field(None, description="Latency of the health check in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "status": "healthy",
                "timestamp": "2023-01-01T00:00:00Z",
                "details": {
                    "database": "connected",
                    "redis": "connected",
                    "messaging": "connected"
                },
                "latency_ms": 5.2
            }
        }
    )


class HealthDataBatch(BaseModel):
    """Model for batch health data ingestion."""
    health_checks: List[HealthData] = Field(..., description="List of health data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "health_checks": []  # Truncated for brevity
            }
        }
    )


class HealthQuery(BaseModel):
    """Model for querying health data."""
    service_name: Optional[str] = Field(None, description="Filter by service name")
    status: Optional[str] = Field(None, description="Filter by status")
    start_time: Optional[datetime] = Field(None, description="Filter by start time (inclusive)")
    end_time: Optional[datetime] = Field(None, description="Filter by end time (inclusive)")
    details: Dict[str, Any] = Field(default_factory=dict, description="Filter by details")
    limit: int = Field(100, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "status": "healthy",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "details": {
                    "database": "connected"
                },
                "limit": 100,
                "offset": 0
            }
        }
    )


class HealthStatistics(BaseModel):
    """Model for health statistics."""
    total_checks: int = Field(..., description="Total number of health checks")
    healthy_count: int = Field(..., description="Number of healthy checks")
    degraded_count: int = Field(..., description="Number of degraded checks")
    unhealthy_count: int = Field(..., description="Number of unhealthy checks")
    healthy_rate: float = Field(..., description="Healthy rate as a percentage")
    average_latency_ms: Optional[float] = Field(None, description="Average latency in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_checks": 1000,
                "healthy_count": 950,
                "degraded_count": 40,
                "unhealthy_count": 10,
                "healthy_rate": 95.0,
                "average_latency_ms": 5.5
            }
        }
    )


class HealthResponse(BaseModel):
    """Response model for health queries."""
    health_checks: List[HealthData] = Field(..., description="List of health data")
    total: int = Field(..., description="Total number of health checks matching the query")
    statistics: Optional[HealthStatistics] = Field(None, description="Statistics about the health checks")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "health_checks": [],  # Truncated for brevity
                "total": 1000,
                "statistics": None
            }
        }
    )


# Dependency Models
class DependencyType(str, Enum):
    """Types of service dependencies."""
    SYNCHRONOUS = "synchronous"
    ASYNCHRONOUS = "asynchronous"
    DATABASE = "database"
    CACHE = "cache"
    MESSAGING = "messaging"
    STORAGE = "storage"
    API = "api"


class DependencyStatus(str, Enum):
    """Status of a dependency."""
    ACTIVE = "active"
    DEGRADED = "degraded"
    FAILED = "failed"
    UNKNOWN = "unknown"


class DependencyResponse(BaseModel):
    """Response model for a service dependency."""
    source_service: str = Field(..., description="Source service name")
    target_service: str = Field(..., description="Target service name")
    dependency_type: DependencyType = Field(..., description="Type of dependency")
    status: DependencyStatus = Field(..., description="Current status of the dependency")
    call_count: int = Field(..., description="Number of calls between services")
    average_latency_ms: float = Field(..., description="Average latency in milliseconds")
    error_rate: float = Field(..., description="Error rate as a percentage")
    last_seen: datetime = Field(..., description="Timestamp of the last call")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source_service": "api_gateway",
                "target_service": "user_service",
                "dependency_type": "synchronous",
                "status": "active",
                "call_count": 1000,
                "average_latency_ms": 50.5,
                "error_rate": 0.2,
                "last_seen": "2023-01-01T00:00:00Z"
            }
        }
    )


class DependencyGraphResponse(BaseModel):
    """Response model for a service dependency graph."""
    services: List[str] = Field(..., description="List of service names in the graph")
    dependencies: List[DependencyResponse] = Field(..., description="List of dependencies between services")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the graph")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "services": ["api_gateway", "user_service", "auth_service"],
                "dependencies": [],  # Truncated for brevity
                "timestamp": "2023-01-01T00:00:00Z"
            }
        }
    )


class DependencyData(BaseModel):
    """Model for dependency data."""
    source_service: str = Field(..., description="Source service name")
    target_service: str = Field(..., description="Target service name")
    dependency_type: DependencyType = Field(..., description="Type of dependency")
    timestamp: datetime = Field(..., description="Timestamp when the dependency was recorded")
    latency_ms: Optional[float] = Field(None, description="Latency in milliseconds")
    success: bool = Field(True, description="Whether the dependency call was successful")
    error_message: Optional[str] = Field(None, description="Error message if the call failed")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional dependency details")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source_service": "api_gateway",
                "target_service": "user_service",
                "dependency_type": "synchronous",
                "timestamp": "2023-01-01T00:00:00Z",
                "latency_ms": 25.5,
                "success": True,
                "error_message": None,
                "details": {
                    "endpoint": "/api/v1/users",
                    "method": "GET"
                }
            }
        }
    )


class DependencyDataBatch(BaseModel):
    """Model for batch dependency data ingestion."""
    dependencies: List[DependencyData] = Field(..., description="List of dependency data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "dependencies": []  # Truncated for brevity
            }
        }
    )


class DependencyQuery(BaseModel):
    """Model for querying dependency data."""
    source_service: Optional[str] = Field(None, description="Filter by source service")
    target_service: Optional[str] = Field(None, description="Filter by target service")
    dependency_type: Optional[DependencyType] = Field(None, description="Filter by dependency type")
    start_time: Optional[datetime] = Field(None, description="Filter by start time (inclusive)")
    end_time: Optional[datetime] = Field(None, description="Filter by end time (inclusive)")
    success: Optional[bool] = Field(None, description="Filter by success status")
    min_latency_ms: Optional[float] = Field(None, description="Filter by minimum latency")
    max_latency_ms: Optional[float] = Field(None, description="Filter by maximum latency")
    details: Dict[str, Any] = Field(default_factory=dict, description="Filter by details")
    limit: int = Field(100, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "source_service": "api_gateway",
                "dependency_type": "synchronous",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "success": True,
                "limit": 100,
                "offset": 0
            }
        }
    )


class DependencyStatistics(BaseModel):
    """Model for dependency statistics."""
    total_calls: int = Field(..., description="Total number of dependency calls")
    success_count: int = Field(..., description="Number of successful calls")
    error_count: int = Field(..., description="Number of failed calls")
    success_rate: float = Field(..., description="Success rate as a percentage")
    average_latency_ms: Optional[float] = Field(None, description="Average latency in milliseconds")
    p95_latency_ms: Optional[float] = Field(None, description="95th percentile latency in milliseconds")
    p99_latency_ms: Optional[float] = Field(None, description="99th percentile latency in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_calls": 1000,
                "success_count": 980,
                "error_count": 20,
                "success_rate": 98.0,
                "average_latency_ms": 25.5,
                "p95_latency_ms": 75.0,
                "p99_latency_ms": 150.0
            }
        }
    )


class DependencyPathNode(BaseModel):
    """Node in a dependency path."""
    service_name: str = Field(..., description="Service name")
    dependency_type: DependencyType = Field(..., description="Type of dependency")
    status: DependencyStatus = Field(..., description="Current status of the dependency")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "dependency_type": "synchronous",
                "status": "active"
            }
        }
    )


# Event Models
class EventSeverity(str, Enum):
    """Severity levels for events."""
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class EventData(BaseModel):
    """Model for event data."""
    service_name: str = Field(..., description="Name of the service that generated the event")
    event_type: str = Field(..., description="Type of event")
    severity: EventSeverity = Field(..., description="Severity level of the event")
    timestamp: datetime = Field(..., description="Timestamp when the event occurred")
    message: str = Field(..., description="Event message")
    correlation_id: Optional[str] = Field(None, description="Correlation ID for tracing")
    details: Dict[str, Any] = Field(default_factory=dict, description="Additional event details")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "event_type": "user_login",
                "severity": "info",
                "timestamp": "2023-01-01T00:00:00Z",
                "message": "User successfully logged in",
                "correlation_id": "abc123",
                "details": {
                    "user_id": "user123",
                    "ip_address": "192.168.1.1"
                }
            }
        }
    )


class EventDataBatch(BaseModel):
    """Model for batch event data ingestion."""
    events: List[EventData] = Field(..., description="List of event data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "events": []  # Truncated for brevity
            }
        }
    )

class EventRequest(BaseModel):
    """Model for event publishing requests."""
    event_type: str = Field(..., description="Type of event")
    source_service: str = Field(..., description="Service that is publishing the event")
    event_data: Dict[str, Any] = Field(..., description="Event data payload")
    correlation_id: Optional[str] = Field(None, description="Correlation ID for tracing")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    channel: Optional[str] = Field(None, description="Channel to publish the event to")
    headers: Dict[str, str] = Field(default_factory=dict, description="Additional headers")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "event_type": "test.event",
                "source_service": "test_client",
                "event_data": {
                    "message": "This is a test event",
                    "timestamp": "2023-01-01T00:00:00Z"
                },
                "correlation_id": "test-123",
                "metadata": {
                    "test": True,
                    "environment": "development"
                },
                "channel": "default",
                "headers": {}
            }
        }
    )


class EventPublishResponse(BaseModel):
    """Response model for event publishing."""
    success: bool = Field(..., description="Whether the event was published successfully")
    message: str = Field(..., description="Response message")
    event_id: Optional[str] = Field(None, description="Generated event ID")
    correlation_id: Optional[str] = Field(None, description="Correlation ID")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "success": True,
                "message": "Event published successfully",
                "event_id": "evt_123456789",
                "correlation_id": "test-123"
            }
        }
    )


class EventQuery(BaseModel):
    """Model for querying event data."""
    service_name: Optional[str] = Field(None, description="Filter by service name")
    event_type: Optional[str] = Field(None, description="Filter by event type")
    severity: Optional[EventSeverity] = Field(None, description="Filter by severity level")
    start_time: Optional[datetime] = Field(None, description="Filter by start time (inclusive)")
    end_time: Optional[datetime] = Field(None, description="Filter by end time (inclusive)")
    message_contains: Optional[str] = Field(None, description="Filter by message content")
    correlation_id: Optional[str] = Field(None, description="Filter by correlation ID")
    details: Dict[str, Any] = Field(default_factory=dict, description="Filter by details")
    limit: int = Field(100, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "severity": "error",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "limit": 100,
                "offset": 0
            }
        }
    )


class EventStatistics(BaseModel):
    """Model for event statistics."""
    total_events: int = Field(..., description="Total number of events")
    by_severity: Dict[str, int] = Field(..., description="Count of events by severity")
    by_service: Dict[str, int] = Field(..., description="Count of events by service")
    by_event_type: Dict[str, int] = Field(..., description="Count of events by type")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_events": 1000,
                "by_severity": {
                    "debug": 200,
                    "info": 500,
                    "warning": 200,
                    "error": 80,
                    "critical": 20
                },
                "by_service": {
                    "api_gateway": 300,
                    "user_service": 400,
                    "product_service": 300
                },
                "by_event_type": {
                    "user_login": 200,
                    "product_view": 300,
                    "order_placed": 500
                }
            }
        }
    )


class EventResponse(BaseModel):
    """Response model for event queries."""
    events: List[EventData] = Field(..., description="List of event data")
    total: int = Field(..., description="Total number of events matching the query")
    statistics: Optional[EventStatistics] = Field(None, description="Statistics about the events")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "events": [],  # Truncated for brevity
                "total": 1000,
                "statistics": None
            }
        }
    )


# Telemetry data models for observability service
class TraceData(BaseModel):
    """Model for trace data ingestion."""
    service_name: str = Field(..., description="Name of the service generating the trace")
    trace_id: str = Field(..., description="Unique trace identifier")
    span_id: str = Field(..., description="Unique span identifier")
    parent_span_id: Optional[str] = Field(None, description="Parent span identifier")
    name: str = Field(..., description="Name of the span")
    kind: str = Field(..., description="Kind of span (server, client, etc.)")
    start_time: datetime = Field(..., description="Start time of the span")
    end_time: datetime = Field(..., description="End time of the span")
    attributes: Dict[str, Any] = Field(default_factory=dict, description="Span attributes")
    events: List[Dict[str, Any]] = Field(default_factory=list, description="Span events")
    status_code: str = Field(..., description="Status code of the span")
    status_message: Optional[str] = Field(None, description="Status message")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_service",
                "trace_id": "0af7651916cd43dd8448eb211c80319c",
                "span_id": "b7ad6b7169203331",
                "parent_span_id": "5b4185666d50f5a9",
                "name": "HTTP GET /api/users",
                "kind": "server",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T00:00:01Z",
                "attributes": {
                    "http.method": "GET",
                    "http.url": "/api/users",
                    "http.status_code": 200
                },
                "events": [],
                "status_code": "ok",
                "status_message": None
            }
        }
    )


class DependencyData(BaseModel):
    """Model for dependency data ingestion."""
    service_name: str = Field(..., description="Name of the service reporting dependencies")
    dependencies: List[Dict[str, Any]] = Field(..., description="List of dependencies")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_service",
                "dependencies": [
                    {
                        "name": "database_service",
                        "type": "http",
                        "status": "healthy",
                        "latency_ms": 15.2,
                        "details": {"connection": "established"}
                    }
                ]
            }
        }
    )



class DependencyPathResponse(BaseModel):
    """Response model for a dependency path."""
    path: List[DependencyPathNode] = Field(..., description="Path of dependencies between services")
    total_latency_ms: float = Field(..., description="Total latency of the path in milliseconds")
    error_probability: float = Field(..., description="Probability of an error along this path")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "path": [],  # Truncated for brevity
                "total_latency_ms": 150.5,
                "error_probability": 0.05
            }
        }
    )


class CriticalDependencyResponse(BaseModel):
    """Response model for critical dependencies."""
    service_name: str = Field(..., description="Service name")
    critical_dependencies: List[DependencyResponse] = Field(..., description="List of critical dependencies")
    impact_score: float = Field(..., description="Impact score (0-1) indicating criticality")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_gateway",
                "critical_dependencies": [],  # Truncated for brevity
                "impact_score": 0.85
            }
        }
    )


class DependencyImpactResponse(BaseModel):
    """Response model for dependency impact analysis."""
    affected_service: str = Field(..., description="Service that would be affected")
    impacting_service: str = Field(..., description="Service that would cause the impact")
    impact_level: float = Field(..., description="Impact level (0-1)")
    affected_operations: List[str] = Field(..., description="Operations that would be affected")
    estimated_users_affected: int = Field(..., description="Estimated number of users that would be affected")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "affected_service": "api_gateway",
                "impacting_service": "user_service",
                "impact_level": 0.75,
                "affected_operations": ["login", "user_profile"],
                "estimated_users_affected": 5000
            }
        }
    )


# Removed duplicate TraceData model definition - using the one defined at line ~535


# Query Models
class QueryData(BaseModel):
    """Model for query data."""
    query_type: str = Field(..., description="Type of query (advanced, correlation, topology, dependency)")
    parameters: Dict[str, Any] = Field(..., description="Query parameters")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the query")
    execution_time_ms: Optional[float] = Field(None, description="Query execution time in milliseconds")
    result_count: Optional[int] = Field(None, description="Number of results returned")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "query_type": "advanced",
                "parameters": {
                    "service_name": "api_gateway",
                    "start_time": "2023-01-01T00:00:00Z",
                    "end_time": "2023-01-01T01:00:00Z",
                    "data_types": ["trace", "metric", "event"]
                },
                "timestamp": "2023-01-01T00:00:00Z",
                "execution_time_ms": 150.5,
                "result_count": 42
            }
        }
    )


class QueryDataBatch(BaseModel):
    """Model for batch query data ingestion."""
    queries: List[QueryData] = Field(..., description="List of query data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "queries": []  # Truncated for brevity
            }
        }
    )


class QueryQuery(BaseModel):
    """Model for querying query data."""
    query_type: Optional[str] = Field(None, description="Filter by query type")
    service_name: Optional[str] = Field(None, description="Filter by service name")
    start_time: Optional[datetime] = Field(None, description="Filter by start time")
    end_time: Optional[datetime] = Field(None, description="Filter by end time")
    min_execution_time_ms: Optional[float] = Field(None, description="Filter by minimum execution time")
    max_execution_time_ms: Optional[float] = Field(None, description="Filter by maximum execution time")
    parameters: Optional[Dict[str, Any]] = Field(None, description="Filter by query parameters")
    limit: int = Field(100, description="Maximum number of results to return")
    offset: int = Field(0, description="Offset for pagination")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "query_type": "advanced",
                "service_name": "api_gateway",
                "start_time": "2023-01-01T00:00:00Z",
                "end_time": "2023-01-01T01:00:00Z",
                "min_execution_time_ms": 50.0,
                "parameters": {
                    "data_types": ["trace"]
                },
                "limit": 100,
                "offset": 0
            }
        }
    )


class QueryStatistics(BaseModel):
    """Model for query statistics."""
    total_queries: int = Field(..., description="Total number of queries")
    by_query_type: Dict[str, int] = Field(..., description="Count of queries by type")
    average_execution_time_ms: float = Field(..., description="Average execution time in milliseconds")
    p95_execution_time_ms: float = Field(..., description="95th percentile execution time in milliseconds")
    p99_execution_time_ms: float = Field(..., description="99th percentile execution time in milliseconds")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "total_queries": 1000,
                "by_query_type": {
                    "advanced": 500,
                    "correlation": 300,
                    "topology": 100,
                    "dependency": 100
                },
                "average_execution_time_ms": 75.5,
                "p95_execution_time_ms": 150.0,
                "p99_execution_time_ms": 250.0
            }
        }
    )


class QueryResponse(BaseModel):
    """Response model for query queries."""
    queries: List[QueryData] = Field(..., description="List of query data")
    total: int = Field(..., description="Total number of queries matching the query")
    statistics: Optional[QueryStatistics] = Field(None, description="Query statistics")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "queries": [],  # Truncated for brevity
                "total": 1000,
                "statistics": None
            }
        }
    )


class MetricData(BaseModel):
    """Model for metric data ingestion."""
    service_name: str = Field(..., description="Name of the service generating the metrics")
    metrics: str = Field(..., description="Prometheus format metrics data")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "service_name": "api_service",
                "metrics": "# HELP http_requests_total Total number of HTTP requests\n# TYPE http_requests_total counter\nhttp_requests_total{method=\"get\",endpoint=\"/api/users\"} 100\n"
            }
        }
    )


# This DependencyData model was removed to avoid duplication with the one at line ~588


# Error Models
class ErrorResponse(BaseModel):
    """Standard error response model."""
    error: str = Field(..., description="Error message")
    code: int = Field(..., description="Error code")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the error")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "error": "Resource not found",
                "code": 404,
                "details": {"resource_id": "123", "resource_type": "trace"},
                "timestamp": "2023-01-01T00:00:00Z"
            }
        }
    )


class ValidationErrorResponse(BaseModel):
    """Validation error response model."""
    error: str = Field("Validation error", description="Error message")
    code: int = Field(422, description="Error code")
    details: Dict[str, List[str]] = Field(..., description="Validation error details by field")
    timestamp: datetime = Field(default_factory=datetime.now, description="Timestamp of the error")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "error": "Validation error",
                "code": 422,
                "details": {
                    "start_time": ["Invalid datetime format"],
                    "service_name": ["Field required"]
                },
                "timestamp": "2023-01-01T00:00:00Z"
            }
        }
    )
