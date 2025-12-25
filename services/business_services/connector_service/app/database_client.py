"""
Database Client for Connector Service.

Provides interface to Database Service for storing connection profiles securely.
"""

import httpx
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime

logger = logging.getLogger(__name__)


class DatabaseClient:
    """Client for interacting with Database Service."""
    
    def __init__(self, base_url: str, service_name: str = "connector_service"):
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
    
    async def execute_query(
        self,
        query: str,
        parameters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Execute a read query against the database.
        
        Args:
            query: SQL query to execute
            parameters: Query parameters
            
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
                    "use_cache": True
                }
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(f"Database query failed: {e}")
            raise
    
    async def store_connection_profile(
        self,
        profile_id: str,
        profile_data: Dict[str, Any]
    ) -> bool:
        """
        Store connection profile securely in database.
        
        Args:
            profile_id: Unique profile identifier
            profile_data: Profile data to store
            
        Returns:
            Success status
        """
        command = """
            INSERT INTO connector_profiles (id, profile_data, created_at, updated_at)
            VALUES (:id, :profile_data, :created_at, :updated_at)
            ON CONFLICT (id) DO UPDATE SET
                profile_data = EXCLUDED.profile_data,
                updated_at = EXCLUDED.updated_at
        """
        
        try:
            result = await self.execute_command(
                command=command,
                parameters={
                    "id": profile_id,
                    "profile_data": profile_data,
                    "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat()
                }
            )
            return result.get("success", False)
        except Exception as e:
            logger.error(f"Failed to store connection profile: {e}")
            return False
    
    async def get_connection_profile(self, profile_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve connection profile from database.
        
        Args:
            profile_id: Profile identifier
            
        Returns:
            Profile data or None if not found
        """
        query = """
            SELECT profile_data FROM connector_profiles
            WHERE id = :id
        """
        
        try:
            result = await self.execute_query(
                query=query,
                parameters={"id": profile_id}
            )
            
            if result.get("success") and result.get("data"):
                rows = result["data"].get("rows", [])
                if rows:
                    return rows[0].get("profile_data")
            return None
        except Exception as e:
            logger.error(f"Failed to retrieve connection profile: {e}")
            return None
    
    async def list_connection_profiles(self) -> List[Dict[str, Any]]:
        """
        List all connection profiles.
        
        Returns:
            List of profile data
        """
        query = """
            SELECT id, profile_data, created_at, updated_at
            FROM connector_profiles
            ORDER BY created_at DESC
        """
        
        try:
            result = await self.execute_query(query=query)
            
            if result.get("success") and result.get("data"):
                return result["data"].get("rows", [])
            return []
        except Exception as e:
            logger.error(f"Failed to list connection profiles: {e}")
            return []
    
    async def delete_connection_profile(self, profile_id: str) -> bool:
        """
        Delete connection profile from database.
        
        Args:
            profile_id: Profile identifier
            
        Returns:
            Success status
        """
        command = """
            DELETE FROM connector_profiles WHERE id = :id
        """
        
        try:
            result = await self.execute_command(
                command=command,
                parameters={"id": profile_id}
            )
            return result.get("success", False)
        except Exception as e:
            logger.error(f"Failed to delete connection profile: {e}")
            return False
    
    async def close(self):
        """Close the HTTP client."""
        if self.client and not self.client.is_closed:
            await self.client.aclose()
