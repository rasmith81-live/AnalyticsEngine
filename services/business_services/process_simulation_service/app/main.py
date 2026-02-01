"""Process Simulation Service - Main Application.

Discrete event simulation for business process scenarios and what-if analysis.
"""

import logging
import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router as api_router
from .config import get_settings

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global service start time
service_start_time = time.time()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    global service_start_time
    service_start_time = time.time()
    
    settings = get_settings()
    logger.info(f"Starting {settings.service_name} v{settings.service_version}")
    
    # Startup tasks
    try:
        logger.info("Process Simulation Service started successfully")
        yield
    except Exception as e:
        logger.error(f"Failed to start Process Simulation Service: {e}")
        raise
    finally:
        # Shutdown tasks
        logger.info("Process Simulation Service shutdown complete")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    
    app = FastAPI(
        title="Process Simulation Service",
        description="Discrete event simulation for business process scenarios and what-if analysis",
        version=settings.service_version,
        lifespan=lifespan,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json"
    )
    
    # Add CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Include API routes
    app.include_router(api_router, prefix="/api/v1")
    
    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "service": settings.service_name,
            "version": settings.service_version,
            "status": "running"
        }
    
    # Health check
    @app.get("/health")
    async def health():
        return {"status": "healthy"}
    
    return app


# Create the application instance
app = create_app()


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )
