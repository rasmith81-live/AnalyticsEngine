"""
Metrics module for the Database Service.

This module provides Prometheus metrics collection and export functionality for the Database Service,
including HTTP request metrics, database operation metrics, system metrics, and SLO/SLI tracking.
"""

import time
import asyncio
import logging
import platform
import functools
from typing import Dict, List, Any, Callable, Optional, Union, TypeVar, cast
from datetime import datetime

import aiohttp
import psutil
from prometheus_client import (
    Counter, Gauge, Histogram, Summary, 
    REGISTRY, generate_latest, CONTENT_TYPE_LATEST,
    push_to_gateway
)

logger = logging.getLogger(__name__)

# Type definitions for decorators
F = TypeVar('F', bound=Callable[..., Any])
AsyncF = TypeVar('AsyncF', bound=Callable[..., Any])

class DatabaseServiceMetrics:
    """Metrics collection for the Database Service."""
    
    def __init__(self):
        """Initialize metrics."""
        # Service info and health metrics
        self.service_info = Gauge(
            'database_service_info', 
            'Database Service information',
            ['version', 'python_version', 'platform']
        )
        self.service_health = Gauge('database_service_health', 'Database Service health status (1=healthy, 0=unhealthy)')
        self.service_ready = Gauge('database_service_ready', 'Database Service readiness status (1=ready, 0=not ready)')
        self.service_uptime = Gauge('database_service_uptime_seconds', 'Database Service uptime in seconds')
        
        # Database connection metrics
        self.db_connection_pool_size = Gauge('database_connection_pool_size', 'Database connection pool size')
        self.db_connection_pool_used = Gauge('database_connection_pool_used', 'Database connections in use')
        self.db_connection_errors = Counter('database_connection_errors_total', 'Database connection errors')
        
        # Database operation metrics
        self.db_operations_total = Counter(
            'database_operations_total', 
            'Database operations count',
            ['operation', 'entity_type']
        )
        self.db_operation_errors_total = Counter(
            'database_operation_errors_total', 
            'Database operation errors count',
            ['operation', 'entity_type', 'error_type']
        )
        self.db_operation_duration_seconds = Histogram(
            'database_operation_duration_seconds', 
            'Database operation duration in seconds',
            ['operation', 'entity_type'],
            buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
        )
        
        # Query metrics
        self.query_count = Counter(
            'database_query_total', 
            'Database query count',
            ['query_type', 'entity_type']
        )
        self.query_duration_seconds = Histogram(
            'database_query_duration_seconds', 
            'Database query duration in seconds',
            ['query_type', 'entity_type'],
            buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
        )
        self.query_errors = Counter(
            'database_query_errors_total', 
            'Database query errors',
            ['query_type', 'entity_type', 'error_type']
        )
        
        # Cache metrics
        self.cache_hits = Counter('database_cache_hits_total', 'Cache hits')
        self.cache_misses = Counter('database_cache_misses_total', 'Cache misses')
        self.cache_size = Gauge('database_cache_size', 'Cache size in items')
        
        # HTTP request metrics
        self.http_requests_total = Counter(
            'http_requests_total', 
            'Total HTTP requests',
            ['method', 'path']
        )
        self.http_request_duration_seconds = Histogram(
            'http_request_duration_seconds', 
            'HTTP request duration in seconds',
            ['method', 'path', 'status_code'],
            buckets=[0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
        )
        self.http_exceptions_total = Counter(
            'http_exceptions_total', 
            'Total HTTP exceptions',
            ['method', 'path', 'exception_type']
        )
        
        # System metrics
        self.system_cpu_usage = Gauge('system_cpu_usage', 'System CPU usage percentage')
        self.system_memory_usage = Gauge('system_memory_usage', 'System memory usage percentage')
        self.system_disk_usage = Gauge('system_disk_usage', 'System disk usage percentage')
        
        # TimescaleDB specific metrics
        self.timescale_chunks_total = Gauge(
            'timescale_chunks_total', 
            'Total number of TimescaleDB chunks',
            ['table_name']
        )
        self.timescale_chunk_size_bytes = Gauge(
            'timescale_chunk_size_bytes', 
            'Size of TimescaleDB chunks in bytes',
            ['table_name']
        )
        self.timescale_compression_ratio = Gauge(
            'timescale_compression_ratio', 
            'TimescaleDB compression ratio',
            ['table_name']
        )
        
        # Migration metrics
        self.migration_operations_total = Counter(
            'migration_operations_total', 
            'Migration operations count',
            ['operation_type']
        )
        self.migration_errors_total = Counter(
            'migration_errors_total', 
            'Migration errors count',
            ['operation_type', 'error_type']
        )
        self.migration_duration_seconds = Histogram(
            'migration_duration_seconds', 
            'Migration duration in seconds',
            ['operation_type'],
            buckets=[0.1, 0.5, 1, 5, 10, 30, 60, 120, 300, 600]
        )
        
        # SLO/SLI metrics
        self.slo_request_total = Counter(
            'slo_request_total', 
            'Total requests for SLO calculation',
            ['path']
        )
        self.slo_request_success_total = Counter(
            'slo_request_success_total', 
            'Successful requests for SLO calculation',
            ['path']
        )
        self.slo_request_latency_met_total = Counter(
            'slo_request_latency_met_total', 
            'Requests meeting latency SLO',
            ['path']
        )
        
        # Service start time for uptime calculation
        self.start_time = time.time()
    
    def initialize(self, service_name: str, version: str = "1.0.0"):
        """Initialize service info metrics."""
        self.service_name = service_name
        self.service_info.labels(
            version=version,
            python_version=platform.python_version(),
            platform=platform.platform()
        ).set(1)
        logger.info(f"Initialized metrics for {service_name}")


# Create a singleton instance
metrics = DatabaseServiceMetrics()


def track_endpoint_execution(func: F) -> F:
    """Decorator to track endpoint execution metrics."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        endpoint_name = func.__name__
        
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            logger.debug(f"Endpoint {endpoint_name} executed in {duration:.4f} seconds")
            return result
        except Exception as e:
            metrics.http_exceptions_total.labels(
                method="UNKNOWN", 
                path=endpoint_name,
                exception_type=type(e).__name__
            ).inc()
            raise
    
    return cast(F, wrapper)


def track_db_operation(operation: str, entity_type: str) -> Callable[[AsyncF], AsyncF]:
    """Decorator to track database operation metrics."""
    def decorator(func: AsyncF) -> AsyncF:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                # Track operation count
                metrics.db_operations_total.labels(
                    operation=operation,
                    entity_type=entity_type
                ).inc()
                
                # Execute operation
                result = await func(*args, **kwargs)
                
                # Track duration
                duration = time.time() - start_time
                metrics.db_operation_duration_seconds.labels(
                    operation=operation,
                    entity_type=entity_type
                ).observe(duration)
                
                return result
            except Exception as e:
                # Track error
                metrics.db_operation_errors_total.labels(
                    operation=operation,
                    entity_type=entity_type,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return cast(AsyncF, wrapper)
    
    return decorator


def track_query(query_type: str, entity_type: str) -> Callable[[AsyncF], AsyncF]:
    """Decorator to track database query metrics."""
    def decorator(func: AsyncF) -> AsyncF:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                # Track query count
                metrics.query_count.labels(
                    query_type=query_type,
                    entity_type=entity_type
                ).inc()
                
                # Execute query
                result = await func(*args, **kwargs)
                
                # Track duration
                duration = time.time() - start_time
                metrics.query_duration_seconds.labels(
                    query_type=query_type,
                    entity_type=entity_type
                ).observe(duration)
                
                return result
            except Exception as e:
                # Track error
                metrics.query_errors.labels(
                    query_type=query_type,
                    entity_type=entity_type,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return cast(AsyncF, wrapper)
    
    return decorator


def track_cache_operation(func: F) -> F:
    """Decorator to track cache operation metrics."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # The first arg is self (the cache instance)
        cache_instance = args[0]
        
        # Update cache size metric
        if hasattr(cache_instance, 'size'):
            metrics.cache_size.set(cache_instance.size)
        
        # Track cache hits/misses based on function name
        if func.__name__ == 'get' and len(args) > 1:
            key = args[1]  # The key being looked up
            result = func(*args, **kwargs)
            
            if result is not None:
                metrics.cache_hits.inc()
            else:
                metrics.cache_misses.inc()
            
            return result
        
        # For other cache operations
        return func(*args, **kwargs)
    
    return cast(F, wrapper)


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
        
        # Update service uptime
        uptime = time.time() - metrics.start_time
        metrics.service_uptime.set(uptime)
        
        logger.debug("System metrics updated")
    except Exception as e:
        logger.error(f"Failed to update system metrics: {str(e)}")


def update_db_connection_metrics(pool_size: int, used_connections: int):
    """Update database connection metrics."""
    metrics.db_connection_pool_size.set(pool_size)
    metrics.db_connection_pool_used.set(used_connections)


def update_timescale_metrics(table_metrics: Dict[str, Dict[str, float]]):
    """Update TimescaleDB specific metrics."""
    for table_name, table_data in table_metrics.items():
        if 'chunks' in table_data:
            metrics.timescale_chunks_total.labels(table_name=table_name).set(table_data['chunks'])
        
        if 'size_bytes' in table_data:
            metrics.timescale_chunk_size_bytes.labels(table_name=table_name).set(table_data['size_bytes'])
        
        if 'compression_ratio' in table_data:
            metrics.timescale_compression_ratio.labels(table_name=table_name).set(table_data['compression_ratio'])


async def export_metrics_to_observability(
    push_gateway: Optional[str] = None,
    job_name: str = "database_service"
):
    """
    Export metrics to the Observability Service and optionally to Prometheus Pushgateway.

    Args:
        exporter: The OTLPMetricExporter instance to use for exporting.
        push_gateway: URL of the Prometheus Pushgateway (optional).
        job_name: Job name for Prometheus Pushgateway.
    """
    try:
        # The OTLP exporter will handle the export automatically.
        # This function can be used to trigger a force flush if needed, but typically
        # the periodic exporting reader handles this.
        logger.debug("Metrics are being exported periodically by the OTLP exporter.")

        # Export to Prometheus Pushgateway if configured
        if push_gateway:
            try:
                push_to_gateway(
                    gateway=push_gateway,
                    job=job_name,
                    registry=REGISTRY
                )
                logger.debug(f"Metrics pushed to Pushgateway at {push_gateway}")
            except Exception as e:
                logger.error(f"Failed to push metrics to Pushgateway: {str(e)}")

    except Exception as e:
        logger.error(f"Error during metrics export process: {str(e)}")
