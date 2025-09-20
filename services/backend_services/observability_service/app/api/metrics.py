"""
Metrics API Router

This module provides API endpoints for metric data ingestion and retrieval.
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
    MetricData,
    MetricDataBatch,
    MetricQuery,
    MetricResponse,
    MetricStatistics,
    ErrorResponse
)
from ..telemetry import trace_method, add_span_attributes, get_correlation_id
from ..metrics import track_telemetry_ingestion, track_telemetry_processing, track_metric_processing

logger = get_logger(__name__)

# Create router
router = APIRouter()

@router.post(
    "/ingest",
    response_model=MetricResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.ingest_metrics", kind="SERVER")


async def ingest_metrics(
    metric: MetricData = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest metrics from external services.
    
    Args:
        metric: Metric data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        MetricResponse: Response with metric name
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "metric.name": metric.name,
            "metric.service": metric.service,
            "metric.type": metric.type,
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        if not metric.timestamp:
            metric.timestamp = datetime.utcnow()
        
        # Store metric data
        await db_client.store_metric_data(metric.model_dump())
        
        # Track telemetry ingestion
        track_telemetry_ingestion("metric")
        
        # Track metric processing
        track_metric_processing(metric.service, metric.type)
        
        # Publish event
        await messaging_client.publish_event(
            event_type="metric.created",
            event_data={
                "metric": metric.model_dump(),
                "correlation_id": correlation_id
            },
            correlation_id=correlation_id
        )
        
        # Track processing time
        track_telemetry_processing("metric", time.time() - start_time)
        
        # Return response
        return MetricResponse(
            name=metric.name,
            status="success",
            message="Metric ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest metric: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest metric: {str(e)}"
        )


@router.post(
    "/",
    response_model=MetricResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.ingest_metric", kind="SERVER")


async def ingest_metric(
    metric: MetricData = Body(...),

    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest a single metric.
    
    Args:
        metric: Metric data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        MetricResponse: Response with metric name
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "metric.name": metric.name,
            "metric.service": metric.service,
            "metric.type": metric.type,
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        if not metric.timestamp:
            metric.timestamp = datetime.utcnow()
        
        # Store metric data
        await db_client.store_metric_data(metric.model_dump())
        
        # Track telemetry ingestion
        track_telemetry_ingestion("metric")
        
        # Track metric processing
        track_metric_processing(metric.service, metric.type)
        
        # Publish event
        await messaging_client.publish_event(
            event_type="metric.created",
            event_data={
                "metric": metric.model_dump(),
                "correlation_id": correlation_id
            },
            correlation_id=correlation_id
        )
        
        # Track processing time
        track_telemetry_processing("metric", time.time() - start_time)
        
        # Return response
        return MetricResponse(
            name=metric.name,
            status="success",
            message="Metric ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest metric: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest metric: {str(e)}"
        )


@router.post(
    "/batch",
    response_model=MetricResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.ingest_metric_batch", kind="SERVER")
async def ingest_metric_batch(
    batch: MetricDataBatch = Body(...),

    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Ingest a batch of metrics.
    
    Args:
        batch: Batch of metric data to ingest
        db_client: Database client
        messaging_client: Messaging client
        
    Returns:
        MetricResponse: Response with success status
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "metric.batch_size": len(batch.metrics),
            "correlation_id": correlation_id
        })
        
        # Set timestamp if not provided
        current_time = datetime.utcnow()
        for metric in batch.metrics:
            if not metric.timestamp:
                metric.timestamp = current_time
        
        # Store metric data
        for metric in batch.metrics:
            await db_client.store_metric_data(metric.model_dump())
            
            # Track metric processing
            track_metric_processing(metric.service, metric.type)
        
        # Track telemetry ingestion
        track_telemetry_ingestion("metric", len(batch.metrics))
        
        # Publish events
        for metric in batch.metrics:
            await messaging_client.publish_event(
                event_type="metric.created",
                event_data={
                    "metric": metric.model_dump(),
                    "correlation_id": correlation_id
                },
                correlation_id=correlation_id
            )
        
        # Track processing time
        track_telemetry_processing("metric", time.time() - start_time)
        
        # Return response
        return MetricResponse(
            name=None,
            status="success",
            message=f"Batch of {len(batch.metrics)} metrics ingested successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to ingest metric batch: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to ingest metric batch: {str(e)}"
        )


@router.post(
    "/query/request",
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.request_metrics_query", kind="SERVER")
async def request_metrics_query(
    query: MetricQuery = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Request metrics query via messaging.
    
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
            "metric.query.name": query.name,
            "metric.query.service": query.service,
            "metric.query.type": query.type,
            "metric.query.start_time": query.start_time.isoformat() if query.start_time else None,
            "metric.query.end_time": query.end_time.isoformat() if query.end_time else None,
            "metric.query.limit": query.limit,
            "correlation_id": correlation_id
        })
        
        # Publish metrics query request
        request_data = {
            "query_type": "query_metrics",
            "query_params": query.model_dump()
        }
        
        message_id = await messaging_client.publish_event(
            event_type="query.metric.request",
            event_data=request_data,
            correlation_id=correlation_id
        )
        
        return {
            "status": "accepted",
            "message": "Metrics query request submitted successfully",
            "request_id": message_id,
            "correlation_id": correlation_id,
            "note": "Query will be processed asynchronously. Use request_id to track status."
        }
        
    except Exception as e:
        logger.error(f"Failed to request metrics query: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to request metrics query: {str(e)}"
        )


@router.get(
    "/statistics",
    response_model=MetricStatistics,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.get_metric_statistics", kind="SERVER")
async def get_metric_statistics(
    name: Optional[str] = Query(None, description="Filter by metric name"),
    service: Optional[str] = Query(None, description="Filter by service"),
    metric_type: Optional[str] = Query(None, description="Filter by metric type"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get metric statistics.
    
    Args:
        name: Filter by metric name
        service: Filter by service
        metric_type: Filter by metric type
        start_time: Start time
        end_time: End time
        db_client: Database client
        
    Returns:
        MetricStatistics: Metric statistics
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
            "metric.statistics.name": name,
            "metric.statistics.service": service,
            "metric.statistics.type": metric_type,
            "metric.statistics.start_time": start_time.isoformat(),
            "metric.statistics.end_time": end_time.isoformat(),
            "correlation_id": correlation_id
        })
        
        # Build query parameters
        query_params = {
            "timestamp": {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        }
        
        if name:
            query_params["name"] = name
        
        if service:
            query_params["service"] = service
        
        if metric_type:
            query_params["type"] = metric_type
        
        # Query metric data
        metric_data = await db_client.query_metric_data(query_params)
        
        # Calculate statistics
        total_metrics = len(metric_data)
        services = set()
        metric_names = set()
        metric_types = set()
        total_value = 0
        min_value = float('inf')
        max_value = float('-inf')
        
        for metric in metric_data:
            services.add(metric.get("service", "unknown"))
            metric_names.add(metric.get("name", "unknown"))
            metric_types.add(metric.get("type", "unknown"))
            
            value = metric.get("value", 0)
            total_value += value
            min_value = min(min_value, value)
            max_value = max(max_value, value)
        
        # Calculate average value
        avg_value = total_value / total_metrics if total_metrics > 0 else 0
        
        # Handle empty result
        if total_metrics == 0:
            min_value = 0
            max_value = 0
        
        # Return statistics
        return MetricStatistics(
            total_metrics=total_metrics,
            service_count=len(services),
            services=list(services),
            metric_name_count=len(metric_names),
            metric_names=list(metric_names),
            metric_type_count=len(metric_types),
            metric_types=list(metric_types),
            min_value=min_value,
            max_value=max_value,
            avg_value=avg_value,
            start_time=start_time,
            end_time=end_time
        )
        
    except Exception as e:
        logger.error(f"Failed to get metric statistics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get metric statistics: {str(e)}"
        )


@router.get(
    "/services",
    response_model=List[str],
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.get_metric_services", kind="SERVER")
async def get_metric_services(
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get list of services that have reported metrics.
    
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
        services = await db_client.query_distinct_values("metric", "service")
        
        # Return services
        return services
        
    except Exception as e:
        logger.error(f"Failed to get metric services: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get metric services: {str(e)}"
        )


@router.get(
    "/types",
    response_model=List[str],
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.get_metric_types", kind="SERVER")
async def get_metric_types(
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get list of metric types.
    
    Args:
        db_client: Database client
        
    Returns:
        List[str]: List of metric types
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "correlation_id": correlation_id
        })
        
        # Query distinct metric types
        types = await db_client.query_distinct_values("metric", "type")
        
        # Return types
        return types
        
    except Exception as e:
        logger.error(f"Failed to get metric types: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get metric types: {str(e)}"
        )


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.metrics.delete_metrics", kind="SERVER")
async def delete_metrics(
    name: Optional[str] = Query(None, description="Filter by metric name"),
    service: Optional[str] = Query(None, description="Filter by service"),
    metric_type: Optional[str] = Query(None, description="Filter by metric type"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Delete metrics based on criteria.
    
    Args:
        name: Filter by metric name
        service: Filter by service
        metric_type: Filter by metric type
        start_time: Start time
        end_time: End time
        db_client: Database client
    """
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "metric.delete.name": name,
            "metric.delete.service": service,
            "metric.delete.type": metric_type,
            "metric.delete.start_time": start_time.isoformat() if start_time else None,
            "metric.delete.end_time": end_time.isoformat() if end_time else None,
            "correlation_id": correlation_id
        })
        
        # Build query parameters
        query_params = {}
        
        if name:
            query_params["name"] = name
        
        if service:
            query_params["service"] = service
        
        if metric_type:
            query_params["type"] = metric_type
        
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
        
        # Check if query params are empty
        if not query_params:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one filter parameter is required"
            )
        
        # Delete metric data
        await db_client.delete_metric_data(query_params)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete metrics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to delete metrics: {str(e)}"
        )
