"""
Service A - Business logic service demonstrating CQRS and event-driven architecture.

This service:
- Uses Database Service for all CQRS operations
- Uses Messaging Service for event publishing and subscription
- Implements business logic for item management
- Demonstrates real-time processing and analytics
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Request, Response
from fastapi.middleware.cors import CORSMiddleware
import logging
import time
import uuid
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
from contextlib import asynccontextmanager
from prometheus_client import make_wsgi_app
from fastapi.middleware.wsgi import WSGIMiddleware

# Import OpenTelemetry modules
from opentelemetry.trace import SpanKind
from .telemetry import initialize_telemetry, instrument_fastapi, extract_correlation_id_from_headers, add_span_attributes, trace_method

from .messaging_client import MessagingClient
from .models import (
    ItemCreate, ItemUpdate, ItemResponse, ItemListResponse, ItemAnalytics,
    ItemMetrics, ItemEvent, EventCallback, ServiceHealth, DependencyStatus,
    ErrorResponse, ValidationErrorResponse
)
from .config import get_settings
from .metrics import (
    metrics, track_endpoint_execution, track_message_processing, 
    track_db_operation, track_domain_event, update_system_metrics,
    update_db_connection_metrics, export_metrics_to_observability
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global service instances
messaging_client: Optional[MessagingClient] = None
service_start_time = time.time()
metrics_export_task: Optional[asyncio.Task] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global messaging_client, metrics_export_task
    
    # Startup
    try:
        settings = get_settings()
        
        # Initialize metrics with service info
        metrics.initialize(service_name=settings.service_name)
        
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
        
        # Set up event subscriptions if enabled
        if settings.subscribe_to_events:
            await setup_event_subscriptions()
            
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
        
        logger.info("Service B started successfully")
        yield
        
    except Exception as e:
        logger.error(f"Failed to start Service B: {str(e)}")
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
        
        if messaging_client:
            await messaging_client.close()
        logger.info("Service B shutdown complete")


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
async def setup_event_subscriptions():
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
        
        # Subscribe to item events from other services
        await messaging_client.subscribe_to_item_events(
            callback_url=settings.event_callback_url,
            correlation_id=correlation_id
        )
        
        # Subscribe to service A events for cross-service communication
        await messaging_client.subscribe_to_service_events(
            target_service="service_a",
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
    title="Service B",
    description="Business logic service demonstrating CQRS and event-driven architecture",
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


# Health check endpoint
@app.get("/health", response_model=ServiceHealth, responses={503: {"model": ErrorResponse}})
@track_endpoint_execution
@trace_method(name="health_check_endpoint", kind=SpanKind.SERVER)
async def health_check(
    msg_client: MessagingClient = Depends(get_messaging_client),
    request: Request = None
):
    """Check service health and dependencies."""
    try:
        correlation_id = getattr(request.state, "correlation_id", None) if request else None
        add_span_attributes({"endpoint": "health", "correlation_id": correlation_id})

        dependencies = []
        
        # Check messaging service
        try:
            start_time_ms = time.time()
            msg_health = await msg_client.check_health()
            response_time_ms = (time.time() - start_time_ms) * 1000
            msg_connected = msg_health.get("status") == "healthy"
            dependencies.append(DependencyStatus(
                service_name="messaging_service",
                url=msg_client.base_url,
                status="healthy" if msg_connected else "unhealthy",
                response_time_ms=response_time_ms,
                last_check=datetime.utcnow(),
                error=msg_health.get("error")
            ))
        except Exception as e:
            dependencies.append(DependencyStatus(
                service_name="messaging_service",
                url=msg_client.base_url,
                status="unhealthy",
                response_time_ms=0,
                last_check=datetime.utcnow(),
                error=str(e)
            ))

        # Get active subscriptions count
        active_subscriptions = 0
        try:
            subscriptions = await msg_client.list_subscriptions()
            active_subscriptions = len([s for s in subscriptions if s.get("status") == "active"])
        except Exception as e:
            logger.error(f"Could not retrieve subscriptions for health check: {e}")

        # Determine overall status
        all_deps_healthy = all(dep.status == "healthy" for dep in dependencies)
        overall_status = "healthy" if all_deps_healthy else "unhealthy"
        
        # Update service health metric
        metrics.service_health.set(1 if overall_status == "healthy" else 0)
        
        uptime = time.time() - service_start_time
        
        return ServiceHealth(
            status=overall_status,
            timestamp=datetime.utcnow(),
            dependencies=dependencies,
            active_subscriptions=active_subscriptions,
            uptime_seconds=uptime,
            version="1.0.0",
            error=None if overall_status == "healthy" else "One or more dependencies are unhealthy"
        )
        
    except Exception as e:
        logger.error(f"Health check failed catastrophically: {str(e)}")
        raise HTTPException(status_code=503, detail=f"Service unhealthy: {str(e)}")


# Item management endpoints
@app.post("/items", status_code=202)
@trace_method(name="create_item_endpoint", kind=SpanKind.SERVER)
async def create_item(
    item: ItemCreate,
    background_tasks: BackgroundTasks,
    msg_client: MessagingClient = Depends(get_messaging_client),
    request: Request = None
):
    """Create a new item."""
    try:
        # Get correlation ID from request state or generate a new one
        correlation_id = getattr(request.state, "correlation_id", None) if request else None
        if not correlation_id:
            correlation_id = str(uuid.uuid4())
        
        # Add span attributes for item creation
        add_span_attributes({
            "endpoint": "create_item",
            "correlation_id": correlation_id,
            "item_type": item.item_type if hasattr(item, "item_type") else "unknown"
        })
        
        # Publish a command to create the item
        background_tasks.add_task(
            msg_client.publish_command,
            command_type="CreateItemCommand",
            payload=item.dict(),
            correlation_id=correlation_id
        )
        
        logger.info(f"Published CreateItemCommand with correlation ID {correlation_id}")
        return {"message": "Create item command received", "correlation_id": correlation_id}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to create item: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/items/{item_id}", response_model=ItemResponse, status_code=501)
@trace_method(name="get_item_endpoint", kind=SpanKind.SERVER)
async def get_item(item_id: int):
    """Get an item by ID."""
    try:
        # Get correlation ID from request state or generate a new one
        correlation_id = getattr(request.state, "correlation_id", None) if request else None
        
        # Add span attributes for item retrieval
        add_span_attributes({
            "endpoint": "get_item",
            "item.id": item_id,
            "correlation_id": correlation_id
        })
        
        # This endpoint is not implemented in a pure event-driven model.
        # Service A should maintain its own read model populated by events.
        raise HTTPException(status_code=501, detail="Not Implemented: Service A does not support synchronous queries.")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.put("/items/{item_id}", status_code=202)
async def update_item(
    item_id: int,
    item_update: ItemUpdate,
    background_tasks: BackgroundTasks,
    msg_client: MessagingClient = Depends(get_messaging_client)
):
    """Update an existing item."""
    try:
        correlation_id = str(uuid.uuid4())
        
        # Publish a command to update the item
        payload = {"item_id": item_id, "update_data": item_update.dict(exclude_unset=True)}
        background_tasks.add_task(
            msg_client.publish_command,
            command_type="UpdateItemCommand",
            payload=payload,
            correlation_id=correlation_id
        )

        logger.info(f"Published UpdateItemCommand for item {item_id} with correlation ID {correlation_id}")
        return {"message": "Update item command received", "correlation_id": correlation_id}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to update item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.delete("/items/{item_id}", status_code=202)
async def delete_item(
    item_id: int,
    background_tasks: BackgroundTasks,
    msg_client: MessagingClient = Depends(get_messaging_client)
):
    """Delete an item."""
    try:
        correlation_id = str(uuid.uuid4())
        
        # Publish a command to delete the item
        payload = {"item_id": item_id}
        background_tasks.add_task(
            msg_client.publish_command,
            command_type="DeleteItemCommand",
            payload=payload,
            correlation_id=correlation_id
        )
        
        logger.info(f"Published DeleteItemCommand for item {item_id} with correlation ID {correlation_id}")
        return {"message": "Delete item command received", "correlation_id": correlation_id}
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete item {item_id}: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/items", response_model=ItemListResponse, status_code=501)
async def list_items():
    """List items with filters and pagination."""
    try:
        raise HTTPException(status_code=501, detail="Not Implemented: Service A does not support synchronous queries.")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to list items: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


# Analytics endpoints
@app.get("/analytics", response_model=ItemAnalytics, status_code=501)
async def get_analytics():
    """Get item analytics."""
    try:
        raise HTTPException(status_code=501, detail="Not Implemented: Service A does not support synchronous queries.")
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get analytics: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


@app.get("/metrics", response_model=ItemMetrics, status_code=501)
async def get_metrics():
    """Get service metrics."""
    try:
        raise HTTPException(status_code=501, detail="Not Implemented: Metrics are not available through this endpoint in an event-driven model.")
        
    except Exception as e:
        logger.error(f"Failed to get metrics: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


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




# Background task functions






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
            
            # Handle different event types
            if event_type and event_type.startswith("item."):
                return await process_item_event(event_type, event_data)
            elif event_type and event_type.startswith("service_b."):
                return await process_service_b_event(event_type, event_data)
            else:
                logger.warning(f"Unknown event type: {event_type}")
                return True  # Acknowledge unknown events to avoid reprocessing
        
        return True
        
    except Exception as e:
        logger.error(f"Failed to process event: {e}")
        return False


@trace_method(name="process_item_event", kind=SpanKind.CONSUMER)
async def process_item_event(event_type: str, event_data: Dict[str, Any]) -> bool:
    """Process item-related events."""
    try:
        item_id = event_data.get("item_id")
        item_uuid = event_data.get("item_uuid")
        correlation_id = event_data.get("correlation_id")
        
        # Add span attributes for item event processing
        add_span_attributes({
            "messaging.event_type": event_type,
            "messaging.item.id": item_id,
            "messaging.item.uuid": item_uuid,
            "correlation_id": correlation_id
        })
        
        logger.info(f"Processing item event {event_type} for item {item_id}")
        
        # Add business logic here based on event type
        if event_type == "item.created":
            # Handle item creation from other services
            pass
        elif event_type == "item.updated":
            # Handle item updates from other services
            pass
        elif event_type == "item.deleted":
            # Handle item deletion from other services
            pass
        
        return True
        
    except Exception as e:
        # Record error in span
        add_span_attributes({
            "error": True,
            "error.message": str(e)
        })
        logger.error(f"Failed to process item event: {e}")
        return False


@trace_method(name="process_service_b_event", kind=SpanKind.CONSUMER)
async def process_service_b_event(event_type: str, event_data: Dict[str, Any]) -> bool:
    """Process events from Service B."""
    try:
        correlation_id = event_data.get("correlation_id")
        
        # Add span attributes for service B event processing
        add_span_attributes({
            "messaging.event_type": event_type,
            "messaging.source_service": "service_b",
            "correlation_id": correlation_id
        })
        
        logger.info(f"Processing Service B event: {event_type}")
        
        # Add cross-service communication logic here
        # This demonstrates how services can react to events from other services
        
        return True
        
    except Exception as e:
        # Record error in span
        add_span_attributes({
            "error": True,
            "error.message": str(e)
        })
        logger.error(f"Failed to process Service B event: {e}")
        return False


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
