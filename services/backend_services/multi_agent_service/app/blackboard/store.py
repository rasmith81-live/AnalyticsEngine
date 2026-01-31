# =============================================================================
# Redis Blackboard Store
# Based on: Tangi Vass - "Adversarial Vibe Coding" / LIZA System
# Reference: https://github.com/liza-mas/liza
# =============================================================================
"""Redis-backed persistence for the blackboard."""

from typing import Optional
import json
import logging
import redis.asyncio as redis

from .models import AgentBlackboard

logger = logging.getLogger(__name__)


class RedisBlackboardStore:
    """
    Redis-backed persistence for the blackboard.
    
    Provides atomic state operations and replaces pub/sub
    with centralized state management.
    """
    
    def __init__(self, redis_client: redis.Redis, key_prefix: str = "blackboard"):
        self.redis = redis_client
        self.key_prefix = key_prefix
    
    @classmethod
    async def create(
        cls,
        host: str = "localhost",
        port: int = 6379,
        db: int = 1,
        password: Optional[str] = None
    ) -> "RedisBlackboardStore":
        """Create a new RedisBlackboardStore with a connection."""
        redis_client = redis.Redis(
            host=host,
            port=port,
            db=db,
            password=password,
            decode_responses=True
        )
        # Test connection
        try:
            await redis_client.ping()
            logger.info(f"Connected to Redis at {host}:{port}")
        except Exception as e:
            logger.warning(f"Could not connect to Redis: {e}. Using in-memory fallback.")
            return InMemoryBlackboardStore()
        
        return cls(redis_client)
    
    def _get_key(self, session_id: str) -> str:
        """Get the Redis key for a session's blackboard."""
        return f"{self.key_prefix}:{session_id}:state"
    
    def _get_audit_key(self, session_id: str) -> str:
        """Get the Redis key for a session's audit log."""
        return f"{self.key_prefix}:{session_id}:audit"
    
    async def save_blackboard(self, blackboard: AgentBlackboard) -> None:
        """Atomically save the entire blackboard state."""
        key = self._get_key(blackboard.session_id)
        await self.redis.set(key, blackboard.model_dump_json())
        logger.debug(f"Saved blackboard for session {blackboard.session_id}")
    
    async def load_blackboard(self, session_id: str) -> Optional[AgentBlackboard]:
        """Load a blackboard for a session."""
        key = self._get_key(session_id)
        data = await self.redis.get(key)
        
        if data:
            return AgentBlackboard.model_validate_json(data)
        return None
    
    async def create_blackboard(self, session_id: str) -> AgentBlackboard:
        """Create a new blackboard for a session."""
        blackboard = AgentBlackboard(session_id=session_id)
        await self.save_blackboard(blackboard)
        return blackboard
    
    async def get_or_create_blackboard(self, session_id: str) -> AgentBlackboard:
        """Get existing or create new blackboard for a session."""
        blackboard = await self.load_blackboard(session_id)
        if not blackboard:
            blackboard = await self.create_blackboard(session_id)
        return blackboard
    
    async def delete_blackboard(self, session_id: str) -> bool:
        """Delete a blackboard for a session."""
        key = self._get_key(session_id)
        result = await self.redis.delete(key)
        return result > 0
    
    async def append_audit_entry(self, session_id: str, entry: dict) -> None:
        """Append an audit log entry."""
        key = self._get_audit_key(session_id)
        await self.redis.rpush(key, json.dumps(entry))
    
    async def get_audit_log(self, session_id: str, limit: int = 100) -> list:
        """Get audit log entries for a session."""
        key = self._get_audit_key(session_id)
        entries = await self.redis.lrange(key, -limit, -1)
        return [json.loads(e) for e in entries]
    
    async def list_sessions(self) -> list:
        """List all session IDs with blackboards."""
        pattern = f"{self.key_prefix}:*:state"
        keys = []
        async for key in self.redis.scan_iter(match=pattern):
            # Extract session_id from key
            parts = key.split(":")
            if len(parts) >= 2:
                keys.append(parts[1])
        return keys
    
    async def close(self) -> None:
        """Close the Redis connection."""
        await self.redis.close()


class InMemoryBlackboardStore:
    """
    In-memory fallback store when Redis is not available.
    
    Useful for development and testing.
    """
    
    def __init__(self):
        self._blackboards: dict[str, AgentBlackboard] = {}
        self._audit_logs: dict[str, list] = {}
    
    async def save_blackboard(self, blackboard: AgentBlackboard) -> None:
        """Save the blackboard to memory."""
        self._blackboards[blackboard.session_id] = blackboard
    
    async def load_blackboard(self, session_id: str) -> Optional[AgentBlackboard]:
        """Load a blackboard from memory."""
        return self._blackboards.get(session_id)
    
    async def create_blackboard(self, session_id: str) -> AgentBlackboard:
        """Create a new blackboard."""
        blackboard = AgentBlackboard(session_id=session_id)
        self._blackboards[session_id] = blackboard
        return blackboard
    
    async def get_or_create_blackboard(self, session_id: str) -> AgentBlackboard:
        """Get existing or create new blackboard."""
        if session_id not in self._blackboards:
            return await self.create_blackboard(session_id)
        return self._blackboards[session_id]
    
    async def delete_blackboard(self, session_id: str) -> bool:
        """Delete a blackboard."""
        if session_id in self._blackboards:
            del self._blackboards[session_id]
            return True
        return False
    
    async def append_audit_entry(self, session_id: str, entry: dict) -> None:
        """Append an audit log entry."""
        if session_id not in self._audit_logs:
            self._audit_logs[session_id] = []
        self._audit_logs[session_id].append(entry)
    
    async def get_audit_log(self, session_id: str, limit: int = 100) -> list:
        """Get audit log entries."""
        entries = self._audit_logs.get(session_id, [])
        return entries[-limit:]
    
    async def list_sessions(self) -> list:
        """List all session IDs."""
        return list(self._blackboards.keys())
    
    async def close(self) -> None:
        """No-op for in-memory store."""
        pass
