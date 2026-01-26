"""
Metrics module for the Messaging Service.

This module provides Prometheus metrics collection and export functionality for the Messaging Service,
including Redis operations metrics, message processing metrics, channel metrics, and system metrics.
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

class MessagingServiceMetrics:
    """Metrics collection for the Messaging Service."""
    
    def __init__(self):
        """Initialize metrics."""
        # Service info and health metrics
        self.service_info = Gauge(
            'messaging_service_info', 
            'Messaging Service information',
            ['version', 'python_version', 'platform']
        )
        self.service_health = Gauge('messaging_service_health', 'Messaging Service health status (1=healthy, 0=unhealthy)')
        self.service_ready = Gauge('messaging_service_ready', 'Messaging Service readiness status (1=ready, 0=not ready)')
        self.service_uptime = Gauge('messaging_service_uptime_seconds', 'Messaging Service uptime in seconds')
        
        # Redis connection metrics
        self.redis_connection_pool_size = Gauge('redis_connection_pool_size', 'Redis connection pool size')
        self.redis_connection_pool_used = Gauge('redis_connection_pool_used', 'Redis connections in use')
        self.redis_connection_errors = Counter('redis_connection_errors_total', 'Redis connection errors')
        
        # Redis operation metrics
        self.redis_operations_total = Counter(
            'redis_operations_total', 
            'Redis operations count',
            ['operation']
        )
        self.redis_operation_errors_total = Counter(
            'redis_operation_errors_total', 
            'Redis operation errors count',
            ['operation', 'error_type']
        )
        self.redis_operation_duration_seconds = Histogram(
            'redis_operation_duration_seconds', 
            'Redis operation duration in seconds',
            ['operation'],
            buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
        )
        
        # Message metrics
        self.messages_published_total = Counter(
            'messages_published_total', 
            'Total messages published',
            ['channel']
        )
        self.messages_consumed_total = Counter(
            'messages_consumed_total', 
            'Total messages consumed',
            ['channel', 'consumer']
        )
        
        # Service-to-service traffic metrics (for lineage tracking)
        self.service_messages_published = Counter(
            'service_messages_published_total',
            'Messages published by source service',
            ['source_service', 'event_type', 'channel']
        )
        self.service_messages_consumed = Counter(
            'service_messages_consumed_total',
            'Messages consumed by target service',
            ['source_service', 'target_service', 'event_type', 'channel']
        )
        self.service_traffic_bytes = Counter(
            'service_traffic_bytes_total',
            'Total bytes transferred between services',
            ['source_service', 'target_service']
        )
        self.service_message_latency = Histogram(
            'service_message_latency_seconds',
            'Message delivery latency between services',
            ['source_service', 'target_service'],
            buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5]
        )
        
        # HTTP traffic metrics (for UI and API gateway traffic)
        self.http_traffic_total = Counter(
            'http_traffic_total',
            'HTTP requests between services',
            ['source', 'target', 'method', 'endpoint']
        )
        self.http_traffic_bytes = Counter(
            'http_traffic_bytes_total',
            'HTTP traffic bytes between services',
            ['source', 'target', 'direction']
        )
        self.message_size_bytes = Histogram(
            'message_size_bytes', 
            'Message size in bytes',
            ['channel'],
            buckets=[10, 100, 1000, 10000, 100000, 1000000]
        )
        self.message_processing_duration_seconds = Histogram(
            'message_processing_duration_seconds', 
            'Message processing duration in seconds',
            ['channel', 'consumer'],
            buckets=[0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1, 2.5, 5, 10]
        )
        self.message_processing_errors_total = Counter(
            'message_processing_errors_total', 
            'Message processing errors',
            ['channel', 'consumer', 'error_type']
        )
        
        # Channel metrics
        self.active_channels = Gauge('active_channels', 'Number of active channels')
        self.channel_subscribers = Gauge(
            'channel_subscribers', 
            'Number of subscribers per channel',
            ['channel']
        )
        self.channel_message_rate = Gauge(
            'channel_message_rate', 
            'Message rate per channel (messages/sec)',
            ['channel']
        )
        
        # Subscription metrics
        self.active_subscriptions = Gauge('active_subscriptions', 'Number of active subscriptions')
        self.subscription_events_total = Counter(
            'subscription_events_total', 
            'Subscription events',
            ['event_type']
        )
        self.subscription_errors_total = Counter(
            'subscription_errors_total', 
            'Subscription errors',
            ['error_type']
        )
        
        # Dead Letter Queue metrics
        self.dlq_messages_total = Counter('dlq_messages_total', 'Total messages sent to DLQ')
        self.dlq_retries_total = Counter('dlq_retries_total', 'Total message retry attempts')
        self.dlq_size = Gauge('dlq_size', 'Current size of the Dead Letter Queue')
        
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
metrics = MessagingServiceMetrics()


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


def track_redis_operation(operation: str) -> Callable[[AsyncF], AsyncF]:
    """Decorator to track Redis operation metrics."""
    def decorator(func: AsyncF) -> AsyncF:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                # Track operation count
                metrics.redis_operations_total.labels(operation=operation).inc()
                
                # Execute operation
                result = await func(*args, **kwargs)
                
                # Track duration
                duration = time.time() - start_time
                metrics.redis_operation_duration_seconds.labels(operation=operation).observe(duration)
                
                return result
            except Exception as e:
                # Track error
                metrics.redis_operation_errors_total.labels(
                    operation=operation,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return cast(AsyncF, wrapper)
    
    return decorator


def track_message_processing(channel: str, consumer: str) -> Callable[[AsyncF], AsyncF]:
    """Decorator to track message processing metrics."""
    def decorator(func: AsyncF) -> AsyncF:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                # Execute message processing
                result = await func(*args, **kwargs)
                
                # Track message consumed
                metrics.messages_consumed_total.labels(
                    channel=channel,
                    consumer=consumer
                ).inc()
                
                # Track duration
                duration = time.time() - start_time
                metrics.message_processing_duration_seconds.labels(
                    channel=channel,
                    consumer=consumer
                ).observe(duration)
                
                return result
            except Exception as e:
                # Track error
                metrics.message_processing_errors_total.labels(
                    channel=channel,
                    consumer=consumer,
                    error_type=type(e).__name__
                ).inc()
                raise
        
        return cast(AsyncF, wrapper)
    
    return decorator


def track_message_publish(func: F) -> F:
    """Decorator to track message publishing metrics."""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # Extract channel and message from arguments
        # Assuming first arg after self is channel, second is message
        if len(args) >= 3:
            channel = args[1]
            message = args[2]
        else:
            channel = kwargs.get('channel', 'unknown')
            message = kwargs.get('message', '')
        
        # Track message size if available
        if message:
            try:
                message_size = len(str(message))
                metrics.message_size_bytes.labels(channel=channel).observe(message_size)
            except Exception:
                pass
        
        # Track message published
        metrics.messages_published_total.labels(channel=channel).inc()
        
        # Execute publish operation
        return await func(*args, **kwargs)
    
    return cast(F, wrapper)


def track_service_publish(source_service: str, event_type: str, channel: str, message_size: int = 0):
    """Track a message published by a specific service."""
    try:
        metrics.service_messages_published.labels(
            source_service=source_service,
            event_type=event_type,
            channel=channel
        ).inc()
        logger.debug(f"Tracked publish: {source_service} -> {channel} ({event_type})")
    except Exception as e:
        logger.debug(f"Error tracking service publish: {e}")


def track_service_consume(source_service: str, target_service: str, event_type: str, channel: str, message_size: int = 0, latency_seconds: float = 0):
    """Track a message consumed by a specific service from another service."""
    try:
        metrics.service_messages_consumed.labels(
            source_service=source_service,
            target_service=target_service,
            event_type=event_type,
            channel=channel
        ).inc()
        
        if message_size > 0:
            metrics.service_traffic_bytes.labels(
                source_service=source_service,
                target_service=target_service
            ).inc(message_size)
        
        if latency_seconds > 0:
            metrics.service_message_latency.labels(
                source_service=source_service,
                target_service=target_service
            ).observe(latency_seconds)
        
        logger.debug(f"Tracked consume: {source_service} -> {target_service} ({event_type})")
    except Exception as e:
        logger.debug(f"Error tracking service consume: {e}")


def track_http_traffic(source: str, target: str, method: str, endpoint: str, request_bytes: int = 0, response_bytes: int = 0):
    """Track HTTP traffic between services."""
    try:
        metrics.http_traffic_total.labels(
            source=source,
            target=target,
            method=method,
            endpoint=endpoint
        ).inc()
        
        if request_bytes > 0:
            metrics.http_traffic_bytes.labels(
                source=source,
                target=target,
                direction='request'
            ).inc(request_bytes)
        
        if response_bytes > 0:
            metrics.http_traffic_bytes.labels(
                source=source,
                target=target,
                direction='response'
            ).inc(response_bytes)
        
        logger.debug(f"Tracked HTTP: {source} -> {target} {method} {endpoint}")
    except Exception as e:
        logger.debug(f"Error tracking HTTP traffic: {e}")


def get_service_traffic_summary() -> Dict[str, Any]:
    """Get a summary of service-to-service traffic for visualization."""
    try:
        from prometheus_client import REGISTRY
        
        traffic_data = {
            "links": [],
            "nodes": set()
        }
        
        # Collect service message traffic
        for metric in REGISTRY.collect():
            if metric.name == 'service_messages_consumed_total':
                for sample in metric.samples:
                    if sample.name == 'service_messages_consumed_total':
                        source = sample.labels.get('source_service', 'unknown')
                        target = sample.labels.get('target_service', 'unknown')
                        value = sample.value
                        
                        if value > 0:
                            traffic_data["nodes"].add(source)
                            traffic_data["nodes"].add(target)
                            traffic_data["links"].append({
                                "source": source,
                                "target": target,
                                "value": int(value),
                                "type": "message"
                            })
            
            elif metric.name == 'http_traffic_total':
                for sample in metric.samples:
                    if sample.name == 'http_traffic_total':
                        source = sample.labels.get('source', 'unknown')
                        target = sample.labels.get('target', 'unknown')
                        value = sample.value
                        
                        if value > 0:
                            traffic_data["nodes"].add(source)
                            traffic_data["nodes"].add(target)
                            traffic_data["links"].append({
                                "source": source,
                                "target": target,
                                "value": int(value),
                                "type": "http"
                            })
        
        traffic_data["nodes"] = list(traffic_data["nodes"])
        return traffic_data
    except Exception as e:
        logger.error(f"Error getting service traffic summary: {e}")
        return {"links": [], "nodes": []}


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


def update_redis_connection_metrics(pool_size: int, used_connections: int):
    """Update Redis connection metrics."""
    metrics.redis_connection_pool_size.set(pool_size)
    metrics.redis_connection_pool_used.set(used_connections)


def update_channel_metrics(channels_data: Dict[str, Dict[str, Any]]):
    """Update channel metrics."""
    # Update active channels count
    metrics.active_channels.set(len(channels_data))
    
    # Update per-channel metrics
    for channel_name, channel_data in channels_data.items():
        if 'subscribers' in channel_data:
            metrics.channel_subscribers.labels(channel=channel_name).set(channel_data['subscribers'])
        
        if 'message_rate' in channel_data:
            metrics.channel_message_rate.labels(channel=channel_name).set(channel_data['message_rate'])


def update_subscription_metrics(active_count: int):
    """Update subscription metrics."""
    metrics.active_subscriptions.set(active_count)


def update_dlq_metrics(dlq_size: int):
    """Update DLQ metrics."""
    metrics.dlq_size.set(dlq_size)


async def export_metrics_to_observability(
    observability_url: Optional[str] = None,
    push_gateway: Optional[str] = None,
    job_name: str = "messaging_service",
    timeout: float = 2.0
):
    """
    Export Prometheus metrics to Prometheus Pushgateway.
    
    The observability service doesn't accept metrics via HTTP POST - it only exposes
    its own metrics via GET /metrics for Prometheus to scrape. This function now focuses
    on pushing metrics to the Prometheus Pushgateway instead.
    
    Args:
        observability_url: URL of the Observability Service (not used for pushing metrics)
        push_gateway: URL of the Prometheus Pushgateway
        job_name: Job name for Prometheus metrics
        timeout: Timeout in seconds for HTTP requests
    """
    try:
        # Get metrics data from the registry
        metrics_data = generate_latest(REGISTRY)
        
        # Log that we're not exporting to observability service since it doesn't accept metrics
        if observability_url:
            logger.debug(
                f"Note: Not pushing metrics to observability service at {observability_url} - "
                f"the service only exposes metrics via GET /metrics and doesn't accept metrics via POST."
            )
        
        # Export to Prometheus Pushgateway if URL is provided
        if push_gateway:
            try:
                logger.debug(f"Pushing metrics to Prometheus Pushgateway at {push_gateway}")
                
                # Validate the push_gateway URL format
                if not push_gateway.startswith(('http://', 'https://')):
                    logger.warning(f"Invalid Pushgateway URL format: {push_gateway}. Must start with http:// or https://")
                    return
                
                # Push metrics to Pushgateway with timeout
                push_to_gateway(
                    gateway=push_gateway,
                    job=job_name,
                    registry=REGISTRY,
                    timeout=timeout
                )
                logger.debug(f"Successfully pushed metrics to Pushgateway at {push_gateway}")
            except Exception as e:
                # Rate-limit warnings for Pushgateway errors to reduce log noise
                error_count = getattr(export_metrics_to_observability, '_pushgateway_error_count', 0) + 1
                export_metrics_to_observability._pushgateway_error_count = error_count
                
                if error_count % 10 == 1:  # Log warning on 1st, 11th, 21st, etc. occurrence
                    logger.warning(f"Failed to push metrics to Pushgateway: {str(e)}")
                else:
                    logger.debug(f"Failed to push metrics to Pushgateway: {str(e)}")
        else:
            logger.debug("Prometheus Pushgateway URL not configured, skipping metrics export")
    
    except Exception as e:
        logger.warning(f"Error in metrics export function: {str(e)}")
        # Log the full traceback at debug level for troubleshooting
        import traceback
        logger.debug(f"Metrics export error traceback: {traceback.format_exc()}")

        # Continue execution - metrics export should not break the application
