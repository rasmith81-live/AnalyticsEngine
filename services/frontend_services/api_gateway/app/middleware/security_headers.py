"""
Security Headers Middleware
Implements security best practices including HSTS.
"""
from typing import Callable
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.config import settings

class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Middleware that adds security headers to responses.
    Includes HSTS (HTTP Strict Transport Security) enforcement.
    """
    
    def __init__(self, app):
        super().__init__(app)
        
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and add security headers.
        
        Args:
            request: FastAPI request
            call_next: Next middleware
            
        Returns:
            Response with security headers
        """
        response = await call_next(request)
        
        # Add HSTS header
        # max-age=31536000 (1 year), includeSubDomains
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        
        # Add other security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        
        return response
