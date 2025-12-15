"""
Traces API Router

This module provides API endpoints for trace data ingestion and retrieval.
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
    TraceData,
    TraceDataBatch,
    TraceQuery,
    TraceResponse,
    TraceStatistics,
    ErrorResponse
)
from ..telemetry import trace_method, add_span_attributes, get_correlation_id
from ..metrics import track_telemetry_ingestion, track_telemetry_processing

logger = get_logger(__name__)

# Create router
router = APIRouter()

async def generic_query_request(
    request_type: str,
    payload: Dict[str, Any],
    messaging_client: MessagingClient
) -> Dict[str, Any]:
    """
    Generic helper to publish a query or command request event.
    """
    correlation_id = get_correlation_id()
    add_span_attributes(payload)

    try:
        event_type = f"query.{request_type}.request" if 'query' in request_type else f"command.{request_type}.request"
        message_id = await messaging_client.publish_event(
            event_type=event_type,
            event_data=payload,
            channel="database",
            correlation_id=correlation_id
        )
        
        return {
            "status": "accepted",
            "message": f"{request_type.replace('_', ' ').title()} request submitted successfully",
            "request_id": message_id,
            "correlation_id": correlation_id,
            "note": "Request will be processed asynchronously. Use request_id to track status."
        }
    except Exception as e:
        logger.error(f"Failed to submit {request_type} request: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to submit {request_type} request: {str(e)}"
        )

@router.post(
    "/",
    response_model=TraceResponse,
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.traces.ingest_trace", kind="SERVER")
async def ingest_trace(
    trace: TraceData = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Publish a single trace for ingestion.
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        add_span_attributes({
            "trace.id": trace.trace_id,
            "trace.service": trace.service,
            "correlation_id": correlation_id
        })
        
        if not trace.timestamp:
            trace.timestamp = datetime.utcnow()
        
        await messaging_client.publish_event(
            event_type="telemetry.trace.ingested",
            event_data={"trace": trace.model_dump()},
            channel="database",
            correlation_id=correlation_id
        )
        
        track_telemetry_ingestion("trace")
        track_telemetry_processing("trace", time.time() - start_time)
        
        return TraceResponse(
            trace_id=trace.trace_id,
            status="accepted",
            message="Trace ingestion request published successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to publish trace ingestion request: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to publish trace ingestion request: {str(e)}"
        )


@router.post(
    "/batch",
    response_model=TraceResponse,
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.traces.ingest_trace_batch", kind="SERVER")
async def ingest_trace_batch(
    batch: TraceDataBatch = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Publish a batch of traces for ingestion.
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        add_span_attributes({
            "trace.batch_size": len(batch.traces),
            "correlation_id": correlation_id
        })
        
        current_time = datetime.utcnow()
        for trace in batch.traces:
            if not trace.timestamp:
                trace.timestamp = current_time
            
            await messaging_client.publish_event(
                event_type="telemetry.trace.ingested",
                event_data={"trace": trace.model_dump()},
                channel="database",
                correlation_id=correlation_id
            )
        
        track_telemetry_ingestion("trace", len(batch.traces))
        track_telemetry_processing("trace", time.time() - start_time)
        
        return TraceResponse(
            trace_id="batch",
            status="accepted",
            message=f"Batch of {len(batch.traces)} traces published for ingestion successfully"
        )
        
    except Exception as e:
        logger.error(f"Failed to publish trace batch for ingestion: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to publish trace batch for ingestion: {str(e)}"
        )


@router.post(
    "/query/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.traces.request_traces_query", kind="SERVER")
async def request_traces_query(
    query: TraceQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to query traces based on criteria.
    """
    return await generic_query_request("trace_query", query.model_dump(), messaging_client)


@router.post(
    "/statistics/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.traces.request_trace_statistics", kind="SERVER")
async def request_trace_statistics(
    query: TraceQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to get trace statistics.
    """
    return await generic_query_request("trace_statistics", query.model_dump(), messaging_client)


@router.post(
    "/delete/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.traces.request_trace_deletion", kind="SERVER")
async def request_trace_deletion(
    query: TraceQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to delete traces based on criteria.
    """
    if not any(query.model_dump().values()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one filter parameter is required for deletion."
        )
    return await generic_query_request("trace_deletion", query.model_dump(), messaging_client)
