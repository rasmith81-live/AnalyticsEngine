# Observability Service

## Overview

Observability Service API

This is the main module for the Observability Service API.
It provides endpoints for telemetry ingestion, querying, and analysis.

## Data Models

### `ErrorResponse`

Standard error response model.

**Fields:**

- `status_code`: `int`
- `detail`: `str`
- `timestamp`: `datetime`
- `path`: `Optional[str]`
- `trace_id`: `Optional[str]`

### `HealthData`

Model for health check data ingestion.

**Fields:**

- `service`: `str`
- `status`: `HealthStatus`
- `timestamp`: `Optional[datetime]`
- `details`: `Dict[str, Any]`
- `latency_ms`: `Optional[float]`

### `HealthDataBatch`

Model for batch health data ingestion.

**Fields:**

- `health_data`: `List[HealthData]`

### `HealthQuery`

Model for health data queries.

**Fields:**

- `service`: `Optional[str]`
- `status`: `Optional[HealthStatus]`
- `start_time`: `Optional[datetime]`
- `end_time`: `Optional[datetime]`
- `limit`: `int`
- `offset`: `int`

### `HealthResponse`

Response model for health operations.

**Fields:**

- `service`: `str`
- `status`: `str`
- `message`: `str`

### `HealthStatistics`

Health statistics model.

**Fields:**

- `total_checks`: `int`
- `healthy_count`: `int`
- `degraded_count`: `int`
- `unhealthy_count`: `int`
- `avg_latency_ms`: `float`
- `service_count`: `int`
- `services`: `List[str]`
- `start_time`: `datetime`
- `end_time`: `datetime`

### `ComponentHealth`

Component health model for service health checks.

**Fields:**

- `status`: `HealthStatus`
- `details`: `Dict[str, Any]`
- `last_check`: `datetime`

### `ServiceHealthResponse`

Service health response model.

**Fields:**

- `service`: `str`
- `status`: `HealthStatus`
- `version`: `str`
- `uptime_seconds`: `float`
- `components`: `Dict[str, ComponentHealth]`

### `DependencyData`

Model for dependency check data ingestion.

**Fields:**

- `service`: `str`
- `name`: `str`
- `type`: `str`
- `status`: `DependencyStatus`
- `timestamp`: `Optional[datetime]`
- `details`: `Dict[str, Any]`
- `latency_ms`: `Optional[float]`

### `DependencyDataBatch`

Model for batch dependency data ingestion.

**Fields:**

- `dependency_data`: `List[DependencyData]`

### `DependencyQuery`

Model for dependency data queries.

**Fields:**

- `service`: `Optional[str]`
- `name`: `Optional[str]`
- `type`: `Optional[str]`
- `status`: `Optional[DependencyStatus]`
- `start_time`: `Optional[datetime]`
- `end_time`: `Optional[datetime]`
- `limit`: `int`
- `offset`: `int`

### `DependencyResponse`

Response model for dependency operations.

**Fields:**

- `name`: `str`
- `status`: `str`
- `message`: `str`

### `DependencyStatistics`

Dependency statistics model.

**Fields:**

- `total_checks`: `int`
- `available_count`: `int`
- `unavailable_count`: `int`
- `degraded_count`: `int`
- `avg_latency_ms`: `float`
- `dependency_count`: `int`
- `service_count`: `int`
- `dependencies`: `List[str]`
- `services`: `List[str]`
- `start_time`: `datetime`
- `end_time`: `datetime`

### `EventData`

Model for event data ingestion.

**Fields:**

- `event_type`: `str`
- `source_service`: `str`
- `event_data`: `Dict[str, Any]`
- `timestamp`: `Optional[datetime]`
- `correlation_id`: `Optional[str]`
- `severity`: `EventSeverity`
- `metadata`: `Dict[str, Any]`

### `EventDataBatch`

Model for batch event data ingestion.

**Fields:**

- `events`: `List[EventData]`

### `EventQuery`

Model for event data queries.

**Fields:**

- `event_type`: `Optional[str]`
- `source_service`: `Optional[str]`
- `severity`: `Optional[EventSeverity]`
- `correlation_id`: `Optional[str]`
- `start_time`: `Optional[datetime]`
- `end_time`: `Optional[datetime]`
- `limit`: `int`
- `offset`: `int`

### `EventResponse`

Response model for event operations.

**Fields:**

- `event_type`: `str`
- `status`: `str`
- `message`: `str`

### `EventStatistics`

Event statistics model.

**Fields:**

- `total_events`: `int`
- `info_count`: `int`
- `warning_count`: `int`
- `error_count`: `int`
- `critical_count`: `int`
- `event_type_count`: `int`
- `service_count`: `int`
- `event_types`: `List[str]`
- `services`: `List[str]`
- `start_time`: `datetime`
- `end_time`: `datetime`

### `EventRequest`

Model for event publishing requests.

**Fields:**

- `event_type`: `str`
- `source_service`: `str`
- `event_data`: `Dict[str, Any]`
- `correlation_id`: `Optional[str]`
- `metadata`: `Dict[str, Any]`
- `channel`: `Optional[str]`
- `headers`: `Dict[str, str]`

### `EventPublishResponse`

Response model for event publishing.

**Fields:**

- `event_id`: `str`
- `status`: `str`
- `message`: `str`
- `channel`: `Optional[str]`

### `MetricData`

Model for metric data ingestion.

**Fields:**

- `name`: `str`
- `value`: `float`
- `timestamp`: `Optional[datetime]`
- `service_name`: `str`
- `aggregation`: `str`
- `labels`: `Dict[str, str]`

### `MetricDataBatch`

Model for batch metric data ingestion.

**Fields:**

- `metrics`: `List[MetricData]`

### `MetricQuery`

Model for metric data queries.

**Fields:**

- `name`: `Optional[str]`
- `service_name`: `Optional[str]`
- `aggregation`: `Optional[str]`
- `labels`: `Dict[str, str]`
- `start_time`: `Optional[datetime]`
- `end_time`: `Optional[datetime]`
- `limit`: `int`
- `offset`: `int`

### `MetricResponse`

Response model for metric operations.

**Fields:**

- `name`: `str`
- `status`: `str`
- `message`: `str`

### `MetricStatistics`

Metric statistics model.

**Fields:**

- `total_metrics`: `int`
- `gauge_count`: `int`
- `counter_count`: `int`
- `histogram_count`: `int`
- `summary_count`: `int`
- `metric_name_count`: `int`
- `service_count`: `int`
- `metric_names`: `List[str]`
- `services`: `List[str]`
- `start_time`: `datetime`
- `end_time`: `datetime`

### `TraceData`

Model for trace data ingestion.

**Fields:**

- `service`: `str`
- `trace_id`: `str`
- `span_id`: `str`
- `parent_span_id`: `Optional[str]`
- `name`: `str`
- `kind`: `str`
- `timestamp`: `Optional[datetime]`
- `duration_ms`: `Optional[float]`
- `attributes`: `Dict[str, Any]`
- `events`: `List[Dict[str, Any]]`
- `status_code`: `str`
- `status_message`: `Optional[str]`

### `TraceDataBatch`

Model for batch trace data ingestion.

**Fields:**

- `traces`: `List[TraceData]`

### `TraceQuery`

Model for trace data queries.

**Fields:**

- `service`: `Optional[str]`
- `trace_id`: `Optional[str]`
- `span_id`: `Optional[str]`
- `parent_span_id`: `Optional[str]`
- `name`: `Optional[str]`
- `kind`: `Optional[str]`
- `status_code`: `Optional[str]`
- `start_time`: `Optional[datetime]`
- `end_time`: `Optional[datetime]`
- `min_duration_ms`: `Optional[float]`
- `max_duration_ms`: `Optional[float]`
- `limit`: `int`
- `offset`: `int`

### `TraceResponse`

Response model for trace operations.

**Fields:**

- `trace_id`: `str`
- `status`: `str`
- `message`: `str`

### `TraceStatistics`

Trace statistics model.

**Fields:**

- `total_traces`: `int`
- `error_count`: `int`
- `error_rate`: `float`
- `avg_duration_ms`: `float`
- `service_count`: `int`
- `services`: `List[str]`
- `start_time`: `datetime`
- `end_time`: `datetime`

### `QueryData`

Model for advanced query data.

**Fields:**

- `query_id`: `str`
- `query_type`: `str`
- `parameters`: `Dict[str, Any]`
- `timestamp`: `Optional[datetime]`

### `QueryDataBatch`

Model for batch query data.

**Fields:**

- `queries`: `List[QueryData]`

### `QueryQuery`

Model for advanced query parameters.

**Fields:**

- `data_types`: `List[str]`
- `service`: `Optional[str]`
- `start_time`: `Optional[datetime]`
- `end_time`: `Optional[datetime]`
- `correlation_id`: `Optional[str]`
- `trace_id`: `Optional[str]`
- `span_id`: `Optional[str]`
- `parent_span_id`: `Optional[str]`
- `metric_name`: `Optional[str]`
- `event_type`: `Optional[str]`
- `limit`: `int`
- `offset`: `int`
- `order_by`: `Optional[str]`
- `order_direction`: `Optional[str]`

### `QueryResponse`

Response model for query operations.

**Fields:**

- `query_id`: `str`
- `status`: `str`
- `message`: `str`
- `results`: `Dict[str, List[Dict[str, Any]]]`
- `execution_time_ms`: `float`

### `QueryStatistics`

Query statistics model.

**Fields:**

- `total_queries`: `int`
- `avg_execution_time_ms`: `float`
- `data_type_counts`: `Dict[str, int]`
- `service_counts`: `Dict[str, int]`
- `start_time`: `datetime`
- `end_time`: `datetime`

### `MetricsIngestRequest`

Model for metrics ingestion requests.

**Fields:**

- `service`: `str`
- `timestamp`: `datetime`
- `metrics`: `str`
- `format`: `str`

### `MetricsIngestResponse`

Model for metrics ingestion responses.

**Fields:**

- `success`: `bool`
- `message`: `str`
- `metrics_count`: `Optional[int]`

### `IncomingEvent`

Generic model for an event received from the messaging service callback.

**Fields:**

- `event_type`: `str`
- `event_data`: `Dict[str, Any]`
- `source_service`: `str`
- `timestamp`: `datetime`
- `correlation_id`: `Optional[str]`
- `message_id`: `Optional[str]`

