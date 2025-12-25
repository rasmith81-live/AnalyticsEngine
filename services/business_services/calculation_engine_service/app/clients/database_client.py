"""
Database Client for Calculation Engine Service.

Provides standardized interface to Database Service.
"""

import httpx
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


class DatabaseClient:
    """Client for interacting with Database Service."""
    
    def __init__(self, base_url: str, service_name: str = "calculation_engine"):
        """
        Initialize Database Client.
        
        Args:
            base_url: Base URL of Database Service
            service_name: Name of this service
        """
        self.base_url = base_url.rstrip('/')
        self.service_name = service_name
        self.client: Optional[httpx.AsyncClient] = None
    
    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create HTTP client."""
        if self.client is None or self.client.is_closed:
            self.client = httpx.AsyncClient(timeout=30.0)
        return self.client
    
    async def execute_query(
        self,
        query: str,
        parameters: Optional[Dict[str, Any]] = None,
        use_cache: bool = True
    ) -> Dict[str, Any]:
        """
        Execute a read query against the database.
        
        Args:
            query: SQL query to execute
            parameters: Query parameters
            use_cache: Use query result caching
            
        Returns:
            Query result
        """
        client = await self._get_client()
        
        try:
            response = await client.post(
                f"{self.base_url}/database/query",
                json={
                    "query": query,
                    "parameters": parameters or {},
                    "service_name": self.service_name,
                    "timeout": 30,
                    "use_cache": use_cache
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Database query failed: {e}")
            raise
    
    async def execute_command(
        self,
        command: str,
        parameters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a write command against the database.
        
        Args:
            command: SQL command to execute
            parameters: Command parameters
            
        Returns:
            Command execution result
        """
        client = await self._get_client()
        
        try:
            response = await client.post(
                f"{self.base_url}/database/command",
                json={
                    "command": command,
                    "parameters": parameters or {},
                    "service_name": self.service_name,
                    "timeout": 30
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Database command failed: {e}")
            raise
    
    async def close(self):
        """Close the HTTP client."""
        if self.client and not self.client.is_closed:
            await self.client.aclose()
