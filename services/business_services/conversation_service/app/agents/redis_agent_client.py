# =============================================================================
# Redis-Based Multi-Agent Service Client
# Event-Driven Communication between L2 Conversation and L1 Multi-Agent
# =============================================================================
"""
Redis Streams and Pub/Sub client for multi-agent service communication.

Architecture:
- Commands (create, message, analyze, finalize) → Redis Streams (reliable, persistent)
- Responses → Redis Pub/Sub (real-time, low latency)
- State → Redis Hash (session state caching)

Stream Keys:
- agent:commands:{service} - Command stream (consumer group processing)
- agent:responses:{session_id} - Response channel (pub/sub)

This replaces HTTP-based communication for internal service-to-service calls.
"""

import asyncio
import json
import logging
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, List, Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)


class CommandType(Enum):
    """Types of commands sent to multi_agent_service."""
    CREATE_SESSION = "create_session"
    GET_SESSION = "get_session"
    SEND_MESSAGE = "send_message"
    RUN_ANALYSIS = "run_analysis"
    FINALIZE_SESSION = "finalize_session"
    CANCEL_SESSION = "cancel_session"
    LIST_SESSIONS = "list_sessions"
    GET_ARTIFACTS = "get_artifacts"
    GET_TASKS = "get_tasks"
    GET_CONTRACT_STATUS = "get_contract_status"
    GET_AGENT_STATE = "get_agent_state"


class ResponseType(Enum):
    """Types of responses from multi_agent_service."""
    SESSION_CREATED = "session_created"
    SESSION_DATA = "session_data"
    MESSAGE_RESPONSE = "message_response"
    ANALYSIS_RESULT = "analysis_result"
    SESSION_FINALIZED = "session_finalized"
    SESSION_CANCELLED = "session_cancelled"
    SESSION_LIST = "session_list"
    ARTIFACTS = "artifacts"
    TASKS = "tasks"
    CONTRACT_STATUS = "contract_status"
    AGENT_STATE = "agent_state"
    ERROR = "error"
    STREAM_CHUNK = "stream_chunk"
    STREAM_COMPLETE = "stream_complete"


@dataclass
class AgentCommand:
    """Command message sent to multi_agent_service."""
    command_id: str
    command_type: CommandType
    session_id: Optional[str]
    payload: Dict[str, Any]
    reply_channel: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    source_service: str = "conversation_service"
    
    def to_dict(self) -> Dict[str, str]:
        """Convert to Redis stream entry (all values must be strings)."""
        return {
            "command_id": self.command_id,
            "command_type": self.command_type.value,
            "session_id": self.session_id or "",
            "payload": json.dumps(self.payload),
            "reply_channel": self.reply_channel,
            "timestamp": self.timestamp,
            "source_service": self.source_service
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "AgentCommand":
        """Create from Redis stream entry."""
        return cls(
            command_id=data["command_id"],
            command_type=CommandType(data["command_type"]),
            session_id=data.get("session_id") or None,
            payload=json.loads(data.get("payload", "{}")),
            reply_channel=data["reply_channel"],
            timestamp=data.get("timestamp", ""),
            source_service=data.get("source_service", "unknown")
        )


@dataclass
class AgentResponse:
    """Response message from multi_agent_service."""
    command_id: str
    response_type: ResponseType
    session_id: Optional[str]
    payload: Dict[str, Any]
    success: bool
    error: Optional[str] = None
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    
    def to_json(self) -> str:
        """Serialize for pub/sub."""
        return json.dumps({
            "command_id": self.command_id,
            "response_type": self.response_type.value,
            "session_id": self.session_id,
            "payload": self.payload,
            "success": self.success,
            "error": self.error,
            "timestamp": self.timestamp
        })
    
    @classmethod
    def from_json(cls, data: str) -> "AgentResponse":
        """Deserialize from pub/sub."""
        d = json.loads(data)
        return cls(
            command_id=d["command_id"],
            response_type=ResponseType(d["response_type"]),
            session_id=d.get("session_id"),
            payload=d.get("payload", {}),
            success=d.get("success", True),
            error=d.get("error"),
            timestamp=d.get("timestamp", "")
        )


class RedisAgentClient:
    """
    Redis-based client for multi-agent service communication.
    
    Uses:
    - Redis Streams for reliable command delivery (with consumer groups)
    - Redis Pub/Sub for real-time response streaming
    - Redis Hash for session state caching
    
    Flow:
    1. Client sends command to stream: agent:commands:multi_agent
    2. multi_agent_service consumes from stream (consumer group)
    3. multi_agent_service publishes response to: agent:responses:{command_id}
    4. Client receives response via pub/sub subscription
    """
    
    # Stream and channel naming
    COMMAND_STREAM = "agent:commands:multi_agent"
    RESPONSE_CHANNEL_PREFIX = "agent:responses:"
    SESSION_CACHE_PREFIX = "agent:session:"
    STREAM_CHANNEL_PREFIX = "agent:stream:"
    
    # Consumer group configuration
    CONSUMER_GROUP = "conversation_service"
    
    # Timeouts
    DEFAULT_TIMEOUT = 30.0  # seconds
    STREAM_TIMEOUT = 120.0  # longer for streaming responses
    
    def __init__(
        self,
        redis_url: Optional[str] = None,
        timeout: float = DEFAULT_TIMEOUT
    ):
        self.redis_url = redis_url or os.getenv(
            "REDIS_URL",
            "redis://redis:6379/0"
        )
        self.timeout = timeout
        self._redis: Optional[redis.Redis] = None
        self._pubsub: Optional[redis.client.PubSub] = None
        self._pending_responses: Dict[str, asyncio.Future] = {}
        self._stream_callbacks: Dict[str, Callable] = {}
        self._listener_task: Optional[asyncio.Task] = None
        self._running = False
    
    async def connect(self) -> None:
        """Connect to Redis and start response listener."""
        if self._redis is not None:
            return
        
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        
        await self._redis.ping()
        self._running = True
        logger.info(f"Connected to Redis at {self.redis_url}")
    
    async def disconnect(self) -> None:
        """Disconnect from Redis."""
        self._running = False
        
        if self._listener_task:
            self._listener_task.cancel()
            try:
                await self._listener_task
            except asyncio.CancelledError:
                pass
        
        if self._pubsub:
            await self._pubsub.close()
        
        if self._redis:
            await self._redis.close()
            self._redis = None
        
        logger.info("Disconnected from Redis")
    
    async def _ensure_connected(self) -> None:
        """Ensure Redis connection is established."""
        if self._redis is None:
            await self.connect()
    
    async def _send_command(
        self,
        command_type: CommandType,
        session_id: Optional[str],
        payload: Dict[str, Any],
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Send a command and wait for response.
        
        Uses Redis Streams for command delivery and Pub/Sub for response.
        """
        await self._ensure_connected()
        
        command_id = str(uuid.uuid4())
        reply_channel = f"{self.RESPONSE_CHANNEL_PREFIX}{command_id}"
        
        command = AgentCommand(
            command_id=command_id,
            command_type=command_type,
            session_id=session_id,
            payload=payload,
            reply_channel=reply_channel
        )
        
        # Create future for response
        response_future: asyncio.Future = asyncio.Future()
        self._pending_responses[command_id] = response_future
        
        # Subscribe to response channel BEFORE sending command
        pubsub = self._redis.pubsub()
        await pubsub.subscribe(reply_channel)
        
        try:
            # Add command to stream
            await self._redis.xadd(
                self.COMMAND_STREAM,
                command.to_dict(),
                maxlen=10000  # Keep last 10k commands
            )
            
            logger.debug(f"Sent command {command_id}: {command_type.value}")
            
            # Wait for response with timeout
            effective_timeout = timeout or self.timeout
            start_time = asyncio.get_event_loop().time()
            
            while True:
                remaining = effective_timeout - (asyncio.get_event_loop().time() - start_time)
                if remaining <= 0:
                    raise asyncio.TimeoutError(f"Command {command_type.value} timed out")
                
                message = await pubsub.get_message(
                    ignore_subscribe_messages=True,
                    timeout=min(remaining, 1.0)
                )
                
                if message and message["type"] == "message":
                    response = AgentResponse.from_json(message["data"])
                    
                    if not response.success:
                        raise Exception(response.error or "Unknown error")
                    
                    return response.payload
                
                await asyncio.sleep(0.01)
        
        finally:
            # Cleanup
            await pubsub.unsubscribe(reply_channel)
            await pubsub.close()
            self._pending_responses.pop(command_id, None)
    
    async def _send_command_with_fallback(
        self,
        command_type: CommandType,
        session_id: Optional[str],
        payload: Dict[str, Any],
        fallback: Dict[str, Any],
        timeout: Optional[float] = None
    ) -> Dict[str, Any]:
        """Send command with fallback on failure."""
        try:
            return await self._send_command(command_type, session_id, payload, timeout)
        except Exception as e:
            logger.warning(f"Command {command_type.value} failed: {e}, using fallback")
            return {**fallback, "degraded": True, "error": str(e)}
    
    # =========================================================================
    # Session Management API
    # =========================================================================
    
    async def create_session(
        self,
        user_id: str,
        context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Create a new design session."""
        return await self._send_command_with_fallback(
            CommandType.CREATE_SESSION,
            session_id=None,
            payload={"user_id": user_id, "context": context or {}},
            fallback={
                "id": str(uuid.uuid4()),
                "user_id": user_id,
                "status": "active"
            }
        )
    
    async def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get session details."""
        try:
            return await self._send_command(
                CommandType.GET_SESSION,
                session_id=session_id,
                payload={}
            )
        except Exception as e:
            logger.warning(f"Failed to get session {session_id}: {e}")
            return None
    
    async def send_message(
        self,
        session_id: str,
        message: str
    ) -> Dict[str, Any]:
        """Send a message to a session."""
        return await self._send_command_with_fallback(
            CommandType.SEND_MESSAGE,
            session_id=session_id,
            payload={"message": message},
            fallback={
                "content": "Service temporarily unavailable. Please try again.",
                "agent_role": "system",
                "success": False
            }
        )
    
    async def send_message_streaming(
        self,
        session_id: str,
        message: str,
        on_chunk: Callable[[str], None]
    ) -> Dict[str, Any]:
        """
        Send a message with streaming response.
        
        Subscribes to stream channel for real-time chunks.
        """
        await self._ensure_connected()
        
        command_id = str(uuid.uuid4())
        reply_channel = f"{self.RESPONSE_CHANNEL_PREFIX}{command_id}"
        stream_channel = f"{self.STREAM_CHANNEL_PREFIX}{command_id}"
        
        command = AgentCommand(
            command_id=command_id,
            command_type=CommandType.SEND_MESSAGE,
            session_id=session_id,
            payload={"message": message, "stream": True},
            reply_channel=reply_channel
        )
        
        pubsub = self._redis.pubsub()
        await pubsub.subscribe(reply_channel, stream_channel)
        
        full_content = []
        final_response = None
        
        try:
            # Send command
            await self._redis.xadd(self.COMMAND_STREAM, command.to_dict())
            
            start_time = asyncio.get_event_loop().time()
            
            while True:
                remaining = self.STREAM_TIMEOUT - (asyncio.get_event_loop().time() - start_time)
                if remaining <= 0:
                    raise asyncio.TimeoutError("Streaming response timed out")
                
                message = await pubsub.get_message(
                    ignore_subscribe_messages=True,
                    timeout=min(remaining, 0.1)
                )
                
                if message and message["type"] == "message":
                    data = json.loads(message["data"])
                    response_type = ResponseType(data.get("response_type", "error"))
                    
                    if response_type == ResponseType.STREAM_CHUNK:
                        chunk = data.get("payload", {}).get("chunk", "")
                        full_content.append(chunk)
                        on_chunk(chunk)
                    
                    elif response_type == ResponseType.STREAM_COMPLETE:
                        final_response = data.get("payload", {})
                        break
                    
                    elif response_type == ResponseType.MESSAGE_RESPONSE:
                        final_response = data.get("payload", {})
                        break
                    
                    elif response_type == ResponseType.ERROR:
                        raise Exception(data.get("error", "Unknown error"))
                
                await asyncio.sleep(0.01)
            
            return final_response or {"content": "".join(full_content), "success": True}
        
        finally:
            await pubsub.unsubscribe(reply_channel, stream_channel)
            await pubsub.close()
    
    async def run_parallel_analysis(
        self,
        session_id: str,
        analysis_type: str = "comprehensive"
    ) -> Dict[str, Any]:
        """Run parallel analysis with multiple agents."""
        return await self._send_command_with_fallback(
            CommandType.RUN_ANALYSIS,
            session_id=session_id,
            payload={"analysis_type": analysis_type},
            fallback={"error": "Analysis service unavailable"},
            timeout=60.0  # Longer timeout for analysis
        )
    
    async def finalize_session(self, session_id: str) -> Dict[str, Any]:
        """Finalize a design session."""
        return await self._send_command_with_fallback(
            CommandType.FINALIZE_SESSION,
            session_id=session_id,
            payload={},
            fallback={"success": False, "error": "Finalization service unavailable"}
        )
    
    async def cancel_session(self, session_id: str) -> Dict[str, Any]:
        """Cancel a design session."""
        return await self._send_command_with_fallback(
            CommandType.CANCEL_SESSION,
            session_id=session_id,
            payload={},
            fallback={"success": False, "error": "Cancel service unavailable"}
        )
    
    async def list_sessions(
        self,
        user_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List all sessions, optionally filtered by user."""
        try:
            result = await self._send_command(
                CommandType.LIST_SESSIONS,
                session_id=None,
                payload={"user_id": user_id}
            )
            return result.get("sessions", [])
        except Exception as e:
            logger.warning(f"Failed to list sessions: {e}")
            return []
    
    # =========================================================================
    # Blackboard Operations
    # =========================================================================
    
    async def get_session_artifacts(self, session_id: str) -> List[Dict[str, Any]]:
        """Get all artifacts for a session."""
        try:
            result = await self._send_command(
                CommandType.GET_ARTIFACTS,
                session_id=session_id,
                payload={}
            )
            return result.get("artifacts", [])
        except Exception as e:
            logger.warning(f"Failed to get artifacts: {e}")
            return []
    
    async def get_session_tasks(self, session_id: str) -> List[Dict[str, Any]]:
        """Get all tasks for a session."""
        try:
            result = await self._send_command(
                CommandType.GET_TASKS,
                session_id=session_id,
                payload={}
            )
            return result.get("tasks", [])
        except Exception as e:
            logger.warning(f"Failed to get tasks: {e}")
            return []
    
    async def get_contract_status(self, session_id: str) -> Dict[str, Any]:
        """Get contract compliance status."""
        return await self._send_command_with_fallback(
            CommandType.GET_CONTRACT_STATUS,
            session_id=session_id,
            payload={},
            fallback={
                "agents": [],
                "degraded_mode": True,
                "degraded_reason": "Contract service unavailable"
            }
        )
    
    async def get_agent_state(
        self,
        session_id: str,
        agent_role: str
    ) -> Dict[str, Any]:
        """Get agent state machine status."""
        return await self._send_command_with_fallback(
            CommandType.GET_AGENT_STATE,
            session_id=session_id,
            payload={"agent_role": agent_role},
            fallback={
                "current_state": "unknown",
                "assumption_count": 0,
                "failed_attempts": 0,
                "contract_violations": 0
            }
        )
    
    # =========================================================================
    # Health & Status
    # =========================================================================
    
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
        return self._redis is not None and self._running


# Singleton instance
_redis_client: Optional[RedisAgentClient] = None


def get_redis_agent_client() -> RedisAgentClient:
    """Get singleton Redis agent client."""
    global _redis_client
    if _redis_client is None:
        _redis_client = RedisAgentClient()
    return _redis_client
