from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from typing import List, Dict
import json
import asyncio
import logging
import redis.asyncio as redis
from ..config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter()

class ConnectionManager:
    """Manages active WebSocket connections."""
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"Client connected: {client_id}")

    def disconnect(self, client_id: str):
        if client_id in self.active_connections:
            del self.active_connections[client_id]
            logger.info(f"Client disconnected: {client_id}")

    async def send_personal_message(self, message: str, client_id: str):
        if client_id in self.active_connections:
            await self.active_connections[client_id].send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            try:
                await connection.send_text(message)
            except Exception as e:
                logger.error(f"Error broadcasting to client: {e}")

manager = ConnectionManager()

@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            # Wait for messages from the client (Heartbeat or Command)
            data = await websocket.receive_text()
            
            # Simple Heartbeat Logic
            if data == "ping":
                await manager.send_personal_message("pong", client_id)
            else:
                # Echo back or process command
                logger.debug(f"Received from {client_id}: {data}")
                
    except WebSocketDisconnect:
        manager.disconnect(client_id)
    except Exception as e:
        logger.error(f"WebSocket error for {client_id}: {e}")
        manager.disconnect(client_id)

async def redis_connector(manager: ConnectionManager):
    """
    Background task to subscribe to Redis and push messages to WebSockets.
    """
    settings = get_settings()
    redis_url = settings.redis_url
    
    try:
        r = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)
        pubsub = r.pubsub()
        
        # Subscribe to a global broadcast channel and specific notification channels
        await pubsub.subscribe("websocket.broadcast", "events.alerts")
        
        logger.info("Connected to Redis Pub/Sub for WebSockets")

        async for message in pubsub.listen():
            if message["type"] == "message":
                payload = message["data"]
                channel = message["channel"]
                logger.debug(f"Received Redis message on {channel}: {payload}")
                
                # Broadcast to all connected clients
                # In a real scenario, you might parse the payload to find a specific target_client_id
                await manager.broadcast(json.dumps({
                    "type": "event",
                    "channel": channel,
                    "data": payload
                }))
                
    except Exception as e:
        logger.error(f"Redis Connector Error: {e}")
        # In production, implement retry logic here or let the task fail and restart
