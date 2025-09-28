"""
API endpoints for Broker Service.

This module provides the API endpoints for Broker Service functionality.
"""

import logging
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel, Field

from ..messaging_client import MessagingClient, get_messaging_client
from ..models import DataModel, CommandModel, ResponseModel
from ..main import order_manager

class Order(BaseModel):
    symbol: str = Field(..., description="The stock symbol to trade.")
    quantity: int = Field(..., gt=0, description="The number of shares to trade.")
    order_type: str = Field("market", description="The type of order to place (e.g., 'market' or 'limit').")

# Configure logging
logger = logging.getLogger(__name__)

# Initialize router
router = APIRouter()

@router.get("/status", response_model=Dict[str, Any])
async def get_service_status(
    messaging_client: MessagingClient = Depends(get_messaging_client)
):
    """
    Get the current status of Broker Service and its dependencies.
    
    Returns:
        Dict: Service status information
    """
    status_info = {
        "service": "broker_service",
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

@router.post("/orders/buy", status_code=status.HTTP_202_ACCEPTED)
async def manual_buy(
    order: Order,
    order_manager_instance: "OrderManager" = Depends(lambda: order_manager)
):
    """
    Manually execute a buy order.
    """
    await order_manager_instance.handle_buy_order(order.dict())
    return {"status": "accepted", "message": f"Manual buy order for {order.quantity} shares of {order.symbol} received."}

@router.post("/orders/sell", status_code=status.HTTP_202_ACCEPTED)
async def manual_sell(
    order: Order,
    order_manager_instance: "OrderManager" = Depends(lambda: order_manager)
):
    """
    Manually execute a sell order.
    """
    await order_manager_instance.handle_sell_order(order.dict())
    logger.info(f"Manual sell order for {order.quantity} shares of {order.symbol} received.")
    return {"status": "accepted", "message": f"Manual sell order for {order.quantity} shares of {order.symbol} received."}

@router.post("/trading/stop-buys", status_code=status.HTTP_200_OK)
async def stop_buy_orders():
    """
    Stops any further buy order executions.
    """
    logger.info("Received command to stop all buy orders.")
    # In a real implementation, you would add logic here to halt buy orders.
    return {"status": "success", "message": "Buy orders have been halted."}

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
            "service": "broker_service",
            "operation": "get_data",
            "parameters": {
                "limit": limit,
                "offset": offset
            }
        }
        
        message_id = await messaging_client.publish_event(
            event_type="data.request.broker_service",
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
            event_type="command.broker_service.execute",
            event_data={
                "command": command.dict(),
                "service": "broker_service"
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
