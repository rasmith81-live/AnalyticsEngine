"""
Metrics module for Observability Service

This module provides Prometheus metrics instrumentation for the Observability Service.
It includes utilities for tracking request counts, latencies, and custom metrics.
"""

import time
import logging
from typing import Dict, Any, Optional, Callable, List, Union
from functools import wraps
import asyncio

# Prometheus imports
try:
    from prometheus_client import Counter, Histogram, Gauge, Summary, Info, REGISTRY
    from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
    from prometheus_client.exposition import choose_encoder
    PROMETHEUS_AVAILABLE = True
except ImportError:
    PROMETHEUS_AVAILABLE = False

from .config import get_settings

logger = logging.getLogger(__name__)

# Define metrics
if PROMETHEUS_AVAILABLE:
    # HTTP request metrics
    HTTP_REQUEST_COUNTER = Counter(
        'observability_http_requests_total',
        'Total number of HTTP requests',
        ['method', 'endpoint', 'status']
    )
    
    HTTP_REQUEST_LATENCY = Histogram(
        'observability_http_request_duration_seconds',
        'HTTP request latency in seconds',
        ['method', 'endpoint'],
        buckets=(0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0, 25.0, 50.0, 75.0, 100.0, float('inf'))
    )
    
    # Database metrics
    DB_QUERY_COUNTER = Counter(
        'observability_db_queries_total',
        'Total number of database queries',
        ['operation', 'status']
    )
    
    DB_QUERY_LATENCY = Histogram(
        'observability_db_query_duration_seconds',
        'Database query latency in seconds',
        ['operation'],
        buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0, float('inf'))
    )
    
    # Messaging metrics
    MESSAGING_COUNTER = Counter(
        'observability_messaging_operations_total',
        'Total number of messaging operations',
        ['operation', 'status']
    )
    
    MESSAGING_LATENCY = Histogram(
        'observability_messaging_operation_duration_seconds',
        'Messaging operation latency in seconds',
        ['operation'],
        buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, float('inf'))
    )
    
    # Telemetry metrics
    TELEMETRY_INGESTION_COUNTER = Counter(
        'observability_telemetry_ingestion_total',
        'Total number of telemetry items ingested',
        ['type']
    )
    
    TELEMETRY_PROCESSING_LATENCY = Histogram(
        'observability_telemetry_processing_duration_seconds',
        'Telemetry processing latency in seconds',
        ['type'],
        buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, float('inf'))
    )
    
    # Service health metrics
    SERVICE_INFO = Info(
        'observability_service_info',
        'Information about the Observability Service'
    )
    
    SERVICE_UPTIME = Gauge(
        'observability_service_uptime_seconds',
        'Uptime of the Observability Service in seconds'
    )
    
    SERVICE_HEALTH = Gauge(
        'observability_service_health',
        'Health status of the Observability Service (1=healthy, 0=unhealthy)',
        ['component']
    )
    
    # Resource usage metrics
    RESOURCE_USAGE = Gauge(
        'observability_resource_usage',
        'Resource usage of the Observability Service',
        ['resource_type']
    )
    
    # API rate limiting metrics
    RATE_LIMIT_HITS = Counter(
        'observability_rate_limit_hits_total',
        'Total number of rate limit hits',
        ['endpoint']
    )
    
    # Custom metrics for observability data
    TRACE_COUNT = Counter(
        'observability_traces_total',
        'Total number of traces processed',
        ['service', 'status']
    )
    
    METRIC_COUNT = Counter(
        'observability_metrics_total',
        'Total number of metrics processed',
        ['service', 'type']
    )
    
    HEALTH_CHECK_COUNT = Counter(
        'observability_health_checks_total',
        'Total number of health checks processed',
        ['service', 'status']
    )
    
    DEPENDENCY_CHECK_COUNT = Counter(
        'observability_dependency_checks_total',
        'Total number of dependency checks processed',
        ['service', 'dependency', 'status']
    )
    
    # Event metrics
    EVENT_COUNT = Counter(
        'observability_events_total',
        'Total number of events processed',
        ['service', 'type', 'severity']
    )
    
    # Query metrics
    QUERY_EXECUTION_LATENCY = Histogram(
        'observability_query_execution_duration_seconds',
        'Query execution latency in seconds',
        ['type'],
        buckets=(0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0, float('inf'))
    )


def initialize_metrics(service_name: str, version: str) -> bool:
    """
    Initialize metrics for the service.
    
    Args:
        service_name: Name of the service
        version: Version of the service
        
    Returns:
        bool: True if initialization was successful, False otherwise
    """
    if not PROMETHEUS_AVAILABLE:
        logger.warning("Prometheus client not available, skipping metrics initialization")
        return False
    
    try:
        # Set service info
        SERVICE_INFO.info({
            'name': service_name,
            'version': version
        })
        
        # Initialize uptime metric
        SERVICE_UPTIME.set_function(lambda: time.time() - _service_start_time)
        
        # Set default health status
        SERVICE_HEALTH.labels(component='service').set(1)
        SERVICE_HEALTH.labels(component='database').set(1)
        SERVICE_HEALTH.labels(component='messaging').set(1)
        
        logger.info(f"Metrics initialized for service {service_name} v{version}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to initialize metrics: {str(e)}")
        return False


# Service start time for uptime calculation
_service_start_time = time.time()


def track_request_metrics(
    method: str,
    endpoint: str,
    status_code: int,
    duration: float
) -> None:
    """
    Track HTTP request metrics.
    
    Args:
        method: HTTP method
        endpoint: API endpoint
        status_code: HTTP status code
        duration: Request duration in seconds
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Increment request counter
        HTTP_REQUEST_COUNTER.labels(
            method=method,
            endpoint=endpoint,
            status=str(status_code)
        ).inc()
        
        # Record request latency
        HTTP_REQUEST_LATENCY.labels(
            method=method,
            endpoint=endpoint
        ).observe(duration)
        
    except Exception as e:
        logger.debug(f"Failed to track request metrics: {str(e)}")


def track_db_metrics(
    operation: str,
    success: bool,
    duration: float
) -> None:
    """
    Track database operation metrics.
    
    Args:
        operation: Database operation type
        success: Whether the operation was successful
        duration: Operation duration in seconds
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Increment query counter
        DB_QUERY_COUNTER.labels(
            operation=operation,
            status="success" if success else "error"
        ).inc()
        
        # Record query latency
        DB_QUERY_LATENCY.labels(
            operation=operation
        ).observe(duration)
        
    except Exception as e:
        logger.debug(f"Failed to track database metrics: {str(e)}")


def track_messaging_metrics(
    operation: str,
    success: bool,
    duration: float
) -> None:
    """
    Track messaging operation metrics.
    
    Args:
        operation: Messaging operation type
        success: Whether the operation was successful
        duration: Operation duration in seconds
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Increment messaging counter
        MESSAGING_COUNTER.labels(
            operation=operation,
            status="success" if success else "error"
        ).inc()
        
        # Record messaging latency
        MESSAGING_LATENCY.labels(
            operation=operation
        ).observe(duration)
        
    except Exception as e:
        logger.debug(f"Failed to track messaging metrics: {str(e)}")


def track_telemetry_ingestion(
    telemetry_type: str,
    count: int = 1
) -> None:
    """
    Track telemetry ingestion metrics.
    
    Args:
        telemetry_type: Type of telemetry (trace, metric, health, dependency)
        count: Number of items ingested
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Increment ingestion counter
        TELEMETRY_INGESTION_COUNTER.labels(
            type=telemetry_type
        ).inc(count)
        
    except Exception as e:
        logger.debug(f"Failed to track telemetry ingestion metrics: {str(e)}")


def track_telemetry_processing(
    telemetry_type: str,
    duration: float
) -> None:
    """
    Track telemetry processing metrics.
    
    Args:
        telemetry_type: Type of telemetry (trace, metric, health, dependency)
        duration: Processing duration in seconds
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Record processing latency
        TELEMETRY_PROCESSING_LATENCY.labels(
            type=telemetry_type
        ).observe(duration)
        
    except Exception as e:
        logger.debug(f"Failed to track telemetry processing metrics: {str(e)}")


def update_health_status(component: str, healthy: bool) -> None:
    """
    Update service health status.
    
    Args:
        component: Service component (service, database, messaging)
        healthy: Whether the component is healthy
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        SERVICE_HEALTH.labels(component=component).set(1 if healthy else 0)
    except Exception as e:
        logger.debug(f"Failed to update health status: {str(e)}")


def update_resource_usage(resource_type: str, value: float) -> None:
    """
    Update resource usage metrics.
    
    Args:
        resource_type: Type of resource (cpu, memory, disk, etc.)
        value: Resource usage value
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        RESOURCE_USAGE.labels(resource_type=resource_type).set(value)
    except Exception as e:
        logger.debug(f"Failed to update resource usage: {str(e)}")


def track_rate_limit_hit(endpoint: str) -> None:
    """
    Track rate limit hit.
    
    Args:
        endpoint: API endpoint that hit the rate limit
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        RATE_LIMIT_HITS.labels(endpoint=endpoint).inc()
    except Exception as e:
        logger.debug(f"Failed to track rate limit hit: {str(e)}")


def track_trace_processing(service: str, status: str) -> None:
    """
    Track trace processing.
    
    Args:
        service: Service that generated the trace
        status: Processing status (success, error)
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        TRACE_COUNT.labels(service=service, status=status).inc()
    except Exception as e:
        logger.debug(f"Failed to track trace processing: {str(e)}")


def track_metric_processing(service: str, metric_type: str) -> None:
    """
    Track metric processing.
    
    Args:
        service: Service that generated the metric
        metric_type: Type of metric
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        METRIC_COUNT.labels(service=service, type=metric_type).inc()
    except Exception as e:
        logger.debug(f"Failed to track metric processing: {str(e)}")


def track_health_check_processing(service: str, status: str) -> None:
    """
    Track health check processing.
    
    Args:
        service: Service that generated the health check
        status: Health check status (healthy, unhealthy)
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        HEALTH_CHECK_COUNT.labels(service=service, status=status).inc()
    except Exception as e:
        logger.debug(f"Failed to track health check processing: {str(e)}")


def track_dependency_check_processing(service: str, dependency: str, status: str) -> None:
    """
    Track dependency check processing.
    
    Args:
        service: Service that generated the dependency check
        dependency: Dependency being checked
        status: Dependency check status (healthy, unhealthy)
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        DEPENDENCY_CHECK_COUNT.labels(service=service, dependency=dependency, status=status).inc()
    except Exception as e:
        logger.debug(f"Failed to track dependency check processing: {str(e)}")


def track_event_processing(service: str, event_type: str, severity: str = "info") -> None:
    """
    Track event processing.
    
    Args:
        service: Service that generated the event
        event_type: Type of event
        severity: Severity level of the event (debug, info, warning, error, critical)
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Ensure EVENT_COUNT is defined
        if 'EVENT_COUNT' not in globals():
            global EVENT_COUNT
            if PROMETHEUS_AVAILABLE:
                EVENT_COUNT = Counter(
                    'observability_events_total',
                    'Total number of events processed',
                    ['service', 'type', 'severity']
                )
        
        EVENT_COUNT.labels(service=service, type=event_type, severity=severity).inc()
    except Exception as e:
        logger.debug(f"Failed to track event processing: {str(e)}")


def track_query_execution(query_type: str, duration: float, data_types_count: Optional[int] = None) -> None:
    """
    Track query execution metrics.
    
    Args:
        query_type: Type of query (advanced, correlated, topology, dependencies)
        duration: Query execution duration in seconds
        data_types_count: Optional count of data types in the query
    """
    if not PROMETHEUS_AVAILABLE:
        return
    
    try:
        # Ensure QUERY_EXECUTION_LATENCY is defined
        if 'QUERY_EXECUTION_LATENCY' not in globals():
            global QUERY_EXECUTION_LATENCY
            if PROMETHEUS_AVAILABLE:
                QUERY_EXECUTION_LATENCY = Histogram(
                    'observability_query_execution_duration_seconds',
                    'Query execution latency in seconds',
                    ['type', 'data_types'],
                    buckets=(0.01, 0.025, 0.05, 0.075, 0.1, 0.25, 0.5, 0.75, 1.0, 2.5, 5.0, 7.5, 10.0, float('inf'))
                )
        
        # Use data_types_count if provided, otherwise default to 1
        data_types = str(data_types_count) if data_types_count is not None else '1'
        QUERY_EXECUTION_LATENCY.labels(type=query_type, data_types=data_types).observe(duration)
    except Exception as e:
        logger.debug(f"Failed to track query execution: {str(e)}")


def timed_metric(
    metric_type: str,
    labels: Optional[Dict[str, str]] = None
) -> Callable:
    """
    Decorator to time a function and record metrics.
    
    Args:
        metric_type: Type of metric to record (db, messaging, telemetry)
        labels: Additional labels for the metric
        
    Returns:
        Callable: Decorated function
    """
    def decorator(func):
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            
            try:
                result = await func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                raise
            finally:
                duration = time.time() - start_time
                
                if metric_type == 'db':
                    operation = labels.get('operation', func.__name__) if labels else func.__name__
                    track_db_metrics(operation, success, duration)
                elif metric_type == 'messaging':
                    operation = labels.get('operation', func.__name__) if labels else func.__name__
                    track_messaging_metrics(operation, success, duration)
                elif metric_type == 'telemetry':
                    telemetry_type = labels.get('type', 'unknown') if labels else 'unknown'
                    track_telemetry_processing(telemetry_type, duration)
        
        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            start_time = time.time()
            success = True
            
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                success = False
                raise
            finally:
                duration = time.time() - start_time
                
                if metric_type == 'db':
                    operation = labels.get('operation', func.__name__) if labels else func.__name__
                    track_db_metrics(operation, success, duration)
                elif metric_type == 'messaging':
                    operation = labels.get('operation', func.__name__) if labels else func.__name__
                    track_messaging_metrics(operation, success, duration)
                elif metric_type == 'telemetry':
                    telemetry_type = labels.get('type', 'unknown') if labels else 'unknown'
                    track_telemetry_processing(telemetry_type, duration)
        
        if asyncio.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator


async def get_metrics() -> bytes:
    """
    Get Prometheus metrics in the appropriate format.
    
    Returns:
        bytes: Prometheus metrics in the appropriate format
    """
    if not PROMETHEUS_AVAILABLE:
        return b"# Prometheus metrics not available"
    
    try:
        # Generate metrics
        encoder, content_type = choose_encoder({})
        return encoder(REGISTRY)
    except Exception as e:
        logger.error(f"Failed to generate metrics: {str(e)}")
        return f"# Error generating metrics: {str(e)}".encode('utf-8')


def get_metrics_content_type() -> str:
    """
    Get the content type for Prometheus metrics.
    
    Returns:
        str: Content type for Prometheus metrics
    """
    if not PROMETHEUS_AVAILABLE:
        return "text/plain"
    
    return CONTENT_TYPE_LATEST
