"""
Prometheus metrics for the Archival Service.

This module provides metrics collection and export functionality for the Archival Service,
including service health, archival operations, storage metrics, and system metrics.
"""

import asyncio
import logging
import time
import platform
import os
import datetime
from typing import Dict, Any, Optional, List, Callable
import functools
import psutil

import aiohttp
from prometheus_client import (
    Counter, Gauge, Histogram, Summary, 
    REGISTRY, push_to_gateway, generate_latest,
    CONTENT_TYPE_LATEST
)

from .config import settings

# Configure logging
logger = logging.getLogger(__name__)

class ArchivalMetrics:
    """Metrics collection for the Archival Service."""
    
    def __init__(self):
        """Initialize metrics."""
        self.initialized = False
        
        # Service info and health metrics
        self.service_info = None
        self.service_health = None
        self.service_ready = None
        self.service_uptime = None
        
        # Archival operation metrics
        self.archival_operations_total = None
        self.archival_operations_success = None
        self.archival_operations_failed = None
        self.archival_operation_duration = None
        self.archival_data_size_bytes = None
        
        # Storage metrics
        self.storage_operations_total = None
        self.storage_operations_success = None
        self.storage_operations_failed = None
        self.storage_operation_duration = None
        self.storage_data_size_bytes = None
        
        # Redis metrics
        self.redis_operations_total = None
        self.redis_operations_success = None
        self.redis_operations_failed = None
        self.redis_operation_duration = None
        
        # HTTP metrics
        self.http_requests_total = None
        self.http_request_duration_seconds = None
        self.http_exceptions_total = None
        
        # System metrics
        self.system_cpu_usage = None
        self.system_memory_usage = None
        self.system_disk_usage = None
        
        # SLO/SLI metrics
        self.slo_request_total = None
        self.slo_request_success_total = None
        self.slo_request_latency_met_total = None
    
    def initialize(self, service_name: str):
        """Initialize all metrics with proper labels.
        
        Args:
            service_name: Name of the service for labels
        """
        if self.initialized:
            return
        
        # Service info and health metrics
        self.service_info = Gauge(
            'archival_service_info',
            'Archival Service information',
            ['version', 'python_version', 'hostname']
        )
        self.service_health = Gauge(
            'archival_service_health',
            'Health status of the Archival Service (1 = healthy, 0 = unhealthy)'
        )
        self.service_ready = Gauge(
            'archival_service_ready',
            'Readiness status of the Archival Service (1 = ready, 0 = not ready)'
        )
        self.service_uptime = Gauge(
            'archival_service_uptime_seconds',
            'Uptime of the Archival Service in seconds'
        )
        
        # Archival operation metrics
        self.archival_operations_total = Counter(
            'archival_operations_total',
            'Total number of archival operations',
            ['operation', 'table_name']
        )
        self.archival_operations_success = Counter(
            'archival_operations_success',
            'Number of successful archival operations',
            ['operation', 'table_name']
        )
        self.archival_operations_failed = Counter(
            'archival_operations_failed',
            'Number of failed archival operations',
            ['operation', 'table_name', 'error_type']
        )
        self.archival_operation_duration = Histogram(
            'archival_operation_duration_seconds',
            'Duration of archival operations in seconds',
            ['operation', 'table_name'],
            buckets=(0.1, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0, 120.0, 300.0)
        )
        self.archival_data_size_bytes = Summary(
            'archival_data_size_bytes',
            'Size of archived data in bytes',
            ['table_name']
        )
        
        # Storage metrics
        self.storage_operations_total = Counter(
            'storage_operations_total',
            'Total number of storage operations',
            ['operation']
        )
        self.storage_operations_success = Counter(
            'storage_operations_success',
            'Number of successful storage operations',
            ['operation']
        )
        self.storage_operations_failed = Counter(
            'storage_operations_failed',
            'Number of failed storage operations',
            ['operation', 'error_type']
        )
        self.storage_operation_duration = Histogram(
            'storage_operation_duration_seconds',
            'Duration of storage operations in seconds',
            ['operation'],
            buckets=(0.1, 0.5, 1.0, 2.5, 5.0, 10.0, 30.0, 60.0)
        )
        self.storage_data_size_bytes = Gauge(
            'storage_data_size_bytes',
            'Size of data in storage in bytes',
            ['container']
        )
        
        # Redis metrics
        self.redis_operations_total = Counter(
            'redis_operations_total',
            'Total number of Redis operations',
            ['operation']
        )
        self.redis_operations_success = Counter(
            'redis_operations_success',
            'Number of successful Redis operations',
            ['operation']
        )
        self.redis_operations_failed = Counter(
            'redis_operations_failed',
            'Number of failed Redis operations',
            ['operation', 'error_type']
        )
        self.redis_operation_duration = Histogram(
            'redis_operation_duration_seconds',
            'Duration of Redis operations in seconds',
            ['operation'],
            buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0)
        )
        
        # HTTP metrics
        self.http_requests_total = Counter(
            'http_requests_total',
            'Total number of HTTP requests',
            ['method', 'path']
        )
        self.http_request_duration_seconds = Histogram(
            'http_request_duration_seconds',
            'HTTP request duration in seconds',
            ['method', 'path', 'status_code'],
            buckets=(0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0)
        )
        self.http_exceptions_total = Counter(
            'http_exceptions_total',
            'Total number of HTTP exceptions',
            ['method', 'path', 'exception_type']
        )
        
        # System metrics
        self.system_cpu_usage = Gauge(
            'system_cpu_usage_percent',
            'System CPU usage percentage'
        )
        self.system_memory_usage = Gauge(
            'system_memory_usage_bytes',
            'System memory usage in bytes',
            ['type']
        )
        self.system_disk_usage = Gauge(
            'system_disk_usage_bytes',
            'System disk usage in bytes',
            ['path', 'type']
        )
        
        # SLO/SLI metrics
        self.slo_request_total = Counter(
            'slo_request_total',
            'Total number of requests for SLO tracking',
            ['path']
        )
        self.slo_request_success_total = Counter(
            'slo_request_success_total',
            'Number of successful requests for SLO tracking',
            ['path']
        )
        self.slo_request_latency_met_total = Counter(
            'slo_request_latency_met_total',
            'Number of requests meeting latency SLO',
            ['path']
        )
        
        # Set service info
        self.service_info.labels(
            version='1.0.0',
            python_version=platform.python_version(),
            hostname=platform.node()
        ).set(1)
        
        # Initialize uptime with service start time
        self.start_time = time.time()
        
        self.initialized = True
        logger.info("Archival Service metrics initialized")


# Create a singleton instance
metrics = ArchivalMetrics()


def update_system_metrics():
    """Update system metrics (CPU, memory, disk)."""
    try:
        # CPU usage
        metrics.system_cpu_usage.set(psutil.cpu_percent(interval=None))
        
        # Memory usage
        memory = psutil.virtual_memory()
        metrics.system_memory_usage.labels(type='total').set(memory.total)
        metrics.system_memory_usage.labels(type='available').set(memory.available)
        metrics.system_memory_usage.labels(type='used').set(memory.used)
        
        # Disk usage
        for partition in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                metrics.system_disk_usage.labels(
                    path=partition.mountpoint, type='total'
                ).set(usage.total)
                metrics.system_disk_usage.labels(
                    path=partition.mountpoint, type='used'
                ).set(usage.used)
                metrics.system_disk_usage.labels(
                    path=partition.mountpoint, type='free'
                ).set(usage.free)
            except (PermissionError, FileNotFoundError):
                # Skip partitions that can't be read
                pass
        
        # Update service uptime
        metrics.service_uptime.set(time.time() - metrics.start_time)
    except Exception as e:
        logger.error(f"Error updating system metrics: {str(e)}")


def update_storage_metrics(container_name: str, size_bytes: int):
    """Update storage metrics.
    
    Args:
        container_name: Name of the storage container
        size_bytes: Size of data in bytes
    """
    metrics.storage_data_size_bytes.labels(container=container_name).set(size_bytes)


async def export_metrics_to_observability(
    observability_url: str,
    push_gateway: Optional[str] = None,
    job_name: str = "archival_service"
):
    """Export metrics to the Observability Service and optionally to a Prometheus Pushgateway.
    
    Args:
        observability_url: URL of the Observability Service metrics ingestion endpoint
        push_gateway: Optional URL of the Prometheus Pushgateway
        job_name: Job name for the Prometheus Pushgateway
    """
    if not metrics.initialized:
        logger.warning("Metrics not initialized, skipping export")
        return
    
    # Generate metrics data
    prometheus_data = generate_latest().decode('utf-8')

    payload = {
        "service": job_name,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "metrics": prometheus_data,
        "format": "prometheus"
    }

    # Export to Observability Service
    if observability_url:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    observability_url,
                    json=payload,
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status not in [200, 202]:
                        response_text = await response.text()
                        logger.error(
                            f"Failed to export metrics to Observability Service: "
                            f"Status {response.status}, Response: {response_text}"
                        )
                    else:
                        logger.debug("Successfully exported metrics to Observability Service")
        except Exception as e:
            logger.error(f"Error exporting metrics to Observability Service: {str(e)}")
    
    # Export to Prometheus Pushgateway
    if push_gateway:
        try:
            # This is a blocking call, so we run it in a thread pool
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                None,
                functools.partial(
                    push_to_gateway,
                    push_gateway,
                    job=job_name,
                    registry=REGISTRY
                )
            )
            logger.debug(f"Successfully exported metrics to Pushgateway: {push_gateway}")
        except Exception as e:
            logger.error(f"Error exporting metrics to Pushgateway: {str(e)}")


def track_endpoint_execution(func):
    """Decorator to track endpoint execution metrics.
    
    Args:
        func: The endpoint function to track
    
    Returns:
        Wrapped function with metrics tracking
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        path = func.__name__
        method = "GET"  # Default method
        
        # Try to extract method from FastAPI request
        for arg in args:
            if hasattr(arg, "method"):
                method = arg.method
                break
        
        start_time = time.time()
        
        try:
            result = await func(*args, **kwargs)
            duration = time.time() - start_time
            
            # Record successful request
            status_code = 200
            if hasattr(result, "status_code"):
                status_code = result.status_code
            
            metrics.http_request_duration_seconds.labels(
                method=method, path=path, status_code=status_code
            ).observe(duration)
            
            return result
        except Exception as e:
            # Record exception
            metrics.http_exceptions_total.labels(
                method=method, path=path, exception_type=type(e).__name__
            ).inc()
            raise
    
    return wrapper


def track_archival_operation(operation_name: str):
    """Decorator to track archival operation metrics.
    
    Args:
        operation_name: Name of the archival operation
    
    Returns:
        Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Try to extract table name from args or kwargs
            table_name = "unknown"
            if len(args) > 1 and hasattr(args[1], "table_name"):
                table_name = args[1].table_name
            elif "event" in kwargs and hasattr(kwargs["event"], "table_name"):
                table_name = kwargs["event"].table_name
            
            # Increment total operations counter
            metrics.archival_operations_total.labels(
                operation=operation_name, table_name=table_name
            ).inc()
            
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                
                # Record duration
                duration = time.time() - start_time
                metrics.archival_operation_duration.labels(
                    operation=operation_name, table_name=table_name
                ).observe(duration)
                
                # Record success
                metrics.archival_operations_success.labels(
                    operation=operation_name, table_name=table_name
                ).inc()
                
                # Record data size if available
                if isinstance(result, tuple) and len(result) > 1:
                    # Assuming the second element is the data size
                    data_size = result[1]
                    if isinstance(data_size, (int, float)):
                        metrics.archival_data_size_bytes.labels(table_name=table_name).observe(data_size)
                
                return result
            except Exception as e:
                # Record failure
                metrics.archival_operations_failed.labels(
                    operation=operation_name,
                    table_name=table_name,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return wrapper
    
    return decorator


def track_storage_operation(operation_name: str):
    """Decorator to track storage operation metrics.
    
    Args:
        operation_name: Name of the storage operation
    
    Returns:
        Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Increment total operations counter
            metrics.storage_operations_total.labels(operation=operation_name).inc()
            
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                
                # Record duration
                duration = time.time() - start_time
                metrics.storage_operation_duration.labels(operation=operation_name).observe(duration)
                
                # Record success
                metrics.storage_operations_success.labels(operation=operation_name).inc()
                
                return result
            except Exception as e:
                # Record failure
                metrics.storage_operations_failed.labels(
                    operation=operation_name,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return wrapper
    
    return decorator


def track_redis_operation(operation_name: str):
    """Decorator to track Redis operation metrics.
    
    Args:
        operation_name: Name of the Redis operation
    
    Returns:
        Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Increment total operations counter
            metrics.redis_operations_total.labels(operation=operation_name).inc()
            
            start_time = time.time()
            
            try:
                result = await func(*args, **kwargs)
                
                # Record duration
                duration = time.time() - start_time
                metrics.redis_operation_duration.labels(operation=operation_name).observe(duration)
                
                # Record success
                metrics.redis_operations_success.labels(operation=operation_name).inc()
                
                return result
            except Exception as e:
                # Record failure
                metrics.redis_operations_failed.labels(
                    operation=operation_name,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return wrapper
    
    return decorator
