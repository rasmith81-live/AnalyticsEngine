"""
Dashboard WebSocket API
Real-time dashboard updates via WebSocket
"""
import asyncio
import logging
import json
from typing import Dict, List, Any, Optional
from datetime import datetime

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query, HTTPException
import httpx

from app.core.websocket_manager import websocket_manager
from app.core.pubsub import pubsub_service
from app.core.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()


@router.websocket("/dashboard")
async def dashboard_websocket(
    websocket: WebSocket,
    dashboard_id: Optional[str] = Query(None),
    user_id: Optional[str] = Query(None)
):
    """
    WebSocket endpoint for real-time dashboard updates
    
    Clients connect and subscribe to KPI updates for their dashboard.
    Receives calculated KPI results from calculation engine via Redis pub/sub.
    
    Query Parameters:
        dashboard_id: Optional dashboard identifier
        user_id: Optional user identifier
    
    Message Types (Client -> Server):
        - subscribe_kpi: Subscribe to KPI updates
        - unsubscribe_kpi: Unsubscribe from KPI updates
        - subscribe_dashboard: Subscribe to all KPIs in a dashboard
        - ping: Keep connection alive
    
    Message Types (Server -> Client):
        - connection_established: Initial connection confirmation
        - kpi_update: Real-time KPI calculation result
        - subscription_confirmed: Subscription confirmation
        - error: Error message
        - heartbeat: Periodic heartbeat
        - pong: Response to ping
    """
    await websocket.accept()
    
    # Register connection
    client_info = {
        "dashboard_id": dashboard_id,
        "user_id": user_id,
        "connected_at": datetime.utcnow().isoformat()
    }
    connection_id = await websocket_manager.connect(websocket, client_info)
    
    try:
        # Send connection established message
        await websocket.send_json({
            "type": "connection_established",
            "connection_id": connection_id,
            "timestamp": datetime.utcnow().isoformat(),
            "message": "Connected to dashboard WebSocket"
        })
        
        logger.info(
            f"Dashboard WebSocket connected: {connection_id} "
            f"(dashboard={dashboard_id}, user={user_id})"
        )
        
        # Listen for client messages
        while True:
            try:
                # Receive message from client
                data = await websocket.receive_json()
                message_type = data.get("type")
                
                if message_type == "subscribe_kpi":
                    await handle_subscribe_kpi(connection_id, data, websocket)
                
                elif message_type == "unsubscribe_kpi":
                    await handle_unsubscribe_kpi(connection_id, data, websocket)
                
                elif message_type == "subscribe_dashboard":
                    await handle_subscribe_dashboard(connection_id, data, websocket)
                
                elif message_type == "ping":
                    await websocket.send_json({
                        "type": "pong",
                        "timestamp": datetime.utcnow().isoformat()
                    })
                
                else:
                    await websocket.send_json({
                        "type": "error",
                        "message": f"Unknown message type: {message_type}",
                        "timestamp": datetime.utcnow().isoformat()
                    })
            
            except WebSocketDisconnect:
                logger.info(f"Dashboard WebSocket disconnected: {connection_id}")
                break
            
            except json.JSONDecodeError:
                await websocket.send_json({
                    "type": "error",
                    "message": "Invalid JSON",
                    "timestamp": datetime.utcnow().isoformat()
                })
            
            except Exception as e:
                logger.error(f"Error processing message from {connection_id}: {e}")
                await websocket.send_json({
                    "type": "error",
                    "message": str(e),
                    "timestamp": datetime.utcnow().isoformat()
                })
    
    finally:
        # Unregister connection
        await websocket_manager.disconnect(connection_id)
        logger.info(f"Dashboard WebSocket cleanup complete: {connection_id}")


async def handle_subscribe_kpi(connection_id: str, data: Dict[str, Any], websocket: WebSocket):
    """
    Handle KPI subscription request
    
    Expected data:
        {
            "type": "subscribe_kpi",
            "kpi_code": "DIO",
            "entity_id": "warehouse_001",
            "period": "minute"
        }
    """
    try:
        kpi_code = data.get("kpi_code")
        entity_id = data.get("entity_id")
        period = data.get("period", "minute")
        
        if not kpi_code or not entity_id:
            await websocket.send_json({
                "type": "error",
                "message": "Missing kpi_code or entity_id",
                "timestamp": datetime.utcnow().isoformat()
            })
            return
        
        # Subscribe to calculated KPI results channel
        channel = f"kpi.calculated.{kpi_code}.{entity_id}.{period}"
        await websocket_manager.subscribe(connection_id, channel)
        
        # Subscribe to Redis pub/sub for this channel
        async def kpi_message_handler(ch: str, message: Any):
            """Handler for KPI update messages"""
            await websocket_manager.broadcast_to_channel(channel, {
                "type": "kpi_update",
                "kpi_code": kpi_code,
                "entity_id": entity_id,
                "period": period,
                "data": message,
                "timestamp": datetime.utcnow().isoformat()
            })
        
        await pubsub_service.subscribe(channel, kpi_message_handler)
        
        # Also subscribe calculation engine to start streaming
        await subscribe_calculation_engine(kpi_code, entity_id, period)
        
        # Send confirmation
        await websocket.send_json({
            "type": "subscription_confirmed",
            "kpi_code": kpi_code,
            "entity_id": entity_id,
            "period": period,
            "channel": channel,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        logger.info(f"Connection {connection_id} subscribed to KPI: {kpi_code}:{entity_id}:{period}")
    
    except Exception as e:
        logger.error(f"Error subscribing to KPI: {e}")
        await websocket.send_json({
            "type": "error",
            "message": f"Subscription failed: {str(e)}",
            "timestamp": datetime.utcnow().isoformat()
        })


async def handle_unsubscribe_kpi(connection_id: str, data: Dict[str, Any], websocket: WebSocket):
    """
    Handle KPI unsubscription request
    
    Expected data:
        {
            "type": "unsubscribe_kpi",
            "kpi_code": "DIO",
            "entity_id": "warehouse_001",
            "period": "minute"
        }
    """
    try:
        kpi_code = data.get("kpi_code")
        entity_id = data.get("entity_id")
        period = data.get("period", "minute")
        
        if not kpi_code or not entity_id:
            await websocket.send_json({
                "type": "error",
                "message": "Missing kpi_code or entity_id",
                "timestamp": datetime.utcnow().isoformat()
            })
            return
        
        # Unsubscribe from channel
        channel = f"kpi.calculated.{kpi_code}.{entity_id}.{period}"
        await websocket_manager.unsubscribe(connection_id, channel)
        
        # Send confirmation
        await websocket.send_json({
            "type": "unsubscription_confirmed",
            "kpi_code": kpi_code,
            "entity_id": entity_id,
            "period": period,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        logger.info(f"Connection {connection_id} unsubscribed from KPI: {kpi_code}:{entity_id}:{period}")
    
    except Exception as e:
        logger.error(f"Error unsubscribing from KPI: {e}")
        await websocket.send_json({
            "type": "error",
            "message": f"Unsubscription failed: {str(e)}",
            "timestamp": datetime.utcnow().isoformat()
        })


async def handle_subscribe_dashboard(connection_id: str, data: Dict[str, Any], websocket: WebSocket):
    """
    Handle dashboard subscription request
    
    Subscribes to all KPIs in a dashboard configuration.
    
    Expected data:
        {
            "type": "subscribe_dashboard",
            "kpis": [
                {"kpi_code": "DIO", "entity_id": "warehouse_001", "period": "minute"},
                {"kpi_code": "DSO", "entity_id": "warehouse_001", "period": "hour"}
            ]
        }
    """
    try:
        kpis = data.get("kpis", [])
        
        if not kpis:
            await websocket.send_json({
                "type": "error",
                "message": "No KPIs specified",
                "timestamp": datetime.utcnow().isoformat()
            })
            return
        
        # Subscribe to each KPI
        subscribed_kpis = []
        for kpi_config in kpis:
            kpi_code = kpi_config.get("kpi_code")
            entity_id = kpi_config.get("entity_id")
            period = kpi_config.get("period", "minute")
            
            if kpi_code and entity_id:
                # Subscribe to channel
                channel = f"kpi.calculated.{kpi_code}.{entity_id}.{period}"
                await websocket_manager.subscribe(connection_id, channel)
                
                # Subscribe to Redis pub/sub
                async def kpi_message_handler(ch: str, message: Any):
                    await websocket_manager.broadcast_to_channel(channel, {
                        "type": "kpi_update",
                        "kpi_code": kpi_code,
                        "entity_id": entity_id,
                        "period": period,
                        "data": message,
                        "timestamp": datetime.utcnow().isoformat()
                    })
                
                await pubsub_service.subscribe(channel, kpi_message_handler)
                
                # Subscribe calculation engine
                await subscribe_calculation_engine(kpi_code, entity_id, period)
                
                subscribed_kpis.append({
                    "kpi_code": kpi_code,
                    "entity_id": entity_id,
                    "period": period
                })
        
        # Send confirmation
        await websocket.send_json({
            "type": "dashboard_subscription_confirmed",
            "subscribed_kpis": subscribed_kpis,
            "count": len(subscribed_kpis),
            "timestamp": datetime.utcnow().isoformat()
        })
        
        logger.info(f"Connection {connection_id} subscribed to {len(subscribed_kpis)} KPIs")
    
    except Exception as e:
        logger.error(f"Error subscribing to dashboard: {e}")
        await websocket.send_json({
            "type": "error",
            "message": f"Dashboard subscription failed: {str(e)}",
            "timestamp": datetime.utcnow().isoformat()
        })


async def subscribe_calculation_engine(kpi_code: str, entity_id: str, period: str):
    """
    Subscribe calculation engine to start streaming KPI calculations
    
    Args:
        kpi_code: KPI code
        entity_id: Entity ID
        period: Time period
    """
    try:
        # Get calculation engine URL from settings
        calc_engine_url = settings.SERVICE_REGISTRY.get("calculation_engine", {}).get("url")
        
        if not calc_engine_url:
            logger.warning("Calculation engine URL not configured")
            return
        
        # Subscribe calculation engine to stream
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.post(
                f"{calc_engine_url}/stream/subscribe",
                params={
                    "kpi_code": kpi_code,
                    "entity_id": entity_id,
                    "period": period
                }
            )
            response.raise_for_status()
            
            logger.info(f"Calculation engine subscribed to {kpi_code}:{entity_id}:{period}")
    
    except Exception as e:
        logger.error(f"Failed to subscribe calculation engine: {e}")


@router.get("/ws/stats")
async def get_websocket_stats():
    """
    Get WebSocket connection statistics
    
    Returns:
        Statistics about active connections and subscriptions
    """
    stats = await websocket_manager.get_stats()
    return stats
