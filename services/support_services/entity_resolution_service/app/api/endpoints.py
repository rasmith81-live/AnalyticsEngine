"""
API endpoints for Entity Resolution Service.

This module provides the API endpoints for Entity Resolution Service functionality.
"""

import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from ..messaging_client import MessagingClient, get_messaging_client
from ..models import (
    DataModel, CommandModel, ResponseModel, 
    SemanticExtractionRequest, SemanticExtractionResponse,
    IntentExtractionRequest, IntentExtractionResponse, BusinessIntent, ExtractedEntity
)
from ..engine.semantic_extractor import semantic_extractor

# Configure logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

@router.get("/status", response_model=Dict[str, Any])
async def get_service_status(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Get the current status of Entity Resolution Service and its dependencies.
    
    Returns:
        Dict: Service status information
    """
    status_info = {
        "service": "entity_resolution_service",
        "status": "operational",
        "dependencies": {}
    }
    
    # Check messaging connection (primary dependency for event-driven architecture)
    try:
        msg_health = await messaging_client.check_health()
        is_healthy = isinstance(msg_health, dict) and msg_health.get("status") in ["ok", "healthy", "operational"]

        status_info["dependencies"]["messaging"] = {
            "status": "connected" if is_healthy else "error",
            "details": msg_health
        }

        if not is_healthy:
            status_info["status"] = "degraded"
            
    except Exception as e:
        logger.error(f"Error checking messaging connection: {e}")
        status_info["dependencies"]["messaging"] = {
            "status": "error",
            "details": {"error": str(e)}
        }
        status_info["status"] = "degraded"
    
    return status_info

@router.post("/data/request", response_model=Dict[str, Any], status_code=status.HTTP_202_ACCEPTED)
async def request_data(
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Request data from the service with pagination via messaging.
    
    Args:
        limit: Maximum number of records to return
        offset: Number of records to skip
        messaging_client: Messaging client dependency
        
    Returns:
        Dict: Data request status with request ID for tracking
    """
    try:
        # Publish data request event for database service to process
        request_data = {
            "service": "entity_resolution_service",
            "operation": "get_data",
            "parameters": {
                "limit": limit,
                "offset": offset
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="data.request.entity_resolution_service",
            event_data=request_data,
            correlation_id=None
        )
        
        return {
            "status": "accepted",
            "message": "Data request submitted successfully",
            "request_id": message_id,
            "note": "Data will be processed asynchronously. Use request_id to track status."
        }
    except Exception as e:
        logger.error(f"Error requesting data: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to request data: {str(e)}"
        )

@router.post("/semantic/extract", response_model=SemanticExtractionResponse)
async def extract_entities_semantic(
    request: SemanticExtractionRequest
):
    """
    Extract business entities from text using NLP-based semantic analysis.
    
    This endpoint uses spaCy for Part-of-Speech tagging and noun phrase extraction
    to identify business entities without relying on predefined keywords.
    
    Args:
        request: SemanticExtractionRequest with text to analyze
        
    Returns:
        SemanticExtractionResponse with extracted entities, inferred domain, and module
    """
    try:
        result = await semantic_extractor.extract(
            text=request.text,
            name=request.name,
            description=request.description,
            formula=request.formula,
            source_file=request.source_file
        )
        return result
    except Exception as e:
        logger.error(f"Error in semantic extraction: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Semantic extraction failed: {str(e)}"
        )


@router.post("/semantic/extract-intent", response_model=IntentExtractionResponse)
async def extract_intent(
    request: IntentExtractionRequest
):
    """
    Extract structured business intent from text using LLM.
    
    This endpoint combines NLP entity extraction with LLM-based intent analysis
    to return a structured BusinessIntent including domain, entities, action, and metrics.
    
    Use this when:
    - BMS metadata is sparse and semantic matching fails
    - Processing conversational queries
    - Need structured intent from unstructured text
    
    Args:
        request: IntentExtractionRequest with text and optional context
        
    Returns:
        IntentExtractionResponse with BusinessIntent, raw entities, and noun phrases
    """
    try:
        result = await semantic_extractor.extract_intent(
            text=request.text,
            context=request.context,
            source_file=request.source_file
        )
        
        # Convert raw entities to ExtractedEntity models
        raw_entities = []
        for e in result.get("raw_entities", []):
            if hasattr(e, "dict"):
                raw_entities.append(e)
            elif isinstance(e, dict):
                raw_entities.append(ExtractedEntity(**e))
        
        return IntentExtractionResponse(
            intent=BusinessIntent(**result["intent"]),
            raw_entities=raw_entities,
            noun_phrases=result.get("noun_phrases", []),
            processing_time_ms=result.get("processing_time_ms", 0.0)
        )
    except Exception as e:
        logger.error(f"Error in intent extraction: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Intent extraction failed: {str(e)}"
        )


class BatchExtractionRequest(BaseModel):
    """Request for batch entity extraction from multiple KPIs."""
    kpi_texts: List[str] = Field(..., description="List of KPI text strings (name + description)")

class BatchExtractionResponse(BaseModel):
    """Response from batch entity extraction."""
    entities: List[str] = Field(default_factory=list, description="Distinct entity names")
    count: int = Field(default=0, description="Number of entities extracted")

@router.post("/semantic/extract-batch", response_model=BatchExtractionResponse)
async def extract_batch(request: BatchExtractionRequest):
    """
    Extract distinct entities from multiple KPIs in a single LLM call.
    Much more efficient than calling /semantic/extract for each KPI.
    """
    try:
        entities = await semantic_extractor.extract_batch(request.kpi_texts)
        return BatchExtractionResponse(
            entities=entities,
            count=len(entities)
        )
    except Exception as e:
        logger.error(f"Error in batch extraction: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Batch extraction failed: {str(e)}"
        )

@router.post("/command", response_model=Dict[str, Any], status_code=status.HTTP_202_ACCEPTED)
async def execute_command(
    command: CommandModel,
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Execute a command through the messaging system.
    
    Args:
        command: Command model with action and parameters
        messaging_client: Messaging client dependency
        
    Returns:
        Dict: Command execution status
    """
    try:
        # Publish command event for processing
        message_id = await messaging_client.publish_event(
            event_type="command.entity_resolution_service.execute",
            event_data={
                "command": command.dict(),
                "service": "entity_resolution_service"
            },
            correlation_id=None
        )
        
        return {
            "status": "accepted",
            "message_id": message_id,
            "command_id": command.command_id
        }
    except Exception as e:
        logger.error(f"Error executing command: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to execute command: {str(e)}"
        )
