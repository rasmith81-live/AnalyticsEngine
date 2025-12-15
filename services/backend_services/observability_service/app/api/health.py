"""
Health API Router

This module provides API endpoints for health data ingestion and retrieval.
"""

from ..logging import get_logger
import time
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body, status
from fastapi.responses import JSONResponse

from ..config import get_settings
from ..messaging_client import MessagingClient
from ..models import (
    HealthData,
    HealthDataBatch,
    HealthQuery,
    HealthResponse,
    HealthStatistics,
    ErrorResponse
)
from ..telemetry import trace_method, add_span_attributes, get_correlation_id
from ..metrics import track_telemetry_ingestion, track_telemetry_processing, track_health_check_processing

logger = get_logger(__name__)

# Create router
router = APIRouter()


@router.post(
    "/",
    response_model=HealthResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.ingest_health_data", kind="SERVER")
async def ingest_health_data(
    health_data: HealthData = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest health check data.
    
    Args:
        health_data: Health data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        HealthResponse: Response with service name
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.service": health_data.service,
            "health.status": health_data.status,
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        if not health_data.timestamp:
            health_data.timestamp = datetime.utcnow()
        
        # Track telemetry ingestion
        track_telemetry_ingestion("health")
        
        # Track health check processing
        track_health_check_processing(health_data.service, health_data.status.value)
        
        # Publish event using standardized event type
        await messaging_client.publish_event(
            event_type="telemetry.health.ingested",
            event_data={
                "health": health_data.model_dump(),
                "correlation_id": correlation_id
            },
            correlation_id=correlation_id
        )
        
        # Track processing time
        track_telemetry_processing("health", time.time() - start_time)
        
        # Return response
        return HealthResponse(
            service=health_data.service,
            status="success",
            message="Health data ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest health data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest health data: {str(e)}"
        )


@router.post(
    "/batch",
    response_model=HealthResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.ingest_health_batch", kind="SERVER")
async def ingest_health_batch(
    batch: HealthDataBatch = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest a batch of health check data.
    
    Args:
        batch: Batch of health data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        HealthResponse: Response with success status
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.batch_size": len(batch.health_checks),
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        current_time = datetime.utcnow()
        for health_data in batch.health_checks:
            if not health_data.timestamp:
                health_data.timestamp = current_time
        
        # Track telemetry ingestion
        track_telemetry_ingestion("health", len(batch.health_checks))
        
        # Process and publish events
        for health_data in batch.health_checks:
            # Track health check processing
            track_health_check_processing(health_data.service, health_data.status.value)
            
            await messaging_client.publish_event(
                event_type="telemetry.health.ingested",
                event_data={
                    "health": health_data.model_dump(),
                    "correlation_id": correlation_id
                },
                correlation_id=correlation_id
            )
        
        # Track processing time
        track_telemetry_processing("health", time.time() - start_time)
        
        # Return response
        return HealthResponse(
            service=None,
            status="success",
            message=f"Batch of {len(batch.health_checks)} health checks ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest health batch: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest health batch: {str(e)}"
        )


@router.get(
    "/{service}",
    response_model=HealthData,
    responses={
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.get_service_health", kind="SERVER")
async def get_service_health(
    service: str = Path(..., description="Service name"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get the latest health check for a service.
    
    Args:
        service: Service name
        db_client: Database client
        
    Returns:
        HealthData: Health data for the service
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.service": service,
            "correlation_id": correlation_id
        })
        
        # Request health data via messaging (CQRS)
        logger.warning("Synchronous get_service_health is not fully supported in decoupled architecture.")
        
        # Return mock data to avoid runtime errors
        return HealthData(
            service=service,
            status="healthy",
            timestamp=datetime.utcnow(),
            details={"note": "Mock data - synchronous read not supported"}
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get service health: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get service health: {str(e)}"
        )


@router.post(
    "/query",
    response_model=List[HealthData],
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.query_health", kind="SERVER")
async def query_health(
    query: HealthQuery = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Query health data based on criteria.
    
    Args:
        query: Query parameters
        messaging_client: Messaging client
        
    Returns:
        List[HealthData]: List of health data
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.query.service": query.service,
            "health.query.status": query.status,
            "correlation_id": correlation_id
        })
        
        # Request health data via messaging (CQRS)
        logger.warning("Synchronous query_health is not fully supported in decoupled architecture.")
        
        # Return empty list
        return []
        
    except Exception as e:
        logger.error(f"Failed to query health data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to query health data: {str(e)}"
        )


@router.get(
    "/statistics",
    response_model=HealthStatistics,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.get_health_statistics", kind="SERVER")
async def get_health_statistics(
    service: Optional[str] = Query(None, description="Filter by service"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get health statistics.
    
    Args:
        service: Filter by service
        start_time: Start time
        end_time: End time
        messaging_client: Messaging client
        
    Returns:
        HealthStatistics: Health statistics
    """
    correlation_id = get_correlation_id()
    
    try:
        # Request health statistics via messaging (CQRS)
        logger.warning("Synchronous get_health_statistics is not fully supported in decoupled architecture.")
        
        # Return empty statistics
        return HealthStatistics(
            total_checks=0,
            healthy_count=0,
            degraded_count=0,
            unhealthy_count=0,
            avg_latency_ms=0.0,
            service_count=0,
            services=[],
            service_versions={},
            start_time=start_time or datetime.utcnow(),
            end_time=end_time or datetime.utcnow()
        )
        
    except Exception as e:
        logger.error(f"Failed to get health statistics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get health statistics: {str(e)}"
        )


@router.get(
    "/services",
    response_model=List[str],
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.get_health_services", kind="SERVER")
async def get_health_services(
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get list of services that have reported health checks.
    
    Args:
        messaging_client: Messaging client
        
    Returns:
        List[str]: List of service names
    """
    correlation_id = get_correlation_id()
    
    try:
        # Request health services via messaging (CQRS)
        logger.warning("Synchronous get_health_services is not fully supported in decoupled architecture.")
        
        # Return empty list
        return []
        
    except Exception as e:
        logger.error(f"Failed to get health services: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get health services: {str(e)}"
        )


@router.delete(
    "/{service}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.health.delete_service_health", kind="SERVER")
async def delete_service_health(
    service: str = Path(..., description="Service name"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Delete health data for a service.
    
    Args:
        service: Service name
        start_time: Start time
        end_time: End time
        messaging_client: Messaging client
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.delete.service": service,
            "correlation_id": correlation_id
        })
        
        # Request deletion via messaging
        logger.warning("Synchronous delete_service_health is not fully supported in decoupled architecture. Use request based deletion.")
        
        await messaging_client.publish_event(
            event_type="command.health.delete",
            event_data={"service": service, "start_time": str(start_time), "end_time": str(end_time)},
            channel="database",
            correlation_id=correlation_id
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete service health: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete service health: {str(e)}"
        )
