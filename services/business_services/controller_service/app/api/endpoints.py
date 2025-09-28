"""
API endpoints for Controller Service.

This module provides the API endpoints for Controller Service functionality.
"""

import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from ..messaging_client import MessagingClient, get_messaging_client
from ..models import DataModel, CommandModel, ResponseModel
from ..config import get_settings
from ..session_monitor import SessionMonitor, TradingSession
from ..main import session_monitor
import httpx

# Configure logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

@router.get("/status", response_model=Dict[str, Any])
async def get_service_status(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Get the current status of Controller Service and its dependencies.
    
    Returns:
        Dict: Service status information
    """
    status_info = {
        "service": "controller_service",
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
            "service": "controller_service",
            "operation": "get_data",
            "parameters": {
                "limit": limit,
                "offset": offset
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="data.request.controller_service",
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
            event_type="command.controller_service.execute",
            event_data={
                "command": command.dict(),
                "service": "controller_service"
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


def get_session_monitor() -> SessionMonitor:
    """Dependency to get session monitor instance."""
    if session_monitor is None:
        raise HTTPException(status_code=503, detail="Session monitor not initialized")
    return session_monitor

@router.get("/session/status", response_model=Dict[str, TradingSession])
async def get_session_status(
    monitor: SessionMonitor = Depends(get_session_monitor)
):
    """
    Get the current NYSE trading session status.
    """
    return {"session": monitor.current_session}

@router.post("/trading/start", status_code=status.HTTP_202_ACCEPTED)
async def start_trading(
    session_monitor: SessionMonitor = Depends(get_session_monitor),
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Publishes a command to start the market data stream if the market is open.
    """
    if session_monitor.current_session == TradingSession.CLOSED:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Market is closed. Cannot start trading."
        )
    
    await messaging_client.publish_command(
        command_type="StartMarketDataStream",
        payload={}
    )

    await messaging_client.publish_command(
        command_type="StartNewsDataStream",
        payload={}
    )

    await messaging_client.publish_command(
        command_type="DetermineTradingSession",
        payload={}
    )
    
    return {"status": "accepted", "message": "Start market, news, and session determination commands published."}

@router.post("/trading/stop", status_code=status.HTTP_202_ACCEPTED)
async def stop_trading(messaging_client: MessagingClient = Depends(get_messaging_client)):
    """
    Publishes commands to stop the market data stream and halt buy orders.
    """

    await messaging_client.publish_command(
        command_type="StopMarketDataStream",
        payload={}
    )
    
    await messaging_client.publish_command(
        command_type="HaltBuyOrders",
        payload={}
    )
    
    return {"status": "accepted", "message": "Stop trading commands published."}

@router.post("/trading/crashdown", status_code=status.HTTP_202_ACCEPTED)
async def crashdown_trading(messaging_client: MessagingClient = Depends(get_messaging_client)):
    """
    Publishes a command to halt all trading and exit open positions due to deteriorating market conditions.
    """
    await messaging_client.publish_command(
        command_type="HaltTradingAndCrashPositions",
        payload={}
    )
    
    return {"status": "accepted", "message": "Trading crashdown command published."}

@router.post("/trading/winddown", status_code=status.HTTP_202_ACCEPTED)
async def winddown_trading(messaging_client: MessagingClient = Depends(get_messaging_client)):
    """
    Publishes a command to halt all trading and exit open positions gracefully at end of trading period.
    """
    await messaging_client.publish_command(
        command_type="HaltTradingAndWinddownPositions",
        payload={}
    )
    
    return {"status": "accepted", "message": "Trading crashdown command published."}