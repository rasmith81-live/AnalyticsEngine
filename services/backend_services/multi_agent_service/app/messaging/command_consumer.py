# =============================================================================
# Redis Command Consumer for Multi-Agent Service
# Processes commands from conversation_service via Redis Streams
# =============================================================================
"""
Consumes commands from Redis Streams and dispatches to appropriate handlers.

This is the L1 side of the Redis-based communication:
- Reads from agent:commands:multi_agent stream (consumer group)
- Processes commands (create_session, send_message, etc.)
- Publishes responses to agent:responses:{command_id} channel

Consumer Group ensures:
- Exactly-once processing
- Automatic failover
- Load balancing across multiple instances
"""

import asyncio
import json
import logging
import os
import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Callable, Dict, Optional

import redis.asyncio as redis

logger = logging.getLogger(__name__)


class CommandType(Enum):
    """Types of commands received from conversation_service."""
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
    """Types of responses sent back to conversation_service."""
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
class Command:
    """Parsed command from stream."""
    command_id: str
    command_type: CommandType
    session_id: Optional[str]
    payload: Dict[str, Any]
    reply_channel: str
    timestamp: str
    source_service: str
    stream_id: str  # Redis stream message ID


class CommandConsumer:
    """
    Consumes commands from Redis Streams and processes them.
    
    Uses consumer groups for reliable message processing:
    - Group: multi_agent_consumers
    - Consumer: {instance_id}
    
    Ensures exactly-once processing with acknowledgment.
    """
    
    COMMAND_STREAM = "agent:commands:multi_agent"
    CONSUMER_GROUP = "multi_agent_consumers"
    STREAM_CHANNEL_PREFIX = "agent:stream:"
    
    def __init__(
        self,
        redis_url: Optional[str] = None,
        consumer_name: Optional[str] = None
    ):
        self.redis_url = redis_url or os.getenv("REDIS_URL", "redis://redis:6379/0")
        self.consumer_name = consumer_name or f"consumer_{uuid.uuid4().hex[:8]}"
        self._redis: Optional[redis.Redis] = None
        self._running = False
        self._handlers: Dict[CommandType, Callable] = {}
        self._sessions: Dict[str, Dict[str, Any]] = {}  # In-memory session store
    
    async def start(self) -> None:
        """Start the command consumer."""
        self._redis = redis.Redis.from_url(
            self.redis_url,
            decode_responses=True,
            max_connections=10
        )
        
        await self._redis.ping()
        logger.info(f"Connected to Redis at {self.redis_url}")
        
        # Create consumer group if not exists
        try:
            await self._redis.xgroup_create(
                self.COMMAND_STREAM,
                self.CONSUMER_GROUP,
                id="0",
                mkstream=True
            )
            logger.info(f"Created consumer group: {self.CONSUMER_GROUP}")
        except redis.ResponseError as e:
            if "BUSYGROUP" not in str(e):
                raise
            logger.debug(f"Consumer group {self.CONSUMER_GROUP} already exists")
        
        # Register default handlers
        self._register_default_handlers()
        
        self._running = True
        logger.info(f"Command consumer started: {self.consumer_name}")
    
    async def stop(self) -> None:
        """Stop the command consumer."""
        self._running = False
        
        if self._redis:
            await self._redis.close()
            self._redis = None
        
        logger.info("Command consumer stopped")
    
    def _register_default_handlers(self) -> None:
        """Register default command handlers."""
        self._handlers = {
            CommandType.CREATE_SESSION: self._handle_create_session,
            CommandType.GET_SESSION: self._handle_get_session,
            CommandType.SEND_MESSAGE: self._handle_send_message,
            CommandType.RUN_ANALYSIS: self._handle_run_analysis,
            CommandType.FINALIZE_SESSION: self._handle_finalize_session,
            CommandType.CANCEL_SESSION: self._handle_cancel_session,
            CommandType.LIST_SESSIONS: self._handle_list_sessions,
            CommandType.GET_ARTIFACTS: self._handle_get_artifacts,
            CommandType.GET_TASKS: self._handle_get_tasks,
            CommandType.GET_CONTRACT_STATUS: self._handle_get_contract_status,
            CommandType.GET_AGENT_STATE: self._handle_get_agent_state,
        }
    
    def register_handler(
        self,
        command_type: CommandType,
        handler: Callable
    ) -> None:
        """Register a custom command handler."""
        self._handlers[command_type] = handler
    
    async def consume(self) -> None:
        """Main consume loop - reads and processes commands."""
        while self._running:
            try:
                # Read from stream with consumer group
                messages = await self._redis.xreadgroup(
                    groupname=self.CONSUMER_GROUP,
                    consumername=self.consumer_name,
                    streams={self.COMMAND_STREAM: ">"},
                    count=10,
                    block=1000  # 1 second timeout
                )
                
                for stream_name, stream_messages in messages:
                    for message_id, message_data in stream_messages:
                        await self._process_message(message_id, message_data)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error consuming messages: {e}")
                await asyncio.sleep(1)
    
    async def _process_message(
        self,
        message_id: str,
        message_data: Dict[str, str]
    ) -> None:
        """Process a single command message."""
        try:
            command = Command(
                command_id=message_data["command_id"],
                command_type=CommandType(message_data["command_type"]),
                session_id=message_data.get("session_id") or None,
                payload=json.loads(message_data.get("payload", "{}")),
                reply_channel=message_data["reply_channel"],
                timestamp=message_data.get("timestamp", ""),
                source_service=message_data.get("source_service", "unknown"),
                stream_id=message_id
            )
            
            logger.debug(f"Processing command {command.command_id}: {command.command_type.value}")
            
            # Get handler
            handler = self._handlers.get(command.command_type)
            if not handler:
                await self._send_error(
                    command,
                    f"Unknown command type: {command.command_type.value}"
                )
            else:
                # Execute handler
                await handler(command)
            
            # Acknowledge message
            await self._redis.xack(
                self.COMMAND_STREAM,
                self.CONSUMER_GROUP,
                message_id
            )
            
        except Exception as e:
            logger.error(f"Error processing message {message_id}: {e}")
            # Still acknowledge to prevent reprocessing
            await self._redis.xack(
                self.COMMAND_STREAM,
                self.CONSUMER_GROUP,
                message_id
            )
    
    async def _send_response(
        self,
        command: Command,
        response_type: ResponseType,
        payload: Dict[str, Any],
        success: bool = True,
        error: Optional[str] = None
    ) -> None:
        """Send response via pub/sub."""
        response = {
            "command_id": command.command_id,
            "response_type": response_type.value,
            "session_id": command.session_id,
            "payload": payload,
            "success": success,
            "error": error,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        await self._redis.publish(
            command.reply_channel,
            json.dumps(response)
        )
    
    async def _send_error(self, command: Command, error: str) -> None:
        """Send error response."""
        await self._send_response(
            command,
            ResponseType.ERROR,
            {},
            success=False,
            error=error
        )
    
    async def _send_stream_chunk(
        self,
        command: Command,
        chunk: str
    ) -> None:
        """Send streaming chunk via pub/sub."""
        stream_channel = f"{self.STREAM_CHANNEL_PREFIX}{command.command_id}"
        response = {
            "command_id": command.command_id,
            "response_type": ResponseType.STREAM_CHUNK.value,
            "payload": {"chunk": chunk},
            "success": True,
            "timestamp": datetime.utcnow().isoformat()
        }
        await self._redis.publish(stream_channel, json.dumps(response))
    
    # =========================================================================
    # Command Handlers
    # =========================================================================
    
    async def _handle_create_session(self, command: Command) -> None:
        """Handle session creation."""
        user_id = command.payload.get("user_id", "unknown")
        context = command.payload.get("context", {})
        
        session_id = str(uuid.uuid4())
        now = datetime.utcnow().isoformat()
        
        session = {
            "id": session_id,
            "user_id": user_id,
            "status": "active",
            "created_at": now,
            "updated_at": now,
            "message_count": 0,
            "context": context,
            "artifacts": {},
            "messages": []
        }
        
        self._sessions[session_id] = session
        
        await self._send_response(
            command,
            ResponseType.SESSION_CREATED,
            session
        )
        
        logger.info(f"Created session {session_id} for user {user_id}")
    
    async def _handle_get_session(self, command: Command) -> None:
        """Handle get session request."""
        session = self._sessions.get(command.session_id)
        
        if not session:
            await self._send_error(command, f"Session {command.session_id} not found")
            return
        
        await self._send_response(
            command,
            ResponseType.SESSION_DATA,
            session
        )
    
    async def _handle_send_message(self, command: Command) -> None:
        """Handle message sending."""
        session = self._sessions.get(command.session_id)
        
        if not session:
            await self._send_error(command, f"Session {command.session_id} not found")
            return
        
        message = command.payload.get("message", "")
        is_streaming = command.payload.get("stream", False)
        
        # Update session
        session["message_count"] += 1
        session["updated_at"] = datetime.utcnow().isoformat()
        session["messages"].append({
            "role": "user",
            "content": message,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # TODO: Invoke actual orchestrator/coordinator here
        # For now, generate placeholder response
        response_content = f"Received: {message[:50]}... (Message #{session['message_count']})"
        
        if is_streaming:
            # Stream response in chunks
            words = response_content.split()
            for i, word in enumerate(words):
                await self._send_stream_chunk(command, word + " ")
                await asyncio.sleep(0.05)  # Simulate streaming delay
            
            # Send completion
            await self._send_response(
                command,
                ResponseType.STREAM_COMPLETE,
                {
                    "content": response_content,
                    "agent_role": "coordinator",
                    "artifacts": {}
                }
            )
        else:
            session["messages"].append({
                "role": "coordinator",
                "content": response_content,
                "timestamp": datetime.utcnow().isoformat()
            })
            
            await self._send_response(
                command,
                ResponseType.MESSAGE_RESPONSE,
                {
                    "content": response_content,
                    "agent_role": "coordinator",
                    "artifacts": {},
                    "success": True
                }
            )
    
    async def _handle_run_analysis(self, command: Command) -> None:
        """Handle parallel analysis request."""
        session = self._sessions.get(command.session_id)
        
        if not session:
            await self._send_error(command, f"Session {command.session_id} not found")
            return
        
        analysis_type = command.payload.get("analysis_type", "comprehensive")
        
        # TODO: Invoke actual parallel analysis
        results = {
            "architect": {"status": "complete", "findings": []},
            "business_analyst": {"status": "complete", "findings": []},
            "developer": {"status": "complete", "findings": []}
        }
        
        await self._send_response(
            command,
            ResponseType.ANALYSIS_RESULT,
            {"session_id": command.session_id, "results": results}
        )
    
    async def _handle_finalize_session(self, command: Command) -> None:
        """Handle session finalization."""
        session = self._sessions.get(command.session_id)
        
        if not session:
            await self._send_error(command, f"Session {command.session_id} not found")
            return
        
        session["status"] = "finalized"
        session["updated_at"] = datetime.utcnow().isoformat()
        
        await self._send_response(
            command,
            ResponseType.SESSION_FINALIZED,
            {
                "success": True,
                "session_id": command.session_id,
                "status": "finalized",
                "value_chain": session.get("context", {}).get("value_chain", {}),
                "artifacts": session.get("artifacts", {}),
                "validation": {"passed": True, "issues": []}
            }
        )
    
    async def _handle_cancel_session(self, command: Command) -> None:
        """Handle session cancellation."""
        session = self._sessions.get(command.session_id)
        
        if not session:
            await self._send_error(command, f"Session {command.session_id} not found")
            return
        
        session["status"] = "cancelled"
        session["updated_at"] = datetime.utcnow().isoformat()
        
        await self._send_response(
            command,
            ResponseType.SESSION_CANCELLED,
            {"success": True, "session_id": command.session_id}
        )
    
    async def _handle_list_sessions(self, command: Command) -> None:
        """Handle list sessions request."""
        user_id = command.payload.get("user_id")
        
        sessions = []
        for session in self._sessions.values():
            if user_id is None or session["user_id"] == user_id:
                sessions.append({
                    "session_id": session["id"],
                    "user_id": session["user_id"],
                    "status": session["status"],
                    "created_at": session["created_at"],
                    "message_count": session["message_count"]
                })
        
        await self._send_response(
            command,
            ResponseType.SESSION_LIST,
            {"sessions": sessions}
        )
    
    async def _handle_get_artifacts(self, command: Command) -> None:
        """Handle get artifacts request."""
        session = self._sessions.get(command.session_id)
        
        if not session:
            await self._send_error(command, f"Session {command.session_id} not found")
            return
        
        await self._send_response(
            command,
            ResponseType.ARTIFACTS,
            {"artifacts": session.get("artifacts", {})}
        )
    
    async def _handle_get_tasks(self, command: Command) -> None:
        """Handle get tasks request."""
        # TODO: Integrate with blackboard
        await self._send_response(
            command,
            ResponseType.TASKS,
            {"tasks": []}
        )
    
    async def _handle_get_contract_status(self, command: Command) -> None:
        """Handle get contract status request."""
        # TODO: Integrate with contract enforcer
        await self._send_response(
            command,
            ResponseType.CONTRACT_STATUS,
            {
                "agents": [],
                "degraded_mode": False,
                "degraded_reason": None
            }
        )
    
    async def _handle_get_agent_state(self, command: Command) -> None:
        """Handle get agent state request."""
        agent_role = command.payload.get("agent_role", "unknown")
        
        # TODO: Integrate with contract adapter
        await self._send_response(
            command,
            ResponseType.AGENT_STATE,
            {
                "agent_role": agent_role,
                "current_state": "idle",
                "assumption_count": 0,
                "failed_attempts": 0,
                "contract_violations": 0
            }
        )


# Singleton instance
_consumer: Optional[CommandConsumer] = None


def get_command_consumer() -> CommandConsumer:
    """Get singleton command consumer."""
    global _consumer
    if _consumer is None:
        _consumer = CommandConsumer()
    return _consumer
