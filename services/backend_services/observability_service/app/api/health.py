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
        
        # Store health data
        await db_client.store_health_data(health_data.model_dump())
        
        # Track telemetry ingestion
        track_telemetry_ingestion("health")
        
        # Track health check processing
        track_health_check_processing(health_data.service, health_data.status)
        
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
        
        # Store health data
        for health_data in batch.health_checks:
            await db_client.store_health_data(health_data.model_dump())
            
            # Track health check processing
            track_health_check_processing(health_data.service, health_data.status)
        
        # Track telemetry ingestion
        track_telemetry_ingestion("health", len(batch.health_checks))
        
        # Publish events
        for health_data in batch.health_checks:
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
        
        # Query health data
        health_data = await db_client.query_health_data(
            {"service": service},
            limit=1,
            order_by="timestamp",
            order_direction="desc"
        )
        
        # Check if health data exists
        if not health_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Health data for service {service} not found"
            )
        
        # Return health data
        return HealthData(**health_data[0])
        
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
        db_client: Database client
        
    Returns:
        List[HealthData]: List of health data
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.query.service": query.service,
            "health.query.status": query.status,
            "health.query.start_time": query.start_time.isoformat() if query.start_time else None,
            "health.query.end_time": query.end_time.isoformat() if query.end_time else None,
            "health.query.limit": query.limit,
            "correlation_id": correlation_id
        })
        
        # Build query parameters
        query_params = {}
        
        if query.service:
            query_params["service"] = query.service
        
        if query.status:
            query_params["status"] = query.status
        
        if query.version:
            query_params["version"] = query.version
        
        if query.start_time and query.end_time:
            query_params["timestamp"] = {
                "gte": query.start_time.isoformat(),
                "lte": query.end_time.isoformat()
            }
        elif query.start_time:
            query_params["timestamp"] = {
                "gte": query.start_time.isoformat()
            }
        elif query.end_time:
            query_params["timestamp"] = {
                "lte": query.end_time.isoformat()
            }
        
        # Query health data
        health_data = await db_client.query_health_data(
            query_params,
            limit=query.limit,
            offset=query.offset,
            order_by=query.order_by,
            order_direction=query.order_direction
        )
        
        # Return health data
        return [HealthData(**data) for data in health_data]
        
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
        db_client: Database client
        
    Returns:
        HealthStatistics: Health statistics
    """
    correlation_id = get_correlation_id()
    
    try:
        # Set default time range if not provided
        if not end_time:
            end_time = datetime.utcnow()
        
        if not start_time:
            start_time = end_time - timedelta(hours=24)
        
        # Add span attributes for telemetry
        add_span_attributes({
            "health.statistics.service": service,
            "health.statistics.start_time": start_time.isoformat(),
            "health.statistics.end_time": end_time.isoformat(),
            "correlation_id": correlation_id
        })
        
        # Build query parameters
        query_params = {
            "timestamp": {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        }
        
        if service:
            query_params["service"] = service
        
        # Query health data
        health_data = await db_client.query_health_data(query_params)
        
        # Calculate statistics
        total_checks = len(health_data)
        services = set()
        healthy_count = 0
        unhealthy_count = 0
        versions = {}
        
        for data in health_data:
            services.add(data.get("service", "unknown"))
            
            if data.get("status") == "healthy":
                healthy_count += 1
            else:
                unhealthy_count += 1
            
            # Track versions
            service_name = data.get("service", "unknown")
            version = data.get("version", "unknown")
            
            if service_name not in versions:
                versions[service_name] = set()
            
            versions[service_name].add(version)
        
        # Calculate health rate
        health_rate = healthy_count / total_checks if total_checks > 0 else 0
        
        # Format versions for response
        service_versions = {
            service: list(vers) for service, vers in versions.items()
        }
        
        # Return statistics
        return HealthStatistics(
            total_checks=total_checks,
            healthy_count=healthy_count,
            unhealthy_count=unhealthy_count,
            health_rate=health_rate,
            service_count=len(services),
            services=list(services),
            service_versions=service_versions,
            start_time=start_time,
            end_time=end_time
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
        db_client: Database client
        
    Returns:
        List[str]: List of service names
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "correlation_id": correlation_id
        })
        
        # Query distinct services
        services = await db_client.query_distinct_values("health", "service")
        
        # Return services
        return services
        
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
        db_client: Database client
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "health.delete.service": service,
            "health.delete.start_time": start_time.isoformat() if start_time else None,
            "health.delete.end_time": end_time.isoformat() if end_time else None,
            "correlation_id": correlation_id
        })
        
        # Build query parameters
        query_params = {"service": service}
        
        if start_time and end_time:
            query_params["timestamp"] = {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        elif start_time:
            query_params["timestamp"] = {
                "gte": start_time.isoformat()
            }
        elif end_time:
            query_params["timestamp"] = {
                "lte": end_time.isoformat()
            }
        
        # Check if service exists
        existing_data = await db_client.query_health_data({"service": service}, limit=1)
        
        if not existing_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Health data for service {service} not found"
            )
        
        # Delete health data
        await db_client.delete_health_data(query_params)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete service health: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete service health: {str(e)}"
        )
