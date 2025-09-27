"""
Authorization middleware for the API Gateway service.
Handles role-based access control and permission checking.
"""
from typing import Callable, Dict, List, Optional, Set, Union
import json

from fastapi import Request, Response, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.core.logging import get_logger
from app.core.cache import CacheService

logger = get_logger(__name__)

class AuthorizationMiddleware(BaseHTTPMiddleware):
    """
    Middleware that handles role-based authorization.
    Checks if authenticated users have the required permissions.
    """
    
    def __init__(
        self, 
        app,
        exclude_paths: List[str] = None,
        exclude_prefixes: List[str] = None
    ):
        """
        Initialize the authorization middleware.
        
        Args:
            app: FastAPI application
            exclude_paths: List of paths to exclude from authorization
            exclude_prefixes: List of path prefixes to exclude from authorization
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
        
        logger.info(f"Authorization middleware initialized with {len(self.exclude_paths)} excluded paths")
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """
        Process the request and validate authorization.
        
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
        
        # Check if user is authenticated
        if not hasattr(request.state, "user"):
            # This should not happen if the authentication middleware is properly configured
            logger.error(f"Authorization middleware called without user in request state for {path}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        try:
            # Get user from request state
            user = request.state.user
            
            # Extract service and path for permission checking
            service_path = self._extract_service_path(path)
            method = request.method
            
            # Check if user has permission
            has_permission = await self._check_permission(user, service_path, method)
            
            if not has_permission:
                logger.warning(
                    f"User {user.sub} denied access to {method} {path}",
                    extra={"data": {"user_id": user.sub}}
                )
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="You don't have permission to access this resource"
                )
            
            # Log successful authorization
            logger.info(
                f"User {user.sub} authorized for {method} {path}",
                extra={"data": {"user_id": user.sub}}
            )
            
            # Process request
            return await call_next(request)
            
        except HTTPException as e:
            # Re-raise HTTP exceptions
            raise
            
        except Exception as e:
            # Log and return 403 for other errors
            logger.error(f"Authorization error for {path}: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Authorization error"
            )
    
    def _extract_service_path(self, path: str) -> str:
        """
        Extract service path from request path.
        
        Args:
            path: Request path
            
        Returns:
            Service path for permission checking
        """
        # Remove leading slash and split by slashes
        parts = path.lstrip("/").split("/")
        
        if len(parts) >= 2:
            # Return service/resource format
            return f"{parts[0]}/{parts[1]}"
        elif len(parts) == 1:
            # Return just the service
            return parts[0]
        else:
            # Empty path
            return ""
    
    async def _check_permission(self, user, service_path: str, method: str) -> bool:
        """
        Check if user has permission to access the resource.
        
        Args:
            user: User information from token
            service_path: Service path for permission checking
            method: HTTP method
            
        Returns:
            True if user has permission, False otherwise
        """
        # Check cache first
        cache_key = f"permissions:{user.sub}:{service_path}:{method}"
        cached_result = await CacheService.get(cache_key)
        
        if cached_result is not None:
            return cached_result
        
        # Get user roles from token
        roles = getattr(user, "roles", [])
        
        # If user has admin role, allow all access
        if "admin" in roles:
            await CacheService.set(cache_key, True, 300)  # Cache for 5 minutes
            return True
        
        # Check role-based permissions
        has_permission = False
        
        # Get permissions for this service path and method
        permissions = await self._get_permissions_for_path(service_path, method)
        
        # Check if any of the user's roles have the required permission
        for role in roles:
            if role in permissions:
                has_permission = True
                break
        
        # Cache result
        await CacheService.set(cache_key, has_permission, 300)  # Cache for 5 minutes
        
        return has_permission
    
    async def _get_permissions_for_path(self, service_path: str, method: str) -> Set[str]:
        """
        Get roles that have permission to access the path with the given method.
        
        Args:
            service_path: Service path for permission checking
            method: HTTP method
            
        Returns:
            Set of role names that have permission
        """
        # Check cache first
        cache_key = f"path_permissions:{service_path}:{method}"
        cached_permissions = await CacheService.get(cache_key)
        
        if cached_permissions is not None:
            return set(cached_permissions)
        
        # Get permissions from configuration or database
        # For now, we'll use a simple permission model based on the service
        permissions: Set[str] = set()
        
        # Extract service name from service path
        service = service_path.split("/")[0] if "/" in service_path else service_path
        
        # Define default permissions based on service
        if service == "operations":
            permissions = {"operations_user", "operations_admin"}
        elif service == "analytics":
            permissions = {"analytics_user", "analytics_admin"}
        elif service == "governance":
            permissions = {"governance_user", "governance_admin"}
        else:
            # Default to allowing authenticated users for unknown services
            permissions = {"user"}
        
        # Add read-only permissions for GET requests
        if method == "GET":
            permissions.add("readonly_user")
        
        # Cache permissions
        await CacheService.set(cache_key, list(permissions), 3600)  # Cache for 1 hour
        
        return permissions
