"""
Circuit breaker middleware for the API Gateway service.
Implements the circuit breaker pattern to prevent cascading failures.
Uses Redis for distributed state management across instances.
"""
import asyncio
import time
from enum import Enum
from typing import Callable, Dict, Optional

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from app.core.config import settings
from app.core.logging import get_logger
from app.core.redis_client import redis_client_context

logger = get_logger(__name__)

class CircuitState(str, Enum):
    """Circuit breaker states."""
    CLOSED = "closed"  # Normal operation, requests flow through
    OPEN = "open"      # Circuit is open, requests are rejected
    HALF_OPEN = "half_open"  # Testing if the service has recovered


class CircuitBreakerMiddleware(BaseHTTPMiddleware):
    """
    Middleware that implements the circuit breaker pattern.
    Uses Redis to track circuit state across multiple instances.
    """
    
    def __init__(
        self,
        app,
        failure_threshold: int = None,
        recovery_timeout: int = None,
        excluded_paths: list = None,
    ):
        """
        Initialize the circuit breaker middleware.
        
        Args:
            app: FastAPI application
            failure_threshold: Number of failures before opening the circuit
            recovery_timeout: Seconds to wait before attempting recovery
            excluded_paths: Paths to exclude from circuit breaking
        """
        super().__init__(app)
        self.failure_threshold = failure_threshold or settings.CIRCUIT_BREAKER_FAILURE_THRESHOLD
        self.recovery_timeout = recovery_timeout or settings.CIRCUIT_BREAKER_RECOVERY_TIMEOUT
        self.excluded_paths = excluded_paths or ["/health", "/metrics"]
        
    async def _get_circuit_state(self, service: str) -> CircuitState:
        """
        Get the current circuit state for a service from Redis.
        
        Args:
            service: Service identifier
            
        Returns:
            Current circuit state
        """
        async with redis_client_context() as redis:
            state = await redis.get(f"circuit:{service}:state")
            return CircuitState(state) if state else CircuitState.CLOSED
    
    async def _set_circuit_state(self, service: str, state: CircuitState) -> None:
        """
        Set the circuit state for a service in Redis.
        
        Args:
            service: Service identifier
            state: New circuit state
        """
        async with redis_client_context() as redis:
            await redis.set(f"circuit:{service}:state", state.value)
            
            # Set expiry for OPEN state to auto-transition to HALF_OPEN
            if state == CircuitState.OPEN:
                await redis.set(
                    f"circuit:{service}:recovery_time",
                    int(time.time()) + self.recovery_timeout
                )
    
    async def _get_failure_count(self, service: str) -> int:
        """
        Get the current failure count for a service from Redis.
        
        Args:
            service: Service identifier
            
        Returns:
            Current failure count
        """
        async with redis_client_context() as redis:
            count = await redis.get(f"circuit:{service}:failures")
            return int(count) if count else 0
    
    async def _increment_failure_count(self, service: str) -> int:
        """
        Increment the failure count for a service in Redis.
        
        Args:
            service: Service identifier
            
        Returns:
            New failure count
        """
        async with redis_client_context() as redis:
            new_count = await redis.incr(f"circuit:{service}:failures")
            
            # Set expiry to reset failure count after a period
            await redis.expire(f"circuit:{service}:failures", 60)
            
            return new_count
    
    async def _reset_failure_count(self, service: str) -> None:
        """
        Reset the failure count for a service in Redis.
        
        Args:
            service: Service identifier
        """
        async with redis_client_context() as redis:
            await redis.delete(f"circuit:{service}:failures")
    
    async def _should_attempt_recovery(self, service: str) -> bool:
        """
        Check if it's time to attempt recovery for a service.
        
        Args:
            service: Service identifier
            
        Returns:
            True if recovery should be attempted, False otherwise
        """
        async with redis_client_context() as redis:
            recovery_time = await redis.get(f"circuit:{service}:recovery_time")
            
            if not recovery_time:
                return True
                
            return int(time.time()) >= int(recovery_time)
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request through the circuit breaker.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream or circuit breaker
        """
        # Skip circuit breaker for excluded paths
        if any(request.url.path.startswith(path) for path in self.excluded_paths):
            return await call_next(request)
        
        # Extract service from path
        try:
            _, service, *_ = request.url.path.strip("/").split("/")
        except ValueError:
            # If path doesn't match expected format, let it through
            return await call_next(request)
        
        # Get current circuit state
        state = await self._get_circuit_state(service)
        
        # Handle based on circuit state
        if state == CircuitState.OPEN:
            # Check if we should attempt recovery
            if await self._should_attempt_recovery(service):
                # Transition to half-open state
                await self._set_circuit_state(service, CircuitState.HALF_OPEN)
                logger.info(f"Circuit for {service} transitioning to half-open state")
            else:
                # Circuit is open, reject the request
                logger.warning(f"Circuit for {service} is open, rejecting request")
                return JSONResponse(
                    status_code=503,
                    content={"detail": f"Service {service} is temporarily unavailable"}
                )
        
        # For CLOSED or HALF_OPEN states, try the request
        try:
            # Process the request
            response = await call_next(request)
            
            # If successful in HALF_OPEN state, close the circuit
            if state == CircuitState.HALF_OPEN and response.status_code < 500:
                await self._set_circuit_state(service, CircuitState.CLOSED)
                await self._reset_failure_count(service)
                logger.info(f"Circuit for {service} closed after successful recovery")
            
            return response
            
        except Exception as e:
            # Handle failure
            logger.error(f"Request to {service} failed: {str(e)}")
            
            if state == CircuitState.HALF_OPEN:
                # If failed in HALF_OPEN, back to OPEN
                await self._set_circuit_state(service, CircuitState.OPEN)
                logger.warning(f"Circuit for {service} reopened after failed recovery attempt")
            else:
                # Increment failure count
                failures = await self._increment_failure_count(service)
                
                # If threshold reached, open the circuit
                if failures >= self.failure_threshold:
                    await self._set_circuit_state(service, CircuitState.OPEN)
                    logger.warning(f"Circuit for {service} opened after {failures} failures")
            
            # Return error response
            return JSONResponse(
                status_code=503,
                content={"detail": f"Service {service} is temporarily unavailable"}
            )
