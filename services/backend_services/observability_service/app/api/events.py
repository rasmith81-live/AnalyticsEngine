"""
Events API Router

This module provides API endpoints for event data ingestion and retrieval.
"""

from ..logging import get_logger
import time
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body, status
from fastapi.responses import JSONResponse

from ..config import get_settings
from ..dependencies import get_messaging_client, MessagingClient
from ..models import (
    EventData,
    EventDataBatch,
    EventQuery,
    EventResponse,
    EventStatistics,
    EventRequest,
    EventPublishResponse,
    ErrorResponse,
    IncomingEvent
)
from ..telemetry import trace_method, add_span_attributes, get_correlation_id
from ..metrics import track_telemetry_ingestion, track_telemetry_processing, track_event_processing

logger = get_logger(__name__)

# Create router
router = APIRouter()

@router.post(
    "/callback",
    status_code=status.HTTP_202_ACCEPTED,
    include_in_schema=False  # This is an internal endpoint
)
async def event_callback(    event: IncomingEvent,    messaging_client: MessagingClient = Depends(get_messaging_client)):
    """
    Callback endpoint for receiving events from the messaging service.
    """
    try:
        logger.info(f"Received event via callback: {event.event_type}")
        # Process the event using the messaging client's registered handlers
        await messaging_client.process_event(event)
        return {"status": "received"}
    except Exception as e:
        logger.error(f"Error processing event callback for type {event.event_type}: {e}", exc_info=True)
        # Even if processing fails, acknowledge receipt to prevent retries for bad messages
        return {"status": "error", "detail": str(e)}

@router.post(
    "/",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.events.ingest_event", kind="SERVER")
async def ingest_event(
    event: EventData = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Ingest a single event.
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        add_span_attributes({
            "event.type": event.event_type,
            "event.service": event.service,
            "correlation_id": correlation_id
        })
        
        if not event.timestamp:
            event.timestamp = datetime.utcnow()
        
        track_telemetry_ingestion("event")
        track_event_processing(event.service, event.event_type, event.severity)
        
        await messaging_client.publish_event(
            event_type="telemetry.event.ingested",
            event_data={"event": event.model_dump()},
            channel="database",
            correlation_id=correlation_id
        )
        
        track_telemetry_processing("event", time.time() - start_time)
        
        return EventResponse(
            event_id=None, # ID will be assigned by the database service
            status="success",
            message="Event ingestion request published successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to publish event ingestion request: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to publish event ingestion request: {str(e)}"
        )


@router.post(
    "/batch",
    response_model=EventResponse,
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.events.ingest_event_batch", kind="SERVER")
async def ingest_event_batch(
    batch: EventDataBatch = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Ingest a batch of events by publishing them to the messaging service.
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        add_span_attributes({
            "event.batch_size": len(batch.events),
            "correlation_id": correlation_id
        })
        
        current_time = datetime.utcnow()
        for event in batch.events:
            if not event.timestamp:
                event.timestamp = current_time
            
            await messaging_client.publish_event(
                event_type="telemetry.event.ingested",
                event_data={"event": event.model_dump()},
                channel="database",
                correlation_id=correlation_id
            )
            track_event_processing(event.service, event.event_type, event.severity)
        
        track_telemetry_ingestion("event", len(batch.events))
        track_telemetry_processing("event", time.time() - start_time)
        
        return EventResponse(
            event_id=None,
            status="success",
            message=f"Batch of {len(batch.events)} events published for ingestion successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to publish event batch for ingestion: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to publish event batch for ingestion: {str(e)}"
        )

@router.post(
    "/publish",
    response_model=EventPublishResponse,
    status_code=status.HTTP_202_ACCEPTED,
    responses={
        400: {"model": ErrorResponse, "description": "Bad Request"},
        500: {"model": ErrorResponse, "description": "Internal Server Error"}
    }
)
@trace_method(name="api.events.publish_event", kind="SERVER")
async def publish_event(
    event_request: EventRequest = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Publish an event to the messaging system.
    """
    start_time = time.time()
    correlation_id = event_request.correlation_id or get_correlation_id()
    
    try:
        add_span_attributes({
            "event.type": event_request.event_type,
            "event.source": event_request.source_service,
            "correlation_id": correlation_id
        })
        
        await messaging_client.publish_event(
            event_type=event_request.event_type,
            event_data=event_request.event_data,
            correlation_id=correlation_id,
            channel=event_request.channel or "default"
        )
        
        track_telemetry_processing("event_publish", time.time() - start_time)
        
        return EventPublishResponse(
            success=True,
            message="Event published successfully",
            event_id=None, # Event ID is not known at publish time
            correlation_id=correlation_id
        )
        
    except Exception as e:
        logger.error(f"Failed to publish event: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Event publish failed: {str(e)}"
        )

async def generic_query_request(
    request_type: str,
    payload: Dict[str, Any],
    messaging_client: MessagingClient
) -> Dict[str, Any]:
    """
    Generic helper to publish a query request event.
    """
    correlation_id = get_correlation_id()
    add_span_attributes(payload)

    try:
        message_id = await messaging_client.publish_event(
            event_type=f"query.{request_type}.request",
            event_data=payload,
            channel="database",
            correlation_id=correlation_id
        )
        
        return {
            "status": "accepted",
            "message": f"{request_type.replace('_', ' ').title()} query request submitted successfully",
            "request_id": message_id,
            "correlation_id": correlation_id,
            "note": "Query will be processed asynchronously. Use request_id to track status."
        }
    except Exception as e:
        logger.error(f"Failed to submit {request_type} query request: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to submit {request_type} query request: {str(e)}"
        )

@router.post(
    "/query/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.events.request_event_query", kind="SERVER")
async def request_event_query(
    query: EventQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to query events based on criteria.
    """
    return await generic_query_request("event_query", query.model_dump(), messaging_client)

@router.post(
    "/statistics/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.events.request_event_statistics", kind="SERVER")
async def request_event_statistics(
    query: EventQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to get event statistics.
    """
    return await generic_query_request("event_statistics", query.model_dump(), messaging_client)

@router.post(
    "/services/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.events.request_event_services", kind="SERVER")
async def request_event_services(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request list of services that have reported events.
    """
    return await generic_query_request("event_services", {}, messaging_client)

@router.post(
    "/types/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.events.request_event_types", kind="SERVER")
async def request_event_types(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request list of event types.
    """
    return await generic_query_request("event_types", {}, messaging_client)

@router.post(
    "/delete/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.events.request_events_deletion", kind="SERVER")
async def request_events_deletion(
    query: EventQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to delete events based on criteria.
    """
    if not any(query.model_dump().values()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one filter parameter is required for deletion."
        )
    return await generic_query_request("event_deletion", query.model_dump(), messaging_client)
