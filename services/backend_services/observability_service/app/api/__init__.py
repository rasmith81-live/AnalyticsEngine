"""
API package for Observability Service

This package contains the API routers for the Observability Service.
"""

from fastapi import APIRouter

from .traces import router as traces_router
from .metrics import router as metrics_router
from .health import router as health_router
from .dependencies import router as dependencies_router
from .events import router as events_router
from .query import router as query_router

# Create API router
api_router = APIRouter()

# Include routers
api_router.include_router(traces_router, prefix="/traces", tags=["Traces"])
api_router.include_router(metrics_router, prefix="/metrics", tags=["Metrics"])
api_router.include_router(health_router, prefix="/health", tags=["Health"])
api_router.include_router(dependencies_router, prefix="/dependencies", tags=["Dependencies"])
api_router.include_router(events_router, prefix="/events", tags=["Events"])
api_router.include_router(query_router, prefix="/query", tags=["Query"])
