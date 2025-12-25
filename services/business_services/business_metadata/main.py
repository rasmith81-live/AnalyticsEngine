"""Business Metadata Service - Main FastAPI Application.

Integrates with backend services:
- database_service for database and Redis
- messaging_service for event publishing
"""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pathlib import Path

from .config import settings
from . import dependencies
from .api import router as metadata_router
from .api.schema_extraction_api import router as schema_extraction_router
from .consumers import ConversationEventConsumer
from .services.entity_event_handler import EntityEventHandler
from .services.schema_metrics import SchemaMetrics

# Configure logging
logging.basicConfig(
    level=settings.log_level,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global consumer and handler instances
conversation_consumer: ConversationEventConsumer = None
entity_event_handler: EntityEventHandler = None
schema_metrics: SchemaMetrics = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle manager for FastAPI application."""
    global conversation_consumer, entity_event_handler, schema_metrics
    
    # Startup
    logger.info(f"Starting {settings.service_name} service...")
    
    try:
        # Initialize backend services
        await dependencies.initialize_backend_services()
        logger.info("Backend services initialized successfully")
        
        # Run migrations
        logger.info("Running database migrations...")
        await dependencies.db_manager.run_migrations(service_name=settings.service_name)
        logger.info("Migrations completed successfully")
        
        # Initialize Schema Metrics (with ObservabilityClient if available)
        try:
            from ..support_services.observability_service.app.observability_client import ObservabilityClient
            obs_client = ObservabilityClient(
                service_name=settings.service_name,
                observability_url=settings.observability_url if hasattr(settings, 'observability_url') else None
            )
            schema_metrics = SchemaMetrics(observability_client=obs_client)
            logger.info("Schema Metrics initialized with ObservabilityClient")
        except Exception as e:
            logger.warning(f"Could not initialize ObservabilityClient: {e}. Schema Metrics will run without observability.")
            schema_metrics = SchemaMetrics(observability_client=None)
        
        # Initialize and start Entity Event Handler
        entity_event_handler = EntityEventHandler(
            db_manager=dependencies.db_manager,
            messaging_client=dependencies.messaging_client,
            event_publisher=dependencies.event_publisher,
            output_dir=Path("schemas")
        )
        # Pass schema_metrics to the handler's extractor
        entity_event_handler.extractor.metrics = schema_metrics
        await entity_event_handler.start()
        logger.info("Entity Event Handler started - listening for entity events")
        
        # Initialize and start Conversation Event Consumer
        conversation_consumer = ConversationEventConsumer(
            db_manager=dependencies.db_manager,
            messaging_client=dependencies.messaging_client,
            event_publisher=dependencies.event_publisher
        )
        await conversation_consumer.start()
        logger.info("Conversation Event Consumer started")
        
        logger.info(f"{settings.service_name} service started on port {settings.service_port}")
        
        yield
        
    finally:
        # Shutdown
        logger.info(f"Shutting down {settings.service_name} service...")
        
        if entity_event_handler:
            await entity_event_handler.stop()
            logger.info("Entity Event Handler stopped")
        
        if conversation_consumer:
            await conversation_consumer.stop()
            logger.info("Conversation Event Consumer stopped")
            
        await dependencies.shutdown_backend_services()
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
app.include_router(schema_extraction_router)


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
