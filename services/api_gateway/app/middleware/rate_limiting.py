"""
Rate limiting middleware for the API Gateway service.
Implements distributed rate limiting using Redis as the backend.
"""
import time
from typing import Callable, Dict, Optional, Tuple

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.core.config import settings
from app.core.logging import get_logger
from app.core.redis_client import redis_client_context
from app.core.metrics import record_rate_limit_hit

logger = get_logger(__name__)

class RateLimitingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that implements rate limiting.
    Uses Redis to track request counts across multiple instances.
    """
    
    def __init__(
        self,
        app,
        limit: int = None,
        window: int = None,
        excluded_paths: list = None,
    ):
        """
        Initialize the rate limiting middleware.
        
        Args:
            app: FastAPI application
            limit: Maximum requests per window
            window: Time window in seconds
            excluded_paths: Paths to exclude from rate limiting
        """
        super().__init__(app)
        self.limit = limit or settings.RATE_LIMIT_DEFAULT
        self.window = window or settings.RATE_LIMIT_WINDOW
        self.excluded_paths = excluded_paths or ["/health", "/metrics"]
    
    async def _get_rate_limit_key(self, request: Request) -> str:
        """
        Generate a rate limit key based on client IP and path.
        
        Args:
            request: FastAPI request
            
        Returns:
            Redis key for rate limiting
        """
        # Get client IP, considering forwarded headers
        client_ip = request.client.host
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            client_ip = forwarded.split(",")[0].strip()
        
        # Get service from path
        try:
            _, service, *_ = request.url.path.strip("/").split("/")
        except ValueError:
            service = "root"
        
        # Create a key that includes the client IP and service
        return f"ratelimit:{client_ip}:{service}"
    
    async def _check_rate_limit(self, key: str) -> Tuple[bool, int, int]:
        """
        Check if the request is within rate limits.
        
        Args:
            key: Redis key for rate limiting
            
        Returns:
            Tuple of (is_allowed, current_count, limit)
        """
        async with redis_client_context() as redis:
            # Get current window timestamp
            current_window = int(time.time() / self.window) * self.window
            window_key = f"{key}:{current_window}"
            
            # Increment the counter for this window
            count = await redis.incr(window_key)
            
            # Set expiry for the counter
            if count == 1:
                await redis.expire(window_key, self.window * 2)  # 2x window for overlap
            
            # Check if within limit
            is_allowed = count <= self.limit
            
            return is_allowed, count, self.limit
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request through rate limiting.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream or rate limit exceeded
        """
        # Skip rate limiting for excluded paths
        if any(request.url.path.startswith(path) for path in self.excluded_paths):
            return await call_next(request)
        
        # Get rate limit key
        key = await self._get_rate_limit_key(request)
        
        # Check rate limit
        is_allowed, count, limit = await self._check_rate_limit(key)
        
        # Add rate limit headers to response
        async def add_headers(response: Response) -> Response:
            response.headers["X-RateLimit-Limit"] = str(limit)
            response.headers["X-RateLimit-Remaining"] = str(max(0, limit - count))
            response.headers["X-RateLimit-Reset"] = str(
                int(time.time() / self.window) * self.window + self.window
            )
            return response
        
        # If rate limit exceeded, return 429 Too Many Requests
        if not is_allowed:
            logger.warning(f"Rate limit exceeded for {key}: {count}/{limit}")
            response = JSONResponse(
                status_code=429,
                content={"detail": "Rate limit exceeded. Please try again later."}
            )
            return await add_headers(response)
        
        # Process the request
        response = await call_next(request)
        
        # Add rate limit headers
        return await add_headers(response)
