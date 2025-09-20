"""
API endpoints for Market Data Provider Service.

This module provides the API endpoints for Market Data Provider Service functionality.
"""

import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from ..messaging_client import MessagingClient, get_messaging_client
from ..models import DataModel, CommandModel, ResponseModel

# Configure logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

@router.get("/status", response_model=Dict[str, Any])
async def get_service_status(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Get the current status of Market Data Provider Service and its dependencies.
    
    Returns:
        Dict: Service status information
    """
    status_info = {
        "service": "market_data_provider_service",
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
            "service": "market_data_provider_service",
            "operation": "get_data",
            "parameters": {
                "limit": limit,
                "offset": offset
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="data.request.market_data_provider_service",
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
            event_type="command.market_data_provider_service.execute",
            event_data={
                "command": command.dict(),
                "service": "market_data_provider_service"
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
