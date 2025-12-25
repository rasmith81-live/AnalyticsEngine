"""
Error handling middleware for the API Gateway service.
Provides consistent error responses and logging.
"""
from typing import Callable, Dict, Any, Optional
import traceback
import uuid

from fastapi import Request, Response, HTTPException, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from pydantic import BaseModel, Field

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

class ErrorResponse(BaseModel):
    """Error response model using Pydantic v2."""
    status: str = Field("error", description="Response status")
    code: int = Field(..., description="HTTP status code")
    message: str = Field(..., description="Error message")
    error_id: str = Field(..., description="Unique error ID for tracking")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")

class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """
    Middleware that handles errors and provides consistent error responses.
    """
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and handle any errors.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream or error response
        """
        # Generate error ID for tracking
        error_id = str(uuid.uuid4())
        
        try:
            # Process the request
            response = await call_next(request)
            return response
            
        except HTTPException as e:
            # Handle FastAPI HTTP exceptions
            return await self._handle_http_exception(request, e, error_id)
            
        except Exception as e:
            # Handle unexpected exceptions
            return await self._handle_unexpected_exception(request, e, error_id)
    
    async def _handle_http_exception(self, request: Request, exc: HTTPException, error_id: str) -> Response:
        """
        Handle FastAPI HTTP exceptions.
        
        Args:
            request: FastAPI request
            exc: HTTP exception
            error_id: Unique error ID
            
        Returns:
            JSON response with error details
        """
        # Log the exception
        logger.warning(
            f"HTTP error {exc.status_code}: {exc.detail}",
            extra={
                "data": {
                    "error_id": error_id,
                    "status_code": exc.status_code,
                    "path": request.url.path,
                    "method": request.method
                }
            }
        )
        
        # Create error response
        error_response = ErrorResponse(
            code=exc.status_code,
            message=str(exc.detail),
            error_id=error_id
        )
        
        # Add CORS headers to error response
        headers = dict(exc.headers) if exc.headers else {}
        headers.update({
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": "true",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*"
        })
        
        # Return JSON response
        return JSONResponse(
            status_code=exc.status_code,
            content=error_response.model_dump(),
            headers=headers
        )
    
    async def _handle_unexpected_exception(self, request: Request, exc: Exception, error_id: str) -> Response:
        """
        Handle unexpected exceptions.
        
        Args:
            request: FastAPI request
            exc: Exception
            error_id: Unique error ID
            
        Returns:
            JSON response with error details
        """
        # Get exception traceback
        tb = traceback.format_exc()
        
        # Log the exception
        logger.error(
            f"Unexpected error: {str(exc)}",
            extra={
                "data": {
                    "error_id": error_id,
                    "path": request.url.path,
                    "method": request.method,
                    "traceback": tb
                }
            }
        )
        
        # Create error response
        error_response = ErrorResponse(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            message="An unexpected error occurred",
            error_id=error_id,
            details={
                "type": exc.__class__.__name__
            } if settings.DEBUG else None
        )
        
        # Return JSON response
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=error_response.model_dump()
        )
