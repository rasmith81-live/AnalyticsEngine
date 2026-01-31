# =============================================================================
# Metadata Event Client for Multi-Agent Service
# Redis-based client for business_metadata communication
# =============================================================================
"""
Event client for agents to interact with business_metadata service.

Replaces HTTP calls with Redis Streams for:
- Entity CRUD operations
- KPI CRUD operations
- Module operations
- Value chain operations
"""

import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add shared path for imports
shared_path = Path(__file__).parent.parent.parent.parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from events.schemas import CommandType
from events.redis_client import BaseEventClient

logger = logging.getLogger(__name__)


class MetadataEventClient(BaseEventClient):
    """
    Redis-based client for business_metadata service.
    
    Used by agents to create/read/update entities, KPIs, modules,
    and value chains via Redis Streams.
    """
    
    def __init__(self, redis_url: Optional[str] = None, timeout: float = 30.0):
        super().__init__(
            service_name="multi_agent_service",
            target_service="business_metadata",
            redis_url=redis_url,
            timeout=timeout
        )
    
    # =========================================================================
    # Entity Operations
    # =========================================================================
    
    async def create_entity(
        self,
        code: str,
        name: str,
        description: str = "",
        module_code: Optional[str] = None,
        attributes: Optional[List[Dict[str, Any]]] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new entity."""
        return await self.send_command(
            CommandType.CREATE_ENTITY,
            {
                "code": code,
                "name": name,
                "description": description,
                "module_code": module_code,
                "attributes": attributes or []
            },
            session_id=session_id
        )
    
    async def update_entity(
        self,
        code: str,
        updates: Dict[str, Any],
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update an existing entity."""
        return await self.send_command(
            CommandType.UPDATE_ENTITY,
            {"code": code, "updates": updates},
            session_id=session_id
        )
    
    async def delete_entity(
        self,
        code: str,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Delete an entity."""
        return await self.send_command(
            CommandType.DELETE_ENTITY,
            {"code": code},
            session_id=session_id
        )
    
    async def get_entity(
        self,
        code: str,
        session_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Get entity by code."""
        try:
            return await self.send_command(
                CommandType.GET_ENTITY,
                {"code": code},
                session_id=session_id
            )
        except Exception as e:
            logger.warning(f"Failed to get entity {code}: {e}")
            return None
    
    async def list_entities(
        self,
        module_code: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List entities, optionally filtered by module."""
        try:
            result = await self.send_command(
                CommandType.LIST_ENTITIES,
                {"module_code": module_code},
                session_id=session_id
            )
            return result.get("entities", [])
        except Exception as e:
            logger.warning(f"Failed to list entities: {e}")
            return []
    
    # =========================================================================
    # KPI Operations
    # =========================================================================
    
    async def create_kpi(
        self,
        code: str,
        name: str,
        description: str = "",
        formula: str = "",
        module_code: Optional[str] = None,
        unit: str = "",
        calculation_type: str = "simple",
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new KPI."""
        return await self.send_command(
            CommandType.CREATE_KPI,
            {
                "code": code,
                "name": name,
                "description": description,
                "formula": formula,
                "module_code": module_code,
                "unit": unit,
                "calculation_type": calculation_type
            },
            session_id=session_id
        )
    
    async def update_kpi(
        self,
        code: str,
        updates: Dict[str, Any],
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update an existing KPI."""
        return await self.send_command(
            CommandType.UPDATE_KPI,
            {"code": code, "updates": updates},
            session_id=session_id
        )
    
    async def delete_kpi(
        self,
        code: str,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Delete a KPI."""
        return await self.send_command(
            CommandType.DELETE_KPI,
            {"code": code},
            session_id=session_id
        )
    
    async def get_kpi(
        self,
        code: str,
        session_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Get KPI by code."""
        try:
            return await self.send_command(
                CommandType.GET_KPI,
                {"code": code},
                session_id=session_id
            )
        except Exception as e:
            logger.warning(f"Failed to get KPI {code}: {e}")
            return None
    
    async def list_kpis(
        self,
        module_code: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List KPIs, optionally filtered by module."""
        try:
            result = await self.send_command(
                CommandType.LIST_KPIS,
                {"module_code": module_code},
                session_id=session_id
            )
            return result.get("kpis", [])
        except Exception as e:
            logger.warning(f"Failed to list KPIs: {e}")
            return []
    
    # =========================================================================
    # Module Operations
    # =========================================================================
    
    async def create_module(
        self,
        code: str,
        name: str,
        description: str = "",
        value_chain_code: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new module."""
        return await self.send_command(
            CommandType.CREATE_MODULE,
            {
                "code": code,
                "name": name,
                "description": description,
                "value_chain_code": value_chain_code
            },
            session_id=session_id
        )
    
    async def update_module(
        self,
        code: str,
        updates: Dict[str, Any],
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update an existing module."""
        return await self.send_command(
            CommandType.UPDATE_MODULE,
            {"code": code, "updates": updates},
            session_id=session_id
        )
    
    async def get_module(
        self,
        code: str,
        session_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Get module by code."""
        try:
            return await self.send_command(
                CommandType.GET_MODULE,
                {"code": code},
                session_id=session_id
            )
        except Exception as e:
            logger.warning(f"Failed to get module {code}: {e}")
            return None
    
    async def list_modules(
        self,
        value_chain_code: Optional[str] = None,
        session_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List modules, optionally filtered by value chain."""
        try:
            result = await self.send_command(
                CommandType.LIST_MODULES,
                {"value_chain_code": value_chain_code},
                session_id=session_id
            )
            return result.get("modules", [])
        except Exception as e:
            logger.warning(f"Failed to list modules: {e}")
            return []
    
    # =========================================================================
    # Value Chain Operations
    # =========================================================================
    
    async def create_value_chain(
        self,
        code: str,
        name: str,
        description: str = "",
        industry: str = "",
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a new value chain."""
        return await self.send_command(
            CommandType.CREATE_VALUE_CHAIN,
            {
                "code": code,
                "name": name,
                "description": description,
                "industry": industry
            },
            session_id=session_id
        )
    
    async def update_value_chain(
        self,
        code: str,
        updates: Dict[str, Any],
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Update an existing value chain."""
        return await self.send_command(
            CommandType.UPDATE_VALUE_CHAIN,
            {"code": code, "updates": updates},
            session_id=session_id
        )
    
    async def get_value_chain(
        self,
        code: str,
        session_id: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """Get value chain by code."""
        try:
            return await self.send_command(
                CommandType.GET_VALUE_CHAIN,
                {"code": code},
                session_id=session_id
            )
        except Exception as e:
            logger.warning(f"Failed to get value chain {code}: {e}")
            return None
    
    async def list_value_chains(
        self,
        session_id: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List all value chains."""
        try:
            result = await self.send_command(
                CommandType.LIST_VALUE_CHAINS,
                {},
                session_id=session_id
            )
            return result.get("value_chains", [])
        except Exception as e:
            logger.warning(f"Failed to list value chains: {e}")
            return []


# Singleton instance
_metadata_client: Optional[MetadataEventClient] = None


def get_metadata_client() -> MetadataEventClient:
    """Get singleton metadata client."""
    global _metadata_client
    if _metadata_client is None:
        _metadata_client = MetadataEventClient()
    return _metadata_client
