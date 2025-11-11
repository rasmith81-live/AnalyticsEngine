"""
WebSocket Connection Manager for API Gateway
Manages WebSocket connections for real-time dashboard updates
"""
import asyncio
import logging
import json
from typing import Dict, Set, Optional, Any, Callable
from datetime import datetime
from collections import defaultdict
import uuid

from fastapi import WebSocket, WebSocketDisconnect
from starlette.websockets import WebSocketState

logger = logging.getLogger(__name__)


class WebSocketConnection:
    """Represents a single WebSocket connection"""
    
    def __init__(self, websocket: WebSocket, connection_id: str, client_info: Dict[str, Any]):
        self.websocket = websocket
        self.connection_id = connection_id
        self.client_info = client_info
        self.subscriptions: Set[str] = set()
        self.connected_at = datetime.utcnow()
        self.last_activity = datetime.utcnow()
        self.message_count = 0
    
    async def send_json(self, data: Dict[str, Any]):
        """Send JSON message to client"""
        try:
            if self.websocket.client_state == WebSocketState.CONNECTED:
                await self.websocket.send_json(data)
                self.message_count += 1
                self.last_activity = datetime.utcnow()
                return True
            return False
        except Exception as e:
            logger.error(f"Error sending message to {self.connection_id}: {e}")
            return False
    
    async def close(self, code: int = 1000, reason: str = ""):
        """Close the WebSocket connection"""
        try:
            if self.websocket.client_state == WebSocketState.CONNECTED:
                await self.websocket.close(code=code, reason=reason)
        except Exception as e:
            logger.error(f"Error closing connection {self.connection_id}: {e}")


class WebSocketManager:
    """
    Manages WebSocket connections for real-time dashboard updates
    
    Responsibilities:
    - Track active WebSocket connections
    - Manage subscriptions per connection
    - Broadcast messages to subscribed connections
    - Handle connection lifecycle (connect, disconnect, timeout)
    - Provide connection statistics
    """
    
    def __init__(self, heartbeat_interval: int = 30, connection_timeout: int = 300):
        """
        Initialize WebSocket manager
        
        Args:
            heartbeat_interval: Seconds between heartbeat messages
            connection_timeout: Seconds before inactive connection is closed
        """
        self.heartbeat_interval = heartbeat_interval
        self.connection_timeout = connection_timeout
        
        # Map: connection_id -> WebSocketConnection
        self._connections: Dict[str, WebSocketConnection] = {}
        
        # Map: channel -> Set[connection_id]
        self._channel_subscriptions: Dict[str, Set[str]] = defaultdict(set)
        
        # Map: kpi_code -> Set[connection_id]
        self._kpi_subscriptions: Dict[str, Set[str]] = defaultdict(set)
        
        # Lock for thread-safe operations
        self._lock = asyncio.Lock()
        
        # Background tasks
        self._heartbeat_task: Optional[asyncio.Task] = None
        self._cleanup_task: Optional[asyncio.Task] = None
        self._running = False
        
        logger.info("WebSocketManager initialized")
    
    async def start(self):
        """Start background tasks"""
        self._running = True
        self._heartbeat_task = asyncio.create_task(self._heartbeat_loop())
        self._cleanup_task = asyncio.create_task(self._cleanup_loop())
        logger.info("WebSocketManager started")
    
    async def stop(self):
        """Stop background tasks and close all connections"""
        self._running = False
        
        # Close all connections
        async with self._lock:
            for connection in list(self._connections.values()):
                await connection.close(code=1001, reason="Server shutting down")
            self._connections.clear()
            self._channel_subscriptions.clear()
            self._kpi_subscriptions.clear()
        
        # Cancel background tasks
        if self._heartbeat_task:
            self._heartbeat_task.cancel()
            try:
                await self._heartbeat_task
            except asyncio.CancelledError:
                pass
        
        if self._cleanup_task:
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass
        
        logger.info("WebSocketManager stopped")
    
    async def connect(
        self,
        websocket: WebSocket,
        client_info: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        Register a new WebSocket connection
        
        Args:
            websocket: WebSocket instance
            client_info: Optional client information
            
        Returns:
            Connection ID
        """
        connection_id = str(uuid.uuid4())
        
        async with self._lock:
            connection = WebSocketConnection(
                websocket=websocket,
                connection_id=connection_id,
                client_info=client_info or {}
            )
            self._connections[connection_id] = connection
        
        logger.info(f"WebSocket connected: {connection_id}")
        return connection_id
    
    async def disconnect(self, connection_id: str):
        """
        Unregister a WebSocket connection
        
        Args:
            connection_id: Connection ID to disconnect
        """
        async with self._lock:
            if connection_id in self._connections:
                connection = self._connections[connection_id]
                
                # Remove from all subscriptions
                for channel in connection.subscriptions:
                    self._channel_subscriptions[channel].discard(connection_id)
                    
                    # Extract KPI code from channel if applicable
                    if channel.startswith("kpi.calculated."):
                        parts = channel.split(".")
                        if len(parts) >= 3:
                            kpi_code = parts[2]
                            self._kpi_subscriptions[kpi_code].discard(connection_id)
                
                # Remove connection
                del self._connections[connection_id]
                
                logger.info(f"WebSocket disconnected: {connection_id}")
    
    async def subscribe(self, connection_id: str, channel: str):
        """
        Subscribe a connection to a channel
        
        Args:
            connection_id: Connection ID
            channel: Channel to subscribe to
        """
        async with self._lock:
            if connection_id in self._connections:
                connection = self._connections[connection_id]
                connection.subscriptions.add(channel)
                self._channel_subscriptions[channel].add(connection_id)
                
                # Track KPI subscriptions
                if channel.startswith("kpi.calculated."):
                    parts = channel.split(".")
                    if len(parts) >= 3:
                        kpi_code = parts[2]
                        self._kpi_subscriptions[kpi_code].add(connection_id)
                
                logger.debug(f"Connection {connection_id} subscribed to {channel}")
    
    async def unsubscribe(self, connection_id: str, channel: str):
        """
        Unsubscribe a connection from a channel
        
        Args:
            connection_id: Connection ID
            channel: Channel to unsubscribe from
        """
        async with self._lock:
            if connection_id in self._connections:
                connection = self._connections[connection_id]
                connection.subscriptions.discard(channel)
                self._channel_subscriptions[channel].discard(connection_id)
                
                # Remove KPI subscription
                if channel.startswith("kpi.calculated."):
                    parts = channel.split(".")
                    if len(parts) >= 3:
                        kpi_code = parts[2]
                        self._kpi_subscriptions[kpi_code].discard(connection_id)
                
                logger.debug(f"Connection {connection_id} unsubscribed from {channel}")
    
    async def broadcast_to_channel(self, channel: str, message: Dict[str, Any]):
        """
        Broadcast message to all connections subscribed to a channel
        
        Args:
            channel: Channel to broadcast to
            message: Message to send
        """
        async with self._lock:
            subscriber_ids = self._channel_subscriptions.get(channel, set()).copy()
        
        if not subscriber_ids:
            logger.debug(f"No subscribers for channel: {channel}")
            return
        
        # Send to all subscribers
        success_count = 0
        failed_connections = []
        
        for connection_id in subscriber_ids:
            async with self._lock:
                connection = self._connections.get(connection_id)
            
            if connection:
                success = await connection.send_json(message)
                if success:
                    success_count += 1
                else:
                    failed_connections.append(connection_id)
        
        # Clean up failed connections
        for connection_id in failed_connections:
            await self.disconnect(connection_id)
        
        logger.debug(
            f"Broadcast to {channel}: {success_count} successful, "
            f"{len(failed_connections)} failed"
        )
    
    async def send_to_connection(self, connection_id: str, message: Dict[str, Any]) -> bool:
        """
        Send message to a specific connection
        
        Args:
            connection_id: Connection ID
            message: Message to send
            
        Returns:
            True if sent successfully
        """
        async with self._lock:
            connection = self._connections.get(connection_id)
        
        if connection:
            return await connection.send_json(message)
        return False
    
    async def get_connection_info(self, connection_id: str) -> Optional[Dict[str, Any]]:
        """
        Get information about a connection
        
        Args:
            connection_id: Connection ID
            
        Returns:
            Connection information or None
        """
        async with self._lock:
            connection = self._connections.get(connection_id)
            if connection:
                return {
                    "connection_id": connection.connection_id,
                    "client_info": connection.client_info,
                    "subscriptions": list(connection.subscriptions),
                    "connected_at": connection.connected_at.isoformat(),
                    "last_activity": connection.last_activity.isoformat(),
                    "message_count": connection.message_count,
                    "uptime_seconds": (datetime.utcnow() - connection.connected_at).total_seconds()
                }
        return None
    
    async def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about connections and subscriptions
        
        Returns:
            Statistics dictionary
        """
        async with self._lock:
            return {
                "total_connections": len(self._connections),
                "total_channels": len(self._channel_subscriptions),
                "total_kpi_subscriptions": sum(len(subs) for subs in self._kpi_subscriptions.values()),
                "channels": {
                    channel: len(subscribers)
                    for channel, subscribers in self._channel_subscriptions.items()
                },
                "kpis": {
                    kpi_code: len(subscribers)
                    for kpi_code, subscribers in self._kpi_subscriptions.items()
                }
            }
    
    async def _heartbeat_loop(self):
        """Send periodic heartbeat messages to all connections"""
        logger.info("Heartbeat loop started")
        
        try:
            while self._running:
                await asyncio.sleep(self.heartbeat_interval)
                
                async with self._lock:
                    connections = list(self._connections.values())
                
                heartbeat_message = {
                    "type": "heartbeat",
                    "timestamp": datetime.utcnow().isoformat()
                }
                
                for connection in connections:
                    await connection.send_json(heartbeat_message)
        
        except asyncio.CancelledError:
            logger.info("Heartbeat loop cancelled")
            raise
        
        except Exception as e:
            logger.error(f"Heartbeat loop error: {e}")
    
    async def _cleanup_loop(self):
        """Clean up inactive connections"""
        logger.info("Cleanup loop started")
        
        try:
            while self._running:
                await asyncio.sleep(60)  # Check every minute
                
                now = datetime.utcnow()
                inactive_connections = []
                
                async with self._lock:
                    for connection_id, connection in self._connections.items():
                        inactive_seconds = (now - connection.last_activity).total_seconds()
                        if inactive_seconds > self.connection_timeout:
                            inactive_connections.append(connection_id)
                
                # Disconnect inactive connections
                for connection_id in inactive_connections:
                    logger.warning(f"Closing inactive connection: {connection_id}")
                    await self.disconnect(connection_id)
                
                if inactive_connections:
                    logger.info(f"Cleaned up {len(inactive_connections)} inactive connections")
        
        except asyncio.CancelledError:
            logger.info("Cleanup loop cancelled")
            raise
        
        except Exception as e:
            logger.error(f"Cleanup loop error: {e}")


# Global WebSocket manager instance
websocket_manager = WebSocketManager()
