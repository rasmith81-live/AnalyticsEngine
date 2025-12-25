"""
Database Client for Demo Config Service.

Provides interface to Database Service for storing client configurations and proposals.
"""

import httpx
import logging
from typing import Dict, Any, Optional, List
from datetime import datetime

logger = logging.getLogger(__name__)


class DatabaseClient:
    """Client for interacting with Database Service."""
    
    def __init__(self, base_url: str, service_name: str = "demo_config_service"):
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
        """Execute a write command against the database."""
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
        """Execute a read query against the database."""
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
    
    async def store_client_config(
        self,
        client_id: str,
        config_data: Dict[str, Any]
    ) -> bool:
        """Store client configuration in database."""
        command = """
            INSERT INTO client_configs (client_id, config_data, created_at, updated_at)
            VALUES (:client_id, :config_data, :created_at, :updated_at)
            ON CONFLICT (client_id) DO UPDATE SET
                config_data = EXCLUDED.config_data,
                updated_at = EXCLUDED.updated_at
        """
        
        try:
            result = await self.execute_command(
                command=command,
                parameters={
                    "client_id": client_id,
                    "config_data": config_data,
                    "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat()
                }
            )
            return result.get("success", False)
        except Exception as e:
            logger.error(f"Failed to store client config: {e}")
            return False
    
    async def get_client_config(self, client_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve client configuration from database."""
        query = """
            SELECT config_data FROM client_configs
            WHERE client_id = :client_id
        """
        
        try:
            result = await self.execute_query(
                query=query,
                parameters={"client_id": client_id}
            )
            
            if result.get("success") and result.get("data"):
                rows = result["data"].get("rows", [])
                if rows:
                    return rows[0].get("config_data")
            return None
        except Exception as e:
            logger.error(f"Failed to retrieve client config: {e}")
            return None
    
    async def list_client_configs(self) -> List[Dict[str, Any]]:
        """List all client configurations."""
        query = """
            SELECT client_id, config_data, created_at, updated_at
            FROM client_configs
            ORDER BY created_at DESC
        """
        
        try:
            result = await self.execute_query(query=query)
            
            if result.get("success") and result.get("data"):
                return result["data"].get("rows", [])
            return []
        except Exception as e:
            logger.error(f"Failed to list client configs: {e}")
            return []
    
    async def delete_client_config(self, client_id: str) -> bool:
        """Delete client configuration from database."""
        command = """
            DELETE FROM client_configs WHERE client_id = :client_id
        """
        
        try:
            result = await self.execute_command(
                command=command,
                parameters={"client_id": client_id}
            )
            return result.get("success", False)
        except Exception as e:
            logger.error(f"Failed to delete client config: {e}")
            return False
    
    async def store_service_proposal(
        self,
        proposal_id: str,
        proposal_data: Dict[str, Any]
    ) -> bool:
        """Store service proposal in database."""
        command = """
            INSERT INTO service_proposals (proposal_id, proposal_data, created_at)
            VALUES (:proposal_id, :proposal_data, :created_at)
            ON CONFLICT (proposal_id) DO UPDATE SET
                proposal_data = EXCLUDED.proposal_data
        """
        
        try:
            result = await self.execute_command(
                command=command,
                parameters={
                    "proposal_id": proposal_id,
                    "proposal_data": proposal_data,
                    "created_at": datetime.utcnow().isoformat()
                }
            )
            return result.get("success", False)
        except Exception as e:
            logger.error(f"Failed to store service proposal: {e}")
            return False
    
    async def get_service_proposal(self, proposal_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve service proposal from database."""
        query = """
            SELECT proposal_data FROM service_proposals
            WHERE proposal_id = :proposal_id
        """
        
        try:
            result = await self.execute_query(
                query=query,
                parameters={"proposal_id": proposal_id}
            )
            
            if result.get("success") and result.get("data"):
                rows = result["data"].get("rows", [])
                if rows:
                    return rows[0].get("proposal_data")
            return None
        except Exception as e:
            logger.error(f"Failed to retrieve service proposal: {e}")
            return None
    
    async def close(self):
        """Close the HTTP client."""
        if self.client and not self.client.is_closed:
            await self.client.aclose()
