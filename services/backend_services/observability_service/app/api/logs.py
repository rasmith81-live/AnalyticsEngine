"""
Logs API Router

This module provides API endpoints for log data ingestion and retrieval.
"""

from ..logging import get_logger
import time
from typing import Dict, List, Any, Optional
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Body, status

from ..config import get_settings
from ..dependencies import get_messaging_client, MessagingClient
from ..models import (
    LogData,
    LogDataBatch,
    LogQuery,
    LogResponse,
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
    response_model=LogResponse,
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.logs.ingest_log", kind="SERVER")
async def ingest_log(
    log: LogData = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Publish a single log entry for ingestion.
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        add_span_attributes({
            "log.service": log.service,
            "log.severity": log.severity,
            "correlation_id": correlation_id
        })
        
        if not log.timestamp:
            log.timestamp = datetime.utcnow()
        
        await messaging_client.publish_event(
            event_type="telemetry.log.ingested",
            event_data={"log": log.model_dump()},
            channel="database",
            correlation_id=correlation_id
        )
        
        track_telemetry_ingestion("log")
        track_telemetry_processing("log", time.time() - start_time)
        
        return LogResponse(
            status="accepted",
            message="Log ingestion request published successfully",
            count=1
        )
        
    except Exception as e:
        logger.error(f"Failed to publish log ingestion request: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to publish log ingestion request: {str(e)}"
        )


@router.post(
    "/batch",
    response_model=LogResponse,
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.logs.ingest_log_batch", kind="SERVER")
async def ingest_log_batch(
    batch: LogDataBatch = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Publish a batch of logs for ingestion.
    """
    start_time = time.time()
    correlation_id = get_correlation_id()
    
    try:
        add_span_attributes({
            "log.batch_size": len(batch.logs),
            "correlation_id": correlation_id
        })
        
        current_time = datetime.utcnow()
        for log in batch.logs:
            if not log.timestamp:
                log.timestamp = current_time
            
            await messaging_client.publish_event(
                event_type="telemetry.log.ingested",
                event_data={"log": log.model_dump()},
                channel="database",
                correlation_id=correlation_id
            )
        
        track_telemetry_ingestion("log", len(batch.logs))
        track_telemetry_processing("log", time.time() - start_time)
        
        return LogResponse(
            status="accepted",
            message=f"Batch of {len(batch.logs)} logs published for ingestion successfully",
            count=len(batch.logs)
        )
        
    except Exception as e:
        logger.error(f"Failed to publish log batch for ingestion: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to publish log batch for ingestion: {str(e)}"
        )


@router.post(
    "/query/request",
    response_model=Dict[str, Any],
    status_code=status.HTTP_202_ACCEPTED
)
@trace_method(name="api.logs.request_logs_query", kind="SERVER")
async def request_logs_query(
    query: LogQuery = Body(...),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request to query logs based on criteria.
    """
    return await generic_query_request("log_query", query.model_dump(), messaging_client)
