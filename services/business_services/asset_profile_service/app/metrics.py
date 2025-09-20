"""
Metrics module for Asset Profile Service.

This module provides Prometheus metrics instrumentation for Asset Profile Service, including:
- HTTP request metrics (counters, histograms)
- Business domain event metrics
- System metrics (CPU, memory)
- Service health metrics
- Database operation metrics
- SLO/SLI metrics for tracking service level objectives

It supports exporting metrics to the Observability Service for centralized
monitoring and alerting.
"""

import time
import logging
import functools
import asyncio
import psutil
from typing import Callable, Any, Optional, Dict, List
from prometheus_client import Counter, Histogram, Gauge, Summary, Info
from contextlib import contextmanager

# Configure logging
logger = logging.getLogger(__name__)


class ServiceMetrics:
    """Asset Profile Service metrics collection using Prometheus client."""
    
    def __init__(self):
        """Initialize metrics collectors."""
        self.service_name = "asset_profile_service"
        
        # Service information
        self.service_info = Info(
            "service_info", 
            "Service information"
        )
        
        # Service health metrics
        self.service_health = Gauge(
            "service_health",
            "Service health status (1 = healthy, 0 = unhealthy)"
        )
        self.service_ready = Gauge(
            "service_ready",
            "Service readiness status (1 = ready, 0 = not ready)"
        )
        
        # HTTP request metrics
        self.http_requests_total = Counter(
            "http_requests_total",
            "Total number of HTTP requests",
            ["method", "path"]
        )
        self.http_request_duration_seconds = Histogram(
            "http_request_duration_seconds",
            "HTTP request duration in seconds",
            ["method", "path", "status_code"],
            buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
        )
        self.http_exceptions_total = Counter(
            "http_exceptions_total",
            "Total number of HTTP exceptions",
            ["method", "path", "exception_type"]
        )
        self.http_requests_in_progress = Gauge(
            "http_requests_in_progress",
            "Number of HTTP requests in progress",
            ["method", "path"]
        )

        self.request_success = Counter(
            "request_success_total",
            "Total number of successful requests.",
            ["method", "path"]
        )
        self.request_client_errors = Counter(
            "request_client_errors_total",
            "Total number of client error requests.",
            ["method", "path"]
        )
        self.request_server_errors = Counter(
            "request_server_errors_total",
            "Total number of server error requests.",
            ["method", "path"]
        )
        self.request_exceptions = Counter(
            "request_exceptions_total",
            "Total number of exceptions raised handling requests.",
            ["method", "path"]
        )
        
        # Business domain metrics
        self.domain_events_total = Counter(
            "domain_events_total",
            "Total number of domain events",
            ["event_type", "status"]
        )
        self.domain_event_processing_seconds = Histogram(
            "domain_event_processing_seconds",
            "Domain event processing duration in seconds",
            ["event_type"],
            buckets=[0.01, 0.05, 0.1, 0.5, 1, 5, 10, 30, 60]
        )
        
        # System metrics
        self.system_cpu_usage = Gauge(
            "system_cpu_usage",
            "System CPU usage percentage"
        )
        self.system_memory_usage = Gauge(
            "system_memory_usage",
            "System memory usage percentage"
        )
        self.system_disk_usage = Gauge(
            "system_disk_usage",
            "System disk usage percentage"
        )
        
        # Database metrics
        self.db_operations_total = Counter(
            "db_operations_total",
            "Total number of database operations",
            ["operation", "status"]
        )
        self.db_operation_duration_seconds = Histogram(
            "db_operation_duration_seconds",
            "Database operation duration in seconds",
            ["operation"],
            buckets=[0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10]
        )
        self.db_connections = Gauge(
            "db_connections",
            "Number of database connections",
            ["state"]
        )
        self.db_connection_errors = Counter(
            "db_connection_errors",
            "Total number of database connection errors",
            ["error_type"]
        )
        
        # Message processing metrics
        self.messages_processed_total = Counter(
            "messages_processed_total",
            "Total number of messages processed",
            ["message_type", "status"]
        )
        self.message_processing_duration_seconds = Histogram(
            "message_processing_duration_seconds",
            "Message processing duration in seconds",
            ["message_type"],
            buckets=[0.01, 0.05, 0.1, 0.5, 1, 5, 10, 30, 60]
        )
        self.message_queue_size = Gauge(
            "message_queue_size",
            "Size of message queue",
            ["queue_name"]
        )
        
        # SLO/SLI metrics
        self.slo_request_success_total = Counter(
            "slo_request_success_total",
            "Total number of successful requests for SLO calculation",
            ["path"]
        )
        self.slo_request_total = Counter(
            "slo_request_total",
            "Total number of requests for SLO calculation",
            ["path"]
        )
        self.slo_request_latency_met_total = Counter(
            "slo_request_latency_met_total",
            "Total number of requests meeting latency SLO",
            ["path"]
        )
        self.slo_success_ratio = Gauge(
            "slo_success_ratio",
            "Success ratio for SLO calculation (0-1)",
            ["path"]
        )
        self.slo_latency_compliance = Gauge(
            "slo_latency_compliance",
            "Latency compliance ratio for SLO calculation (0-1)",
            ["path"]
        )
        
    def initialize(self, service_name: str = None):
        """Initialize service metrics with service information.
        
        Args:
            service_name: Optional name override for the service
        """
        if service_name:
            self.service_name = service_name
            
        # Set service info
        self.service_info.info({
            "name": self.service_name,
            "version": "1.0.0",
            "start_time": str(time.time())
        })
        
        # Initialize service health metrics
        self.service_health.set(1)  # Start as healthy
        self.service_ready.set(0)   # Start as not ready
        
        logger.info(f"Metrics initialized for service: {self.service_name}")


# Create a singleton instance
metrics = ServiceMetrics()


def track_endpoint_execution(func):
    """Decorator to track endpoint execution metrics."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        endpoint_name = func.__name__
        method = "unknown"
        path = endpoint_name
        
        # Try to determine HTTP method and path from FastAPI request
        for arg in args:
            if hasattr(arg, "method") and hasattr(arg, "url"):
                method = arg.method
                path = arg.url.path
                break
        
        # Track in-progress requests
        metrics.http_requests_in_progress.labels(method=method, path=path).inc()
        
        start_time = time.time()
        try:
            result = await func(*args, **kwargs)
            
            # Track successful execution time
            duration = time.time() - start_time
            status_code = 200
            
            # Try to determine actual status code from response
            if hasattr(result, "status_code"):
                status_code = result.status_code
                
            metrics.http_request_duration_seconds.labels(
                method=method, 
                path=endpoint_name,
                status_code=status_code
            ).observe(duration)
            
            return result
            
        except Exception as e:
            # Track exceptions
            metrics.http_exceptions_total.labels(
                method=method,
                path=endpoint_name,
                exception_type=type(e).__name__
            ).inc()
            raise
        finally:
            # Decrement in-progress counter
            metrics.http_requests_in_progress.labels(method=method, path=path).dec()
    
    return wrapper


def track_message_processing(message_type: str):
    """Decorator to track message processing metrics."""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                
                # Track successful message processing
                metrics.messages_processed_total.labels(
                    message_type=message_type,
                    status="success"
                ).inc()
                
                duration = time.time() - start_time
                metrics.message_processing_duration_seconds.labels(
                    message_type=message_type
                ).observe(duration)
                
                return result
                
            except Exception as e:
                # Track failed message processing
                metrics.messages_processed_total.labels(
                    message_type=message_type,
                    status="error"
                ).inc()
                raise
        
        return wrapper
    
    return decorator


def track_db_operation(operation: str):
    """Decorator to track database operation metrics."""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                
                # Track successful database operation
                metrics.db_operations_total.labels(
                    operation=operation,
                    status="success"
                ).inc()
                
                duration = time.time() - start_time
                metrics.db_operation_duration_seconds.labels(
                    operation=operation
                ).observe(duration)
                
                return result
                
            except Exception as e:
                # Track failed database operation
                metrics.db_operations_total.labels(
                    operation=operation,
                    status="error"
                ).inc()
                
                # Track specific database errors
                error_type = type(e).__name__
                if "connection" in str(e).lower():
                    metrics.db_connection_errors.labels(
                        error_type=error_type
                    ).inc()
                
                raise
        
        return wrapper
    
    return decorator


def track_domain_event(event_type: str):
    """Decorator to track domain event metrics."""
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                
                # Track successful domain event
                metrics.domain_events_total.labels(
                    event_type=event_type,
                    status="success"
                ).inc()
                
                duration = time.time() - start_time
                metrics.domain_event_processing_seconds.labels(
                    event_type=event_type
                ).observe(duration)
                
                return result
                
            except Exception as e:
                # Track failed domain event
                metrics.domain_events_total.labels(
                    event_type=event_type,
                    status="error"
                ).inc()
                raise
        
        return wrapper
    
    return decorator


@contextmanager
def track_operation_time(metric: Histogram, **labels):
    """Context manager to track operation time using a histogram metric."""
    start_time = time.time()
    try:
        yield
    finally:
        duration = time.time() - start_time
        metric.labels(**labels).observe(duration)


def update_system_metrics():
    """Update system metrics (CPU, memory, disk)."""
    try:
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=None)
        metrics.system_cpu_usage.set(cpu_percent)
        
        # Memory usage
        memory = psutil.virtual_memory()
        metrics.system_memory_usage.set(memory.percent)
        
        # Disk usage
        disk = psutil.disk_usage('/')
        metrics.system_disk_usage.set(disk.percent)
        
    except Exception as e:
        logger.error(f"Error updating system metrics: {str(e)}")


def update_db_connection_metrics(connected: bool):
    """Update database connection metrics.
    
    Args:
        connected: Whether database connection is successful
    """
    if connected:
        metrics.db_connections.labels(state="connected").inc()
        metrics.db_connections.labels(state="disconnected").set(0)
    else:
        metrics.db_connections.labels(state="disconnected").inc()
        metrics.db_connections.labels(state="connected").set(0)


def update_message_queue_metrics(queue_name: str, size: int):
    """Update message queue size metrics.
    
    Args:
        queue_name: Name of the queue
        size: Current size of the queue
    """
    metrics.message_queue_size.labels(queue_name=queue_name).set(size)


def update_slo_metrics(path: str):
    """Update SLO metrics for a specific path.
    
    Args:
        path: API path to update SLO metrics for
    """
    try:
        # Calculate success ratio
        success_total = metrics.slo_request_success_total.labels(path=path)._value.get()
        request_total = metrics.slo_request_total.labels(path=path)._value.get()
        
        if request_total > 0:
            success_ratio = success_total / request_total
            metrics.slo_success_ratio.labels(path=path).set(success_ratio)
        
        # Calculate latency compliance
        latency_met_total = metrics.slo_request_latency_met_total.labels(path=path)._value.get()
        
        if request_total > 0:
            latency_compliance = latency_met_total / request_total
            metrics.slo_latency_compliance.labels(path=path).set(latency_compliance)
            
    except Exception as e:
        logger.error(f"Error updating SLO metrics: {str(e)}")


def set_service_health(healthy: bool):
    """
    Set service health status.
    
    Args:
        healthy: Whether the service is healthy
    """
    metrics.service_health.set(1 if healthy else 0)


def set_service_ready(ready: bool):
    """
    Set service ready status.
    
    Args:
        ready: Whether the service is ready
    """
    metrics.service_ready.set(1 if ready else 0)


async def export_metrics_to_observability(observability_url: str, push_gateway: str = None, job_name: str = "asset_profile_service"):
    """Export collected metrics to the Observability Service.
    
    This function sends the collected Prometheus metrics to the Observability Service
    for centralized storage and analysis. It supports two export methods:
    1. Direct HTTP POST to the Observability Service's metrics ingestion endpoint
    2. Push to a Prometheus Pushgateway (if configured)
    
    Args:
        observability_url: URL of the Observability Service
        push_gateway: Optional URL of Prometheus Pushgateway
        job_name: Job name for metrics export
    """
    import aiohttp
    from io import StringIO
    from prometheus_client import generate_latest, REGISTRY
    import json
    from datetime import datetime
    
    # Generate metrics in Prometheus text format
    output = StringIO()
    output.write(generate_latest(REGISTRY).decode('utf-8'))
    prometheus_data = output.getvalue()
    
    # Prepare metrics data for Observability Service
    metrics_data = {
        "service": metrics.service_name,
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": prometheus_data,
        "format": "prometheus"
    }
    
    # Export metrics to Observability Service
    try:
        async with aiohttp.ClientSession() as session:
            # Send to Observability Service metrics ingestion endpoint
            async with session.post(
                f"{observability_url}/metrics/ingest",
                json=metrics_data,
                headers={"Content-Type": "application/json"},
                timeout=10
            ) as response:
                if response.status != 200 and response.status != 202:
                    response_text = await response.text()
                    logger.warning(f"Failed to export metrics to Observability Service: {response.status} - {response_text}")
                else:
                    logger.debug(f"Successfully exported metrics to Observability Service")
                    
            # If push gateway is configured, also push metrics there
            if push_gateway:
                import requests
                from prometheus_client import push_to_gateway
                try:
                    # This is synchronous but we're running in an async context
                    # Use a thread pool executor for this operation
                    import concurrent.futures
                    with concurrent.futures.ThreadPoolExecutor() as executor:
                        await asyncio.get_event_loop().run_in_executor(
                            executor,
                            lambda: push_to_gateway(push_gateway, job=job_name, registry=REGISTRY)
                        )
                    logger.debug(f"Successfully pushed metrics to Pushgateway")
                except Exception as e:
                    logger.warning(f"Failed to push metrics to Pushgateway: {str(e)}")
    
    except Exception as e:
        logger.error(f"Error exporting metrics: {str(e)}")
        raise

# TODO: Implement additional metrics export methods as needed
