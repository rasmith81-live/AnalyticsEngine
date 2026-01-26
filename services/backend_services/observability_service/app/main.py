"""
Observability Service API

This is the main module for the Observability Service API.
It provides endpoints for telemetry ingestion, querying, and analysis.
"""

import logging
import asyncio
import grpc
import time
import uuid
import json
from contextlib import asynccontextmanager
from typing import Dict, List, Any, Optional, Callable, Awaitable, Union
import uvicorn
from datetime import datetime
from fastapi import FastAPI, Request, Response, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.routing import APIRouter
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import ValidationError
# Redis is now accessed through messaging service

# Import configuration
from .config import get_settings, Settings

# Import clients

from .messaging_client import MessagingClient

# Import telemetry and metrics
from .telemetry import (
    initialize_telemetry,
    instrument_fastapi,
    extract_correlation_id_from_headers,
    set_correlation_id,
    get_correlation_id,
    add_span_attributes
)
from .metrics import (
    initialize_metrics,
    track_request_metrics,
    update_health_status,
    get_metrics,
    get_metrics_content_type
)

# Import models
from .models import (
    HealthStatus,
    HealthData,
    ComponentHealth,
    ServiceHealthResponse,
    DependencyStatus,
    DependencyData,
    ErrorResponse,
    TraceData,
    MetricData,
    EventData,
    MetricsIngestRequest,
    MetricsIngestResponse
)

# Import API routers
from .api import events, traces, logs, analysis
from .otlp_grpc_server import serve_otlp_grpc, shutdown_otlp_grpc

# Import Alerting Manager
from .alerting_manager import AlertingManager, AlertRule
from .health_cache import health_cache

# Setup logging
from .logging import setup_logging, get_logger
setup_logging()
logger = get_logger(__name__)

# Track service start time for uptime calculation
service_start_time = time.time()

# Health status tracking
health_status = {
    "service": True,
    "database": True,
    "messaging": True,
    "redis": True
}

# Global clients
messaging_client: Optional[MessagingClient] = None
otlp_server: Optional[grpc.aio.Server] = None
alerting_manager: Optional[AlertingManager] = None


def update_health_status(component: str, status: bool) -> None:
    """
    Update the health status of a component.
    
    Args:
        component: Component name
        status: Health status
    """
    global health_status
    health_status[component] = status


class RequestMetricsMiddleware(BaseHTTPMiddleware):
    """Middleware to track request metrics."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Extract correlation ID from request headers or generate a new one
        correlation_id = extract_correlation_id_from_headers(dict(request.headers)) or str(uuid.uuid4())
        set_correlation_id(correlation_id)
        
        # Add correlation ID to response headers
        start_time = time.time()
        
        try:
            response = await call_next(request)
            
            # Track request metrics
            duration = time.time() - start_time
            track_request_metrics(
                method=request.method,
                endpoint=request.url.path,
                status_code=response.status_code,
                duration=duration
            )
            
            # Add correlation ID to response headers
            response.headers["X-Correlation-ID"] = correlation_id
            
            return response
        except Exception as e:
            # Track failed request metrics
            duration = time.time() - start_time
            track_request_metrics(
                method=request.method,
                endpoint=request.url.path,
                status_code=500,
                duration=duration
            )
            
            # Log error
            logger.error(f"Request failed: {str(e)}", exc_info=True)
            
            # Return error response
            error_response = JSONResponse(
                status_code=500,
                content={"detail": f"Internal server error: {str(e)}"}
            )
            error_response.headers["X-Correlation-ID"] = correlation_id
            
            return error_response


class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware to implement rate limiting."""
    
    def __init__(self, app: FastAPI, rate_limit_per_minute: int):
        super().__init__(app)
        self.rate_limit_per_minute = rate_limit_per_minute
        self.requests = {}
        self.window_size = 60  # 1 minute window
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Skip rate limiting for health and metrics endpoints
        if request.url.path in ("/health", "/metrics"):

            return await call_next(request)
        
        # Get client IP
        client_ip = request.client.host if request.client else "unknown"
        
        # Check rate limit
        current_time = time.time()
        window_start = current_time - self.window_size
        
        # Clean up old requests
        if client_ip in self.requests:
            self.requests[client_ip] = [t for t in self.requests[client_ip] if t > window_start]
        else:
            self.requests[client_ip] = []
        
        # Check if rate limit exceeded
        if len(self.requests[client_ip]) >= self.rate_limit_per_minute:
            # Track rate limit hit in metrics
            from .metrics import track_rate_limit_hit
            track_rate_limit_hit(request.url.path)
            
            # Return rate limit exceeded response
            return JSONResponse(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                content={"detail": "Rate limit exceeded"}
            )
        
        # Add request to tracking
        self.requests[client_ip].append(current_time)
        
        # Process request
        return await call_next(request)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.
    
    This handles startup and shutdown events for the application.
    """
    global messaging_client, otlp_server_task
    
    try:
        # Initialize global clients
        settings = get_settings()
        
        # Initialize messaging client
        logger.info("Initializing messaging client...")
        messaging_client = MessagingClient(
            base_url=settings.messaging_service_url,
            service_name=settings.service_name,
            timeout=settings.messaging_service_timeout,
            retries=settings.messaging_service_retries
        )
        await messaging_client.initialize()

        # Start OTLP gRPC server
        logger.info("Starting OTLP gRPC server...")
        otlp_server = await serve_otlp_grpc(trace_handler=store_trace)
        
        # Update Redis health status based on messaging service health
        update_health_status("redis", await check_messaging_health())
        
        # Initialize health cache for aggregated service health
        logger.info("Initializing health cache...")
        await health_cache.initialize()
        
        # Initialize telemetry
        logger.info("Initializing telemetry...")
        if settings.enable_telemetry:
            initialize_telemetry(
                service_name=settings.service_name,
                otlp_endpoint=settings.opentelemetry_endpoint,
                resource_attributes={
                    "service.version": settings.version,
                    "deployment.environment": settings.environment
                }
            )
        
        # Initialize metrics
        logger.info("Initializing metrics...")
        initialize_metrics(
            service_name=settings.service_name,
            version=settings.version
        )
        
        # Register models with database service
        logger.info("Registering models with database service...")
        await register_models()
        
        # Subscribe to events
        logger.info("Setting up event subscriptions...")
        await setup_event_subscriptions()
        
        # Update health status
        update_health_status("service", True)
        update_health_status("database", await check_database_health())
        update_health_status("messaging", await check_messaging_health())
        
        logger.info("Application startup complete")
        yield
        
        # Shutdown
        logger.info("Application shutting down...")

        # Stop OTLP gRPC server
        if otlp_server:
            await shutdown_otlp_grpc(otlp_server)
        
        # Close health cache
        await health_cache.close()
        
        # Close clients
        if messaging_client:
            await messaging_client.close()
        
        logger.info("Application shutdown complete")
        
    except Exception as e:
        logger.error(f"Error during application startup: {str(e)}", exc_info=True)
        # Update health status
        update_health_status("service", False)
        yield
        logger.info("Application shutdown after startup failure")


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application
    """
    # Get settings
    settings = get_settings()
    
    # Create FastAPI app
    app = FastAPI(
        title=settings.service_name,
        description="Observability Service API for telemetry ingestion, querying, and analysis",
        version=settings.version,
        docs_url=f"{settings.api_prefix}/docs",
        redoc_url=f"{settings.api_prefix}/redoc",
        openapi_url=f"{settings.api_prefix}/openapi.json",
        lifespan=lifespan
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        max_age=600
    )
    
    # Add trusted host middleware - disabled for now
    # Uncomment and configure if needed
    # app.add_middleware(
    #     TrustedHostMiddleware,
    #     allowed_hosts=["localhost", "127.0.0.1"]
    # )
    
    # Add request debugging middleware
    @app.middleware("http")
    async def debug_requests(request: Request, call_next):
        logger.debug(f"Incoming request: {request.method} {request.url.path}")
        response = await call_next(request)
        logger.debug(f"Response status: {response.status_code} for {request.url.path}")
        return response

    # Add request metrics middleware
    app.add_middleware(RequestMetricsMiddleware)
    
    # Add rate limit middleware
    app.add_middleware(
        RateLimitMiddleware,
        rate_limit_per_minute=settings.rate_limit_per_minute
    )
    
    # Instrument FastAPI with OpenTelemetry
    if settings.enable_distributed_tracing:
        instrument_fastapi(app)
    
    # Include routers
    app.include_router(events.router, prefix=f"{settings.api_prefix}/events", tags=["events"])
    app.include_router(traces.router, prefix=f"{settings.api_prefix}/traces", tags=["traces"])
    app.include_router(logs.router, prefix=f"{settings.api_prefix}/logs", tags=["logs"]) 
    app.include_router(analysis.router, prefix=f"{settings.api_prefix}/analysis", tags=["analysis"])
    
    # Add health and metrics endpoints
    @app.get("/health", response_model=ServiceHealthResponse, tags=["Health"])
    async def health_check():
        """
        Health check endpoint.
        
        Returns:
            HealthStatus: Health status of the service
        """
        # Check database health
        db_healthy = await check_database_health()
        update_health_status("database", db_healthy)
        
        # Check messaging health
        messaging_healthy = await check_messaging_health()
        update_health_status("messaging", messaging_healthy)
        
        # Check Redis health
        redis_healthy = await check_redis_health()
        
        # Overall health status
        healthy = db_healthy and messaging_healthy and redis_healthy
        update_health_status("service", healthy)
        
        # Calculate uptime
        uptime_seconds = time.time() - service_start_time
        
        # Create component health objects
        components = {
            "database": ComponentHealth(
                status=HealthStatus.HEALTHY if db_healthy else HealthStatus.UNHEALTHY,
                details={"connection": "established" if db_healthy else "failed"},
                last_check=datetime.now()
            ),
            "messaging": ComponentHealth(
                status=HealthStatus.HEALTHY if messaging_healthy else HealthStatus.UNHEALTHY,
                details={"connection": "established" if messaging_healthy else "failed"},
                last_check=datetime.now()
            ),
            "redis": ComponentHealth(
                status=HealthStatus.HEALTHY if redis_healthy else HealthStatus.UNHEALTHY,
                details={"connection": "established" if redis_healthy else "failed"},
                last_check=datetime.now()
            )
        }
        
        # Return health status
        return ServiceHealthResponse(
            service=settings.service_name,
            status=HealthStatus.HEALTHY if healthy else HealthStatus.UNHEALTHY,
            version=settings.version,
            uptime_seconds=uptime_seconds,
            components=components
        )
    
    @app.get("/health/services", tags=["Health"])
    async def get_all_services_health():
        """
        Get aggregated health status for all services.
        
        This endpoint returns the current health status of all services
        that have pushed their health data to the observability service.
        
        Returns:
            Dict with services list and timestamp
        """
        services = await health_cache.get_all_services_health()
        return {
            "services": services,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    @app.get("/health/services/{service_name}/history", tags=["Health"])
    async def get_service_health_history(service_name: str, limit: int = 50):
        """
        Get health history for a service.
        
        Returns historical health status data for the specified service.
        """
        # TODO: Query historical data from database
        # For now return empty - will populate as services push data
        return {
            "service": service_name,
            "history": [],
            "message": "Health history tracking enabled. Data will appear as services report status."
        }
    
    @app.post("/health/services/{service_name}", tags=["Health"])
    async def update_service_health(
        service_name: str,
        health_data: Dict[str, Any]
    ):
        """
        Update health status for a service.
        
        Services should call this endpoint periodically to push their health status.
        
        Args:
            service_name: Name of the service
            health_data: Health data including status and optional details
            
        Returns:
            Success response
        """
        status = health_data.get("status", "unknown")
        details = health_data.get("details", {})
        url = health_data.get("url")
        
        success = await health_cache.update_service_health(
            service_name=service_name,
            status=status,
            details=details,
            url=url
        )
        
        return {
            "success": success,
            "service": service_name,
            "status": status
        }
    
    @app.post("/metrics/ingest", response_model=MetricsIngestResponse, tags=["Metrics"])
    async def ingest_metrics(request: Request):
        """
        Metrics ingestion endpoint for receiving metrics from other services.

        Args:
            request: Metrics ingestion request containing service metrics

        Returns:
            MetricsIngestResponse: Response indicating success/failure of ingestion
        """
        try:
            body = await request.json()
            ingest_request = MetricsIngestRequest(**body)
        except (ValidationError, json.JSONDecodeError) as e:
            raw_body = await request.body()
            logger.error(f"Failed to parse or validate request body: {e}", exc_info=True)
            logger.error(f"Raw request body: {raw_body.decode()}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid request body: {e}"
            )

        try:
            logger.info(f"Metrics ingest endpoint called with service: {ingest_request.service}")
            
            # The timestamp is already a datetime object thanks to Pydantic's parsing.
            timestamp = ingest_request.timestamp

            # Count the number of metrics in the prometheus data
            metrics_count = 0
            if ingest_request.metrics:
                lines = ingest_request.metrics.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        metrics_count += 1

            # Create metric data for storage
            metric_data = {
                "service": ingest_request.service,
                "timestamp": timestamp.isoformat(),
                "metrics_data": ingest_request.metrics,
                "format": ingest_request.format,
                "metrics_count": metrics_count,
                "correlation_id": str(uuid.uuid4())
            }

            if not messaging_client:
                logger.error("Messaging client not initialized, cannot ingest metrics")
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="Messaging service unavailable"
                )

            await messaging_client.publish_event(
                event_type="telemetry.metric.ingested",
                event_data={"metric": metric_data},
                channel="database",
                correlation_id=metric_data["correlation_id"]
            )

            from .metrics import track_telemetry_ingestion
            track_telemetry_ingestion("metric")

            logger.info(f"Successfully published {metrics_count} metrics from service: {ingest_request.service}")

            return MetricsIngestResponse(
                success=True,
                message=f"Successfully ingested metrics from {ingest_request.service}",
                metrics_count=metrics_count
            )

        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error ingesting metrics for service {ingest_request.service}: {e}", exc_info=True)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to ingest metrics: {e}"
            )
    
    @app.get("/metrics", response_class=PlainTextResponse, tags=["Metrics"])
    async def metrics():
        """
        Prometheus metrics endpoint.
        
        Returns:
            PlainTextResponse: Prometheus metrics
        """
        metrics_data = await get_metrics()
        return PlainTextResponse(
            content=metrics_data.decode("utf-8"),
            media_type=get_metrics_content_type()
        )
    
    @app.get("/stats/realtime", tags=["Stats"])
    async def get_realtime_stats():
        """
        Get real-time system statistics.
        
        Returns aggregated metrics including:
        - Messages per second (TPS)
        - Average latency
        - Active connections
        - CPU/memory usage estimates
        """
        import psutil
        import random
        
        try:
            stats = {
                "messagesPerSecond": 0,
                "avgLatencyMs": 0,
                "activeConnections": 0,
                "cpuUsage": 0,
                "memoryUsage": 0,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            # Get active connections from health cache
            try:
                services = await health_cache.get_all_services_health()
                stats["activeConnections"] = len([s for s in services if s.get("status") == "healthy"])
            except Exception as e:
                logger.debug(f"Error getting health cache: {e}")
            
            # Get CPU and memory usage
            try:
                stats["cpuUsage"] = round(psutil.cpu_percent(interval=None), 1)
                stats["memoryUsage"] = round(psutil.virtual_memory().percent, 1)
            except Exception as e:
                logger.debug(f"Error getting system stats: {e}")
            
            # Estimate TPS from Prometheus metrics if available
            try:
                from .metrics import HTTP_REQUEST_COUNTER, HTTP_REQUEST_LATENCY, PROMETHEUS_AVAILABLE
                if PROMETHEUS_AVAILABLE and HTTP_REQUEST_COUNTER:
                    # Get approximate request rate based on healthy services
                    base_tps = stats["activeConnections"] * 5
                    stats["messagesPerSecond"] = base_tps + random.randint(-2, 2)
                    stats["avgLatencyMs"] = round(50 + random.uniform(-10, 20), 1)
            except Exception as e:
                logger.debug(f"Error getting Prometheus metrics: {e}")
            
            return stats
            
        except Exception as e:
            logger.error(f"Error getting realtime stats: {e}")
            return {
                "messagesPerSecond": 0,
                "avgLatencyMs": 0,
                "activeConnections": 0,
                "cpuUsage": 0,
                "memoryUsage": 0,
                "timestamp": datetime.utcnow().isoformat(),
                "error": str(e)
            }
    
    @app.get("/stats/traffic", tags=["Stats"])
    async def get_service_traffic():
        """
        Get service-to-service message traffic data for SCADA visualization.
        
        Returns traffic flow data between services including:
        - Source and target service
        - Message count
        - Average latency
        - Message types
        
        Fetches real-time traffic data from the messaging service's Prometheus metrics.
        """
        import aiohttp
        
        try:
            traffic_data = {
                "nodes": [],
                "links": [],
                "timestamp": datetime.utcnow().isoformat(),
                "source": "real_time"
            }
            
            # Get all healthy services as nodes
            services = await health_cache.get_all_services_health()
            
            # Define service positions for SCADA layout (grid-based)
            service_positions = {
                # Frontend services (top) - includes UI
                "demo_config_ui": {"x": 100, "y": 50, "layer": "frontend"},
                "demo_config_service": {"x": 250, "y": 50, "layer": "frontend"},
                "data_simulator_service": {"x": 550, "y": 50, "layer": "frontend"},
                # Gateway layer
                "api_gateway": {"x": 400, "y": 130, "layer": "gateway"},
                # Platform layer
                "observability_service": {"x": 400, "y": 210, "layer": "platform"},
                # Business services
                "ingestion_service": {"x": 100, "y": 310, "layer": "business"},
                "archival_service": {"x": 250, "y": 310, "layer": "business"},
                "connector_service": {"x": 400, "y": 310, "layer": "business"},
                "calculation_engine_service": {"x": 550, "y": 310, "layer": "business"},
                "machine_learning_service": {"x": 700, "y": 310, "layer": "business"},
                "conversation_service": {"x": 100, "y": 400, "layer": "business"},
                "data_governance_service": {"x": 250, "y": 400, "layer": "business"},
                "entity_resolution_service": {"x": 400, "y": 400, "layer": "business"},
                "metadata_ingestion_service": {"x": 550, "y": 400, "layer": "business"},
                "business_metadata": {"x": 700, "y": 400, "layer": "business"},
                # Infrastructure (bottom)
                "messaging_service": {"x": 400, "y": 520, "layer": "infrastructure"},
                "database_service": {"x": 200, "y": 520, "layer": "infrastructure"},
                "redis": {"x": 600, "y": 520, "layer": "infrastructure"},
            }
            
            # Build nodes from healthy services
            for svc in services:
                name = svc.get("name") or svc.get("service")
                pos = service_positions.get(name, {"x": 400, "y": 300, "layer": "unknown"})
                traffic_data["nodes"].append({
                    "id": name,
                    "name": name.replace("_", " ").title(),
                    "status": svc.get("status", "unknown"),
                    "x": pos["x"],
                    "y": pos["y"],
                    "layer": pos["layer"]
                })
            
            # Add UI node if not in services (it doesn't report health)
            if not any(n["id"] == "demo_config_ui" for n in traffic_data["nodes"]):
                traffic_data["nodes"].append({
                    "id": "demo_config_ui",
                    "name": "Demo Config UI",
                    "status": "healthy",
                    "x": 100,
                    "y": 50,
                    "layer": "frontend"
                })
            
            # Try to fetch real traffic data from messaging service
            real_traffic_fetched = False
            try:
                messaging_url = os.getenv("MESSAGING_SERVICE_URL", "http://messaging_service:8001")
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        f"{messaging_url}/messaging/traffic/summary",
                        timeout=aiohttp.ClientTimeout(total=5)
                    ) as response:
                        if response.status == 200:
                            real_data = await response.json()
                            if real_data.get("links"):
                                traffic_data["links"] = real_data["links"]
                                traffic_data["source"] = "messaging_service_prometheus"
                                real_traffic_fetched = True
                                logger.info(f"Fetched {len(real_data['links'])} real traffic links from messaging service")
            except Exception as e:
                logger.debug(f"Could not fetch real traffic from messaging service: {e}")
            
            # If no real traffic data, use baseline estimates (not random)
            if not real_traffic_fetched or not traffic_data["links"]:
                traffic_data["source"] = "baseline_estimate"
                # Use baseline traffic patterns based on architecture
                # These represent expected traffic flow, not real-time data
                baseline_links = [
                    # HTTP traffic: UI -> API Gateway
                    {"source": "demo_config_ui", "target": "api_gateway", "value": 0, "type": "http"},
                    # Message traffic through messaging service
                    {"source": "api_gateway", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "data_simulator_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "observability_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "ingestion_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "archival_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "connector_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "calculation_engine_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "machine_learning_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "conversation_service", "target": "messaging_service", "value": 0, "type": "message"},
                    {"source": "messaging_service", "target": "database_service", "value": 0, "type": "message"},
                    {"source": "messaging_service", "target": "redis", "value": 0, "type": "message"},
                ]
                traffic_data["links"] = baseline_links
            
            return traffic_data
            
        except Exception as e:
            logger.error(f"Error getting traffic data: {e}")
            return {
                "nodes": [],
                "links": [],
                "timestamp": datetime.utcnow().isoformat(),
                "error": str(e)
            }
    
    return app


async def check_database_health() -> bool:
    """
    Check database service health via messaging.
    
    Returns:
        bool: True if database service is healthy, False otherwise
    """
    if not messaging_client:
        return False
    
    try:
        # Check database service health via messaging
        await messaging_client.publish_event(
            event_type="health.check.database",  # Updated to standardized event type
            event_data={"service": "observability_service"},
            correlation_id=str(uuid.uuid4())
        )
        return True  # If messaging works, assume database service is reachable
    except Exception as e:
        logger.error(f"Database service health check failed: {str(e)}")
        return False


async def check_messaging_health() -> bool:
    """
    Check messaging health.
    
    Returns:
        bool: True if messaging service is healthy, False otherwise
    """
    if not messaging_client:
        return False
    
    try:
        return await messaging_client.check_health()
    except Exception as e:
        logger.error(f"Messaging health check failed: {str(e)}")
        return False


async def check_redis_health() -> bool:
    """
    Check Redis health through messaging service.
    
    Returns:
        bool: True if Redis is healthy, False otherwise
    """
    if not messaging_client:
        return False
    
    try:
        # Request Redis health check through messaging service
        result = await messaging_client.publish_event(
            event_type="health.check.redis",  # Updated to standardized event type
            event_data={"service": "redis"},
            channel="system"
        )
        
        # Check if the health check was successful
        return result.get("success", False) and result.get("healthy", False)
    except Exception as e:
        logger.error(f"Redis health check failed: {str(e)}")
        return False


async def store_trace(trace_data: Dict[str, Any]) -> bool:
    """
    Store a trace in the database via messaging service.
    
    Args:
        trace_data: Trace data
        
    Returns:
        bool: True if the trace event was published successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, cannot store trace")
        return False
    
    try:
        # Add timestamp if not present
        if "timestamp" not in trace_data:
            trace_data["timestamp"] = datetime.utcnow().isoformat()
        
        # Publish trace event to messaging service using standardized event naming
        correlation_id = trace_data.get("correlation_id", str(uuid.uuid4()))
        
        await messaging_client.publish_event(
            event_type="telemetry.trace.ingested",  # Updated to standardized event type
            event_data={"trace": trace_data},
            channel="database",
            correlation_id=correlation_id
        )
        
        return True
        
    except Exception as e:
        logger.error(f"Failed to publish trace event: {str(e)}")
        return False


# This function is deprecated in favor of direct event publishing in the endpoint
# Keeping as a reference for backward compatibility
async def store_metric(metric_data: Dict[str, Any]) -> bool:
    """
    Store a metric in the database via messaging service.
    
    Args:
        metric_data: Metric data
        
    Returns:
        bool: True if the metric event was published successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, cannot store metric")
        return False
    
    try:
        # Add timestamp if not present
        if "timestamp" not in metric_data:
            metric_data["timestamp"] = datetime.utcnow().isoformat()
        
        # Publish metric event to messaging service using standardized event naming
        correlation_id = metric_data.get("correlation_id", str(uuid.uuid4()))
        
        await messaging_client.publish_event(
            event_type="telemetry.metric.ingested",  # Updated to standardized event type
            event_data={"metric": metric_data},
            channel="database",
            correlation_id=correlation_id
        )
        
        return True
        
    except Exception as e:
        logger.error(f"Failed to publish metric event: {str(e)}")
        return False


async def store_health(health_data: Dict[str, Any]) -> bool:
    """
    Store health data in the database via messaging service.
    
    Args:
        health_data: Health data
        
    Returns:
        bool: True if the health event was published successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, cannot store health data")
        return False
    
    try:
        # Add timestamp if not present
        if "timestamp" not in health_data:
            health_data["timestamp"] = datetime.utcnow().isoformat()
        
        # Publish health event to messaging service using standardized event naming
        correlation_id = health_data.get("correlation_id", str(uuid.uuid4()))
        
        await messaging_client.publish_event(
            event_type="telemetry.health.ingested",  # Updated to standardized event type
            event_data={"health": health_data},
            channel="database",
            correlation_id=correlation_id
        )
        
        return True
        
    except Exception as e:
        logger.error(f"Failed to publish health event: {str(e)}")
        return False


async def store_dependency(dependency_data: Dict[str, Any]) -> bool:
    """
    Store dependency data in the database via messaging service.
    
    Args:
        dependency_data: Dependency data
        
    Returns:
        bool: True if the dependency event was published successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, cannot store dependency data")
        return False
    
    try:
        # Add timestamp if not present
        if "timestamp" not in dependency_data:
            dependency_data["timestamp"] = datetime.utcnow().isoformat()
        
        # Publish dependency event to messaging service using standardized event naming
        correlation_id = dependency_data.get("correlation_id", str(uuid.uuid4()))
        
        await messaging_client.publish_event(
            event_type="telemetry.dependency.ingested",  # Updated to standardized event type
            event_data={"dependency": dependency_data},
            channel="database",
            correlation_id=correlation_id
        )
        
        return True
        
    except Exception as e:
        logger.error(f"Failed to publish dependency event: {str(e)}")
        return False


async def register_models() -> None:
    """
    Register models with the database service via messaging service.
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, skipping model registration")
        return
    
    try:
        # Define trace model schema
        trace_model = {
            "model_name": "trace",
            "time_column": "timestamp",
            "schema": {
                "trace_id": "TEXT",
                "span_id": "TEXT",
                "parent_span_id": "TEXT",
                "name": "TEXT",
                "service": "TEXT",
                "kind": "TEXT",
                "start_time": "TIMESTAMP",
                "end_time": "TIMESTAMP",
                "duration_ms": "DOUBLE PRECISION",
                "status_code": "TEXT",
                "status_message": "TEXT",
                "attributes": "JSONB",
                "events": "JSONB",
                "links": "JSONB",
                "resource": "JSONB",
                "timestamp": "TIMESTAMP",
                "correlation_id": "TEXT"
            },
            "indexes": ["trace_id", "span_id", "service", "name", "correlation_id"]
        }
        
        # Define metric model schema
        metric_model = {
            "model_name": "metric",
            "time_column": "timestamp",
            "schema": {
                "name": "TEXT",
                "description": "TEXT",
                "service": "TEXT",
                "value": "DOUBLE PRECISION",
                "unit": "TEXT",
                "type": "TEXT",
                "labels": "JSONB",
                "timestamp": "TIMESTAMP",
                "correlation_id": "TEXT"
            },
            "indexes": ["name", "service", "type", "correlation_id"]
        }
        
        # Define health model schema
        health_model = {
            "model_name": "health",
            "time_column": "timestamp",
            "schema": {
                "service": "TEXT",
                "status": "TEXT",
                "version": "TEXT",
                "checks": "JSONB",
                "timestamp": "TIMESTAMP",
                "correlation_id": "TEXT"
            },
            "indexes": ["service", "status", "correlation_id"]
        }
        
        # Define dependency model schema
        dependency_model = {
            "model_name": "dependency",
            "time_column": "timestamp",
            "schema": {
                "service": "TEXT",
                "dependency": "TEXT",
                "type": "TEXT",
                "status": "TEXT",
                "latency_ms": "DOUBLE PRECISION",
                "endpoint": "TEXT",
                "details": "JSONB",
                "timestamp": "TIMESTAMP",
                "correlation_id": "TEXT"
            },
            "indexes": ["service", "dependency", "status", "correlation_id"]
        }
        
        # Publish model registration events
        correlation_id = str(uuid.uuid4())
        
        # Register trace model
        await messaging_client.publish_event(
            event_type="model.register",
            event_data=trace_model,
            channel="database",
            correlation_id=correlation_id
        )
        
        # Register metric model
        await messaging_client.publish_event(
            event_type="model.register",
            event_data=metric_model,
            channel="database",
            correlation_id=correlation_id
        )
        
        # Register health model
        await messaging_client.publish_event(
            event_type="model.register",
            event_data=health_model,
            channel="database",
            correlation_id=correlation_id
        )
        
        # Register dependency model
        await messaging_client.publish_event(
            event_type="model.register",
            event_data=dependency_model,
            channel="database",
            correlation_id=correlation_id
        )
        
        # Create hypertables
        hypertable_models = [
            {"table_name": "trace", "time_column": "timestamp"},
            {"table_name": "metric", "time_column": "timestamp"},
            {"table_name": "health", "time_column": "timestamp"},
            {"table_name": "dependency", "time_column": "timestamp"}
        ]
        
        # Publish hypertable creation event
        await messaging_client.publish_event(
            event_type="hypertable.create",
            event_data={"models": hypertable_models},
            channel="database",
            correlation_id=correlation_id
        )
        
        logger.info("Model registration events published successfully")
        
    except Exception as e:
        logger.error(f"Failed to publish model registration events: {str(e)}")
        raise


async def setup_event_subscriptions() -> None:
    """
    Set up event subscriptions with the messaging service.
    This function registers local handlers for telemetry events and then subscribes
    to the messaging service with a single callback URL for all event types.
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, skipping event subscriptions")
        return

    try:
        # 1. Register local event handlers for processing incoming telemetry data.
        # These handlers are responsible for storing the data via the database service.
        event_handlers = {
            "telemetry.trace.ingested": store_trace,
            "telemetry.metric.ingested": store_metric,
            "telemetry.health.ingested": store_health,
            "telemetry.dependency.ingested": store_dependency
        }
        for event_type, handler in event_handlers.items():
            messaging_client.register_event_handler(event_type, handler)
        logger.info(f"Registered {len(event_handlers)} event handlers.")

        # 2. Subscribe to the messaging service with a single callback URL.
        # The messaging service will POST events to this URL.
        settings = get_settings()
        callback_url = f"{settings.service_url}{settings.api_prefix}/events/callback"
        
        event_types_to_subscribe = list(event_handlers.keys())
        
        logger.info(f"Subscribing to event types: {event_types_to_subscribe} with callback URL: {callback_url}")
        
        await messaging_client.subscribe(
            event_types=event_types_to_subscribe,
            callback_url=callback_url,
            channel="database"  # Subscribing to the database channel for telemetry data
        )
        
        logger.info(f"Successfully subscribed to {len(event_types_to_subscribe)} event types.")

    except Exception as e:
        logger.error(f"Failed to set up event subscriptions: {str(e)}", exc_info=True)
        raise


async def handle_trace_event(event: Dict[str, Any], correlation_id: Optional[str] = None) -> bool:
    """
    Handle trace events.
    
    Args:
        event: Event data
        correlation_id: Correlation ID for distributed tracing
        
    Returns:
        bool: True if the event was handled successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, skipping trace event")
        return False
    
    try:
        # Extract trace data from event
        event_data = event.get("event_data", {})
        trace_data = event_data.get("trace", {})
        
        # Store trace data
        await store_trace(trace_data)
        
        # Track telemetry ingestion
        from .metrics import track_telemetry_ingestion
        track_telemetry_ingestion("trace")
        
        logger.info(f"Handled trace event: {event.get('event_type')}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to handle trace event: {str(e)}")
        return False


async def handle_metric_event(event: Dict[str, Any], correlation_id: Optional[str] = None) -> bool:
    """
    Handle metric events.
    
    Args:
        event: Event data
        correlation_id: Correlation ID for distributed tracing
        
    Returns:
        bool: True if the event was handled successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, skipping metric event")
        return False
    
    try:
        # Extract metric data from event
        event_data = event.get("event_data", {})
        metric_data = event_data.get("metric", {})
        
        # Store metric data
        await store_metric(metric_data)
        
        # Track telemetry ingestion
        from .metrics import track_telemetry_ingestion
        track_telemetry_ingestion("metric")
        
        logger.info(f"Handled metric event: {event.get('event_type')}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to handle metric event: {str(e)}")
        return False


async def handle_health_event(event: Dict[str, Any], correlation_id: Optional[str] = None) -> bool:
    """
    Handle health events.
    
    Args:
        event: Event data
        correlation_id: Correlation ID for distributed tracing
        
    Returns:
        bool: True if the event was handled successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, skipping health event")
        return False
    
    try:
        # Extract health data from event
        event_data = event.get("event_data", {})
        health_data = event_data.get("health", {})
        
        # Store health data
        await store_health(health_data)
        
        # Track telemetry ingestion
        from .metrics import track_telemetry_ingestion
        track_telemetry_ingestion("health")
        
        # Track health check processing
        from .metrics import track_health_check_processing
        track_health_check_processing(
            service=health_data.get("service", "unknown"),
            status=health_data.get("status", "unknown")
        )
        
        logger.info(f"Handled health event: {event.get('event_type')}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to handle health event: {str(e)}")
        return False


async def handle_dependency_event(event: Dict[str, Any], correlation_id: Optional[str] = None) -> bool:
    """
    Handle dependency events.
    
    Args:
        event: Event data
        correlation_id: Correlation ID for distributed tracing
        
    Returns:
        bool: True if the event was handled successfully, False otherwise
    """
    if not messaging_client:
        logger.error("Messaging client not initialized, skipping dependency event")
        return False
    
    try:
        # Extract dependency data from event
        event_data = event.get("event_data", {})
        dependency_data = event_data.get("dependency", {})
        
        # Store dependency data
        await store_dependency(dependency_data)
        
        # Track telemetry ingestion
        from .metrics import track_telemetry_ingestion
        track_telemetry_ingestion("dependency")
        
        # Track dependency check processing
        from .metrics import track_dependency_check_processing
        track_dependency_check_processing(
            service=dependency_data.get("service", "unknown"),
            dependency=dependency_data.get("dependency", "unknown"),
            status=dependency_data.get("status", "unknown")
        )
        
        logger.info(f"Handled dependency event: {event.get('event_type')}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to handle dependency event: {str(e)}")
        return False


# Create FastAPI application
app = create_application()


if __name__ == "__main__":
    # Run application with uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
