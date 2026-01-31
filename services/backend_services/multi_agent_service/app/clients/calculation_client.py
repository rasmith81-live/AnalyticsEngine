# =============================================================================
# Calculation Event Client for Multi-Agent Service
# Redis-based client for calculation_engine communication
# =============================================================================
"""
Event client for agents to interact with calculation_engine service.

Replaces HTTP calls with Redis Streams for:
- KPI calculations
- Batch calculations
- Dashboard calculations
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


class CalculationEventClient(BaseEventClient):
    """
    Redis-based client for calculation_engine service.
    
    Used by agents to execute KPI calculations via Redis Streams.
    """
    
    def __init__(self, redis_url: Optional[str] = None, timeout: float = 60.0):
        super().__init__(
            service_name="multi_agent_service",
            target_service="calculation_engine",
            redis_url=redis_url,
            timeout=timeout  # Longer timeout for calculations
        )
    
    async def calculate_kpi(
        self,
        kpi_code: str,
        parameters: Optional[Dict[str, Any]] = None,
        time_range: Optional[Dict[str, str]] = None,
        filters: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calculate a single KPI.
        
        Args:
            kpi_code: Code of the KPI to calculate
            parameters: Calculation parameters
            time_range: Optional time range (start, end)
            filters: Optional data filters
            session_id: Session ID for tracing
            
        Returns:
            Calculation result with value and metadata
        """
        return await self.send_command(
            CommandType.CALCULATE_KPI,
            {
                "kpi_code": kpi_code,
                "parameters": parameters or {},
                "time_range": time_range,
                "filters": filters
            },
            session_id=session_id,
            timeout=60.0
        )
    
    async def calculate_batch(
        self,
        kpi_codes: List[str],
        parameters: Optional[Dict[str, Any]] = None,
        time_range: Optional[Dict[str, str]] = None,
        filters: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Calculate multiple KPIs in batch.
        
        Args:
            kpi_codes: List of KPI codes to calculate
            parameters: Shared calculation parameters
            time_range: Optional time range
            filters: Optional data filters
            session_id: Session ID for tracing
            
        Returns:
            Batch results with values for each KPI
        """
        return await self.send_command(
            CommandType.CALCULATE_BATCH,
            {
                "kpi_codes": kpi_codes,
                "parameters": parameters or {},
                "time_range": time_range,
                "filters": filters
            },
            session_id=session_id,
            timeout=120.0  # Longer timeout for batch
        )
    
    async def calculate_kpi_with_fallback(
        self,
        kpi_code: str,
        parameters: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Calculate KPI with fallback on failure."""
        return await self.send_command_with_fallback(
            CommandType.CALCULATE_KPI,
            {"kpi_code": kpi_code, "parameters": parameters or {}},
            fallback={
                "kpi_code": kpi_code,
                "value": None,
                "error": "Calculation service unavailable"
            },
            session_id=session_id
        )


# Singleton instance
_calculation_client: Optional[CalculationEventClient] = None


def get_calculation_client() -> CalculationEventClient:
    """Get singleton calculation client."""
    global _calculation_client
    if _calculation_client is None:
        _calculation_client = CalculationEventClient()
    return _calculation_client
