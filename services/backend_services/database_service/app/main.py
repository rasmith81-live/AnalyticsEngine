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
from .news_consumer import NewsConsumer
from .models import (
    QueryRequest, QueryResponse, CommandRequest, CommandResponse,
    MigrationRequest, MigrationResponse, HypertableRequest, HypertableResponse,
    ModelRegistrationRequest, ModelDiscoveryResponse, HealthResponse
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
news_consumer = None
service_start_time = datetime.utcnow()

# Background task cancellation handles
metrics_export_task = None
system_metrics_task = None

@asynccontextmanager
@trace_method(name="main.lifespan")
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global database_manager, retention_manager, messaging_client, telemetry_consumer, command_consumer, metrics_export_task, system_metrics_task
    
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

        # Initialize and start news consumer
        news_consumer = NewsConsumer(
            database_manager=database_manager,
            messaging_client=messaging_client
        )
        await news_consumer.start()
        
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

        # Stop news consumer
        if news_consumer:
            await news_consumer.stop()
        
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
            query_type=request.query_type,
            query=request.query,
            parameters=request.parameters
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
            "result_size": len(result) if isinstance(result, list) else 1,
            "success": True
        })
        
        return QueryResponse(
            success=True,
            result=result,
            execution_time=execution_time
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
