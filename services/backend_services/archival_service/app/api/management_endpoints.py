"""
API endpoints for archival management operations.

This module provides endpoints for managing the archival process,
including retention status, archival statistics, and triggering archival operations.
"""

import logging
import uuid
from datetime import datetime
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status

from ..config import settings
from ..management import (
    ArchivalManager, 
    ArchivalStats, 
    RetentionStatus, 
    get_archival_manager
)
from ..telemetry import trace_method, add_span_attributes

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(tags=["management"])


@trace_method(name="get_manager", kind="INTERNAL")
def get_manager() -> ArchivalManager:
    """Get the archival manager instance.
    
    Returns:
        ArchivalManager: The archival manager instance.
    """
    # Add span attributes for manager creation
    add_span_attributes({
        "manager.database_service_url": settings.database_service_url,
        "manager.archival_service_url": f"http://{settings.host}:{settings.port}",
        "manager.access_timestamp": datetime.utcnow().isoformat()
    })
    
    return get_archival_manager(
        database_service_url=settings.database_service_url,
        archival_service_url=f"http://{settings.host}:{settings.port}"
    )


@router.get("/retention/status", response_model=RetentionStatus)
@trace_method(name="get_retention_status", kind="SERVER")
async def get_retention_status(
    request: Request,
    manager: ArchivalManager = Depends(get_manager)
):
    """
    Get the current retention status for all hypertables.
    
    Returns:
        RetentionStatus: The current retention status.
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "management.retention_status",
            "timestamp": datetime.utcnow().isoformat()
        })
        
        retention_status = await manager.get_retention_status()
        
        # Add span attributes for retention status
        add_span_attributes({
            "retention.total_tables": len(retention_status.tables),
            "retention.total_size_bytes": retention_status.total_size_bytes,
            "retention.oldest_data": retention_status.oldest_data.isoformat() if retention_status.oldest_data else None
        })
        
        return retention_status
    except Exception as e:
        logger.exception("Error retrieving retention status")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving retention status: {str(e)}"
        )


@router.get("/stats", response_model=ArchivalStats)
@trace_method(name="get_archival_stats", kind="SERVER")
async def get_archival_stats(
    request: Request,
    manager: ArchivalManager = Depends(get_manager)
):
    """
    Get statistics about the archival process.
    
    Returns:
        ArchivalStats: Statistics about the archival process.
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "management.archival_stats",
            "timestamp": datetime.utcnow().isoformat()
        })
        
        stats = await manager.calculate_archival_stats()
        
        # Add span attributes for archival stats
        add_span_attributes({
            "archival.total_archived_bytes": stats.total_archived_bytes,
            "archival.total_archived_chunks": stats.total_archived_chunks,
            "archival.avg_chunk_size_bytes": stats.avg_chunk_size_bytes,
            "archival.compression_ratio": stats.compression_ratio
        })
        
        return stats
    except Exception as e:
        logger.exception("Error calculating archival statistics")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error calculating archival statistics: {str(e)}"
        )


@router.get("/health", response_model=Dict)
@trace_method(name="get_services_health", kind="SERVER")
async def get_services_health(
    request: Request,
    manager: ArchivalManager = Depends(get_manager)
):
    """
    Get health status of both the Database Service and Archival Service.
    
    Returns:
        Dict: Health status of both services.
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "management.services_health",
            "timestamp": datetime.utcnow().isoformat()
        })
        
        health_status = await manager.get_health_status()
        
        # Add span attributes for services health
        for service, details in health_status.items():
            add_span_attributes({
                f"health.{service}.status": details.get("status", "unknown")
            })
        
        return health_status
    except Exception as e:
        logger.exception("Error retrieving services health status")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving services health status: {str(e)}"
        )


@router.post("/trigger/{table_name}", response_model=Dict)
@trace_method(name="trigger_archival", kind="SERVER")
async def trigger_archival(
    table_name: str,
    request: Request,
    manager: ArchivalManager = Depends(get_manager)
):
    """
    Manually trigger archival for a specific table.
    
    Args:
        table_name: Name of the table to archive.
        
    Returns:
        Dict: Response from the API.
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "management.trigger_archival",
            "timestamp": datetime.utcnow().isoformat(),
            "archival.table_name": table_name
        })
        
        result = await manager.trigger_archival(table_name)
        
        # Add span attributes for trigger result
        add_span_attributes({
            "archival.trigger_success": result.get("success", False),
            "archival.job_id": result.get("job_id", "unknown")
        })
        
        return result
    except Exception as e:
        logger.exception(f"Error triggering archival for table {table_name}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error triggering archival: {str(e)}"
        )


@router.get("/data/{table_name}", response_model=Dict[str, Any])
@trace_method(name="get_archived_data", kind="SERVER")
async def get_archived_data(
    table_name: str,
    request: Request,
    start_time: str = Query(..., description="Start time in ISO format"),
    end_time: str = Query(..., description="End time in ISO format"),
    limit: int = Query(100, description="Maximum number of records to return"),
    offset: int = Query(0, description="Offset for pagination"),
    columns: Optional[str] = Query(None, description="Comma-separated list of columns to include"),
    metadata_only: bool = Query(False, description="If true, returns only metadata without data"),
    optimize_cost: bool = Query(True, description="If true, optimizes for compute cost over performance")
) -> Dict[str, Any]:
    """Retrieve archived data for a specific table within a time frame.
    
    Args:
        table_name: Name of the table to retrieve data from
        start_time: Start time in ISO format
        end_time: End time in ISO format
        limit: Maximum number of records to return (default: 100)
        offset: Offset for pagination
        columns: Optional comma-separated list of columns to include (reduces data transfer)
        metadata_only: If true, returns only metadata without actual data
        optimize_cost: If true, optimizes for compute cost over performance
        
    Returns:
        Dict with retrieved data and metadata
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "management.get_archived_data",
            "timestamp": datetime.utcnow().isoformat(),
            "archival.table_name": table_name,
            "archival.start_time": start_time,
            "archival.end_time": end_time,
            "archival.limit": limit,
            "archival.offset": offset,
            "archival.metadata_only": metadata_only,
            "archival.optimize_cost": optimize_cost
        })
        
        # Process column filtering if provided
        column_list = None
        if columns:
            column_list = [col.strip() for col in columns.split(',')]
            add_span_attributes({"archival.columns": columns})
        
        # If metadata_only is true, set limit to 0 to avoid retrieving actual data
        effective_limit = 0 if metadata_only else limit
        
        result = await get_manager().retrieve_archived_data(
            table_name=table_name,
            start_time=start_time,
            end_time=end_time,
            limit=effective_limit,
            offset=offset,
            columns=column_list,
            optimize_cost=optimize_cost
        )
        
        # Add span attributes for result
        add_span_attributes({
            "archival.result_count": len(result.get("data", [])),
            "archival.total_count": result.get("metadata", {}).get("total_count", 0),
            "archival.data_size_bytes": len(str(result.get("data", []))) if not metadata_only else 0
        })
        
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error retrieving archived data: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Error retrieving archived data: {str(e)}")
