"""
Authentication middleware for the API Gateway service.
Handles JWT token validation and user authentication.
"""
from typing import Callable, Dict, List, Optional, Union
import time

from fastapi import Request, Response, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.core.logging import get_logger
from app.core.security import decode_token, TokenPayload
from app.core.cache import CacheService

logger = get_logger(__name__)

class AuthenticationMiddleware(BaseHTTPMiddleware):
    """
    Middleware that handles JWT authentication.
    Validates tokens and adds user information to request state.
    """
    
    def __init__(
        self, 
        app,
        exclude_paths: List[str] = None,
        exclude_prefixes: List[str] = None
    ):
        """
        Initialize the authentication middleware.
        
        Args:
            app: FastAPI application
            exclude_paths: List of paths to exclude from authentication
            exclude_prefixes: List of path prefixes to exclude from authentication
        """
        super().__init__(app)
        self.exclude_paths = exclude_paths or []
        self.exclude_prefixes = exclude_prefixes or []
        
        # Add default excluded paths
        self.exclude_paths.extend([
            "/health",
            "/metrics",
            "/docs",
            "/redoc",
            "/openapi.json"
        ])
        
        logger.info(f"Authentication middleware initialized with {len(self.exclude_paths)} excluded paths")
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and validate authentication.
        
        Args:
            request: FastAPI request
            call_next: Next middleware or endpoint handler
            
        Returns:
            Response from downstream
        """
        # Check if path is excluded
        path = request.url.path
        if path in self.exclude_paths or any(path.startswith(prefix) for prefix in self.exclude_prefixes):
            return await call_next(request)
        
        # Get token from header
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            logger.warning(f"Missing or invalid Authorization header for {path}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing or invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        # Extract token
        token = auth_header.replace("Bearer ", "")
        
        try:
            # Validate token
            payload = await self._validate_token(token)
            
            # Add user info to request state
            request.state.user = payload
            request.state.token = token
            
            # Add user ID to logger context
            logger.info(
                f"Authenticated user {payload.sub} for {path}",
                extra={"data": {"user_id": payload.sub}}
            )
            
            # Process request
            return await call_next(request)
            
        except HTTPException as e:
            # Re-raise HTTP exceptions
            raise
            
        except Exception as e:
            # Log and return 401 for other errors
            logger.error(f"Authentication error for {path}: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"}
            )
    
    async def _validate_token(self, token: str) -> TokenPayload:
        """
        Validate a JWT token.
        
        Args:
            token: JWT token
            
        Returns:
            Token payload
            
        Raises:
            HTTPException: If token is invalid
        """
        # Check token cache first
        cache_key = f"token:{token}"
        cached_payload = await CacheService.get(cache_key)
        
        if cached_payload:
            # Check if token is blacklisted
            if cached_payload.get("blacklisted", False):
                logger.warning(f"Blacklisted token used: {token[:10]}...")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has been revoked",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            # Return cached payload
            return TokenPayload(**cached_payload)
        
        # Decode and validate token
        try:
            payload = decode_token(token)
            
            # Cache valid token payload
            ttl = payload.exp - int(time.time())
            if ttl > 0:
                await CacheService.set(cache_key, payload.model_dump(), ttl)
            
            return payload
            
        except Exception as e:
            logger.warning(f"Token validation failed: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"}
            )
