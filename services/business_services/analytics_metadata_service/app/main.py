"""
Analytics Metadata Service

Serves KPI, Object Model, Module, and Value Chain definitions via REST API.
This is the single source of truth for all analytics metadata.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from .config import get_settings
from .loader import get_loader
from .api import kpis, object_models, modules, value_chains
from fastapi import APIRouter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    settings = get_settings()
    
    logger.info(f"Starting {settings.service_name} v{settings.version}")
    logger.info(f"Environment: {settings.environment}")
    
    # Load all definitions on startup
    loader = get_loader()
    loader.load_all()
    
    stats = loader.get_stats()
    logger.info(f"Loaded definitions: {stats}")
    
    yield
    
    logger.info("Shutting down Analytics Metadata Service")


# Create FastAPI app
app = FastAPI(
    title="Analytics Metadata Service",
    description="Single source of truth for KPI, Object Model, Module, and Value Chain definitions",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(kpis.router)
app.include_router(object_models.router)
app.include_router(modules.router)
app.include_router(value_chains.router)


# ============================================================================
# Root Endpoints
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint with service information."""
    settings = get_settings()
    loader = get_loader()
    stats = loader.get_stats()
    
    return {
        "service": settings.service_name,
        "version": settings.version,
        "environment": settings.environment,
        "status": "healthy",
        "definitions": stats,
        "endpoints": {
            "kpis": "/kpis",
            "object_models": "/object-models",
            "modules": "/modules",
            "value_chains": "/value-chains",
            "docs": "/docs",
            "health": "/health"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    settings = get_settings()
    loader = get_loader()
    stats = loader.get_stats()
    
    return {
        "status": "healthy",
        "service": settings.service_name,
        "version": settings.version,
        "definitions_loaded": stats
    }


@app.get("/stats")
async def get_stats():
    """Get statistics about loaded definitions."""
    loader = get_loader()
    return loader.get_stats()


@app.post("/admin/reload")
async def reload_definitions():
    """Reload all definitions from disk without restarting the service."""
    loader = get_loader()
    loader.load_all()
    stats = loader.get_stats()
    logger.info(f"Reloaded definitions: {stats}")
    return {
        "status": "success",
        "message": "Definitions reloaded successfully",
        "definitions": stats
    }


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level.lower()
    )
