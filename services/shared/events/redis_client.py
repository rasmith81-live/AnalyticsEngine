# =============================================================================
# Base Event Client for Redis Streams Communication
# Reusable client for sending commands to services
# =============================================================================
"""
Base Redis event client for service-to-service communication.

Provides:
- Command sending via Redis Streams
- Response receiving via Pub/Sub
- Timeout handling and fallback support
"""

import asyncio
import json
import logging
import os
import uuid
from typing import Any, Callable, Dict, List, Optional, TypeVar

import redis.asyncio as redis

from .schemas import (
    ServiceCommand,
    ServiceResponse,
    CommandType,
    ResponseType,
    get_stream_name,
    get_response_channel,
)

logger = logging.getLogger(__name__)

T = TypeVar('T')


class BaseEventClient:
    """
    Base client for sending commands to services via Redis Streams.
    
    Usage:
        client = BaseEventClient(
            service_name="multi_agent_service",
            target_service="business_metadata"
        )
        await client.connect()
        
        result = await client.send_command(
            CommandType.CREATE_ENTITY,
            {"name": "Customer", "description": "..."}
        )
    """
    
    DEFAULT_TIMEOUT = 30.0
    
    def __init__(
        self,
        service_name: str,
        target_service: str,
        redis_url: Optional[str] = None,
        timeout: float = DEFAULT_TIMEOUT
    ):
        """
        Initialize event client.
        
        Args:
            service_name: Name of this service (source)
            target_service: Name of target service
            redis_url: Redis connection URL
            timeout: Default timeout for commands
        """
        self.service_name = service_name
        self.target_service = target_service
        self.redis_url = redis_url or os.getenv("REDIS_URL", "redis://redis:6379/0")
        self.timeout = timeout
        self._redis: Optional[redis.Redis] = None
        self._stream_name = get_stream_name(target_service)
    
    async def connect(self) -> None:
        """Connect to Redis."""
        if self._redis is not None:
            return
        
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        await self._redis.ping()
        logger.info(f"{self.service_name} connected to Redis for {self.target_service}")
    
    async def disconnect(self) -> None:
        """Disconnect from Redis."""
        if self._redis:
            await self._redis.close()
            self._redis = None
    
    async def _ensure_connected(self) -> None:
        """Ensure Redis connection is established."""
        if self._redis is None:
            await self.connect()
    
    async def send_command(
        self,
        command_type: CommandType,
        payload: Dict[str, Any],
        session_id: Optional[str] = None,
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Send a command and wait for response.
        
        Args:
            command_type: Type of command
            payload: Command payload
            session_id: Optional session ID for tracing
            timeout: Override default timeout
            
        Returns:
            Response payload
            
        Raises:
            TimeoutError: If response not received in time
            Exception: If command fails
        """
        await self._ensure_connected()
        
        command = ServiceCommand.create(
            command_type=command_type,
            source_service=self.service_name,
            target_service=self.target_service,
            payload=payload,
            session_id=session_id,
            ttl_seconds=int(timeout or self.timeout)
        )
        
        # Subscribe to response channel before sending
        pubsub = self._redis.pubsub()
        await pubsub.subscribe(command.reply_channel)
        
        try:
            # Add command to stream
            await self._redis.xadd(
                self._stream_name,
                command.to_stream_dict(),
                maxlen=10000
            )
            
            logger.debug(f"Sent {command_type.value} to {self.target_service}")
            
            # Wait for response
            effective_timeout = timeout or self.timeout
            start_time = asyncio.get_event_loop().time()
            
            while True:
                remaining = effective_timeout - (asyncio.get_event_loop().time() - start_time)
                if remaining <= 0:
                    raise asyncio.TimeoutError(
                        f"Command {command_type.value} to {self.target_service} timed out"
                    )
                
                message = await pubsub.get_message(
                    ignore_subscribe_messages=True,
                    timeout=min(remaining, 1.0)
                )
                
                if message and message["type"] == "message":
                    response = ServiceResponse.from_json(message["data"])
                    
                    if not response.success:
                        raise Exception(response.error or f"{self.target_service} error")
                    
                    return response.payload
                
                await asyncio.sleep(0.01)
        
        finally:
            await pubsub.unsubscribe(command.reply_channel)
            await pubsub.close()
    
    async def send_command_with_fallback(
        self,
        command_type: CommandType,
        payload: Dict[str, Any],
        fallback: Dict[str, Any],
        session_id: Optional[str] = None,
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Send command with fallback on failure.
        
        Args:
            command_type: Type of command
            payload: Command payload
            fallback: Fallback response if command fails
            session_id: Optional session ID
            timeout: Override timeout
            
        Returns:
            Response payload or fallback
        """
        try:
            return await self.send_command(command_type, payload, session_id, timeout)
        except Exception as e:
            logger.warning(
                f"Command {command_type.value} to {self.target_service} failed: {e}"
            )
            return {**fallback, "degraded": True, "error": str(e)}
    
    async def send_fire_and_forget(
        self,
        command_type: CommandType,
        payload: Dict[str, Any],
        session_id: Optional[str] = None
    ) -> str:
        """
        Send command without waiting for response.
        
        Args:
            command_type: Type of command
            payload: Command payload
            session_id: Optional session ID
            
        Returns:
            Command ID for tracking
        """
        await self._ensure_connected()
        
        command = ServiceCommand.create(
            command_type=command_type,
            source_service=self.service_name,
            target_service=self.target_service,
            payload=payload,
            session_id=session_id
        )
        
        await self._redis.xadd(
            self._stream_name,
            command.to_stream_dict(),
            maxlen=10000
        )
        
        logger.debug(f"Sent {command_type.value} to {self.target_service} (fire-and-forget)")
        return command.command_id
    
    async def health_check(self) -> bool:
        """Check if Redis connection is healthy."""
        try:
            await self._ensure_connected()
            await self._redis.ping()
            return True
        except Exception:
            return False
    
    def is_available(self) -> bool:
        """Check if client is connected."""
        return self._redis is not None
