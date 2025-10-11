"""
API package for Service A.

This package contains all API routers and endpoints for Service A.
"""

from fastapi import APIRouter

from .endpoints import router as endpoints_router

# Main API router
router = APIRouter()

# Include all endpoint routers
router.include_router(endpoints_router)
