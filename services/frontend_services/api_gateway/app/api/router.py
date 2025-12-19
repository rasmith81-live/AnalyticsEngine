from fastapi import APIRouter

from .v1.analytics import router as analytics_router
from .v1.archive import router as archive_router
from .v1.database import router as database_router
from .v1.messages import router as messages_router
from .v1.messaging import router as messaging_router
from .v1.observability import router as observability_router

# Business Service Routers
from .v1.metadata import router as metadata_router
from .v1.calculations import router as calculations_router
from .v1.config import router as config_router
from .v1.connector import router as connector_router
from .v1.ingestion import router as ingestion_router
from .v1.entity_resolution import router as entity_resolution_router
from .v1.conversation import router as conversation_router
from .v1.metadata_ingestion import router as metadata_ingestion_router

api_router = APIRouter(prefix="/api/v1")

# Existing Backend Service Routes
api_router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
api_router.include_router(archive_router, prefix="/archive", tags=["archive"])
api_router.include_router(database_router, prefix="/database", tags=["database"])
api_router.include_router(messages_router, prefix="/messages", tags=["messages"])
api_router.include_router(messaging_router, prefix="/messaging", tags=["messaging"])
api_router.include_router(observability_router, prefix="/observability", tags=["observability"])

# New Business Service Routes
api_router.include_router(metadata_router, prefix="/metadata", tags=["metadata"])
api_router.include_router(calculations_router, prefix="/calculations", tags=["calculations"])
api_router.include_router(config_router, prefix="/config", tags=["config"])
api_router.include_router(connector_router, prefix="/connector", tags=["connector"])
api_router.include_router(ingestion_router, prefix="/ingestion", tags=["ingestion"])
api_router.include_router(entity_resolution_router, prefix="/entity-resolution", tags=["entity-resolution"])
api_router.include_router(conversation_router, prefix="/conversation", tags=["conversation"])
api_router.include_router(metadata_ingestion_router, prefix="/metadata-ingestion", tags=["metadata-ingestion"])
