# =============================================================================
# Multi-Agent Service Main Application
# Based on: Tangi Vass - "Turning AI Coding Agents into Senior Engineering Peers"
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""FastAPI application for the Multi-Agent Service."""

from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from .config import get_settings
from .api import agent_routes, blackboard_routes, dashboard_routes, health, registry_routes, template_routes, session_routes
from .observability import setup_observability
from .metrics import get_metrics, get_metrics_content_type, set_service_info

logger = logging.getLogger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler for startup and shutdown."""
    import asyncio
    
    # Startup
    logger.info(f"Starting {settings.SERVICE_NAME} v{settings.SERVICE_VERSION}")
    
    # Initialize Redis connection for blackboard
    from .blackboard.store import RedisBlackboardStore
    app.state.blackboard_store = await RedisBlackboardStore.create(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        db=settings.REDIS_DB,
        password=settings.REDIS_PASSWORD
    )
    logger.info("Blackboard store initialized")
    
    # Start Redis command consumer for L2 communication
    from .messaging import get_command_consumer
    consumer = get_command_consumer()
    try:
        await consumer.start()
        app.state.command_consumer = consumer
        app.state.consumer_task = asyncio.create_task(consumer.consume())
        logger.info("Redis command consumer started")
    except Exception as e:
        logger.warning(f"Failed to start command consumer: {e}")
    
    # Set service info for metrics
    set_service_info()
    
    yield
    
    # Shutdown
    logger.info(f"Shutting down {settings.SERVICE_NAME}")
    
    # Stop command consumer
    if hasattr(app.state, 'consumer_task'):
        app.state.consumer_task.cancel()
        try:
            await app.state.consumer_task
        except asyncio.CancelledError:
            pass
    if hasattr(app.state, 'command_consumer'):
        await app.state.command_consumer.stop()
    
    if hasattr(app.state, 'blackboard_store'):
        await app.state.blackboard_store.close()


app = FastAPI(
    title="Multi-Agent Service",
    description="Agent contract infrastructure for AnalyticsEngine",
    version=settings.SERVICE_VERSION,
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup observability (OpenTelemetry)
setup_observability(app)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(agent_routes.router, prefix="/agents", tags=["Agents"])
app.include_router(blackboard_routes.router, prefix="/blackboard", tags=["Blackboard"])
app.include_router(dashboard_routes.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(registry_routes.router, prefix="/api/v1", tags=["Registry"])  # Phase 18
app.include_router(template_routes.router, prefix="/api/v1", tags=["Templates"])  # Phase 19
app.include_router(session_routes.router, prefix="/api/v1/agents", tags=["Sessions"])  # Phase 20


@app.get("/metrics", tags=["Observability"])
async def metrics():
    """Prometheus metrics endpoint."""
    metrics_data = get_metrics()
    if metrics_data is None:
        return Response(
            content="Metrics not available",
            media_type="text/plain",
            status_code=503
        )
    return Response(
        content=metrics_data,
        media_type=get_metrics_content_type()
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG
    )
