"""
Machine Learning Service - Manages ML Models, Training Jobs, and Inference.

This service:
- Uses Database Service for metadata persistence (via messaging/CQRS pattern)
- Uses Messaging Service for event publishing (Training Jobs)
- Exposes API for Model Registry and Inference
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Request
from fastapi.middleware.cors import CORSMiddleware
import logging
import time
import uuid
import asyncio
from typing import Dict, Any, Optional
from contextlib import asynccontextmanager
from prometheus_client import make_wsgi_app
from fastapi.middleware.wsgi import WSGIMiddleware

# Import OpenTelemetry modules
from opentelemetry.trace import SpanKind
from .telemetry import initialize_telemetry, instrument_fastapi, extract_correlation_id_from_headers, add_span_attributes, trace_method

from .messaging_client import MessagingClient
from .database_client import DatabaseClient
from .dependencies import set_messaging_client, set_database_client, get_messaging_client, set_service_start_time
from .models import (
    EventCallback, ServiceHealth, DependencyStatus,
    ErrorResponse
)
from .config import get_settings
from .metrics import (
    metrics, update_system_metrics, export_metrics_to_observability
)
from .api.endpoints import router as api_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global service instances
service_start_time = time.time()
metrics_export_task: Optional[asyncio.Task] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global metrics_export_task
    
    messaging_client = None
    database_client = None

    # Startup
    try:
        settings = get_settings()
        
        # Initialize metrics with service info
        metrics.initialize(service_name=settings.service_name)
        
        # Set service start time
        set_service_start_time(time.time())
        
        # Initialize OpenTelemetry if enabled
        if settings.enable_distributed_tracing:
            initialize_telemetry(
                service_name=settings.service_name,
                otlp_endpoint=settings.otlp_endpoint,
                export_interval_ms=15000,
                resource_attributes={
                    "deployment.environment": "development",
                    "service.version": "1.0.0",
                }
            )
            logger.info(f"OpenTelemetry initialized with endpoint: {settings.otlp_endpoint}")
        
        # Initialize messaging client
        messaging_client = MessagingClient(
            base_url=settings.messaging_service_url,
            service_name=settings.service_name,
            timeout=settings.messaging_service_timeout,
            retries=settings.messaging_service_retries
        )
        await messaging_client.initialize()
        set_messaging_client(messaging_client)
        
        # Initialize database client
        database_client = DatabaseClient(
            base_url=settings.database_service_url,
            service_name=settings.service_name,
            timeout=settings.database_service_timeout,
            retries=settings.database_service_retries
        )
        await database_client.initialize()
        set_database_client(database_client)
        
        # Set up event subscriptions if enabled
        if settings.subscribe_to_events:
            await setup_event_subscriptions(messaging_client)
            
        # Set service as ready in metrics
        metrics.service_ready.set(1)
        
        # Start metrics export if enabled
        if settings.enable_prometheus_metrics:
            metrics_export_task = asyncio.create_task(
                start_metrics_export_loop(
                    interval=settings.metrics_push_interval,
                    observability_url=settings.observability_service_url,
                    push_gateway=settings.prometheus_push_gateway,
                    job_name=settings.metrics_export_job_name
                )
            )
        
        # Start system metrics update task
        asyncio.create_task(update_system_metrics_loop())
        
        logger.info("Machine Learning Service started successfully")
        yield
        
    except Exception as e:
        logger.error(f"Failed to start Machine Learning Service: {str(e)}")
        raise
    finally:
        # Shutdown
        # Set service as not ready in metrics
        metrics.service_ready.set(0)
        
        # Cancel metrics export task if running
        if metrics_export_task:
            metrics_export_task.cancel()
            try:
                await metrics_export_task
            except asyncio.CancelledError:
                pass
        
        # We need to access the local variables or get them from dependencies if we want to close them
        # Since we set them in dependencies, we might need a way to get them or just rely on local vars if available
        # But local vars inside try block might not be available here if exception happened before assignment.
        # However, for simplicity using the local variables initialized to None at start of lifespan.
        
        if messaging_client:
            await messaging_client.close()
            
        if database_client:
            await database_client.close()
            
        logger.info("Machine Learning Service shutdown complete")


async def start_metrics_export_loop(interval: int, observability_url: str, push_gateway: str, job_name: str):
    """Start a loop to export metrics to observability service."""
    logger.info(f"Starting metrics export loop with interval {interval} seconds")
    
    while True:
        try:
            # Export metrics to observability service
            await export_metrics_to_observability(
                observability_url=observability_url,
                push_gateway=push_gateway,
                job_name=job_name
            )
            logger.debug("Metrics exported successfully")
        except Exception as e:
            logger.error(f"Failed to export metrics: {str(e)}")
        
        # Wait for next export interval
        await asyncio.sleep(interval)


async def update_system_metrics_loop():
    """Start a loop to update system metrics."""
    logger.info("Starting system metrics update loop")
    
    while True:
        try:
            # Update system metrics (CPU, memory, etc.)
            update_system_metrics()
            # Wait for 15 seconds before next update
            await asyncio.sleep(15)
        except Exception as e:
            logger.error(f"Failed to update system metrics: {str(e)}")
            await asyncio.sleep(30)  # Longer wait on error


@trace_method(name="setup_event_subscriptions", kind=SpanKind.CLIENT)
async def setup_event_subscriptions(messaging_client: MessagingClient):
    """Set up event subscriptions."""
    if not messaging_client:
        return
    
    try:
        settings = get_settings()
        correlation_id = str(uuid.uuid4())
        
        # Add span attributes for subscription setup
        add_span_attributes({
            "messaging.operation": "subscribe",
            "messaging.callback_url": settings.event_callback_url,
            "correlation_id": correlation_id
        })
        
        # Subscribe to relevant events
        
        # 1. Broker Service events (Ping, etc.)
        await messaging_client.subscribe_to_service_events(
            target_service="broker_service",
            callback_url=settings.event_callback_url,
            correlation_id=correlation_id
        )
        
        # 2. Data Ingestion events (to trigger training)
        await messaging_client.create_subscription(
            channel_pattern="events.data.ingestion.*",
            callback_url=settings.event_callback_url,
            correlation_id=correlation_id
        )
        
        # 3. Model Metadata events (for cache invalidation/updates)
        await messaging_client.create_subscription(
            channel_pattern="events.metadata.model.*",
            callback_url=settings.event_callback_url,
            correlation_id=correlation_id
        )
        
        logger.info("Event subscriptions set up successfully")
        
    except Exception as e:
        # Record error in span
        add_span_attributes({
            "error": True,
            "error.message": str(e)
        })
        logger.error(f"Failed to set up event subscriptions: {e}")


# Initialize FastAPI app with lifespan management
app = FastAPI(
    title="Machine Learning Service",
    description="Manages ML Models, Training Jobs, and Inference",
    version="1.0.0",
    lifespan=lifespan
)

# Mount Prometheus metrics endpoint
app.mount("/metrics", WSGIMiddleware(make_wsgi_app()))

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenTelemetry FastAPI instrumentation
settings = get_settings()
if settings.enable_distributed_tracing:
    instrument_fastapi(app)


# Add metrics middleware
@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    """Middleware to track request metrics and propagate trace context."""
    request_id = str(uuid.uuid4())
    start_time = time.time()
    
    # Extract path for metrics (removing specific IDs for better grouping)
    path = request.url.path
    for param in request.path_params:
        path = path.replace(str(request.path_params[param]), f":{param}")
    
    method = request.method
    
    # Extract correlation ID from headers or generate a new one
    correlation_id = extract_correlation_id_from_headers(dict(request.headers))
    
    # Add correlation ID to request state for access in endpoints
    request.state.correlation_id = correlation_id
    
    # Add span attributes for the request
    add_span_attributes({
        "http.method": method,
        "http.path": path,
        "http.request_id": request_id,
        "correlation_id": correlation_id
    })
    
    # Track request start
    metrics.http_requests_in_progress.labels(method=method, path=path).inc()
    
    try:
        response = await call_next(request)
        status_code = response.status_code
        
        # Add correlation ID to response headers
        response.headers["X-Correlation-ID"] = correlation_id
        
        # Add span attributes for the response
        add_span_attributes({
            "http.status_code": status_code
        })
        
        # Track request success
        if 200 <= status_code < 400:
            metrics.request_success.labels(method=method, path=path).inc()
        elif 400 <= status_code < 500:
            metrics.request_client_errors.labels(method=method, path=path).inc()
        else:
            metrics.request_server_errors.labels(method=method, path=path).inc()
            
        return response
    except Exception as e:
        # Track request exception
        metrics.request_exceptions.labels(method=method, path=path).inc()
        logger.error(f"Request {request_id} failed: {str(e)}")
        # Track exceptions
        metrics.http_exceptions_total.labels(
            method=method, path=path, exception_type=type(e).__name__
        ).inc()
        raise


def get_messaging_client() -> MessagingClient:
    """Dependency to get messaging client instance."""
    if messaging_client is None:
        raise HTTPException(status_code=503, detail="Messaging client not initialized")
    return messaging_client


# Include API router
app.include_router(api_router)


# Event handling endpoints
@app.post("/events/callback")
@trace_method(name="handle_event_callback", kind=SpanKind.CONSUMER)
async def handle_event_callback(
    event: EventCallback,
    request: Request,
    background_tasks: BackgroundTasks,
    msg_client: MessagingClient = Depends(get_messaging_client)
):
    """Handle incoming event callbacks."""
    try:
        # Extract correlation ID from headers or payload
        correlation_id = extract_correlation_id_from_headers(request.headers)
        
        # If no correlation ID in headers, try to get it from payload or metadata
        if not correlation_id:
            if isinstance(event.payload, dict) and "correlation_id" in event.payload:
                correlation_id = event.payload.get("correlation_id")
            elif "correlation_id" in event.metadata:
                correlation_id = event.metadata.get("correlation_id")
            else:
                # Generate a new correlation ID if none exists
                correlation_id = str(uuid.uuid4())
        
        # Add span attributes for event callback
        add_span_attributes({
            "messaging.operation": "callback",
            "messaging.subscription_id": event.subscription_id,
            "messaging.message_id": event.message_id,
            "messaging.channel": event.channel,
            "messaging.delivery_attempt": event.delivery_attempt,
            "correlation_id": correlation_id
        })
        
        logger.info(f"Received event callback: {event.message_id} from channel {event.channel}")
        
        # Process the event based on its type
        success = await process_event(event)
        
        # Acknowledge the message with correlation ID
        background_tasks.add_task(
            acknowledge_event_message,
            msg_client,
            event.subscription_id,
            event.message_id,
            success,
            None,  # No error
            correlation_id
        )
        
        return {"success": True, "message": "Event processed successfully"}
        
    except Exception as e:
        logger.error(f"Failed to handle event callback: {str(e)}")
        
        # Try to get correlation ID even in error case
        correlation_id = None
        try:
            correlation_id = extract_correlation_id_from_headers(request.headers)
            if not correlation_id and isinstance(event.payload, dict):
                correlation_id = event.payload.get("correlation_id")
            if not correlation_id:
                correlation_id = event.metadata.get("correlation_id")
        except:
            # If we can't get correlation ID, continue without it
            pass
        
        # Acknowledge with error and correlation ID if available
        background_tasks.add_task(
            acknowledge_event_message,
            msg_client,
            event.subscription_id,
            event.message_id,
            False,
            str(e),
            correlation_id
        )
        
        # Add error to span
        add_span_attributes({
            "error": True,
            "error.message": str(e)
        })
        
        raise HTTPException(status_code=500, detail=f"Event processing failed: {str(e)}")


@trace_method(name="acknowledge_event_message", kind=SpanKind.CLIENT)
async def acknowledge_event_message(
    msg_client: MessagingClient,
    subscription_id: str,
    message_id: str,
    success: bool,
    error: Optional[str] = None,
    correlation_id: Optional[str] = None
):
    """Background task to acknowledge event message."""
    try:
        # Add span attributes for message acknowledgment
        add_span_attributes({
            "messaging.operation": "acknowledge",
            "messaging.subscription_id": subscription_id,
            "messaging.message_id": message_id,
            "messaging.success": success,
            "correlation_id": correlation_id
        })
        
        if error:
            add_span_attributes({
                "error": True,
                "error.message": error
            })
            
        await msg_client.acknowledge_message(
            subscription_id=subscription_id,
            message_id=message_id,
            success=success,
            error=error,
            correlation_id=correlation_id
        )
        logger.debug(f"Acknowledged message {message_id}")
    except Exception as e:
        # Record error in span
        add_span_attributes({
            "error": True,
            "error.message": str(e)
        })
        logger.error(f"Failed to acknowledge message {message_id}: {e}")


@trace_method(name="process_event", kind=SpanKind.CONSUMER)
async def process_event(event: EventCallback) -> bool:
    """Process an incoming event."""
    try:
        # Extract event data
        payload = event.payload
        
        # Extract correlation ID from payload or metadata
        correlation_id = None
        if isinstance(payload, dict) and "correlation_id" in payload:
            correlation_id = payload.get("correlation_id")
        elif "correlation_id" in event.metadata:
            correlation_id = event.metadata.get("correlation_id")
        
        # Extract event type if available
        event_type = None
        if isinstance(payload, dict):
            event_type = payload.get("event_type")
        
        # Add span attributes for event processing
        add_span_attributes({
            "messaging.operation": "consume",
            "messaging.event_type": event_type,
            "messaging.subscription_id": event.subscription_id,
            "messaging.message_id": event.message_id,
            "messaging.channel": event.channel,
            "correlation_id": correlation_id
        })
        # Process the event based on the extracted event type
        if isinstance(payload, dict):
            if not event_type:
                event_type = payload.get("event_type")
                
            event_data = payload.get("event_data", {})
            
            # Ensure correlation ID is propagated in event data
            if correlation_id and isinstance(event_data, dict) and "correlation_id" not in event_data:
                event_data["correlation_id"] = correlation_id
            
            logger.info(f"Processing event type: {event_type}")
            
            # Handle specific event types for ML service
            if event_type == "broker_service.ping":
                # Heartbeat or keepalive
                return True
            
            elif event_type == "data.ingestion.completed":
                # Trigger training job if configured
                logger.info(f"Data ingestion completed event received: {event_data}")
                # Logic to determine if auto-training should start would go here
                # e.g., check if dataset is linked to any active models with auto-train enabled
                return True

            elif event_type == "metadata.model.updated":
                # Update local cache or invalidate
                logger.info(f"Model metadata updated event received: {event_data}")
                # If we had an in-memory cache for models, we would invalidate it here
                return True
            
            logger.warning(f"Unknown or unhandled event type: {event_type}")
            return True  # Acknowledge unknown events to avoid reprocessing
        
        return True
        
    except Exception as e:
        logger.error(f"Failed to process event: {e}")
        return False


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
