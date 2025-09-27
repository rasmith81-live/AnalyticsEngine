"""
Redis client for direct connection to Redis.
"""
from redis import asyncio as aioredis
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

_redis_pool = None

async def get_redis_pool():
    """Get or create a Redis connection pool."""
    global _redis_pool
    if _redis_pool is None:
        try:
            _redis_pool = aioredis.from_url(
                settings.REDIS_URL,
                encoding="utf-8",
                decode_responses=True,
                max_connections=20
            )
            logger.info(f"Redis connection pool created for {settings.REDIS_URL}")
        except Exception as e:
            logger.error(f"Failed to create Redis connection pool: {e}")
            raise
    return _redis_pool

@asynccontextmanager
async def redis_client_context():
    """
    Context manager for acquiring a Redis client from the pool.
    Yields a Redis client instance.
    """
    pool = await get_redis_pool()
    if not pool:
        raise ConnectionError("Redis connection pool is not available.")
    
    client = None
    try:
        # aioredis pool directly acts as a client
        client = pool
        yield client
    except Exception as e:
        logger.error(f"Redis operation error: {e}")
        raise

async def close_redis_connections():
    """Close the Redis connection pool."""
    global _redis_pool
    if _redis_pool:
        await _redis_pool.close()
        await _redis_pool.wait_closed()
        _redis_pool = None
        logger.info("Redis connection pool closed.")
