"""
Database Service - Centralized database operations for TimescaleDB with CQRS support.

This service consolidates all database functionality:
- Database connection management
- Automated migration execution
- TimescaleDB hypertable operations
- CQRS pattern enforcement
- Schema validation and discovery
"""

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import make_wsgi_app
from prometheus_client.exposition import make_asgi_app
import logging
import os
import asyncio
import json
import time
import uuid
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
from contextlib import asynccontextmanager

from .database_manager import DatabaseManager
from .retention_manager import RetentionManager
from .messaging_client import MessagingClient
from .telemetry_consumers import TelemetryEventConsumer
from .command_consumers import CommandConsumer
from .simulation_data_consumer import SimulationDataConsumer
from .kpi_result_consumer import KPIResultConsumer
from .query_request_handler import QueryRequestHandler
from .subscriber_manager import SubscriberManager
from .stream_publisher import StreamPublisher
from .query_builder import QueryBuilder
from .secure_storage_manager import SecureStorageManager
from .api.migration_utilities_api import router as migration_utilities_router
from .mcp.postgres_mcp_server import create_postgres_mcp_router
from .mcp.knowledge_graph_mcp_server import create_knowledge_graph_mcp_router
from .models import (
    QueryRequest, QueryResponse, AdHocQueryRequest, CommandRequest, CommandResponse,
    MigrationRequest, MigrationResponse, HypertableRequest, HypertableResponse,
    ModelRegistrationRequest, ModelDiscoveryResponse, HealthResponse,
    SecureArtifactRequest, SecureArtifactResponse, SecureArtifactValueResponse
)
from .config import get_settings
from .metrics import metrics, update_system_metrics, update_db_connection_metrics, export_metrics_to_observability, track_endpoint_execution, track_db_operation, track_query, update_timescale_metrics
from .telemetry import initialize_telemetry, instrument_fastapi, instrument_sqlalchemy, trace_method, add_span_attributes, inject_trace_context, extract_correlation_id_from_headers


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global service instances
database_manager = None
retention_manager = None
messaging_client = None
telemetry_consumer = None
command_consumer = None
simulation_data_consumer = None
kpi_result_consumer = None
query_request_handler = None
subscriber_manager = None
stream_publisher = None
secure_storage_manager = None
service_start_time = datetime.utcnow()

# Background task cancellation handles
metrics_export_task = None
system_metrics_task = None

@asynccontextmanager
@trace_method(name="main.lifespan")
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global database_manager, retention_manager, messaging_client, telemetry_consumer, command_consumer, subscriber_manager, stream_publisher, secure_storage_manager, metrics_export_task, system_metrics_task, simulation_data_consumer, kpi_result_consumer, query_request_handler
    
    # Startup
    start_time = datetime.utcnow()
    correlation_id = str(uuid.uuid4())
    
    # Add span attributes for context
    add_span_attributes({
        "correlation_id": correlation_id,
        "timestamp.start": start_time.isoformat(),
        "service": "database_service",
        "event_type": "startup"
    })
    
    try:
        settings = get_settings()
        
        # Initialize OpenTelemetry for distributed tracing if enabled
        if settings.enable_distributed_tracing:
            initialize_telemetry(
                service_name=settings.service_name,
                otlp_endpoint=settings.otlp_endpoint if hasattr(settings, 'otlp_endpoint') else None,
                export_interval_ms=15000,  # Export every 15 seconds
                resource_attributes={
                    "service.version": "1.0.0",
                    "deployment.environment": os.environ.get("DEPLOYMENT_ENVIRONMENT", "development")
                }
            )
            logger.info(f"OpenTelemetry initialized for {settings.service_name}")
        
        # Initialize metrics with service name
        metrics.initialize(settings.service_name)
        metrics.service_ready.set(0)  # Not ready yet
        
        # Initialize database manager
        database_manager = DatabaseManager(get_settings())
        await database_manager.initialize()
        
        # Instrument SQLAlchemy with OpenTelemetry if enabled
        if settings.enable_distributed_tracing and database_manager.async_engine:
            instrument_sqlalchemy(database_manager.async_engine)
        
        # Initialize secure storage manager with sync engine to avoid greenlet context issues
        secure_storage_manager = SecureStorageManager(database_manager.sync_engine)

        # Initialize messaging client for Redis pub/sub
        messaging_client = MessagingClient(
            redis_url=get_settings().redis_url,
            service_name="database_service",
            pool_size=get_settings().redis_pool_size
        )
        await messaging_client.connect()
        
        # Initialize retention manager with database and messaging
        retention_manager = RetentionManager(
            engine=database_manager.async_engine,
            messaging_client=messaging_client
        )
        await retention_manager.start()
        
        # Initialize and start telemetry event consumers
        telemetry_consumer = TelemetryEventConsumer(
            database_manager=database_manager,
            messaging_client=messaging_client
        )
        await telemetry_consumer.start()
        
        # Initialize and start command consumers
        command_consumer = CommandConsumer(
            database_manager=database_manager,
            messaging_client=messaging_client,
            retention_manager=retention_manager
        )
        await command_consumer.start()

        # Initialize and start simulation data consumer
        simulation_data_consumer = SimulationDataConsumer(
            database_manager=database_manager,
            messaging_client=messaging_client
        )
        await simulation_data_consumer.start()
        logger.info("Simulation data consumer started")
        
        # Initialize and start KPI result consumer
        kpi_result_consumer = KPIResultConsumer(
            database_manager=database_manager,
            messaging_client=messaging_client
        )
        await kpi_result_consumer.start()
        logger.info("KPI result consumer started")
        
        # Initialize and start query request handler (for pub/sub database access)
        query_request_handler = QueryRequestHandler(
            database_manager=database_manager,
            redis_url=settings.redis_url
        )
        await query_request_handler.start()
        logger.info("Query request handler started (pub/sub database access)")
        
        # Initialize subscriber manager for stream publishing
        subscriber_manager = SubscriberManager(timeout_seconds=300)
        
        # Initialize stream publisher
        stream_publisher = StreamPublisher(
            db_session_factory=database_manager.get_session,
            messaging_client=messaging_client,
            subscriber_manager=subscriber_manager,
            poll_interval_seconds=30
        )
        await stream_publisher.start()
        logger.info("Stream publisher initialized and started")
        
        # Initialize and include PostgreSQL MCP router
        mcp_router = create_postgres_mcp_router(database_manager)
        app.include_router(mcp_router)
        logger.info("PostgreSQL MCP server initialized and router included")
        
        # Initialize and include Knowledge Graph MCP router
        kg_mcp_router = create_knowledge_graph_mcp_router(database_manager, messaging_client)
        app.include_router(kg_mcp_router)
        logger.info("Knowledge Graph MCP server initialized and router included")
        
        # Start background tasks for metrics
        if settings.enable_prometheus_metrics:
            # Start system metrics update task
            async def update_system_metrics_periodically():
                while True:
                    try:
                        update_system_metrics()
                        # Update database connection metrics
                        if database_manager:
                            conn_status = await database_manager.get_connection_status()
                            update_db_connection_metrics(
                                pool_size=conn_status.get("pool_size", 0),
                                used_connections=conn_status.get("used_connections", 0)
                            )
                            
                            # Update TimescaleDB metrics if available
                            try:
                                perf_stats = await database_manager.get_performance_stats()
                                if "hypertables" in perf_stats:
                                    table_metrics = {}
                                    for table in perf_stats["hypertables"]:
                                        table_name = table.get("table_name", "unknown")
                                        table_metrics[table_name] = {
                                            "chunks": table.get("chunk_count", 0),
                                            "size_bytes": table.get("total_size_bytes", 0),
                                            "compression_ratio": table.get("compression_ratio", 1.0)
                                        }
                                    update_timescale_metrics(table_metrics)
                            except Exception as e:
                                logger.warning(f"Failed to update TimescaleDB metrics: {str(e)}")
                    except Exception as e:
                        logger.error(f"Error updating system metrics: {str(e)}")
                    await asyncio.sleep(15)  # Update every 15 seconds
            
            # Start metrics export task
            async def export_metrics_periodically():
                while True:
                    try:
                        await export_metrics_to_observability(
                            push_gateway=settings.prometheus_push_gateway,
                            job_name=settings.metrics_export_job_name
                        )
                    except Exception as e:
                        logger.error(f"Error exporting metrics: {str(e)}")
                    await asyncio.sleep(settings.metrics_push_interval)
            
            # Create and store task objects for later cancellation
            system_metrics_task = asyncio.create_task(update_system_metrics_periodically())
            metrics_export_task = asyncio.create_task(export_metrics_periodically())
        
        # Set service as ready
        metrics.service_ready.set(1)
        metrics.service_health.set(1)
        
        # Startup complete - add span attributes for success
        startup_end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": startup_end_time.isoformat(),
            "duration_ms": (startup_end_time - start_time).total_seconds() * 1000,
            "success": True
        })
        
        logger.info("Database service started successfully")
        
        # Yield control back to FastAPI
        yield
        
        # Shutdown begins
        shutdown_start_time = datetime.utcnow()
        shutdown_correlation_id = str(uuid.uuid4())
        
        # Add span attributes for shutdown context
        add_span_attributes({
            "correlation_id": shutdown_correlation_id,
            "timestamp.start": shutdown_start_time.isoformat(),
            "service": "database_service",
            "event_type": "shutdown"
        })
        
        # Set service as not ready during shutdown
        metrics.service_ready.set(0)
        
        # Stop metrics background tasks
        if system_metrics_task and not system_metrics_task.cancelled():
            system_metrics_task.cancel()
            try:
                await system_metrics_task
            except asyncio.CancelledError:
                pass
        
        if metrics_export_task and not metrics_export_task.cancelled():
            metrics_export_task.cancel()
            try:
                await metrics_export_task
            except asyncio.CancelledError:
                pass
        
        # Stop telemetry event consumers
        if telemetry_consumer:
            await telemetry_consumer.stop()
        
        # Stop command event consumers
        if command_consumer:
            await command_consumer.stop()

        # Stop stream publisher
        if stream_publisher:
            await stream_publisher.stop()
            logger.info("Stream publisher stopped")
        
        # Stop retention manager
        if retention_manager:
            await retention_manager.stop()
        
        # Disconnect messaging client
        if messaging_client:
            await messaging_client.disconnect()
        
        # Close database connections
        if database_manager:
            await database_manager.close()
        
        # Add span attributes for shutdown success
        shutdown_end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": shutdown_end_time.isoformat(),
            "duration_ms": (shutdown_end_time - shutdown_start_time).total_seconds() * 1000,
            "success": True
        })
            
        logger.info("Database service shutdown complete")
    except Exception as e:
        logger.error(f"Failed to start database service: {str(e)}")
        metrics.service_health.set(0)
        
        # Add span attributes for error
        error_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": error_time.isoformat(),
            "duration_ms": (error_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        raise
        
# Startup and shutdown events are handled by the lifespan context manager

# Initialize FastAPI app with lifespan management
app = FastAPI(
    title="Database Service",
    description="Centralized database operations for TimescaleDB with CQRS support",
    version="1.0.0",
    lifespan=lifespan
)


# Instrument FastAPI with OpenTelemetry if enabled
if get_settings().enable_distributed_tracing:
    instrument_fastapi(app)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# Include migration utilities router
app.include_router(migration_utilities_router)

# MCP router will be included after database_manager is initialized (see lifespan)
# Placeholder - actual inclusion happens dynamically

def get_database_manager() -> DatabaseManager:
    """Dependency to get database manager instance."""
    if database_manager is None:
        raise HTTPException(status_code=503, detail="Database service not initialized")
    return database_manager

def get_retention_manager() -> RetentionManager:
    """Dependency to get retention manager instance."""
    if retention_manager is None:
        raise HTTPException(status_code=503, detail="Retention manager not initialized")
    return retention_manager

def get_messaging_client() -> MessagingClient:
    """Dependency to get messaging client instance."""
    if messaging_client is None:
        raise HTTPException(status_code=503, detail="Messaging client not initialized")
    return messaging_client

def get_subscriber_manager() -> SubscriberManager:
    """Dependency to get subscriber manager instance."""
    if subscriber_manager is None:
        raise HTTPException(status_code=503, detail="Subscriber manager not initialized")
    return subscriber_manager

def get_stream_publisher() -> StreamPublisher:
    """Dependency to get stream publisher instance."""
    if stream_publisher is None:
        raise HTTPException(status_code=503, detail="Stream publisher not initialized")
    return stream_publisher

def get_secure_storage_manager() -> SecureStorageManager:
    """Dependency to get secure storage manager instance."""
    if secure_storage_manager is None:
        raise HTTPException(status_code=503, detail="Secure storage manager not initialized")
    return secure_storage_manager

# Health check endpoint
@app.get("/health", response_model=HealthResponse)
@trace_method(name="database_service.health_check", kind="SERVER")
async def health_check(request: Request, db_manager: DatabaseManager = Depends(get_database_manager)):
    """Check database service health and connectivity."""
    # Extract correlation ID from headers or generate a new one
    correlation_id = extract_correlation_id_from_headers(request.headers) or str(uuid.uuid4())
    start_time = datetime.utcnow()
    settings = get_settings()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/health",
        "service": "database_service",
        "timestamp.start": start_time.isoformat()
    })
    
    try:
        # Use the enhanced check_database_connection method with tracing
        db_status = await db_manager.check_database_connection(correlation_id=correlation_id)
        
        # Build response with service info
        health_status = {
            "database": db_status,
            "service": {
                "name": "database_service",
                "version": settings.version,
                "uptime_seconds": (datetime.utcnow() - service_start_time).total_seconds()
            },
            "timestamp": datetime.utcnow().isoformat(),
            "correlation_id": correlation_id
        }
        
        # Add span attributes for response
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "health.status": "healthy",
            "db.postgresql_version": db_status.get("postgresql_version", "unknown"),
            "db.timescaledb_version": db_status.get("timescaledb_version", "unknown"),
            "db.hypertables_count": db_status.get("hypertables_count", 0),
            "success": True
        })
        
        # Create a properly formatted HealthResponse
        return HealthResponse(
            status="healthy",
            database_connected=db_status.get("connected", True),
            timescaledb_available=db_status.get("timescaledb_available", True),
            connection_pool_status=db_status.get("pool_status", {}),
            active_connections=db_status.get("active_connections", 0),
            timestamp=datetime.utcnow()
        )
        
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
        
        logger.error(f"Health check failed: {str(e)}")
        # Create a properly formatted HealthResponse for error case
        return HealthResponse(
            status="unhealthy",
            database_connected=False,
            timescaledb_available=False,
            connection_pool_status={"status": "error", "message": str(e)},
            active_connections=0,
            timestamp=datetime.utcnow()
        )

# Query execution endpoints
@app.post("/database/query", response_model=QueryResponse)
@track_endpoint_execution
@track_query(query_type="read", entity_type="dynamic")
@trace_method(name="database_service.execute_query", kind="SERVER")
async def execute_query(
    request: QueryRequest, 
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Execute a read query against the database."""
    correlation_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/database/query",
        "timestamp.start": start_time.isoformat(),
        "service_name": request.service_name,
        "query_type": request.query_type,
        "query_hash": hash(request.query),  # Hash the query for privacy
        "has_parameters": bool(request.parameters)
    })
    
    try:
        # Track query metrics
        track_query(request.service_name, request.query_type)
        
        # Execute the query
        query_start_time = time.time()
        result = await db_manager.execute_query(
            service_name=request.service_name,
            query=request.query,
            parameters=request.parameters,
            correlation_id=correlation_id
        )
        execution_time = time.time() - query_start_time
        
        # Track operation metrics
        track_db_operation("query", execution_time)
        
        # Add span attributes for response
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "execution_time_ms": execution_time * 1000,
            "result_size": len(result.get('rows', [])) if isinstance(result, dict) else 0,
            "success": True
        })
        
        return QueryResponse(
            success=True,
            data=result,
            execution_time=execution_time,
            row_count=result.get('row_count', 0),
            cache_hit=result.get('cache_hit', False)
        )
    except Exception as e:
        # Add span attributes for error
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        
        logger.error(f"Query execution failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Query execution failed: {str(e)}")

@app.post("/database/query/adhoc", response_model=QueryResponse)
@track_endpoint_execution
@track_query(query_type="read", entity_type="adhoc")
@trace_method(name="database_service.execute_adhoc_query", kind="SERVER")
async def execute_adhoc_query(
    request: AdHocQueryRequest,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Execute a structured ad-hoc query securely."""
    correlation_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/database/query/adhoc",
        "service_name": request.service_name,
        "table_name": request.table_name,
        "has_filters": bool(request.filters)
    })
    
    try:
        # Build secure SQL
        qb = QueryBuilder()
        sql, params = qb.build_select(
            table_name=request.table_name,
            columns=request.columns,
            filters=request.filters,
            time_range=request.time_range,
            group_by=request.group_by,
            order_by=request.order_by,
            order_direction=request.order_direction,
            limit=request.limit,
            offset=request.offset
        )
        
        # Execute
        query_start_time = time.time()
        result = await db_manager.execute_query(
            service_name=request.service_name,
            query=sql,
            parameters=params,
            correlation_id=correlation_id
        )
        execution_time = time.time() - query_start_time
        
        track_db_operation("adhoc_query", execution_time)
        
        return QueryResponse(
            success=True,
            data=result,
            execution_time=execution_time,
            row_count=result.get('row_count', 0),
            cache_hit=result.get('cache_hit', False)
        )
        
    except ValueError as e:
        logger.warning(f"Invalid ad-hoc query request: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Ad-hoc query failed: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error executing query")

@app.post("/database/command", response_model=CommandResponse)
@track_endpoint_execution
@track_query(query_type="write", entity_type="dynamic")
@trace_method(name="database_service.execute_command", kind="SERVER")
async def execute_command(
    request: CommandRequest,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Execute a write command against the database."""
    correlation_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/database/command",
        "timestamp.start": start_time.isoformat(),
        "service_name": request.service_name,
        "command_hash": hash(request.command),  # Hash the command for privacy
        "has_parameters": bool(request.parameters)
    })
    
    try:
        command_start_time = time.time()
        result = await db_manager.execute_command(
            command=request.command,
            parameters=request.parameters,
            service_name=request.service_name,
            timeout=request.timeout
        )
        execution_time = time.time() - command_start_time
        
        # Add span attributes for response
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "execution_time_ms": execution_time * 1000,
            "affected_rows": result.get('affected_rows', 0),
            "success": True
        })
        
        return CommandResponse(
            success=True,
            data=result.get('data'),
            execution_time=result.get('execution_time', 0),
            affected_rows=result.get('affected_rows', 0)
        )
    except Exception as e:
        # Add span attributes for error
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        
        logger.error(f"Command execution failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Command failed: {str(e)}")

# Migration management endpoints
@app.post("/database/migrations/run", response_model=MigrationResponse)
@track_endpoint_execution
@trace_method(name="database_service.run_migrations", kind="SERVER")
async def run_migrations(
    request: MigrationRequest,
    background_tasks: BackgroundTasks,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Execute database migrations for a service."""
    correlation_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/database/migrations/run",
        "timestamp.start": start_time.isoformat(),
        "service_name": request.service_name,
        "migration_dir": request.migration_dir,
        "target_revision": request.target_revision or "head",
        "revision": request.revision,
        "run_async": request.run_async,
        "auto_create_service": request.auto_create_service
    })
    
    try:
        # Check if service exists
        service_exists = await db_manager.check_service_exists(request.service_name)
        if not service_exists and not request.auto_create_service:
            # Add span attributes for error
            add_span_attributes({
                "timestamp.end": datetime.utcnow().isoformat(),
                "error.type": "ServiceNotFound",
                "error.message": f"Service '{request.service_name}' not found",
                "success": False
            })
            
            raise HTTPException(
                status_code=404, 
                detail=f"Service '{request.service_name}' not found. Set auto_create_service=true to create it."
            )
        
        # Get migration manager for the service
        migration_manager = await db_manager.get_migration_manager(
            service_name=request.service_name,
            migration_dir=request.migration_dir,
            alembic_config_path=request.alembic_config_path,
            auto_create=request.auto_create_service
        )
        
        if request.run_async:
            # Run migrations in background task with tracing
            @trace_method(name="main.run_migrations_background")
            async def run_migrations_background():
                """Run database migrations in the background."""
                start_time = datetime.utcnow()
                correlation_id = str(uuid.uuid4())
                
                # Add span attributes for context
                add_span_attributes({
                    "correlation_id": correlation_id,
                    "timestamp.start": start_time.isoformat(),
                    "task_type": "background_migration",
                    "target_revision": request.target_revision,
                    "revision": request.revision
                })
                
                try:
                    # Run migrations
                    await db_manager.run_migrations(target=request.target_revision, revision=request.revision)
                    
                    # Add span attributes for success
                    end_time = datetime.utcnow()
                    add_span_attributes({
                        "timestamp.end": end_time.isoformat(),
                        "duration_ms": (end_time - start_time).total_seconds() * 1000,
                        "success": True
                    })
                except Exception as e:
                    # Add span attributes for error
                    end_time = datetime.utcnow()
                    add_span_attributes({
                        "timestamp.end": end_time.isoformat(),
                        "duration_ms": (end_time - start_time).total_seconds() * 1000,
                        "error.type": e.__class__.__name__,
                        "error.message": str(e),
                        "success": False
                    })
                    logger.error(f"Error in background migration: {e}", exc_info=True)
            
            # Add the background task
            background_tasks.add_task(run_migrations_background)
            
            # Add span attributes for async response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "migration.status": "started",
                "migration.async": True,
                "success": True
            })
            
            return MigrationResponse(
                service_name=request.service_name,
                status="started",
                message=f"Migration started asynchronously for {request.service_name}",
                details={
                    "target_revision": request.target_revision or "head",
                    "revision": request.revision,
                    "async": True
                }
            )
        else:
            # Run migrations synchronously
            result = await migration_manager.run_migrations(
                target=request.target_revision,
                revision=request.revision
            )
            
            # Add span attributes for sync response
            end_time = datetime.utcnow()
            add_span_attributes({
                "timestamp.end": end_time.isoformat(),
                "duration_ms": (end_time - start_time).total_seconds() * 1000,
                "migration.status": "completed" if result["success"] else "failed",
                "migration.success": result["success"],
                "migration.message": result["message"],
                "success": result["success"]
            })
            
            return MigrationResponse(
                service_name=request.service_name,
                status="completed" if result["success"] else "failed",
                message=result["message"],
                details=result
            )
    except Exception as e:
        # Add span attributes for error
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        
        logger.error(f"Migration failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Migration failed: {str(e)}")

@app.get("/database/migrations/status/{service_name}")
async def get_migration_status(
    service_name: str,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Get current migration status for a service."""
    try:
        status = await db_manager.get_migration_status(service_name)
        return status
    except Exception as e:
        logger.error(f"Failed to get migration status: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Status check failed: {str(e)}")

# TimescaleDB hypertable endpoints
@app.post("/database/hypertables/create", response_model=HypertableResponse)
@track_endpoint_execution
@trace_method(name="database_service.create_hypertable", kind="SERVER")
async def create_hypertable(
    request: HypertableRequest,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Create a TimescaleDB hypertable."""
    correlation_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/database/hypertables/create",
        "timestamp.start": start_time.isoformat(),
        "table_name": request.table_name,
        "time_column": request.time_column,
        "chunk_time_interval": request.chunk_time_interval,
        "if_not_exists": request.if_not_exists,
        "migrate_data": request.migrate_data,
        "create_index": request.create_index,
        "has_partitioning": request.partitioning_column is not None
    })
    
    try:
        # Create hypertable
        result = await db_manager.create_hypertable(
            table_name=request.table_name,
            time_column=request.time_column,
            chunk_time_interval=request.chunk_time_interval,
            if_not_exists=request.if_not_exists,
            migrate_data=request.migrate_data,
            create_index=request.create_index,
            partitioning_column=request.partitioning_column,
            number_partitions=request.number_partitions
        )
        
        # Update metrics
        update_timescale_metrics()
        
        # Add span attributes for response
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "hypertable.created": True,
            "success": True
        })
        
        return HypertableResponse(
            table_name=request.table_name,
            success=True,
            message=f"Hypertable {request.table_name} created successfully",
            details=result
        )
    except Exception as e:
        # Add span attributes for error
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        
        logger.error(f"Hypertable creation failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Hypertable creation failed: {str(e)}")

@app.get("/database/hypertables/list")
async def list_hypertables(db_manager: DatabaseManager = Depends(get_database_manager)):
    """List all TimescaleDB hypertables."""
    try:
        hypertables = await db_manager.list_hypertables()
        return {"hypertables": hypertables}
    except Exception as e:
        logger.error(f"Failed to list hypertables: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Failed to list hypertables: {str(e)}")

# Continuous aggregates endpoints
@app.post("/database/continuous-aggregates/create")
async def create_continuous_aggregate(
    table_name: str,
    view_name: str,
    time_column: str,
    bucket_width: str,
    aggregations: List[str],
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Create a TimescaleDB continuous aggregate."""
    try:
        result = await db_manager.create_continuous_aggregate(
            table_name=table_name,
            view_name=view_name,
            time_column=time_column,
            bucket_width=bucket_width,
            aggregations=aggregations
        )
        return {"success": True, "view_name": view_name, "result": result}
    except Exception as e:
        logger.error(f"Failed to create continuous aggregate: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Continuous aggregate creation failed: {str(e)}")

@app.post("/database/continuous-aggregates/{view_name}/refresh")
async def refresh_continuous_aggregate(
    view_name: str,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Refresh a continuous aggregate."""
    try:
        await db_manager.refresh_continuous_aggregate(view_name)
        return {"success": True, "view_name": view_name, "message": "Refresh completed"}
    except Exception as e:
        logger.error(f"Failed to refresh continuous aggregate: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Refresh failed: {str(e)}")

# Model management endpoints
@app.post("/database/models/register")
async def register_models(
    request: ModelRegistrationRequest,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Register models for a service."""
    try:
        result = await db_manager.register_models(
            service_name=request.service_name,
            models=request.models,
            auto_create_tables=request.auto_create_tables
        )
        return {"success": True, "registered_models": result}
    except Exception as e:
        logger.error(f"Model registration failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Model registration failed: {str(e)}")

@app.get("/database/models/discover/{service_name}", response_model=ModelDiscoveryResponse)
async def discover_models(
    service_name: str,
    db_manager: DatabaseManager = Depends(get_database_manager)
):
    """Discover models for a service."""
    try:
        models = await db_manager.discover_models(service_name)
        return ModelDiscoveryResponse(
            service_name=service_name,
            models=models,
            discovery_time=datetime.utcnow()
        )
    except Exception as e:
        logger.error(f"Model discovery failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Model discovery failed: {str(e)}")

# Data retention and archival endpoints

@app.get("/database/retention/status")
@trace_method(name="database_service.get_retention_status", kind="SERVER")
async def get_retention_status(rm: RetentionManager = Depends(get_retention_manager)):
    """Get data retention status for all hypertables."""
    correlation_id = str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Add span attributes for request context
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/database/retention/status",
        "timestamp.start": start_time.isoformat()
    })
    
    try:
        status = await rm.get_retention_status()
        
        # Add span attributes for response
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "retention_period_days": status.get("retention_period_days"),
            "hypertable_count": len(status.get("hypertables", [])),
            "success": True
        })
        
        return status
    except Exception as e:
        # Add span attributes for error
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        
        logger.error(f"Failed to get retention status: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Retention status failed: {str(e)}")

@app.post("/database/retention/trigger-archival")
async def trigger_archival(
    table_name: Optional[str] = None,
    rm: RetentionManager = Depends(get_retention_manager)
):
    """Manually trigger data archival for one or all tables."""
    try:
        result = await rm.manually_trigger_archival(table_name)
        return result
    except Exception as e:
        logger.error(f"Failed to trigger archival: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Archival trigger failed: {str(e)}")

# Performance and monitoring endpoints
@app.get("/database/performance/stats")
async def get_performance_stats(db_manager: DatabaseManager = Depends(get_database_manager)):
    """Get database performance statistics."""
    try:
        stats = await db_manager.get_performance_stats()
        return stats
    except Exception as e:
        logger.error(f"Failed to get performance stats: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Performance stats failed: {str(e)}")

@app.get("/database/connections/status")
async def get_connection_status(db_manager: DatabaseManager = Depends(get_database_manager)):
    """Get database connection pool status."""
    try:
        status = await db_manager.get_connection_status()
        return status
    except Exception as e:
        logger.error(f"Failed to get connection status: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Connection status failed: {str(e)}")

# ============================================================================
# KPI STREAMING ENDPOINTS
# ============================================================================

@app.post("/stream/subscribe")
@trace_method(name="database_service.stream_subscribe", kind="SERVER")
async def subscribe_to_stream(
    request: Request,
    kpi_code: str,
    entity_id: str,
    period: str,
    subscriber_id: Optional[str] = None,
    sub_mgr: SubscriberManager = Depends(get_subscriber_manager),
    pub: StreamPublisher = Depends(get_stream_publisher)
):
    """
    Subscribe to a KPI stream
    
    Args:
        kpi_code: KPI code to subscribe to
        entity_id: Entity ID for the KPI
        period: Time period ('minute', 'hour', 'day')
        subscriber_id: Optional subscriber ID (generated if not provided)
    
    Returns:
        Subscription details including subscriber_id and stream_key
    """
    correlation_id = extract_correlation_id_from_headers(request.headers) or str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    # Validate period
    if period not in ['minute', 'hour', 'day']:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid period: {period}. Must be 'minute', 'hour', or 'day'"
        )
    
    # Generate subscriber ID if not provided
    if not subscriber_id:
        subscriber_id = str(uuid.uuid4())
    
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/stream/subscribe",
        "kpi_code": kpi_code,
        "entity_id": entity_id,
        "period": period,
        "subscriber_id": subscriber_id,
        "timestamp.start": start_time.isoformat()
    })
    
    try:
        # Add subscriber
        is_first_subscriber = await sub_mgr.add_subscriber(
            subscriber_id=subscriber_id,
            kpi_code=kpi_code,
            entity_id=entity_id,
            period=period
        )
        
        # Start publishing if this is the first subscriber
        if is_first_subscriber:
            await pub.start_stream(kpi_code, entity_id, period)
            logger.info(f"Started stream for {kpi_code}:{entity_id}:{period}")
        
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        subscriber_count = await sub_mgr.get_subscriber_count(kpi_code, entity_id, period)
        
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "is_first_subscriber": is_first_subscriber,
            "subscriber_count": subscriber_count,
            "success": True
        })
        
        return {
            "subscriber_id": subscriber_id,
            "stream_key": stream_key,
            "kpi_code": kpi_code,
            "entity_id": entity_id,
            "period": period,
            "subscriber_count": subscriber_count,
            "channel": f"kpi.stream.{kpi_code}.{entity_id}.{period}",
            "subscribed_at": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        logger.error(f"Failed to subscribe to stream: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Subscription failed: {str(e)}")

@app.post("/stream/unsubscribe")
@trace_method(name="database_service.stream_unsubscribe", kind="SERVER")
async def unsubscribe_from_stream(
    request: Request,
    subscriber_id: str,
    kpi_code: Optional[str] = None,
    entity_id: Optional[str] = None,
    period: Optional[str] = None,
    sub_mgr: SubscriberManager = Depends(get_subscriber_manager),
    pub: StreamPublisher = Depends(get_stream_publisher)
):
    """
    Unsubscribe from KPI stream(s)
    
    Args:
        subscriber_id: Subscriber ID to unsubscribe
        kpi_code: Optional - specific KPI to unsubscribe from
        entity_id: Optional - specific entity to unsubscribe from
        period: Optional - specific period to unsubscribe from
    
    If kpi_code, entity_id, and period are provided, unsubscribes from that specific stream.
    Otherwise, unsubscribes from all streams.
    
    Returns:
        Unsubscription details
    """
    correlation_id = extract_correlation_id_from_headers(request.headers) or str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/stream/unsubscribe",
        "subscriber_id": subscriber_id,
        "timestamp.start": start_time.isoformat()
    })
    
    try:
        # Remove subscriber
        streams_to_stop = await sub_mgr.remove_subscriber(
            subscriber_id=subscriber_id,
            kpi_code=kpi_code,
            entity_id=entity_id,
            period=period
        )
        
        # Stop publishing for streams with no subscribers
        for stream_key in streams_to_stop:
            details = await sub_mgr.get_stream_details(stream_key)
            if details:
                k_code, e_id, p = details
                await pub.stop_stream(k_code, e_id, p)
                logger.info(f"Stopped stream for {stream_key}")
        
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "streams_stopped": len(streams_to_stop),
            "success": True
        })
        
        return {
            "subscriber_id": subscriber_id,
            "streams_stopped": len(streams_to_stop),
            "stopped_streams": list(streams_to_stop),
            "unsubscribed_at": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        logger.error(f"Failed to unsubscribe from stream: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unsubscription failed: {str(e)}")

@app.get("/stream/status")
@trace_method(name="database_service.stream_status", kind="SERVER")
async def get_stream_status(
    request: Request,
    pub: StreamPublisher = Depends(get_stream_publisher),
    sub_mgr: SubscriberManager = Depends(get_subscriber_manager)
):
    """
    Get status of all active streams
    
    Returns:
        Status information for all active streams including subscriber counts
    """
    correlation_id = extract_correlation_id_from_headers(request.headers) or str(uuid.uuid4())
    start_time = datetime.utcnow()
    
    add_span_attributes({
        "correlation_id": correlation_id,
        "endpoint": "/stream/status",
        "timestamp.start": start_time.isoformat()
    })
    
    try:
        # Get publisher status
        pub_status = await pub.get_status()
        
        # Get subscriber stats
        sub_stats = await sub_mgr.get_stats()
        
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "active_streams": pub_status.get("active_stream_count", 0),
            "total_subscribers": sub_stats.get("total_subscribers", 0),
            "success": True
        })
        
        return {
            "publisher": pub_status,
            "subscribers": sub_stats,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    except Exception as e:
        end_time = datetime.utcnow()
        add_span_attributes({
            "timestamp.end": end_time.isoformat(),
            "duration_ms": (end_time - start_time).total_seconds() * 1000,
            "error.type": e.__class__.__name__,
            "error.message": str(e),
            "success": False
        })
        logger.error(f"Failed to get stream status: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Status retrieval failed: {str(e)}")

@app.post("/stream/heartbeat")
@trace_method(name="database_service.stream_heartbeat", kind="SERVER")
async def stream_heartbeat(
    subscriber_id: str,
    sub_mgr: SubscriberManager = Depends(get_subscriber_manager)
):
    """
    Send heartbeat to keep subscription alive
    
    Args:
        subscriber_id: Subscriber ID to update activity for
    
    Returns:
        Heartbeat acknowledgment
    """
    try:
        await sub_mgr.update_activity(subscriber_id)
        return {
            "subscriber_id": subscriber_id,
            "heartbeat_received": datetime.utcnow().isoformat()
        }
    except Exception as e:
        logger.error(f"Failed to process heartbeat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Heartbeat failed: {str(e)}")

# ============================================================================
# SECURE ARTIFACT STORAGE ENDPOINTS
# ============================================================================

@app.post("/secure/artifacts", response_model=SecureArtifactResponse)
async def store_secure_artifact(
    request: SecureArtifactRequest,
    ssm: SecureStorageManager = Depends(get_secure_storage_manager)
):
    """Store or update a sensitive artifact securely."""
    try:
        artifact = ssm.store_artifact(
            key=request.key,
            value=request.value,
            description=request.description,
            category=request.category
        )
        return artifact
    except Exception as e:
        logger.error(f"Failed to store artifact: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/secure/artifacts/{key}", response_model=SecureArtifactValueResponse)
async def get_secure_artifact(
    key: str,
    ssm: SecureStorageManager = Depends(get_secure_storage_manager)
):
    """Retrieve a secure artifact by key (includes decrypted value)."""
    try:
        artifact = ssm.get_artifact(key)
        if not artifact:
            raise HTTPException(status_code=404, detail="Artifact not found")
        return artifact
    except HTTPException:
        raise
    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Decryption failed: {e}")
    except Exception as e:
        logger.error(f"Failed to retrieve artifact: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/secure/artifacts", response_model=List[SecureArtifactResponse])
async def list_secure_artifacts(
    category: Optional[str] = None,
    ssm: SecureStorageManager = Depends(get_secure_storage_manager)
):
    """List secure artifacts (metadata only)."""
    try:
        return ssm.list_artifacts(category=category)
    except Exception as e:
        logger.error(f"Failed to list artifacts: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/secure/artifacts/{key}")
async def delete_secure_artifact(
    key: str,
    ssm: SecureStorageManager = Depends(get_secure_storage_manager)
):
    """Delete a secure artifact."""
    try:
        deleted = ssm.delete_artifact(key)
        if not deleted:
            raise HTTPException(status_code=404, detail="Artifact not found")
        return {"success": True, "message": f"Artifact {key} deleted"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete artifact: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/secure/rotate-keys")
async def rotate_encryption_keys(
    new_secret_key: str,
    ssm: SecureStorageManager = Depends(get_secure_storage_manager)
):
    """Re-encrypt all artifacts with a new key."""
    try:
        count = ssm.rotate_keys(new_secret_key)
        return {"success": True, "rotated_count": count, "message": "Encryption keys rotated successfully"}
    except Exception as e:
        logger.error(f"Failed to rotate keys: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
