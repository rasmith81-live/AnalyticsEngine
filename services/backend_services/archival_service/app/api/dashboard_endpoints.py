"""
API endpoints for the archival dashboard.

This module provides endpoints for retrieving dashboard data including:
- Combined system status
- Detailed metrics
- Retention information
- Recent events
- Issues and alerts
"""

import logging
import uuid
from datetime import datetime
from typing import Dict, List, Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Request, status
import httpx

from ..config import settings
from ..management import (
    ArchivalManager,
    ArchivalStats,
    RetentionStatus,
    get_archival_manager
)
from ..tasks import get_task_manager
from ..monitoring import get_archival_monitor
from ..telemetry import trace_method, add_span_attributes

# Configure logging
logger = logging.getLogger(__name__)

# Create router
router = APIRouter(tags=["dashboard"])


@trace_method(name="get_dashboard_manager", kind="INTERNAL")
def get_manager() -> ArchivalManager:
    """Get the archival manager instance."""
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


@router.get("/system-status")
@trace_method(name="get_system_status", kind="SERVER")
async def get_system_status(request: Request):
    """
    Get the combined system status of both Database and Archival services.
    
    Returns:
        Dict: Combined system status information
    """
    try:
        # Get archival manager
        manager = get_archival_manager()
        
        # Get database service health
        db_health = await manager.get_database_health()
        
        # Get archival service health
        archival_health = {
            "status": "healthy",
            "messaging_connected": True,
            "lakehouse_connected": True,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        try:
            # Get monitoring health
            monitor = get_archival_monitor()
            monitoring_health = await monitor.get_health_status()
            archival_health["monitoring_health"] = monitoring_health
        except Exception as e:
            logger.error(f"Error getting monitoring health: {e}")
            archival_health["monitoring_health"] = {
                "status": "warning",
                "issues": [f"Error getting monitoring health: {str(e)}"]
            }
        
        try:
            # Get task manager health
            task_manager = get_task_manager()
            task_health = await task_manager.get_health_status()
            archival_health["management_health"] = task_health
        except Exception as e:
            logger.error(f"Error getting task manager health: {e}")
            archival_health["management_health"] = {
                "status": "warning",
                "issues": [f"Error getting task manager health: {str(e)}"]
            }
        
        # Determine overall system status
        system_status = "healthy"
        if db_health.get("status") == "critical" or archival_health.get("status") == "critical":
            system_status = "critical"
        elif db_health.get("status") == "degraded" or archival_health.get("status") == "degraded":
            system_status = "degraded"
            
        # Add span attributes for system status
        add_span_attributes({
            "system.status": system_status,
            "database.status": db_health.get("status", "unknown"),
            "archival.status": archival_health.get("status", "unknown"),
            "monitoring.status": archival_health.get("monitoring_health", {}).get("status", "unknown"),
            "management.status": archival_health.get("management_health", {}).get("status", "unknown")
        })
        
        return {
            "status": system_status,
            "timestamp": datetime.utcnow().isoformat(),
            "database_service": db_health,
            "archival_service": archival_health
        }
    except Exception as e:
        logger.exception("Error retrieving system status")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving system status: {str(e)}"
        )


@router.get("/dashboard-metrics")
@trace_method(name="get_dashboard_metrics", kind="SERVER")
async def get_dashboard_metrics(request: Request):
    """
    Get comprehensive metrics for the dashboard.
    
    Returns:
        Dict: Combined metrics from archival and database services
    """
    try:
        # Get archival manager
        manager = get_archival_manager()
        
        # Get retention status
        retention = await manager.get_retention_status()
        
        # Get archival metrics
        monitor = get_archival_monitor()
        archival_metrics = await monitor.get_metrics()
        
        # Get archival stats
        archival_stats = await manager.calculate_archival_stats()
        
        # Calculate additional metrics
        total_events = archival_metrics.get("total_events_received", 0)
        total_archived = archival_metrics.get("total_archived_chunks", 0)
        total_failed = archival_metrics.get("total_failed_chunks", 0)
        
        success_rate = 0
        if total_events > 0:
            success_rate = (total_archived / total_events) * 100
        
        # Calculate archival progress
        total_chunks = sum(table.total_chunks for table in retention.tables)
        eligible_chunks = sum(table.chunks_to_archive for table in retention.tables)
        
        archival_progress = 0
        if total_chunks > 0:
            archival_progress = ((total_chunks - eligible_chunks) / total_chunks) * 100
        
        # Combine all metrics
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "archival_metrics": archival_metrics,
            "archival_stats": archival_stats.model_dump(),
            "retention_status": retention.model_dump(),
            "calculated_metrics": {
                "success_rate": success_rate,
                "archival_progress": archival_progress,
                "total_chunks": total_chunks,
                "eligible_chunks": eligible_chunks,
                "archived_chunks": total_archived,
                "failed_chunks": total_failed
            }
        }
    except Exception as e:
        logger.exception("Error retrieving dashboard metrics")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving dashboard metrics: {str(e)}"
        )


@router.get("/dashboard-events")
@trace_method(name="get_dashboard_events", kind="SERVER")
async def get_dashboard_events(request: Request, limit: int = 10):
    """
    Get recent archival events for the dashboard.
    
    Args:
        limit: Maximum number of events to return
        
    Returns:
        List[Dict]: Recent archival events
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "dashboard.events",
            "timestamp": datetime.utcnow().isoformat(),
            "request.limit": limit
        })
        
        # Get archival monitor
        monitor = get_archival_monitor()
        
        # Get recent events
        events = await monitor.get_recent_events(limit)
        
        # Format events for dashboard
        formatted_events = []
        for event in events:
            formatted_event = {
                "timestamp": event.get("timestamp", datetime.utcnow().isoformat()),
                "table_name": event.get("table_name", ""),
                "chunk_id": event.get("chunk_id", ""),
                "status": event.get("status", ""),
                "processing_time_ms": event.get("processing_time_ms", 0),
                "size_bytes": event.get("size_bytes", 0),
                "destination": event.get("lakehouse_path", "")
            }
            formatted_events.append(formatted_event)
        
        return formatted_events
    except Exception as e:
        logger.exception("Error retrieving dashboard events")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving dashboard events: {str(e)}"
        )


@router.get("/dashboard-issues")
@trace_method(name="get_dashboard_issues", kind="SERVER")
async def get_dashboard_issues(request: Request):
    """
    Get detected issues from both Database and Archival services.
    
    Returns:
        Dict: Detected issues
    """
    try:
        # Add span attributes for request context
        add_span_attributes({
            "correlation_id": getattr(request.state, "correlation_id", str(uuid.uuid4())),
            "endpoint": "dashboard.issues",
            "timestamp": datetime.utcnow().isoformat()
        })
        
        issues = []
        
        # Get archival manager
        manager = get_archival_manager()
        
        # Get database service health
        try:
            db_health = await manager.get_database_health()
            if "issues" in db_health:
                for issue in db_health.get("issues", []):
                    issues.append({
                        "service": "database_service",
                        "message": issue,
                        "severity": "warning"
                    })
        except Exception as e:
            logger.error(f"Error getting database health: {e}")
            issues.append({
                "service": "database_service",
                "message": f"Error connecting to Database Service: {str(e)}",
                "severity": "critical"
            })
        
        # Get monitoring health
        try:
            monitor = get_archival_monitor()
            monitoring_health = await monitor.get_health_status()
            if "issues" in monitoring_health:
                for issue in monitoring_health.get("issues", []):
                    issues.append({
                        "service": "archival_monitoring",
                        "message": issue,
                        "severity": "warning"
                    })
        except Exception as e:
            logger.error(f"Error getting monitoring health: {e}")
            issues.append({
                "service": "archival_monitoring",
                "message": f"Error getting monitoring health: {str(e)}",
                "severity": "warning"
            })
        
        # Get task manager health
        try:
            task_manager = get_task_manager()
            task_health = await task_manager.get_health_status()
            if "issues" in task_health:
                for issue in task_health.get("issues", []):
                    issues.append({
                        "service": "archival_management",
                        "message": issue,
                        "severity": "warning"
                    })
        except Exception as e:
            logger.error(f"Error getting task manager health: {e}")
            issues.append({
                "service": "archival_management",
                "message": f"Error getting task manager health: {str(e)}",
                "severity": "warning"
            })
        
        # Get archival stats to check for potential issues
        try:
            archival_stats = await manager.calculate_archival_stats()
            
            # Check for potential issues
            if archival_stats.pending_chunks > 1000:  # Arbitrary threshold
                issues.append({
                    "service": "archival_service",
                    "message": f"Large backlog: {archival_stats.pending_chunks} chunks pending archival",
                    "severity": "warning"
                })
            
            if archival_stats.failed_chunks > 0:
                failure_rate = archival_stats.failed_chunks / (archival_stats.archived_chunks + archival_stats.failed_chunks) if (archival_stats.archived_chunks + archival_stats.failed_chunks) > 0 else 0
                if failure_rate > 0.1:  # More than 10% failure rate
                    issues.append({
                        "service": "archival_service",
                        "message": f"High failure rate: {failure_rate:.2%}",
                        "severity": "warning"
                    })
                
                if failure_rate > 0.3:  # More than 30% failure rate
                    issues.append({
                        "service": "archival_service",
                        "message": f"Critical failure rate: {failure_rate:.2%}",
                        "severity": "critical"
                    })
            
            if archival_stats.oldest_chunk_age_days and archival_stats.oldest_chunk_age_days > 30:  # Older than 30 days
                issues.append({
                    "service": "archival_service",
                    "message": f"Old chunks: oldest chunk is {archival_stats.oldest_chunk_age_days} days old",
                    "severity": "warning"
                })
        except Exception as e:
            logger.error(f"Error checking for potential issues: {e}")
            issues.append({
                "service": "archival_service",
                "message": f"Error checking for potential issues: {str(e)}",
                "severity": "warning"
            })
        
        critical_issues = sum(1 for issue in issues if issue.get("severity") == "critical")
        warning_issues = sum(1 for issue in issues if issue.get("severity") == "warning")
        
        # Add span attributes for issues
        add_span_attributes({
            "issues.total": len(issues),
            "issues.critical": critical_issues,
            "issues.warning": warning_issues
        })
        
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "total_issues": len(issues),
            "critical_issues": critical_issues,
            "warning_issues": warning_issues,
            "issues": issues
        }
    except Exception as e:
        logger.exception("Error retrieving dashboard issues")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving dashboard issues: {str(e)}"
        )


@router.get("/table-metrics")
@trace_method(name="get_table_metrics", kind="SERVER")
async def get_table_metrics(request: Request):
    """
    Get detailed metrics for each table.
    
    Returns:
        Dict: Table-specific metrics
    """
    try:
        # Get archival manager
        manager = get_archival_manager()
        
        # Get retention status
        retention = await manager.get_retention_status()
        
        # Format table metrics
        table_metrics = []
        for table in retention.tables:
            # Calculate progress
            progress = 0
            if table.total_chunks > 0:
                progress = ((table.total_chunks - table.chunks_to_archive) / table.total_chunks) * 100
            
            table_metrics.append({
                "table_name": table.table_name,
                "total_chunks": table.total_chunks,
                "eligible_chunks": table.chunks_to_archive,
                "progress": progress,
                "oldest_chunk_age_days": table.oldest_chunk_age_days,
                "archival_enabled": table.archival_enabled,
                "retention_policy": table.retention_policy
            })
        
        # Add span attributes for table metrics
        add_span_attributes({
            "tables.count": len(table_metrics),
            "tables.with_archival_enabled": sum(1 for table in table_metrics if table.get("archival_enabled", False))
        })
        
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "tables": table_metrics
        }
    except Exception as e:
        logger.exception("Error retrieving table metrics")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving table metrics: {str(e)}"
        )
