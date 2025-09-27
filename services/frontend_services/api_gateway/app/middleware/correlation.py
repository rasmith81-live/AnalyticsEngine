"""
Correlation ID middleware for the API Gateway service.
Adds and propagates correlation IDs for request tracing.
"""
from typing import Callable
import uuid

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import get_logger

logger = get_logger(__name__)

# Header name for correlation ID
CORRELATION_ID_HEADER = "X-Correlation-ID"

class CorrelationMiddleware(BaseHTTPMiddleware):
    """
    Middleware that adds and propagates correlation IDs.
    Ensures consistent tracking of requests across services.
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and add correlation ID.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream
        """
        # Check if correlation ID is already in request headers
        correlation_id = request.headers.get(CORRELATION_ID_HEADER)
        
        # Generate new correlation ID if not present
        if not correlation_id:
            correlation_id = str(uuid.uuid4())
            logger.debug(f"Generated new correlation ID: {correlation_id}")
        else:
            logger.debug(f"Using existing correlation ID: {correlation_id}")
        
        # Add correlation ID to request state
        request.state.correlation_id = correlation_id
        
        # Add correlation ID to logger context
        logger.info(
            f"Processing request {request.method} {request.url.path}",
            extra={"data": {"correlation_id": correlation_id}}
        )
        
        # Process the request
        response = await call_next(request)
        
        # Add correlation ID to response headers
        response.headers[CORRELATION_ID_HEADER] = correlation_id
        
        return response
