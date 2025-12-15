"""Business Metadata Service - Main FastAPI Application.

Integrates with backend services:
- database_service for database and Redis
- messaging_service for event publishing
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .dependencies import initialize_backend_services, shutdown_backend_services, db_manager
from .api import router as metadata_router

# Configure logging
logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for FastAPI application."""
    # Startup
    logger.info(f"Starting {settings.service_name} service...")
    
    try:
        # Initialize backend services
        await initialize_backend_services()
        logger.info("Backend services initialized successfully")
        
        # Run migrations
        logger.info("Running database migrations...")
        await db_manager.run_migrations(service_name=settings.service_name)
        logger.info("Migrations completed successfully")
        
        logger.info(f"{settings.service_name} service started on port {settings.service_port}")
        
        yield
        
    finally:
        # Shutdown
        logger.info(f"Shutting down {settings.service_name} service...")
        await shutdown_backend_services()
        logger.info("Backend services shut down successfully")


# Create FastAPI app
app = FastAPI(
    title="Business Metadata Service",
    description="Data-driven metadata management for analytics ontology",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(metadata_router)


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "service": settings.service_name,
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }


# Health check
@app.get("/health")
async def health():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": settings.service_name
    }


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=settings.service_port,
        reload=settings.debug,
        log_level=settings.log_level.lower()
    )
