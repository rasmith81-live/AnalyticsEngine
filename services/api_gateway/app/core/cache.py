"""
Cache service for the API Gateway.
Provides caching functionality using a direct Redis connection.
"""
import json
from typing import Any, Dict, Optional, Union
from pydantic import BaseModel

from app.core.logging import get_logger
from app.core.redis_client import redis_client_context

logger = get_logger(__name__)

class CacheService:
    """
    Service for interacting with the Redis cache directly.
    """

    @staticmethod
    async def get(key: str) -> Optional[Dict[str, Any]]:
        """Get a value from the cache."""
        try:
            async with redis_client_context() as redis:
                value = await redis.get(key)
                if value:
                    return json.loads(value)
            return None
        except Exception as e:
            logger.error(f"Error getting cache for key {key}: {e}")
            return None

    @staticmethod
    async def set(key: str, value: Union[Dict[str, Any], BaseModel], ttl: int = 3600) -> bool:
        """Set a value in the cache."""
        try:
            if isinstance(value, BaseModel):
                value_to_cache = value.model_dump_json()
            else:
                value_to_cache = json.dumps(value)

            async with redis_client_context() as redis:
                await redis.set(key, value_to_cache, ex=ttl)
                return True
        except Exception as e:
            logger.error(f"Error setting cache for key {key}: {e}")
            return False

    @staticmethod
    async def delete(key: str) -> bool:
        """Delete a value from the cache."""
        try:
            async with redis_client_context() as redis:
                await redis.delete(key)
                return True
        except Exception as e:
            logger.error(f"Error deleting cache for key {key}: {e}")
            return False

    @staticmethod
    async def exists(key: str) -> bool:
        """Check if a key exists in the cache."""
        try:
            async with redis_client_context() as redis:
                return await redis.exists(key) > 0
        except Exception as e:
            logger.error(f"Error checking existence for key {key}: {e}")
            return False

