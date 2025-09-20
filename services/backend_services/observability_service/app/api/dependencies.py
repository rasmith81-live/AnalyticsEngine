"""
Dependencies API Router

This module provides API endpoints for dependency data ingestion and retrieval.
"""

import logging
import time
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body, status
from fastapi.responses import JSONResponse

from ..config import get_settings
from ..messaging_client import MessagingClient
from ..models import (
    DependencyData,
    DependencyDataBatch,
    DependencyQuery,
    DependencyResponse,
    DependencyStatistics,
    ErrorResponse
)
from ..telemetry import trace_method, add_span_attributes, get_correlation_id
from ..metrics import track_telemetry_ingestion, track_telemetry_processing, track_dependency_check_processing

logger = logging.getLogger(__name__)

# Create router
router = APIRouter()


@router.post(
    "/",
    response_model=DependencyResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.ingest_dependency_data", kind="SERVER")
async def ingest_dependency_data(
    dependency_data: DependencyData = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest dependency check data.
    
    Args:
        dependency_data: Dependency data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        DependencyResponse: Response with dependency name
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "dependency.name": dependency_data.name,
            "dependency.service": dependency_data.service,
            "dependency.type": dependency_data.type,
            "dependency.status": dependency_data.status,
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        if not dependency_data.timestamp:
            dependency_data.timestamp = datetime.utcnow()
        
        # Track telemetry ingestion
        track_telemetry_ingestion("dependency")
        
        # Track dependency check processing
        track_dependency_check_processing(dependency_data.service, dependency_data.type, dependency_data.status)
        
        # Publish event for database service to consume
        await messaging_client.publish_event(
            event_type="telemetry.dependency.ingested",
            event_data={
                "dependency": dependency_data.model_dump(),
                "correlation_id": correlation_id
            },
            correlation_id=correlation_id
        )
        
        # Track processing time
        track_telemetry_processing("dependency", time.time() - start_time)
        
        # Return response
        return DependencyResponse(
            name=dependency_data.name,
            status="success",
            message="Dependency data ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest dependency data: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest dependency data: {str(e)}"
        )


@router.post(
    "/batch",
    response_model=DependencyResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.ingest_dependency_batch", kind="SERVER")
async def ingest_dependency_batch(
    batch: DependencyDataBatch = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest a batch of dependency check data.
    
    Args:
        batch: Batch of dependency data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        DependencyResponse: Response with success status
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "dependency.batch_size": len(batch.dependencies),
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        current_time = datetime.utcnow()
        for dependency_data in batch.dependencies:
            if not dependency_data.timestamp:
                dependency_data.timestamp = current_time
        
        # Store dependency data
        for dependency_data in batch.dependencies:
            await db_client.store_dependency_data(dependency_data.model_dump())
            
            # Track dependency check processing
            track_dependency_check_processing(
                dependency_data.service, 
                dependency_data.type, 
                dependency_data.status
            )
        
        # Track telemetry ingestion
        track_telemetry_ingestion("dependency", len(batch.dependencies))
        
        # Publish events
        for dependency_data in batch.dependencies:
            await messaging_client.publish_event(
                event_type="telemetry.dependency.ingested",
                event_data={
                    "dependency": dependency_data.model_dump(),
                    "correlation_id": correlation_id
                },
                correlation_id=correlation_id
            )
        
        # Track processing time
        track_telemetry_processing("dependency", time.time() - start_time)
        
        # Return response
        return DependencyResponse(
            name=None,
            status="success",
            message=f"Batch of {len(batch.dependencies)} dependency checks ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest dependency batch: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest dependency batch: {str(e)}"
        )


@router.post(
    "/{service}/{name}/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.request_dependency", kind="SERVER")
async def request_dependency(
    service: str = Path(..., description="Service name"),
    name: str = Path(..., description="Dependency name"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Request the latest dependency check for a service and dependency name via messaging.
    
    Args:
        service: Service name
        name: Dependency name
        messaging_client: Messaging client
        
    Returns:
        Dict: Request status with request ID for tracking
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "dependency.service": service,
            "dependency.name": name,
            "correlation_id": correlation_id
        })
        
        # Publish dependency query request event
        request_data = {
            "query_type": "get_dependency",
            "service": service,
            "name": name,
            "parameters": {
                "limit": 1,
                "order_by": "timestamp",
                "order_direction": "desc"
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="query.dependency.request",
            event_data=request_data,
            correlation_id=correlation_id
        )
        
        return {
            "status": "accepted",
            "message": "Dependency query request submitted successfully",
            "request_id": message_id,
            "correlation_id": correlation_id,
            "note": "Query will be processed asynchronously. Use request_id to track status."
        }
        
    except Exception as e:
        logger.error(f"Failed to request dependency: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to request dependency: {str(e)}"
        )


@router.post(
    "/query/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.request_dependency_query", kind="SERVER")
async def request_dependency_query(
    query: DependencyQuery = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Request dependency data query based on criteria via messaging.
    
    Args:
        query: Query parameters
        messaging_client: Messaging client
        
    Returns:
        Dict: Request status with request ID for tracking
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "dependency.query.name": query.name,
            "dependency.query.service": query.service,
            "dependency.query.type": query.type,
            "dependency.query.status": query.status,
            "dependency.query.start_time": query.start_time.isoformat() if query.start_time else None,
            "dependency.query.end_time": query.end_time.isoformat() if query.end_time else None,
            "dependency.query.limit": query.limit,
            "correlation_id": correlation_id
        })
        
        # Publish dependency query request event
        request_data = {
            "query_type": "query_dependencies",
            "query": query.model_dump(),
            "parameters": {
                "limit": query.limit,
                "offset": query.offset,
                "order_by": query.order_by,
                "order_direction": query.order_direction
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="query.dependency.request",
            event_data=request_data,
            correlation_id=correlation_id
        )
        
        return {
            "status": "accepted",
            "message": "Dependency query request submitted successfully",
            "request_id": message_id,
            "correlation_id": correlation_id,
            "note": "Query will be processed asynchronously. Use request_id to track status."
        }
        
    except Exception as e:
        logger.error(f"Failed to request dependency query: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to request dependency query: {str(e)}"
        )


@router.post(
    "/statistics/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.request_dependency_statistics", kind="SERVER")
async def request_dependency_statistics(
    service: Optional[str] = Query(None, description="Filter by service"),
    dependency_type: Optional[str] = Query(None, description="Filter by dependency type"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Request dependency statistics via messaging.
    
    Args:
        service: Filter by service
        dependency_type: Filter by dependency type
        start_time: Start time
        end_time: End time
        messaging_client: Messaging client
        
    Returns:
        Dict: Request status with request ID for tracking
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
            "dependency.statistics.service": service,
            "dependency.statistics.type": dependency_type,
            "dependency.statistics.start_time": start_time.isoformat(),
            "dependency.statistics.end_time": end_time.isoformat(),
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
        
        if dependency_type:
            query_params["type"] = dependency_type
        
        # Query dependency data
        dependency_data = await db_client.query_dependency_data(query_params)
        
        # Calculate statistics
        total_checks = len(dependency_data)
        services = set()
        dependency_names = set()
        dependency_types = set()
        healthy_count = 0
        unhealthy_count = 0
        
        for data in dependency_data:
            services.add(data.get("service", "unknown"))
            dependency_names.add(data.get("name", "unknown"))
            dependency_types.add(data.get("type", "unknown"))
            
            if data.get("status") == "healthy":
                healthy_count += 1
            else:
                unhealthy_count += 1
        
        # Calculate health rate
        health_rate = healthy_count / total_checks if total_checks > 0 else 0
        
        # Return statistics
        return DependencyStatistics(
            total_checks=total_checks,
            healthy_count=healthy_count,
            unhealthy_count=unhealthy_count,
            health_rate=health_rate,
            service_count=len(services),
            services=list(services),
            dependency_count=len(dependency_names),
            dependency_names=list(dependency_names),
            dependency_type_count=len(dependency_types),
            dependency_types=list(dependency_types),
            start_time=start_time,
            end_time=end_time
        )
        
    except Exception as e:
        logger.error(f"Failed to get dependency statistics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get dependency statistics: {str(e)}"
        )


@router.post(
    "/services/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.request_dependency_services", kind="SERVER")
async def request_dependency_services(
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get list of services that have reported dependency checks.
    
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
        services = await db_client.query_distinct_values("dependency", "service")
        
        # Return services
        return services
        
    except Exception as e:
        logger.error(f"Failed to get dependency services: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get dependency services: {str(e)}"
        )


@router.post(
    "/types/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.request_dependency_types", kind="SERVER")
async def request_dependency_types(
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get list of dependency types.
    
    Args:
        db_client: Database client
        
    Returns:
        List[str]: List of dependency types
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "correlation_id": correlation_id
        })
        
        # Query distinct dependency types
        types = await db_client.query_distinct_values("dependency", "type")
        
        # Return types
        return types
        
    except Exception as e:
        logger.error(f"Failed to get dependency types: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get dependency types: {str(e)}"
        )


@router.post(
    "/{service}/{name}/delete",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.dependencies.request_dependency_deletion", kind="SERVER")
async def request_dependency_deletion(
    service: str = Path(..., description="Service name"),
    name: str = Path(..., description="Dependency name"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Delete dependency data for a service and dependency name.
    
    Args:
        service: Service name
        name: Dependency name
        start_time: Start time
        end_time: End time
        db_client: Database client
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "dependency.delete.service": service,
            "dependency.delete.name": name,
            "dependency.delete.start_time": start_time.isoformat() if start_time else None,
            "dependency.delete.end_time": end_time.isoformat() if end_time else None,
            "correlation_id": correlation_id
        })
        
        # Build query parameters
        query_params = {
            "service": service,
            "name": name
        }
        
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
        
        # Check if dependency exists
        existing_data = await db_client.query_dependency_data(
            {"service": service, "name": name},
            limit=1
        )
        
        if not existing_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Dependency data for service {service} and dependency {name} not found"
            )
        
        # Delete dependency data
        await db_client.delete_dependency_data(query_params)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete dependency: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete dependency: {str(e)}"
        )
