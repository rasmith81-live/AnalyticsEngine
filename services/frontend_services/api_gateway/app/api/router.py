from fastapi import APIRouter

from .v1.analytics import router as analytics_router
from .v1.archive import router as archive_router
from .v1.database import router as database_router
from .v1.messages import router as messages_router
from .v1.messaging import router as messaging_router
from .v1.observability import router as observability_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(analytics_router, prefix="/analytics", tags=["analytics"])
api_router.include_router(archive_router, prefix="/archive", tags=["archive"])
api_router.include_router(database_router, prefix="/database", tags=["database"])
api_router.include_router(messages_router, prefix="/messages", tags=["messages"])
api_router.include_router(messaging_router, prefix="/messaging", tags=["messaging"])
api_router.include_router(observability_router, prefix="/observability", tags=["observability"])
