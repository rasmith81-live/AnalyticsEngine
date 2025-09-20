"""
Archival Service - Main Application

This service subscribes to archival events from the Database Service via Redis,
processes data archival requests, and stores data in a lakehouse format.
"""
import asyncio
import logging
import os
import uuid
import time
from datetime import datetime
from typing import Dict, Any, List, Optional

import uvicorn
from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import PlainTextResponse
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel, Field
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from opentelemetry import trace
from opentelemetry.trace import Status, StatusCode

from .telemetry import extract_correlation_id_from_headers
from app.config import settings
from app.management import get_archival_manager, close_archival_manager
from .tasks import start_scheduled_tasks, stop_scheduled_tasks, get_task_manager
from .state import archival_events
from app.models import (
    ArchivalEvent, 
    ArchivalConfirmation, 
    ArchivalStatus,
    HealthResponse
)
from app.metrics import metrics, update_system_metrics, export_metrics_to_observability, track_endpoint_execution, track_archival_operation, track_storage_operation, track_redis_operation
from app.telemetry import initialize_telemetry, instrument_fastapi, extract_correlation_id, add_span_attributes, trace_method, traced_span
from app.messaging_client import MessagingClient
from app.lakehouse_client import LakehouseClient
from . import state

# Import API endpoints
from app.api import monitoring_endpoints, management_endpoints, dashboard_endpoints
from .state import archival_events

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Archival Service",
    description="Service for archiving TimescaleDB data to a lakehouse",
    version="1.0.0"
)

# Initialize OpenTelemetry if enabled
if settings.enable_distributed_tracing:
    try:
        # Initialize telemetry with service info
        initialize_telemetry(
            service_name=settings.service_name,
            otlp_endpoint=settings.otlp_endpoint,
            resource_attributes={
                "deployment.environment": os.getenv("ENVIRONMENT", "development"),
                "service.instance.id": str(uuid.uuid4())[:8],
            },
            trace_sample_rate=settings.trace_sample_rate,
            export_interval_ms=15000
        )
        
        # Instrument FastAPI
        instrument_fastapi(app)
        
        logger.info("OpenTelemetry distributed tracing initialized")
    except Exception as e:
        logger.error(f"Failed to initialize OpenTelemetry: {e}")

# Middleware to extract and propagate correlation IDs
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
        current_span.set_attribute("service.name", "archival_service")
        current_span.set_attribute("environment", settings.environment)
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

# Prometheus metrics task references
system_metrics_task = None
metrics_export_task = None

# Track service start time for uptime calculation
service_start_time = datetime.utcnow()

# Include API endpoint routers
app.include_router(monitoring_endpoints.router, prefix="/api/v1/monitoring")
app.include_router(management_endpoints.router, prefix="/api/v1/management")
app.include_router(dashboard_endpoints.router, prefix="/api/v1/dashboard")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add GZip compression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Global service instances
state.messaging_client = MessagingClient(
    redis_url=settings.redis_url,
    service_name=settings.service_name
)

# Prometheus middleware for HTTP request metrics
class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Skip metrics endpoint to avoid recursion
        if request.url.path == "/metrics":
            return await call_next(request)
            
        method = request.method
        path = request.url.path
        begin = time.time()
        
        # Track request count
        metrics.http_requests_total.labels(method=method, path=path).inc()
        metrics.slo_request_total.labels(path=path).inc()
        
        try:
            response = await call_next(request)
            duration = time.time() - begin
            status_code = response.status_code
            
            # Track request duration
            metrics.http_request_duration_seconds.labels(
                method=method, path=path, status_code=status_code
            ).observe(duration)
            
            # Track SLO metrics
            if 200 <= status_code < 400:
                metrics.slo_request_success_total.labels(path=path).inc()
                if duration < 1.0:  # 1 second SLO threshold
                    metrics.slo_request_latency_met_total.labels(path=path).inc()
                    
            return response
        except Exception as e:
            # Track exceptions
            metrics.http_exceptions_total.labels(
                method=method, path=path, exception_type=type(e).__name__
            ).inc()
            raise

# Add Prometheus middleware if metrics are enabled
if settings.enable_prometheus_metrics:
    app.add_middleware(PrometheusMiddleware)


@app.get("/health", response_model=HealthResponse)
@track_endpoint_execution
@trace_method(name="archival_service.health_check", kind="SERVER")
async def health_check(request: Request):
    """Health check endpoint with comprehensive distributed tracing."""
    # Extract correlation ID from headers or generate a new one
    correlation_id = extract_correlation_id(request) or str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/health",
        "service": "archival_service",
        "timestamp.start": start_time.isoformat(),
        "environment": settings.environment
    })
    
    try:
        # Get task manager health status
        task_manager = get_task_manager()
        health_status = await task_manager.get_health_status()
        
        # Check Redis connection with tracing
        redis_status = await check_redis_connection()
        
        # Check lakehouse connection with tracing
        lakehouse_status = await check_lakehouse_connection()
        
        # Get active archival events count with tracing
        active_events = await get_active_events_count()
        
        # Build comprehensive health response
        response_data = {
            "status": "healthy" if all([health_status.get("status") == "healthy", redis_status, lakehouse_status]) else "unhealthy",
            "messaging_connected": redis_status,
            "lakehouse_connected": lakehouse_status,
            "active_archival_events": active_events,
            "service": {
                "name": "archival_service",
                "version": settings.version,
                "environment": settings.environment,
                "uptime_seconds": (datetime.utcnow() - service_start_time).total_seconds() if 'service_start_time' in globals() else 0
            },
            "components": {
                "task_manager": health_status.get("services", {})
            },
            "timestamp": datetime.utcnow().isoformat(),
            "correlation_id": correlation_id
        }
        
        # Update health metrics
        if response_data["status"] == "healthy":
            metrics.service_health.set(1)
        else:
            metrics.service_health.set(0)
        
        # Add span attributes for response
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "health.status": response_data["status"],
            "health.redis_connected": redis_status,
            "health.lakehouse_connected": lakehouse_status,
            "health.active_events": active_events,
            "success": True
        })
        
        return response_data
        
    except Exception as e:
        # Add span attributes for error
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "health.status": "unhealthy",
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        
        logger.error(f"Health check failed: {str(e)}", exc_info=True)
        # Return a valid HealthResponse model even on failure to avoid validation errors
        return HealthResponse(
            status="unhealthy",
            messaging_connected=False,
            lakehouse_connected=False,
            active_archival_events=0,
            timestamp=datetime.utcnow(),
            monitoring_health={"status": "unknown", "details": "Could not retrieve monitoring health"},
            management_health={"status": "unknown", "details": str(e)}
        )

@app.get("/metrics")
async def metrics_endpoint():
    """Expose Prometheus metrics."""
    return PlainTextResponse(generate_latest(), media_type=CONTENT_TYPE_LATEST)



# Global service instances
archival_manager = None
monitor = None
task_manager = None

# Background task for updating system metrics periodically
@trace_method(name="update_system_metrics_periodically", kind="INTERNAL")
async def update_system_metrics_periodically():
    """Update system metrics every 15 seconds."""
    while True:
        try:
            # Create a child span for each metrics update
            async with traced_span("update_metrics", kind="INTERNAL", attributes={
                "metrics.update_type": "system",
                "metrics.timestamp": datetime.utcnow().isoformat()
            }):
                update_system_metrics()
            await asyncio.sleep(settings.metrics_update_interval)
        except Exception as e:
            logger.error(f"Error updating system metrics: {e}")
            # Add error attributes to the span
            add_span_attributes({
                "error": True,
                "error.type": type(e).__name__,
                "error.message": str(e)
            })
            await asyncio.sleep(5)  # Retry after 5 seconds on error

# Background task for exporting metrics periodically
@trace_method(name="export_metrics_periodically", kind="INTERNAL")
async def export_metrics_periodically():
    """Export metrics to Observability Service and Pushgateway every 15 seconds."""
    while True:
        try:
            # Create a child span for each metrics export
            async with traced_span("export_metrics", kind="CLIENT", attributes={
                "metrics.export_type": "observability_service",
                "metrics.destination": settings.observability_service_url,
                "metrics.timestamp": datetime.utcnow().isoformat()
            }):
                await export_metrics_to_observability(
                    observability_url=settings.observability_service_url,
                    push_gateway=settings.prometheus_push_gateway,
                    job_name=settings.metrics_export_job_name
                )
            await asyncio.sleep(settings.metrics_push_interval)
        except Exception as e:
            logger.error(f"Error exporting metrics: {e}")
            # Add error attributes to the span
            add_span_attributes({
                "error": True,
                "error.type": type(e).__name__,
                "error.message": str(e)
            })
            await asyncio.sleep(5)  # Retry after 5 seconds on error
            await asyncio.sleep(settings.metrics_push_interval)

@app.on_event("startup")
@trace_method(name="startup_event", kind="INTERNAL")
async def startup_event():
    """Initialize service on startup."""
    global archival_manager, system_metrics_task, metrics_export_task
    
    logger.info("Starting Archival Service")
    
    # Add span attributes for startup context
    add_span_attributes({
        "service.name": settings.service_name,
        "service.version": "1.0.0",
        "service.environment": os.getenv("ENVIRONMENT", "development"),
        "service.instance_id": str(uuid.uuid4())[:8],
        "startup.timestamp": datetime.utcnow().isoformat()
    })
    
    
    # Initialize messaging client
    messaging_client = MessagingClient(
        redis_url=settings.redis_url,
        service_name=settings.service_name
    )
    await messaging_client.connect()
    
    # Store client in state for access in other modules
    state.messaging_client = messaging_client

    if settings.enable_prometheus_metrics:
        metrics.initialize(settings.service_name)
        metrics.service_ready.set(0)
        logger.info(f"Prometheus metrics initialized for {settings.service_name}")
        logger.info(f"Metrics will be exported to: {settings.observability_service_url}")
    
    # Subscribe to archival events
    await messaging_client.subscribe(
        topic="archival.events",
        callback=handle_archival_event,
        service_name="archival_service"
    )
    
    # Initialize monitoring
    from app.api.monitoring_endpoints import get_monitor
    monitor = get_monitor()
    logger.info("Monitoring system initialized")
    
    # Initialize archival manager
    global archival_manager
    archival_manager = get_archival_manager(
        database_service_url=settings.database_service_url,
        archival_service_url=f"http://{settings.host}:{settings.port}"
    )
    logger.info("Archival Manager initialized")
    
    # Start scheduled tasks
    await start_scheduled_tasks()
    
    # Start metrics background tasks if enabled
    if settings.enable_prometheus_metrics:
        system_metrics_task = asyncio.create_task(update_system_metrics_periodically())
        metrics_export_task = asyncio.create_task(export_metrics_periodically())
        metrics.service_ready.set(1)
        metrics.service_health.set(1)
    
    logger.info("Archival Service started successfully")
    
    logger.info("Archival Service started")

@app.on_event("shutdown")
@trace_method(name="shutdown_event", kind="INTERNAL")
async def shutdown_event():
    """Clean up resources on shutdown."""
    global system_metrics_task, metrics_export_task
    
    # Add span attributes for shutdown context
    add_span_attributes({
        "service.name": settings.service_name,
        "shutdown.timestamp": datetime.utcnow().isoformat(),
        "shutdown.reason": "application_termination"
    })
    
    # Update service readiness metric
    if settings.enable_prometheus_metrics:
        metrics.service_ready.set(0)
        metrics.service_health.set(0)
    
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
    
    # Stop scheduled tasks
    await stop_scheduled_tasks()
    
    # Close archival manager
    await close_archival_manager()
    
    # Close messaging client
    if state.messaging_client:
        await state.messaging_client.disconnect()

@track_redis_operation(operation_name="handle_event")
@trace_method(name="handle_archival_event", kind="CONSUMER")
async def handle_archival_event(message: Dict[str, Any]):
    """Handle archival events from the Database Service.
    
    Args:
        message: The archival event message
    """
    try:
        # Parse event data
        event = ArchivalEvent(**message["data"])
        event_id = message.get("id", str(uuid.uuid4()))
        correlation_id = message.get("correlation_id") or message.get("metadata", {}).get("correlation_id")
        
        # Add span attributes for event context
        add_span_attributes({
            "event_id": event_id,
            "correlation_id": correlation_id or "not_provided",
            "table_name": event.table_name,
            "chunk_count": len(event.chunks)
        })
        
        # Store event
        archival_events[event_id] = {
            "event": event,
            "status": "received",
            "started_at": datetime.utcnow().isoformat(),
            "completed_at": None,
            "error": None
        }
        
        logger.info(f"Received archival event {event_id} for table {event.table_name}")
        
        # Process event in background
        asyncio.create_task(process_archival(event_id))
    except Exception as e:
        logger.error(f"Error handling archival event: {str(e)}")

@trace_method(name="process_archival", kind="INTERNAL")
async def process_archival(event_id: str):
    """Process an archival event.
    
    Args:
        event_id: The ID of the event to process
    """
    # Get event data
    if event_id not in archival_events:
        logger.error(f"Event {event_id} not found")
        return
        
    # Add span attributes for archival context
    add_span_attributes({
        "event_id": event_id,
        "archival_operation": "process"
    })
    
    tracking = archival_events[event_id]
    event = tracking["event"]
    
    try:
        # Update status
        tracking["status"] = "processing"
        
        # Extract table and chunk information
        table_name = event.table_name
        chunks = event.chunks
        
        # Define the lakehouse path
        current_date = datetime.utcnow().strftime("%Y/%m/%d")
        lakehouse_path = f"timescaledb_archive/{table_name}/{current_date}/{event_id}"
        
        # Process each chunk
        for chunk in chunks:
            # Extract chunk data from TimescaleDB
            chunk_data = await extract_chunk_data(table_name, chunk)
            
            # Write to lakehouse in Delta or Parquet format
            from app.clients import lakehouse_client
            chunk_name = chunk.get("chunk_name", f"chunk_{uuid.uuid4()}")
            await lakehouse_client.write_data(
                path=f"{lakehouse_path}/{chunk_name}",
                data=chunk_data,
                format="parquet"
            )
        
        # Update tracking
        tracking["status"] = "completed"
        tracking["completed_at"] = datetime.utcnow().isoformat()
        
        # Send confirmation to Database Service
        await send_archival_confirmation(
            event_id=event_id,
            status="success",
            lakehouse_path=lakehouse_path
        )
        
        logger.info(f"Completed archival event {event_id} for table {table_name}")
        
    except Exception as e:
        # Update tracking with error
        tracking["status"] = "failed"
        tracking["completed_at"] = datetime.utcnow().isoformat()
        tracking["error"] = str(e)
        
        # Send failure confirmation
        await send_archival_confirmation(
            event_id=event_id,
            status="failed",
            error_message=str(e)
        )
        
        logger.error(f"Error processing archival event {event_id}: {e}", exc_info=True)

@track_archival_operation(operation_name="extract_chunk_data")
@trace_method(name="extract_chunk_data", kind="CLIENT")
async def extract_chunk_data(table_name: str, chunk: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Extract data from a TimescaleDB chunk.
    
    Args:
        table_name: Name of the table
        chunk: Chunk metadata
        
    Returns:
        List of data records from the chunk
    """
    # In a real implementation, this would query the database
    # For this example, we'll simulate data extraction
    
    # Simulate database query delay
    await asyncio.sleep(0.5)
    
    # Generate sample data
    data = [
        {"id": i, "value": f"data_{i}", "timestamp": datetime.utcnow().isoformat()}
        for i in range(100)
    ]
    
    # Record data size in metrics
    data_size = len(data) * 100  # Rough estimate of bytes
    metrics.archival_data_size_bytes.labels(table_name=table_name).observe(data_size)
    
    return data

@track_redis_operation(operation_name="send_confirmation")
@trace_method(name="send_archival_confirmation", kind="PRODUCER")
async def send_archival_confirmation(
    event_id: str, 
    status: str,
    lakehouse_path: Optional[str] = None,
    error_message: Optional[str] = None
):
    """Send archival confirmation to the Database Service.
    
    Args:
        event_id: The ID of the processed event
        status: The final status of the archival
        lakehouse_path: Optional path where data was archived
        error_message: Optional error message if archival failed
    """
    if event_id not in archival_events:
        logger.error(f"Event {event_id} not found for confirmation")
        return
    
    event = archival_events[event_id]["event"]
    
    confirmation = ArchivalConfirmation(
        confirmation_id=str(uuid.uuid4()),
        event_id=event_id,
        table_name=event.table_name,
        schema_name=event.schema_name,
        chunk_id=event.chunk_id,
        status=status,
        lakehouse_path=lakehouse_path,
        error_message=error_message,
        processed_at=datetime.utcnow().isoformat()
    )
    
    # Update metrics based on status
    if status == "success":
        metrics.archival_operations_success.labels(
            operation="complete_archival", table_name=event.table_name
        ).inc()
    else:
        metrics.archival_operations_failed.labels(
            operation="complete_archival", 
            table_name=event.table_name,
            error_type="ArchivalError" if not error_message else "UnknownError"
        ).inc()
    
    # Publish confirmation event
    await messaging_client.publish_event(
        topic="archival.confirmations",
        event_type="data.archival.completed",
        payload=confirmation.model_dump(),
        service_name="archival_service"
    )


@app.get("/api/v1/archival/events")
@track_endpoint_execution
@trace_method(name="list_archival_events", kind="SERVER")
async def list_archival_events():
    """List all archival events.
    
    Returns:
        List of archival events
    """
    return {
        "events": [
            {
                "event_id": event_id,
                "table_name": data["event"].table_name,
                "status": data["status"],
                "started_at": data["started_at"],
                "completed_at": data["completed_at"],
                "error": data["error"]
            }
            for event_id, data in archival_events.items()
        ]
    }

@app.get("/api/v1/archival/events/{event_id}")
@track_endpoint_execution
@trace_method(name="get_archival_event", kind="SERVER")
async def get_archival_event(event_id: str, request: Request):
    # Add correlation ID and event ID to span attributes
    add_span_attributes({
        "correlation_id": getattr(request.state, "correlation_id", "unknown"),
        "event_id": event_id
    })
    """Get details of a specific archival event.
    
    Args:
        event_id: ID of the event to retrieve
        
    Returns:
        Details of the archival event
    """
    if event_id not in archival_events:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")
    
    data = archival_events[event_id]
    return {
        "event_id": event_id,
        "table_name": data["event"].table_name,
        "status": data["status"],
        "started_at": data["started_at"],
        "completed_at": data["completed_at"],
        "error": data["error"],
        "chunks": data["event"].chunks
    }

@trace_method(name="check_redis_connection", kind="CLIENT")
async def check_redis_connection() -> bool:
    if not state.messaging_client:
        return False
    """Check if Redis connection is healthy.
    
    Returns:
        True if connection is healthy, False otherwise
    """
    try:
        # Add span attributes for connection check context
        add_span_attributes({
            "connection.type": "redis",
            "connection.url": settings.redis_url.split("@")[-1]  # Remove credentials if present
        })
        
        await state.messaging_client.ping()
        
        # Add success span attributes
        add_span_attributes({
            "connection.status": "connected",
            "connection.latency_ms": 0  # Would be measured in a real implementation
        })
        
        return True
    except Exception as e:
        logger.error(f"Redis connection check failed: {e}")
        
        # Add error span attributes
        add_span_attributes({
            "connection.status": "failed",
            "error.type": type(e).__name__,
            "error.message": str(e)
        })
        
        return False

@trace_method(name="check_lakehouse_connection", kind="CLIENT")
async def check_lakehouse_connection() -> bool:
    """Check if Lakehouse connection is healthy.
    
    Returns:
        True if connection is healthy, False otherwise
    """
    try:
        # Add span attributes for connection check context
        add_span_attributes({
            "connection.type": "lakehouse",
            "connection.storage_account": settings.storage_account,
            "connection.container": settings.container_name
        })
        
        # In a real implementation, this would check the connection
        # For this example, we'll simulate a connection check
        await asyncio.sleep(0.1)
        
        # Add success span attributes
        add_span_attributes({
            "connection.status": "connected",
            "connection.latency_ms": 100  # Simulated latency
        })
        
        return True
    except Exception as e:
        logger.error(f"Lakehouse connection check failed: {e}")
        
        # Add error span attributes
        add_span_attributes({
            "connection.status": "failed",
            "error.type": type(e).__name__,
            "error.message": str(e)
        })
        
        return False

@trace_method(name="get_active_events_count", kind="INTERNAL")
async def get_active_events_count() -> int:
    """Get count of active archival events.
    
    Returns:
        Count of active events
    """
    try:
        # Calculate active events (those in received or processing state)
        count = len([e for e in archival_events.values() if e["status"] in ["received", "processing"]])
        
        # Add span attributes for event count context
        add_span_attributes({
            "archival.active_events_count": count,
            "archival.total_events_count": len(archival_events)
        })
        
        return count
    except Exception as e:
        logger.error(f"Error getting active events count: {e}")
        
        # Add error span attributes
        add_span_attributes({
            "error.type": type(e).__name__,
            "error.message": str(e)
        })
        
        return 0

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
