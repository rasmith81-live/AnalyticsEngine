from fastapi import APIRouter, Query, HTTPException, status
from typing import Dict, List
import os

from ..code_traceability import tracer
from ..models import UnusedFilesResponse, ErrorResponse

router = APIRouter()

@router.get(
    "/unused-files",
    response_model=UnusedFilesResponse,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
async def get_unused_files(
    period_seconds: int = Query(86400, description="Period in seconds to check for unused files (default: 24h)"),
    root_dir: str = Query(None, description="Root directory to scan (defaults to current working directory)")
):
    """
    Identify files that have not been utilized in the given period.
    """
    try:
        # Default to the app directory if not specified
        if not root_dir:
            # Assuming we are running from services/backend_services/observability_service
            # We want to scan the 'app' directory by default
            current_dir = os.getcwd()
            root_dir = os.path.join(current_dir, "app")
            
        return tracer.get_unused_files(root_dir, period_seconds)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to analyze unused files: {str(e)}"
        )
