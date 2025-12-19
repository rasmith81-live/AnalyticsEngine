"""
Service Dependencies - Manages global service instances and dependency injection.
"""
from typing import Optional
from fastapi import HTTPException, status

from .messaging_client import MessagingClient
from .database_client import DatabaseClient

import time

# Global instances
_messaging_client: Optional[MessagingClient] = None
_database_client: Optional[DatabaseClient] = None
_service_start_time: float = 0.0

def set_messaging_client(client: MessagingClient):
    """Set the global messaging client instance."""
    global _messaging_client
    _messaging_client = client

def set_database_client(client: DatabaseClient):
    """Set the global database client instance."""
    global _database_client
    _database_client = client

def set_service_start_time(start_time: float):
    """Set the service start time."""
    global _service_start_time
    _service_start_time = start_time

def get_messaging_client() -> MessagingClient:
    """Dependency to get messaging client instance."""
    if _messaging_client is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Messaging client not initialized"
        )
    return _messaging_client

def get_database_client() -> DatabaseClient:
    """Dependency to get database client instance."""
    if _database_client is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="Database client not initialized"
        )
    return _database_client

def get_service_uptime() -> float:
    """Get the service uptime in seconds."""
    if _service_start_time == 0.0:
        return 0.0
    return time.time() - _service_start_time
