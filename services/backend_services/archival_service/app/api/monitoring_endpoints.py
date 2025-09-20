"""
API endpoints for monitoring the archival service.

This module provides endpoints for checking health status and retrieving metrics
about the archival process.
"""

import logging
import uuid
from datetime import datetime
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, Request, status

from ..monitoring import ArchivalMonitor
from ..telemetry import trace_method, add_span_attributes

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(tags=["monitoring"])

# Global monitor instance
archival_monitor = ArchivalMonitor()


@router.get("/health", response_model=Dict)
@trace_method(name="get_health", kind="SERVER")
async def get_health(request: Request):
    """
    Get the health status of the archival service.
    
    Returns:
        Dict: Health status information including:
            - status: "healthy", "warning", or "critical"
            - total_events: Total number of events processed
            - success_rate: Percentage of successful archival operations
            - avg_processing_time_ms: Average processing time in milliseconds
            - events_last_hour: Number of events processed in the last hour
            - time_since_last_event_seconds: Time since the last event was processed
            - issues: List of identified issues
            - last_updated: Timestamp of the last update
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "monitoring.health",
            "timestamp": datetime.utcnow().isoformat()
        })
        
        health_status = await archival_monitor.get_health_status()
        
        # Add span attributes for health status
        add_span_attributes({
            "health.status": health_status.get("status", "unknown"),
            "health.total_events": health_status.get("total_events", 0),
            "health.success_rate": health_status.get("success_rate", 0)
        })
        
        # Set HTTP status code based on health status
        if health_status["status"] == "critical":
            return HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=health_status
            )
        
        return health_status
    except Exception as e:
        logger.exception("Error retrieving health status")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving health status: {str(e)}"
        )


@router.get("/metrics", response_model=Dict)
@trace_method(name="get_metrics", kind="SERVER")
async def get_metrics(request: Request):
    """
    Get detailed metrics about the archival process.
    
    Returns:
        Dict: Comprehensive metrics including:
            - total_events_received: Total number of events received
            - total_archived_chunks: Total number of successfully archived chunks
            - total_failed_chunks: Total number of failed archival attempts
            - chunks_archived_last_hour: Number of chunks archived in the last hour
            - chunks_failed_last_hour: Number of chunks that failed archival in the last hour
            - avg_processing_time_ms: Average processing time in milliseconds
            - max_processing_time_ms: Maximum processing time in milliseconds
            - total_archived_bytes: Total bytes archived
            - avg_chunk_size_bytes: Average chunk size in bytes
            - recent_events: List of recent archival events
            - last_updated: Timestamp of the last metrics update
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "monitoring.metrics",
            "timestamp": datetime.utcnow().isoformat()
        })
        
        metrics = await archival_monitor.get_metrics()
        
        # Add span attributes for key metrics
        add_span_attributes({
            "metrics.total_events_received": metrics.get("total_events_received", 0),
            "metrics.total_archived_chunks": metrics.get("total_archived_chunks", 0),
            "metrics.total_failed_chunks": metrics.get("total_failed_chunks", 0),
            "metrics.avg_processing_time_ms": metrics.get("avg_processing_time_ms", 0)
        })
        
        return metrics
    except Exception as e:
        logger.exception("Error retrieving metrics")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving metrics: {str(e)}"
        )


@router.get("/recent-events", response_model=List[Dict])
@trace_method(name="get_recent_events", kind="SERVER")
async def get_recent_events(
    request: Request,
    limit: Optional[int] = Query(10, description="Maximum number of events to return")
):
    """
    Get recent archival events.
    
    Args:
        limit: Maximum number of events to return (default: 10)
    
    Returns:
        List[Dict]: List of recent archival events
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "monitoring.recent_events",
            "timestamp": datetime.utcnow().isoformat(),
            "request.limit": limit
        })
        
        metrics = await archival_monitor.get_metrics()
        events = metrics.get("recent_events", [])
        
        # Get the most recent events up to the limit
        result = events[-limit:] if events else []
        
        # Add span attributes for response
        add_span_attributes({
            "response.event_count": len(result)
        })
        
        return result
    except Exception as e:
        logger.exception("Error retrieving recent events")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving recent events: {str(e)}"
        )


# Export the monitor instance for use in other modules
@trace_method(name="get_monitor", kind="INTERNAL")
def get_monitor() -> ArchivalMonitor:
    """
    Get the archival monitor instance.
    
    Returns:
        ArchivalMonitor: The archival monitor instance.
    """
    # Add span attributes for monitor access
    add_span_attributes({
        "monitor.access_timestamp": datetime.utcnow().isoformat(),
        "monitor.singleton": True
    })
    
    return archival_monitor
