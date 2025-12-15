"""
Messaging Service - Centralized Redis pub/sub messaging for microservices.

This service consolidates all messaging functionality:
- Event publishing and subscription management
- Redis pub/sub operations
- Message routing and delivery
- Webhook notifications
- Dead letter queue handling
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import make_wsgi_app
from prometheus_client.exposition import make_asgi_app
import logging
import os
import time
import asyncio
import uuid
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
from contextlib import asynccontextmanager
import psutil

from .event_publisher import EventPublisher
from .subscription_manager import SubscriptionManager
from .models import (
    PublishMessageRequest, PublishMessageResponse, BulkPublishRequest, BulkPublishResponse,
    SubscriptionRequest, SubscriptionResponse, SubscriptionInfo, MessageAcknowledgment,
    EventRequest, EventResponse, ChannelInfo, ChannelStats,
    HealthResponse, MetricsResponse, ErrorResponse, PublishCommandRequest, CommandReceipt
)
from .config import get_settings
from .metrics import metrics, update_system_metrics, update_redis_connection_metrics, export_metrics_to_observability, track_endpoint_execution, track_redis_operation, track_message_processing, track_message_publish, update_channel_metrics, update_subscription_metrics, update_dlq_metrics
from opentelemetry import trace
from opentelemetry.trace.status import Status, StatusCode
from .telemetry import initialize_telemetry, instrument_fastapi, extract_correlation_id, extract_correlation_id_from_headers, inject_trace_context, add_span_attributes, trace_method, trace_redis_operation, trace_message_processing, traced_span

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global service instances
event_publisher: Optional[EventPublisher] = None
subscription_manager: Optional[SubscriptionManager] = None
service_start_time = time.time()

# Background task cancellation handles
metrics_export_task = None
system_metrics_task = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global event_publisher, subscription_manager, metrics_export_task, system_metrics_task
    
    # Startup
    try:
        settings = get_settings()
        
        # Initialize metrics with service name
        metrics.initialize(settings.service_name)
        metrics.service_ready.set(0)  # Not ready yet
        
        # Initialize OpenTelemetry if endpoint is configured
        if settings.otlp_endpoint and settings.enable_distributed_tracing:
            logger.info(f"Initializing OpenTelemetry with endpoint {settings.otlp_endpoint}")
            try:
                # Set reasonable defaults for retry parameters
                retry_attempts = min(settings.otlp_max_retry_attempts, 3)  # Limit max retries to 3
                batch_size = min(settings.otlp_max_export_batch_size, 50)  # Limit batch size to 50
                delay_millis = 15000  # 15 seconds between batch exports
                
                initialize_telemetry(
                    service_name=settings.service_name,
                    otlp_endpoint=settings.otlp_endpoint,
                    resource_attributes={
                        "service.version": settings.version,
                        "deployment.environment": settings.environment
                    },
                    trace_sample_rate=settings.trace_sample_rate,
                    export_timeout_seconds=settings.metrics_export_timeout,
                    max_export_batch_size=batch_size,
                    max_retry_attempts=retry_attempts,
                    retry_delay_seconds=settings.otlp_retry_delay_seconds,
                    schedule_delay_millis=delay_millis,
                    auto_instrument_packages=True
                )
                logger.info("OpenTelemetry initialization completed successfully")
            except Exception as e:
                logger.warning(f"OpenTelemetry initialization encountered an issue: {str(e)}. Service will continue with limited tracing.")
                # Continue execution - tracing should not break the application
        elif settings.enable_distributed_tracing and not settings.otlp_endpoint:
            logger.info("OpenTelemetry tracing enabled but no OTLP endpoint configured. Using console exporter only.")
            # Initialize minimal telemetry with console exporter
            try:
                initialize_telemetry(
                    service_name=settings.service_name,
                    resource_attributes={
                        "service.version": settings.version,
                        "deployment.environment": settings.environment
                    },
                    trace_sample_rate=settings.trace_sample_rate,
                    auto_instrument_packages=True
                )
            except Exception as e:
                logger.warning(f"Minimal telemetry initialization failed: {str(e)}")
        else:
            logger.info("OpenTelemetry tracing disabled")
        
        # Initialize event publisher
        event_publisher = EventPublisher(
            redis_url=settings.redis_url,
            max_connections=settings.redis_max_connections,
            retry_on_timeout=settings.redis_retry_on_timeout,
            socket_keepalive=settings.redis_socket_keepalive,
            default_ttl=settings.default_message_ttl,
            enable_compression=settings.enable_message_compression,
            max_message_size=settings.max_message_size
        )
        # Wrap Redis operations with metrics tracking
        if hasattr(event_publisher, 'publish') and settings.enable_prometheus_metrics:
            original_publish = event_publisher.publish
            event_publisher.publish = track_redis_operation(operation_name="publish")(original_publish)
            
            if hasattr(event_publisher, 'get_channel_info'):
                original_get_channel = event_publisher.get_channel_info
                event_publisher.get_channel_info = track_redis_operation(operation_name="get_channel_info")(original_get_channel)
                
            if hasattr(event_publisher, 'get_all_channels_info'):
                original_get_all = event_publisher.get_all_channels_info
                event_publisher.get_all_channels_info = track_redis_operation(operation_name="get_all_channels_info")(original_get_all)
        
        await event_publisher.initialize()
        
        # Initialize subscription manager
        subscription_manager = SubscriptionManager(
            redis_url=settings.redis_url,
            max_connections=settings.redis_max_connections,
            heartbeat_interval=settings.subscription_heartbeat_interval,
            subscription_timeout=settings.subscription_timeout,
            max_subscriptions_per_service=settings.max_subscriptions_per_service
        )
        
        # Wrap subscription operations with metrics tracking
        if settings.enable_prometheus_metrics:
            if hasattr(subscription_manager, 'create_subscription'):
                original_create = subscription_manager.create_subscription
                subscription_manager.create_subscription = track_redis_operation(operation="create_subscription")(original_create)
                
            if hasattr(subscription_manager, 'cancel_subscription'):
                original_cancel = subscription_manager.cancel_subscription
                subscription_manager.cancel_subscription = track_redis_operation(operation="cancel_subscription")(original_cancel)
                
            if hasattr(subscription_manager, 'acknowledge_message'):
                original_ack = subscription_manager.acknowledge_message
                subscription_manager.acknowledge_message = track_redis_operation(operation="acknowledge_message")(original_ack)
        
        await subscription_manager.initialize()
        
        # Start background tasks for metrics
        if settings.enable_prometheus_metrics:
            # Start system metrics update task
            async def update_system_metrics_periodically():
                """Update system metrics periodically."""
                while True:
                    try:
                        # Only collect metrics if the feature is enabled
                        if settings.enable_prometheus_metrics:
                            # Update system metrics
                            try:
                                # Call without parameters as per metrics.py implementation
                                update_system_metrics()
                            except Exception as e:
                                logger.warning(f"Failed to update system metrics: {str(e)}")
                            
                            # Update Redis connection metrics
                            try:
                                if event_publisher and hasattr(event_publisher, 'get_connection_stats'):
                                    conn_stats = await event_publisher.get_connection_stats()
                                    update_redis_connection_metrics(
                                        pool_size=conn_stats.get('pool_size', 0),
                                        used_connections=conn_stats.get('used_connections', 0)
                                    )
                            except Exception as e:
                                logger.warning(f"Failed to update Redis connection metrics: {str(e)}")
                            
                            # Update channel metrics
                            try:
                                if event_publisher and hasattr(event_publisher, 'get_all_channels_info'):
                                    channels_info = await event_publisher.get_all_channels_info()
                                    update_channel_metrics(channels_info)
                            except Exception as e:
                                logger.warning(f"Failed to update channel metrics: {str(e)}")
                            
                            # Update subscription metrics
                            try:
                                if subscription_manager and hasattr(subscription_manager, 'get_metrics'):
                                    sub_metrics = await subscription_manager.get_metrics()
                                    update_subscription_metrics(sub_metrics.get('active_subscriptions', 0))
                                    
                                    # Update DLQ metrics if available
                                    if 'dlq_size' in sub_metrics:
                                        update_dlq_metrics(sub_metrics['dlq_size'])
                            except Exception as e:
                                logger.warning(f"Failed to update subscription metrics: {str(e)}")
                                
                            logger.debug("System metrics updated successfully")
                        else:
                            logger.debug("System metrics collection skipped - feature disabled")
                    except Exception as e:
                        # Log as warning instead of error to avoid filling logs
                        logger.warning(f"System metrics collection encountered an issue: {str(e)}")
                    
                    # Wait for the next metrics collection interval
                    await asyncio.sleep(15)  # Update every 15 seconds
            
            # Start metrics export task
            async def export_metrics_periodically():
                """Export metrics to observability service periodically."""
                # Log initial configuration
                logger.info(f"Metrics export configured with: observability_url={settings.observability_service_url}, "
                           f"push_gateway={settings.prometheus_push_gateway}, "
                           f"interval={settings.metrics_push_interval}s")
                
                # Track consecutive failures to avoid log spam
                consecutive_failures = 0
                max_log_failures = 5  # Only log detailed errors for the first few failures
                
                while True:
                    try:
                        # Only attempt to export metrics if the feature is enabled
                        if settings.enable_prometheus_metrics:
                            # Check if observability URL is configured
                            if settings.observability_service_url:
                                try:
                                    await export_metrics_to_observability(
                                        observability_url=settings.observability_service_url,
                                        push_gateway=settings.prometheus_push_gateway if settings.prometheus_push_gateway else None,
                                        job_name=settings.metrics_export_job_name
                                    )
                                    logger.debug("Metrics export to observability service completed")
                                    consecutive_failures = 0  # Reset failure counter on success
                                except Exception as e:
                                    consecutive_failures += 1
                                    if consecutive_failures <= max_log_failures:
                                        logger.warning(f"Metrics export to observability service failed: {str(e)}")
                                    elif consecutive_failures % 60 == 0:  # Log once every ~60 failures
                                        logger.warning(f"Metrics export to observability service still failing after {consecutive_failures} attempts")
                            else:
                                logger.debug("Observability service URL not configured, skipping export")
                                
                            # Try Prometheus Pushgateway export separately
                            if settings.prometheus_push_gateway:
                                try:
                                    await export_metrics_to_observability(
                                        observability_url=None,
                                        push_gateway=settings.prometheus_push_gateway,
                                        job_name=settings.metrics_export_job_name
                                    )
                                    logger.debug("Metrics export to Prometheus Pushgateway completed")
                                except Exception as e:
                                    logger.warning(f"Metrics export to Prometheus Pushgateway failed: {str(e)}")
                        else:
                            logger.debug("Metrics export skipped - feature disabled")
                    except Exception as e:
                        # Log as warning instead of error to avoid filling logs
                        logger.warning(f"Metrics export task encountered an unexpected issue: {str(e)}")
                    
                    # Wait for the next metrics export interval
                    await asyncio.sleep(settings.metrics_push_interval)
            
            # Create and store task objects for later cancellation
            system_metrics_task = asyncio.create_task(update_system_metrics_periodically())
            metrics_export_task = asyncio.create_task(export_metrics_periodically())
        
        # Set service as ready
        metrics.service_ready.set(1)
        metrics.service_health.set(1)
        
        logger.info("Messaging service started successfully")
        yield
        
    except Exception as e:
        logger.error(f"Failed to start messaging service: {str(e)}")
        metrics.service_health.set(0)
        raise
    finally:
        # Shutdown
        # Set service as not ready during shutdown
        metrics.service_ready.set(0)
        
        # Cancel metrics background tasks
        if system_metrics_task:
            system_metrics_task.cancel()
            try:
                await system_metrics_task
            except asyncio.CancelledError:
                pass
        
        if metrics_export_task:
            metrics_export_task.cancel()
            try:
                await metrics_export_task
            except asyncio.CancelledError:
                pass
        
        if event_publisher:
            await event_publisher.close()
        if subscription_manager:
            await subscription_manager.close()
        logger.info("Messaging service shutdown complete")


# Initialize FastAPI app with lifespan management
app = FastAPI(
    title="Messaging Service",
    description="Centralized Redis pub/sub messaging for microservices",
    version="1.0.0",
    lifespan=lifespan
)

# Instrument FastAPI with OpenTelemetry
settings = get_settings()
if settings.enable_distributed_tracing:
    instrument_fastapi(app)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add correlation ID middleware
@app.middleware("http")
async def correlation_id_middleware(request: Request, call_next):
    # Extract correlation ID from request headers or generate a new one
    correlation_id = extract_correlation_id_from_headers(request.headers) or str(uuid.uuid4())
    transaction_id = str(uuid.uuid4())  # Generate unique transaction ID for this request
    start_time = datetime.utcnow()
    
    # Add correlation ID to request state for use in endpoints
    request.state.correlation_id = correlation_id
    request.state.transaction_id = transaction_id
    request.state.start_time = start_time
    
    # Get current span and add detailed attributes
    current_span = trace.get_current_span()
    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
        # Add request context attributes
        current_span.set_attribute("correlation_id", correlation_id)
        current_span.set_attribute("transaction_id", transaction_id)
        current_span.set_attribute("service.name", "messaging_service")
        settings = get_settings()
        current_span.set_attribute("environment", settings.environment)
        current_span.set_attribute("service.version", settings.version)
        current_span.set_attribute("timestamp.start", start_time.isoformat())
        
        # Add HTTP request attributes
        current_span.set_attribute("http.request.path", request.url.path)
        current_span.set_attribute("http.request.method", request.method)
        current_span.set_attribute("http.request.url", str(request.url))
        
        # Add client info if available
        if "user-agent" in request.headers:
            current_span.set_attribute("http.user_agent", request.headers["user-agent"])
        if "x-forwarded-for" in request.headers:
            current_span.set_attribute("http.client_ip", request.headers["x-forwarded-for"])
    
    # Process the request and capture timing
    try:
        response = await call_next(request)
        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        # Add response attributes to span
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("http.response.status_code", response.status_code)
            current_span.set_attribute("http.response.duration_ms", duration_ms)
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("success", response.status_code < 500)
            
            # Set span status based on response code
            if response.status_code >= 500:
                current_span.set_status(Status(StatusCode.ERROR, f"HTTP {response.status_code}"))
            else:
                current_span.set_status(Status(StatusCode.OK))
        
        # Add correlation ID to response headers
        settings = get_settings()
        if settings.propagate_correlation_id:
            response.headers["X-Correlation-ID"] = correlation_id
        
        return response
    except Exception as e:
        # Capture exception details in span
        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("http.response.duration_ms", duration_ms)
            current_span.set_attribute("error.type", e.__class__.__name__)
            current_span.set_attribute("error.message", str(e))
            current_span.set_attribute("success", False)
            current_span.set_status(Status(StatusCode.ERROR, str(e)))
            current_span.record_exception(e)
        
        # Re-raise the exception to be handled by FastAPI
        raise

# Add Prometheus metrics middleware
class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Skip metrics endpoint to avoid recursion
        if request.url.path == "/metrics":
            return await call_next(request)
            
        method = request.method
        path = request.url.path
        begin = time.time()
        
        # Track request count
        metrics.http_requests_total.labels(method=method, path=path).inc()
        
        # Track SLO metrics
        metrics.slo_request_total.labels(path=path).inc()
        
        # Process request and catch exceptions
        try:
            response = await call_next(request)
            duration = time.time() - begin
            status_code = response.status_code
            
            # Record request duration
            metrics.http_request_duration_seconds.labels(
                method=method, path=path, status_code=status_code
            ).observe(duration)
            
            # Track successful requests for SLO
            if 200 <= status_code < 400:
                metrics.slo_request_success_total.labels(path=path).inc()
                
                # Track latency SLO (assuming 1s SLO)
                if duration < 1.0:
                    metrics.slo_request_latency_met_total.labels(path=path).inc()
                    
            return response
        except Exception as e:
            # Track exceptions
            metrics.http_exceptions_total.labels(
                method=method, path=path, exception_type=type(e).__name__
            ).inc()
            raise

# Add metrics middleware
app.add_middleware(PrometheusMiddleware)

# Expose Prometheus metrics endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


def get_event_publisher() -> EventPublisher:
    """Dependency to get event publisher instance."""
    if event_publisher is None:
        raise HTTPException(status_code=503, detail="Event publisher not initialized")
    return event_publisher


def get_subscription_manager() -> SubscriptionManager:
    """Dependency to get subscription manager instance."""
    if subscription_manager is None:
        raise HTTPException(status_code=503, detail="Subscription manager not initialized")
    return subscription_manager


# Health check endpoint
@app.get("/health", response_model=HealthResponse)
@trace_method(name="health_check", kind="SERVER")
async def health_check(
    publisher: EventPublisher = Depends(get_event_publisher),
    sub_manager: SubscriptionManager = Depends(get_subscription_manager),
    request: Request = None
):
    """Check messaging service health and connectivity."""
    start_time = datetime.utcnow()
    settings = get_settings()
    
    # Extract correlation ID from request headers or generate a new one
    correlation_id = extract_correlation_id_from_headers(request.headers) if request else None
    if not correlation_id:
        correlation_id = str(uuid.uuid4())
    
    # Get current span and add detailed attributes
    current_span = trace.get_current_span()
    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
        # Add service context attributes
        current_span.set_attribute("correlation_id", correlation_id)
        current_span.set_attribute("service.name", settings.service_name)
        current_span.set_attribute("service.version", settings.version)
        current_span.set_attribute("environment", settings.environment)
        current_span.set_attribute("endpoint", "/health")
        current_span.set_attribute("timestamp.start", start_time.isoformat())
        
        # Add request attributes if available
        if request:
            current_span.set_attribute("http.request.method", request.method)
            current_span.set_attribute("http.request.url", str(request.url))
    
    try:
        # Check publisher health with tracing
        with traced_span("publisher_health_check", attributes={
            "component": "event_publisher",
            "correlation_id": correlation_id
        }) as publisher_span:
            publisher_health = await publisher.health_check()
            publisher_span.set_attribute("redis.connected", publisher_health.get("redis_connected", False))
            publisher_span.set_attribute("active_channels", publisher_health.get("active_channels", 0))
            publisher_span.set_attribute("status", publisher_health.get("status", "unknown"))
        
        # Check subscription manager health with tracing
        with traced_span("subscription_manager_health_check", attributes={
            "component": "subscription_manager",
            "correlation_id": correlation_id
        }) as sub_span:
            sub_manager_health = await sub_manager.health_check()
            sub_span.set_attribute("active_subscriptions", sub_manager_health.get("active_subscriptions", 0))
            sub_span.set_attribute("status", sub_manager_health.get("status", "unknown"))
        
        # Combine health status
        overall_status = "healthy" if (
            publisher_health.get("status") == "healthy" and 
            sub_manager_health.get("status") == "healthy"
        ) else "unhealthy"
        
        uptime = time.time() - service_start_time
        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        # Add final span attributes
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("health.status", overall_status)
            current_span.set_attribute("health.redis_connected", publisher_health.get("redis_connected", False))
            current_span.set_attribute("health.active_subscriptions", sub_manager_health.get("active_subscriptions", 0))
            current_span.set_attribute("health.active_channels", publisher_health.get("active_channels", 0))
            current_span.set_attribute("health.uptime_seconds", uptime)
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            
            # Set span status based on health status
            if overall_status == "healthy":
                current_span.set_status(Status(StatusCode.OK))
            else:
                error_message = publisher_health.get("error") or sub_manager_health.get("error") or "Service unhealthy"
                current_span.set_status(Status(StatusCode.ERROR, error_message))
        
        # Create response with correlation ID for tracing propagation
        response = HealthResponse(
            status=overall_status,
            timestamp=datetime.utcnow(),
            redis_connected=publisher_health.get("redis_connected", False),
            active_subscriptions=sub_manager_health.get("active_subscriptions", 0),
            active_channels=publisher_health.get("active_channels", 0),
            uptime_seconds=uptime,
            version=settings.version,
            environment=settings.environment,
            service_name=settings.service_name,
            error=publisher_health.get("error") or sub_manager_health.get("error"),
            correlation_id=correlation_id
        )
        
        return response
        
    except Exception as e:
        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        # Record error in span
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            current_span.set_attribute("error.type", e.__class__.__name__)
            current_span.set_attribute("error.message", str(e))
            current_span.set_attribute("health.status", "unhealthy")
            current_span.set_status(Status(StatusCode.ERROR, str(e)))
            current_span.record_exception(e)
        
        logger.error(f"Health check failed: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")


# Command publishing endpoint
@app.post("/messaging/commands/publish", response_model=CommandReceipt)
@trace_method(name="publish_command", kind="SERVER")
async def publish_command(
    request: PublishCommandRequest,
    publisher: EventPublisher = Depends(get_event_publisher),
    request_obj: Request = None
):
    """Publish a command to the command channel."""
    start_time = datetime.utcnow()
    settings = get_settings()
    
    correlation_id = request.correlation_id or (request_obj.state.correlation_id if hasattr(request_obj.state, "correlation_id") else str(uuid.uuid4()))

    current_span = trace.get_current_span()
    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
        add_span_attributes(current_span, {
            "correlation_id": correlation_id,
            "messaging.system": "redis_pubsub",
            "messaging.destination": f"commands.{request.command_type}",
            "messaging.destination_kind": "channel",
            "messaging.operation": "publish_command",
            "service.name": settings.service_name,
            "command.type": request.command_type
        })

    try:
        command_channel = f"commands.{request.command_type}"
        headers = request.metadata or {}
        if settings.propagate_correlation_id:
            headers["X-Correlation-ID"] = correlation_id

        with traced_span("redis_publish_command", kind="PRODUCER", attributes={
            "correlation_id": correlation_id,
            "messaging.channel": command_channel
        }) as publish_span:
            command_id = await publisher.publish_message(
                channel=command_channel,
                payload=request.payload,
                headers=headers,
                correlation_id=correlation_id
            )
            publish_span.set_attribute("messaging.message_id", command_id)

        return CommandReceipt(
            success=True,
            command_id=command_id,
            timestamp=datetime.utcnow(),
            correlation_id=correlation_id
        )

    except Exception as e:
        logger.error(f"Failed to publish command {request.command_type}: {str(e)}")
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_status(Status(StatusCode.ERROR, str(e)))
            current_span.record_exception(e)
        
        return CommandReceipt(
            success=False,
            command_id="",
            timestamp=datetime.utcnow(),
            correlation_id=correlation_id,
            error=str(e)
        )


# Message publishing endpoints
@app.post("/messaging/publish", response_model=PublishMessageResponse)
@trace_method(name="publish_message", kind="SERVER")
async def publish_message(
    request: PublishMessageRequest,
    publisher: EventPublisher = Depends(get_event_publisher),
    request_obj: Request = None
):
    """Publish a message to a channel."""
    start_time = datetime.utcnow()
    settings = get_settings()
    
    # Extract correlation ID from request or state
    correlation_id = None
    if request_obj:
        if hasattr(request_obj.state, "correlation_id"):
            correlation_id = request_obj.state.correlation_id
        else:
            correlation_id = extract_correlation_id_from_headers(request_obj.headers)
    
    if not correlation_id:
        correlation_id = str(uuid.uuid4())
    
    # Get current span and add detailed attributes
    current_span = trace.get_current_span()
    if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
        # Add message context attributes
        current_span.set_attribute("correlation_id", correlation_id)
        current_span.set_attribute("messaging.system", "redis_pubsub")
        current_span.set_attribute("messaging.destination", request.channel)
        current_span.set_attribute("messaging.destination_kind", "channel")
        current_span.set_attribute("messaging.operation", "publish")
        current_span.set_attribute("service.name", settings.service_name)
        current_span.set_attribute("service.version", settings.version)
        current_span.set_attribute("environment", settings.environment)
        current_span.set_attribute("timestamp.start", start_time.isoformat())
        
        # Add message metadata
        if request.metadata and request.metadata.message_id:
            current_span.set_attribute("messaging.message_id", request.metadata.message_id)
        
        # Calculate size based on payload type
        payload_size = 0
        if isinstance(request.payload, str):
            payload_size = len(request.payload.encode())
        elif isinstance(request.payload, bytes):
            payload_size = len(request.payload)
        else:
            import json
            payload_size = len(json.dumps(request.payload).encode())
            
        current_span.set_attribute("messaging.message_size_bytes", payload_size)
        
        if request.metadata and request.metadata.ttl:
            current_span.set_attribute("messaging.message_ttl", request.metadata.ttl)
    
    try:
        # Calculate payload size for validation
        payload_size = 0
        if isinstance(request.payload, str):
            payload_size = len(request.payload.encode())
        elif isinstance(request.payload, bytes):
            payload_size = len(request.payload)
        else:
            import json
            payload_size = len(json.dumps(request.payload).encode())

        # Validate message size with tracing
        with traced_span("validate_message_size", attributes={
            "correlation_id": correlation_id,
            "messaging.max_size_bytes": publisher.max_message_size,
            "messaging.actual_size_bytes": payload_size
        }) as validation_span:
            if payload_size > publisher.max_message_size:
                validation_span.set_status(Status(StatusCode.ERROR, "Message size exceeds limit"))
                raise HTTPException(
                    status_code=400,
                    detail=f"Message exceeds maximum size of {publisher.max_message_size} bytes"
                )
        
        # Add correlation ID to headers if not present
        headers = {}
        if request.metadata and request.metadata.headers:
            headers.update(request.metadata.headers)
            
        if settings.propagate_correlation_id:
            headers["X-Correlation-ID"] = correlation_id
        
        # Publish message with tracing
        with traced_span("redis_publish_operation", kind="PRODUCER", attributes={
            "correlation_id": correlation_id,
            "messaging.channel": request.channel,
            "messaging.system": "redis_pubsub"
        }) as publish_span:
            publish_start = time.time()
            message_id = await publisher.publish_message(
                channel=request.channel,
                payload=request.payload,
                metadata=request.metadata,
                persistent=request.persistent,
                correlation_id=correlation_id,
                headers=headers
            )
            publish_duration_ms = (time.time() - publish_start) * 1000
            
            # Add publish operation details
            publish_span.set_attribute("messaging.message_id", message_id)
            publish_span.set_attribute("messaging.operation_duration_ms", publish_duration_ms)
        
        # Record successful completion
        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            current_span.set_attribute("success", True)
            current_span.set_attribute("messaging.message_id", message_id)
            current_span.set_status(Status(StatusCode.OK))
        
        return PublishMessageResponse(
            success=True,
            message_id=message_id,
            channel=request.channel,
            timestamp=datetime.utcnow(),
            correlation_id=correlation_id
        )
        
    except Exception as e:
        # Record error details
        end_time = datetime.utcnow()
        duration_ms = (end_time - start_time).total_seconds() * 1000
        
        if current_span and hasattr(current_span, "is_recording") and current_span.is_recording():
            current_span.set_attribute("timestamp.end", end_time.isoformat())
            current_span.set_attribute("duration_ms", duration_ms)
            current_span.set_attribute("error.type", e.__class__.__name__)
            current_span.set_attribute("error.message", str(e))
            current_span.set_attribute("success", False)
            current_span.set_status(Status(StatusCode.ERROR, str(e)))
            current_span.record_exception(e)
        
        logger.error(f"Failed to publish message: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Message publish failed: {str(e)}")


@app.post("/messaging/publish/bulk", response_model=BulkPublishResponse)
@track_endpoint_execution
async def publish_bulk_messages(
    request: BulkPublishRequest,
    publisher: EventPublisher = Depends(get_event_publisher),
    request_obj: Request = None
):
    # Extract correlation ID from request headers or generate new one
    correlation_id = extract_correlation_id(request_obj)
    """Publish multiple messages in bulk."""
    try:
        # Convert request messages to publisher format
        messages = []
        for msg_req in request.messages:
            # Add correlation ID to headers if not present
            headers = {}
            if msg_req.metadata and msg_req.metadata.headers:
                headers.update(msg_req.metadata.headers)
            
            if settings.propagate_correlation_id and correlation_id:
                headers["X-Correlation-ID"] = correlation_id
            
            # Add span attributes for message context
            add_span_attributes({
                "messaging.system": "redis_pubsub",
                "messaging.destination": msg_req.channel,
                "messaging.destination_kind": "channel",
                "messaging.message_id": msg_req.metadata.message_id if msg_req.metadata and msg_req.metadata.message_id else None,
                "correlation_id": correlation_id
            })
            
            # Prepare metadata with headers
            metadata = msg_req.metadata
            if headers and metadata:
                if not metadata.headers:
                    metadata.headers = {}
                metadata.headers.update(headers)
            
            messages.append({
                "channel": msg_req.channel,
                "payload": msg_req.payload,
                "metadata": metadata,
                "persistent": msg_req.persistent,
                "correlation_id": correlation_id
            })
        
        # Publish bulk messages
        result = await publisher.publish_bulk(messages, request.fail_on_error)
        
        # Convert results to response format
        response_results = []
        for i, res in enumerate(result["results"]):
            # Extract correlation_id from result or fallback to request correlation_id
            res_correlation_id = res.get("correlation_id", correlation_id) or str(uuid.uuid4())
            
            response_results.append(PublishMessageResponse(
                success=res["success"],
                message_id=res.get("message_id", ""),
                channel=res.get("channel", ""),
                timestamp=datetime.utcnow(),
                correlation_id=res_correlation_id,
                error=res.get("error")
            ))
        
        return BulkPublishResponse(
            success=result["failed_count"] == 0,
            published_count=result["published_count"],
            failed_count=result["failed_count"],
            results=response_results
        )
        
    except Exception as e:
        logger.error(f"Failed to publish bulk messages: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Bulk publish failed: {str(e)}")

# Event publishing endpoints
@app.post("/messaging/events/publish", response_model=EventResponse)
@app.post("/api/v1/events/publish", response_model=EventResponse)
@track_endpoint_execution
async def publish_event(
    request: EventRequest,
    publisher: EventPublisher = Depends(get_event_publisher),
    request_obj: Request = None
):
    """Publish a structured event."""
    # Extract correlation ID from request headers or generate new one
    correlation_id = extract_correlation_id(request_obj)
    
    try:
        # Initialize headers dictionary
        headers = {}
        # Get headers from the FastAPI request object, not the Pydantic model
        if request_obj and hasattr(request_obj, 'headers'):
            headers = dict(request_obj.headers)
            
        # Add correlation ID to headers if not present
        if settings.propagate_correlation_id and correlation_id:
            headers["X-Correlation-ID"] = correlation_id
        
        # Add span attributes for event context
        add_span_attributes({
            "messaging.system": "redis_pubsub",
            "messaging.destination": request.event_type,
            "messaging.destination_kind": "event",
            "messaging.event_id": str(request.id) if hasattr(request, "id") else None,
            "correlation_id": correlation_id
        })
        
        result = await publisher.publish_event(
            event_type=request.event_type,
            source_service=request.source_service,
            event_data=request.event_data,
            correlation_id=request.correlation_id,
            metadata=request.metadata,
            headers=headers
        )
        
        return EventResponse(
            success=True,
            event_id=result["event_id"],
            event_type=request.event_type,
            published_at=datetime.fromisoformat(result["timestamp"].replace('Z', '+00:00')),
            channels=result["published_channels"]
        )
        
    except Exception as e:
        logger.error(f"Failed to publish event: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Event publish failed: {str(e)}")


# Subscription management endpoints
@app.post("/messaging/subscriptions", response_model=SubscriptionResponse)
@track_endpoint_execution
async def create_subscription(
    request: SubscriptionRequest,
    sub_manager: SubscriptionManager = Depends(get_subscription_manager),
    request_obj: Request = None
):
    """Create a new subscription."""
    # Extract correlation ID from request headers or generate new one
    correlation_id = extract_correlation_id(request_obj)
    
    try:
        # Get headers from the FastAPI request object, not the Pydantic model
        headers = {}
        if request_obj and hasattr(request_obj, 'headers'):
            headers = dict(request_obj.headers)

        # Add correlation ID to headers if not present
        if settings.propagate_correlation_id and correlation_id:
            headers["X-Correlation-ID"] = correlation_id

        # Determine the channel or pattern for subscription
        channel_identifier = request.channel_pattern if request.channel_pattern else request.channel
        if not channel_identifier:
            raise HTTPException(status_code=400, detail="Either channel or channel_pattern must be provided")

        # Add span attributes for subscription context
        add_span_attributes({
            "messaging.system": "redis_pubsub",
            "messaging.destination": channel_identifier,
            "messaging.destination_kind": "subscription",
            "messaging.service": request.service_name,
            "messaging.callback_url": request.callback_url,
            "correlation_id": correlation_id
        })

        subscription_info = await sub_manager.create_subscription(
            channel=request.channel,
            channel_pattern=request.channel_pattern,
            callback_url=request.callback_url,
            service_name=request.service_name,
            filter_criteria=request.filter_criteria,
            headers=headers,
            max_retries=request.max_retries,
            retry_delay=request.retry_delay
        )

        # Note: The subscription manager returns a tuple (subscription_id, created_at, status)
        sub_id, created_at, status = subscription_info

        return SubscriptionResponse(
            success=True,
            subscription_id=sub_id,
            channel=request.channel,
            channel_pattern=request.channel_pattern,
            service_name=request.service_name,
            status=status,
            created_at=created_at,
            error=None
        )
        
    except Exception as e:
        logger.error(f"Failed to create subscription: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Subscription creation failed: {str(e)}")

# ... (rest of the code remains the same)

@app.delete("/messaging/subscriptions/{subscription_id}")
@track_endpoint_execution
async def cancel_subscription(
    subscription_id: str,
    sub_manager: SubscriptionManager = Depends(get_subscription_manager)
):
    """Cancel a subscription."""
    try:
        success = await sub_manager.cancel_subscription(subscription_id)
        if not success:
            raise HTTPException(status_code=404, detail="Subscription not found")
        
        return {"success": True, "subscription_id": subscription_id, "message": "Subscription cancelled"}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to cancel subscription: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Subscription cancellation failed: {str(e)}")


@app.get("/messaging/subscriptions/{subscription_id}", response_model=SubscriptionInfo)
@track_endpoint_execution
async def get_subscription_info(
    subscription_id: str,
    sub_manager: SubscriptionManager = Depends(get_subscription_manager)
):
    """Get subscription information."""
    try:
        info = await sub_manager.get_subscription_info(subscription_id)
        if not info:
            raise HTTPException(status_code=404, detail="Subscription not found")
        
        return SubscriptionInfo(**info)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get subscription info: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to get subscription info: {str(e)}")


@app.get("/messaging/subscriptions", response_model=List[SubscriptionInfo])
@track_endpoint_execution
async def list_subscriptions(
    service_name: Optional[str] = None,
    sub_manager: SubscriptionManager = Depends(get_subscription_manager)
):
    """List all subscriptions, optionally filtered by service."""
    try:
        subscriptions = await sub_manager.list_subscriptions(service_name)
        return [SubscriptionInfo(**sub) for sub in subscriptions]
        
    except Exception as e:
        logger.error(f"Failed to list subscriptions: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to list subscriptions: {str(e)}")


# Message acknowledgment endpoint
@app.post("/messaging/acknowledge", response_model=Dict[str, Any])
@track_endpoint_execution
async def acknowledge_message(
    ack: MessageAcknowledgment,
    sub_manager: SubscriptionManager = Depends(get_subscription_manager),
    request_obj: Request = None
):
    # Extract correlation ID from request headers or generate new one
    correlation_id = extract_correlation_id(request_obj)
    """Acknowledge message processing."""
    try:
        # Add span attributes for acknowledgment context
        add_span_attributes({
            "messaging.system": "redis_pubsub",
            "messaging.subscription_id": ack.subscription_id,
            "messaging.message_id": ack.message_id,
            "correlation_id": correlation_id
        })
        
        await sub_manager.acknowledge_message(
            subscription_id=ack.subscription_id,
            message_id=ack.message_id,
            success=ack.success,
            error=ack.error
        )
        
        return {"success": True, "message_id": ack.message_id, "message": "Message acknowledged"}
        
    except Exception as e:
        logger.error(f"Failed to acknowledge message: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Message acknowledgment failed: {str(e)}")


# Channel information endpoints
@app.get("/messaging/channels/{channel_name}", response_model=ChannelInfo)
@track_endpoint_execution
async def get_channel_info(
    channel_name: str,
    publisher: EventPublisher = Depends(get_event_publisher)
):
    """Get information about a channel."""
    try:
        info = await publisher.get_channel_info(channel_name)
        
        return ChannelInfo(
            name=info["name"],
            subscriber_count=info["subscriber_count"],
            message_count=info["message_count"],
            last_activity=datetime.fromisoformat(info["last_activity"]) if info["last_activity"] else None,
            created_at=datetime.utcnow()  # Placeholder - would need to track this
        )
        
    except Exception as e:
        logger.error(f"Failed to get channel info: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to get channel info: {str(e)}")


# Metrics and monitoring endpoints
@app.get("/messaging/metrics", response_model=MetricsResponse)
@track_endpoint_execution
async def get_metrics(
    publisher: EventPublisher = Depends(get_event_publisher),
    sub_manager: SubscriptionManager = Depends(get_subscription_manager)
):
    """Get messaging service metrics."""
    try:
        # Get publisher metrics
        pub_metrics = await publisher.get_metrics()
        
        # Get subscription manager metrics
        sub_metrics = await sub_manager.get_metrics()
        
        # Combine metrics
        return MetricsResponse(
            service_name="messaging_service",
            timestamp=datetime.utcnow(),
            total_messages_published=pub_metrics["published_count"],
            total_messages_delivered=sub_metrics["total_messages_delivered"],
            total_messages_failed=pub_metrics["failed_count"] + sub_metrics["total_messages_failed"],
            active_subscriptions=sub_metrics["active_subscriptions"],
            active_channels=pub_metrics["active_channels_count"],
            redis_memory_usage=None,  # Would need to get from Redis INFO
            avg_message_size=pub_metrics["avg_message_size"],
            messages_per_second=pub_metrics["messages_per_second"],
            error_rate=pub_metrics["error_rate"]
        )
        
    except Exception as e:
        logger.error(f"Failed to get metrics: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to get metrics: {str(e)}")


@app.get("/messaging/performance/stats")
@track_endpoint_execution
async def get_performance_stats(
    publisher: EventPublisher = Depends(get_event_publisher),
    sub_manager: SubscriptionManager = Depends(get_subscription_manager)
):
    """Get detailed performance statistics."""
    try:
        pub_metrics = await publisher.get_metrics()
        sub_metrics = await sub_manager.get_metrics()
        
        return {
            "publisher": pub_metrics,
            "subscription_manager": sub_metrics,
            "combined": {
                "total_throughput": pub_metrics["messages_per_second"],
                "delivery_success_rate": sub_metrics.get("delivery_rate", 0),
                "overall_error_rate": (
                    (pub_metrics["failed_count"] + sub_metrics["total_messages_failed"]) /
                    max(1, pub_metrics["published_count"] + sub_metrics["total_messages_received"])
                ) * 100
            }
        }
        
    except Exception as e:
        logger.error(f"Failed to get performance stats: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to get performance stats: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    # Enable metrics collection in the service
    settings = get_settings()
    print(f"Starting Messaging Service with metrics enabled: {settings.enable_prometheus_metrics}")
    if settings.enable_prometheus_metrics:
        print(f"Metrics will be exported to: {settings.observability_service_url}")
        if settings.prometheus_push_gateway:
            print(f"Using Prometheus Pushgateway: {settings.prometheus_push_gateway}")
    uvicorn.run(app, host="0.0.0.0", port=8001)
