"""
API Gateway main application.
Provides a unified interface to all downstream services.
"""
import asyncio
import httpx
import logging
import time
import uuid
from contextlib import asynccontextmanager
from typing import Dict, List, Optional, Any
from datetime import datetime

from fastapi import FastAPI, Request, Response, HTTPException, Depends, Header, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocketState
from prometheus_client import start_http_server

from app.core.config import settings
from app.core.logging import setup_logging, get_logger
from app.middleware.authentication import AuthenticationMiddleware
from app.middleware.authorization import AuthorizationMiddleware
from app.middleware.circuit_breaker import CircuitBreakerMiddleware
from app.middleware.correlation import CorrelationMiddleware
from app.middleware.error_handler import ErrorHandlerMiddleware
from app.middleware.metrics import MetricsMiddleware, setup_metrics
from app.middleware.rate_limiting import RateLimitingMiddleware
from app.middleware.tracing import TracingMiddleware, setup_tracing
from app.services.health import HealthService
from app.services.registry import service_registry
from app.core.cache import CacheService as GatewayCache
from app.core.pubsub import pubsub_service
from app.api.router import api_router


# Setup logging
setup_logging()
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for the FastAPI application.
    Handles startup and shutdown events.
    """
    # Startup
    logger.info(f"Starting {settings.SERVICE_NAME}")
    
    
    # Initialize service registry
    from app.services.init_registry import initialize_service_registry
    try:
        logger.info("Initializing service registry")
        registered_services = await initialize_service_registry()
        logger.info(f"Registered {len(registered_services)} services")
    except Exception as e:
        logger.error(f"Error initializing service registry: {str(e)}")
    
    # Start PubSub service
    await pubsub_service.start()
    
    # Check service health
    await service_registry.check_all_services_health()


    # Yield control to FastAPI
    yield
    
    # Shutdown
    logger.info(f"Shutting down {settings.SERVICE_NAME}")
    
    # Stop PubSub service
    await pubsub_service.stop()

# Create FastAPI application
app = FastAPI(
    title=settings.SERVICE_NAME,
    description="API Gateway for Supply Chain Analytics Platform",
    version="1.0.0",
    lifespan=lifespan
)

# Add middleware
# Initialize tracing and metrics
setup_tracing(app)
setup_metrics(app)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(ErrorHandlerMiddleware)
app.add_middleware(CorrelationMiddleware)
app.add_middleware(MetricsMiddleware)
app.add_middleware(TracingMiddleware)
app.add_middleware(
    RateLimitingMiddleware,
    limit=settings.RATE_LIMIT,
    window=settings.RATE_LIMIT_WINDOW
)
app.add_middleware(
    CircuitBreakerMiddleware,
    failure_threshold=settings.CIRCUIT_BREAKER_THRESHOLD,
    recovery_timeout=settings.CIRCUIT_BREAKER_RECOVERY_TIME
)
app.add_middleware(
    AuthenticationMiddleware,
    exclude_paths=["/health", "/metrics", "/docs", "/redoc", "/openapi.json"],
    exclude_prefixes=["/auth/"]
)
app.add_middleware(
    AuthorizationMiddleware,
    exclude_paths=["/health", "/metrics", "/docs", "/redoc", "/openapi.json"],
    exclude_prefixes=["/auth/"]
)


# The GraphQL app is mounted inside the lifespan, after the service registry is ready.

# Include the existing API router
app.include_router(api_router)

@app.get("/health")
async def health_check(detailed: bool = False):
    """
    Health check endpoint.
    Aggregates health status from all services.
    
    Args:
        detailed: Whether to include detailed health information
        
    Returns:
        Health status
    """
    health_status = await HealthService.get_health_status(include_details=detailed)
    return health_status.model_dump()

@app.get("/services")
async def list_services():
    """
    List all registered services.
    
    Returns:
        List of services
    """
    services = await service_registry.get_all_services()
    return {"services": [service.model_dump() for service in services]}

@app.websocket("/ws/subscribe/{channel}")
async def websocket_subscribe(websocket: WebSocket, channel: str):
    """
    WebSocket endpoint for subscribing to Redis channels.
    Streams messages from the specified channel to the client.
    """
    await websocket.accept()
    
    try:
        # Create a queue for messages
        message_queue = asyncio.Queue()
        
        # Message handler
        async def message_handler(ch: str, msg: Any):
            await message_queue.put(msg)
        
        # Subscribe to channel
        await pubsub_service.subscribe(channel, message_handler)
        
        # Send initial connection message
        await websocket.send_json({
            "type": "connection_established",
            "channel": channel,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Stream messages to client
        try:
            while True:
                # Wait for messages from the queue
                message = await message_queue.get()
                
                # Send message to client
                await websocket.send_json({
                    "type": "message",
                    "channel": channel,
                    "data": message,
                    "timestamp": datetime.utcnow().isoformat()
                })
        except WebSocketDisconnect:
            # Unsubscribe when client disconnects
            await pubsub_service.unsubscribe(channel, message_handler)
            logger.info(f"WebSocket client disconnected from channel {channel}")
    except Exception as e:
        logger.error(f"Error in WebSocket connection: {str(e)}")
        if websocket.client_state != WebSocketState.DISCONNECTED:
            await websocket.close(code=1011, reason=f"Server error: {str(e)}")

# Root endpoint
@app.get("/")
async def root():
    """
    Root endpoint.
    
    Returns:
        Basic information about the API Gateway
    """
    return {
        "service": settings.SERVICE_NAME,
        "version": "1.0.0",
        "status": "running",
        "docs_url": "/docs"
    }