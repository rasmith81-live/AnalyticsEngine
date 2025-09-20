"""
Query API Router

This module provides API endpoints for advanced querying across telemetry data types.
"""

import logging
import time
from typing import Dict, List, Any, Optional, Union
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body, status, Response
from fastapi.responses import JSONResponse

from ..config import get_settings
from ..messaging_client import MessagingClient
from ..models import (
    QueryData,
    QueryDataBatch,
    QueryQuery,
    QueryResponse,
    QueryStatistics,
    ErrorResponse
)
from ..telemetry import trace_method, add_span_attributes, get_correlation_id
from ..metrics import track_query_execution

logger = logging.getLogger(__name__)

# Create router
router = APIRouter()


@router.post(
    "/advanced",
    response_model=QueryResponse,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.query.execute_advanced_query", kind="SERVER")
async def execute_advanced_query(
    query: QueryQuery = Body(...),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Execute an advanced query across multiple telemetry data types.
    
    Args:
        query: Advanced query parameters
        db_client: Database client
        
    Returns:
        QueryResult: Query results
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Add span attributes for telemetry
        add_span_attributes({
            "query.data_types": query.data_types,
            "query.service": query.service,
            "query.start_time": query.start_time.isoformat() if query.start_time else None,
            "query.end_time": query.end_time.isoformat() if query.end_time else None,
            "query.limit": query.limit,
            "correlation_id": correlation_id
        })
        
        # Set default time range if not provided
        if not query.end_time:
            query.end_time = datetime.utcnow()
        
        if not query.start_time:
            query.start_time = query.end_time - timedelta(hours=24)
        
        # Build base query parameters
        base_params = {}
        
        if query.service:
            base_params["service"] = query.service
        
        if query.start_time and query.end_time:
            base_params["timestamp"] = {
                "gte": query.start_time.isoformat(),
                "lte": query.end_time.isoformat()
            }
        
        # Initialize results
        results = {
            "traces": [],
            "metrics": [],
            "events": [],
            "health": [],
            "dependencies": []
        }
        
        # Query each data type
        for data_type in query.data_types:
            if data_type == "trace":
                # Apply trace-specific filters
                trace_params = base_params.copy()
                if query.trace_id:
                    trace_params["trace_id"] = query.trace_id
                if query.span_id:
                    trace_params["span_id"] = query.span_id
                if query.parent_span_id:
                    trace_params["parent_span_id"] = query.parent_span_id
                
                traces = await db_client.query_trace_data(
                    trace_params,
                    limit=query.limit,
                    offset=query.offset,
                    order_by=query.order_by or "timestamp",
                    order_direction=query.order_direction or "desc"
                )
                results["traces"] = traces
            
            elif data_type == "metric":
                # Apply metric-specific filters
                metric_params = base_params.copy()
                if query.metric_name:
                    metric_params["name"] = query.metric_name
                if query.metric_type:
                    metric_params["type"] = query.metric_type
                
                metrics = await db_client.query_metric_data(
                    metric_params,
                    limit=query.limit,
                    offset=query.offset,
                    order_by=query.order_by or "timestamp",
                    order_direction=query.order_direction or "desc"
                )
                results["metrics"] = metrics
            
            elif data_type == "event":
                # Apply event-specific filters
                event_params = base_params.copy()
                if query.event_type:
                    event_params["event_type"] = query.event_type
                if query.severity:
                    event_params["severity"] = query.severity
                
                events = await db_client.query_event_data(
                    event_params,
                    limit=query.limit,
                    offset=query.offset,
                    order_by=query.order_by or "timestamp",
                    order_direction=query.order_direction or "desc"
                )
                results["events"] = events
            
            elif data_type == "health":
                # Apply health-specific filters
                health_params = base_params.copy()
                if query.health_status:
                    health_params["status"] = query.health_status
                
                health = await db_client.query_health_data(
                    health_params,
                    limit=query.limit,
                    offset=query.offset,
                    order_by=query.order_by or "timestamp",
                    order_direction=query.order_direction or "desc"
                )
                results["health"] = health
            
            elif data_type == "dependency":
                # Apply dependency-specific filters
                dependency_params = base_params.copy()
                if query.dependency_name:
                    dependency_params["name"] = query.dependency_name
                if query.dependency_type:
                    dependency_params["type"] = query.dependency_type
                if query.dependency_status:
                    dependency_params["status"] = query.dependency_status
                
                dependencies = await db_client.query_dependency_data(
                    dependency_params,
                    limit=query.limit,
                    offset=query.offset,
                    order_by=query.order_by or "timestamp",
                    order_direction=query.order_direction or "desc"
                )
                results["dependencies"] = dependencies
        
        # Track query execution time
        execution_time = time.time() - start_time
        track_query_execution("advanced", execution_time, len(query.data_types))
        
        # Return query results
        return QueryResult(
            query=query.model_dump(),
            results=results,
            execution_time=execution_time
        )
        
    except Exception as e:
        logger.error(f"Failed to execute advanced query: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to execute advanced query: {str(e)}"
        )


@router.get(
    "/correlation/{correlation_id}",
    response_model=QueryResponse,
    responses={
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.query.get_correlated_telemetry", kind="SERVER")
async def get_correlated_telemetry(
    correlation_id: str = Path(..., description="Correlation ID"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get all telemetry data correlated by a correlation ID.
    
    Args:
        correlation_id: Correlation ID
        start_time: Start time
        end_time: End time
        db_client: Database client
        
    Returns:
        CorrelatedTelemetry: Correlated telemetry data
    """
    query_start_time = time.time()
    request_correlation_id = get_correlation_id()
    
    try:
        # Set default time range if not provided
        if not end_time:
            end_time = datetime.utcnow()
        
        if not start_time:
            start_time = end_time - timedelta(hours=24)
        
        # Add span attributes for telemetry
        add_span_attributes({
            "query.correlation_id": correlation_id,
            "query.start_time": start_time.isoformat(),
            "query.end_time": end_time.isoformat(),
            "request_correlation_id": request_correlation_id
        })
        
        # Build base query parameters
        base_params = {
            "correlation_id": correlation_id,
            "timestamp": {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        }
        
        # Query each data type
        traces = await db_client.query_trace_data(base_params)
        metrics = await db_client.query_metric_data(base_params)
        events = await db_client.query_event_data(base_params)
        health = await db_client.query_health_data(base_params)
        dependencies = await db_client.query_dependency_data(base_params)
        
        # Check if any data was found
        if not traces and not metrics and not events and not health and not dependencies:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No telemetry data found for correlation ID {correlation_id}"
            )
        
        # Track query execution time
        execution_time = time.time() - query_start_time
        track_query_execution("correlation", execution_time)
        
        # Return correlated telemetry
        return CorrelatedTelemetry(
            correlation_id=correlation_id,
            traces=traces,
            metrics=metrics,
            events=events,
            health=health,
            dependencies=dependencies,
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get correlated telemetry: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get correlated telemetry: {str(e)}"
        )


@router.get(
    "/topology",
    response_model=QueryResponse,
    responses={
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.query.get_service_topology", kind="SERVER")
async def get_service_topology(
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get service topology based on trace data.
    
    Args:
        start_time: Start time
        end_time: End time
        db_client: Database client
        
    Returns:
        ServiceTopology: Service topology
    """
    query_start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Set default time range if not provided
        if not end_time:
            end_time = datetime.utcnow()
        
        if not start_time:
            start_time = end_time - timedelta(hours=24)
        
        # Add span attributes for telemetry
        add_span_attributes({
            "query.topology.start_time": start_time.isoformat(),
            "query.topology.end_time": end_time.isoformat(),
            "correlation_id": correlation_id
        })
        
        # Query trace data
        trace_params = {
            "timestamp": {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        }
        
        traces = await db_client.query_trace_data(trace_params)
        
        # Build service topology
        services = set()
        edges = []
        
        for trace in traces:
            service = trace.get("service")
            if service:
                services.add(service)
            
            # Extract parent-child relationships
            parent_service = trace.get("parent_service")
            if parent_service and service and parent_service != service:
                edge = {
                    "source": parent_service,
                    "target": service,
                    "trace_id": trace.get("trace_id"),
                    "span_id": trace.get("span_id"),
                    "parent_span_id": trace.get("parent_span_id"),
                    "timestamp": trace.get("timestamp")
                }
                edges.append(edge)
        
        # Get service health status
        service_health = {}
        for service in services:
            health_data = await db_client.query_health_data(
                {"service": service},
                limit=1,
                order_by="timestamp",
                order_direction="desc"
            )
            
            if health_data:
                service_health[service] = health_data[0].get("status", "unknown")
            else:
                service_health[service] = "unknown"
        
        # Track query execution time
        execution_time = time.time() - query_start_time
        track_query_execution("topology", execution_time)
        
        # Return service topology
        return ServiceTopology(
            services=list(services),
            edges=edges,
            service_health=service_health,
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time
        )
        
    except Exception as e:
        logger.error(f"Failed to get service topology: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get service topology: {str(e)}"
        )


@router.get(
    "/dependencies/{service}",
    response_model=QueryResponse,
    responses={
        404: {"model": ErrorResponse, "description": "Not Found"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.query.get_service_dependencies", kind="SERVER")
async def get_service_dependencies(
    service: str = Path(..., description="Service name"),
    start_time: Optional[datetime] = Query(None, description="Start time"),
    end_time: Optional[datetime] = Query(None, description="End time"),
    messaging_client: MessagingClient = Depends(lambda: MessagingClient(
        base_url=get_settings().messaging_service_url,
        service_name=get_settings().service_name
    ))
):
    """
    Get dependencies for a specific service.
    
    Args:
        service: Service name
        start_time: Start time
        end_time: End time
        db_client: Database client
        
    Returns:
        ServiceDependencyMap: Service dependency map
    """
    query_start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        # Set default time range if not provided
        if not end_time:
            end_time = datetime.utcnow()
        
        if not start_time:
            start_time = end_time - timedelta(hours=24)
        
        # Add span attributes for telemetry
        add_span_attributes({
            "query.dependencies.service": service,
            "query.dependencies.start_time": start_time.isoformat(),
            "query.dependencies.end_time": end_time.isoformat(),
            "correlation_id": correlation_id
        })
        
        # Query dependency data
        dependency_params = {
            "service": service,
            "timestamp": {
                "gte": start_time.isoformat(),
                "lte": end_time.isoformat()
            }
        }
        
        dependencies = await db_client.query_dependency_data(dependency_params)
        
        # Check if service exists
        if not dependencies:
            # Check if service exists at all
            service_exists = await db_client.query_health_data(
                {"service": service},
                limit=1
            )
            
            if not service_exists:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Service {service} not found"
                )
        
        # Build dependency map
        dependency_map = {}
        
        for dependency in dependencies:
            name = dependency.get("name", "unknown")
            type_name = dependency.get("type", "unknown")
            status = dependency.get("status", "unknown")
            
            if type_name not in dependency_map:
                dependency_map[type_name] = []
            
            # Check if dependency already exists in the list
            existing = next((d for d in dependency_map[type_name] if d["name"] == name), None)
            
            if existing:
                # Update existing dependency with latest status
                if dependency.get("timestamp", "") > existing.get("timestamp", ""):
                    existing["status"] = status
                    existing["timestamp"] = dependency.get("timestamp")
                    existing["details"] = dependency.get("details", {})
            else:
                # Add new dependency
                dependency_map[type_name].append({
                    "name": name,
                    "status": status,
                    "timestamp": dependency.get("timestamp"),
                    "details": dependency.get("details", {})
                })
        
        # Track query execution time
        execution_time = time.time() - query_start_time
        track_query_execution("dependencies", execution_time)
        
        # Return service dependency map
        return ServiceDependencyMap(
            service=service,
            dependency_map=dependency_map,
            start_time=start_time,
            end_time=end_time,
            execution_time=execution_time
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get service dependencies: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get service dependencies: {str(e)}"
        )
