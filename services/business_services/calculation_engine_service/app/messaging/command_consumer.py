# =============================================================================
# Calculation Command Consumer
# Processes calculation commands from multi_agent_service via Redis Streams
# =============================================================================
"""
Command consumer for calculation_engine_service.

Handles:
- KPI calculations
- Batch calculations
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add shared path for imports
shared_path = Path(__file__).parent.parent.parent.parent.parent / "shared"
sys.path.insert(0, str(shared_path))

from events.schemas import ServiceCommand, CommandType, ResponseType
from events.consumer import BaseCommandConsumer

logger = logging.getLogger(__name__)


class CalculationCommandConsumer(BaseCommandConsumer):
    """
    Command consumer for calculation_engine_service.
    
    Processes KPI calculation commands from other services via Redis Streams.
    """
    
    def __init__(
        self,
        calculation_engine,
        redis_url: Optional[str] = None
    ):
        """
        Initialize consumer.
        
        Args:
            calculation_engine: The calculation engine instance
            redis_url: Redis connection URL
        """
        super().__init__(
            service_name="calculation_engine",
            redis_url=redis_url
        )
        self.calculation_engine = calculation_engine
    
    async def _register_handlers(self) -> None:
        """Register command handlers."""
        self.register_handler(CommandType.CALCULATE_KPI, self._handle_calculate_kpi)
        self.register_handler(CommandType.CALCULATE_BATCH, self._handle_calculate_batch)
        self.register_handler(CommandType.HEALTH_CHECK, self._handle_health_check)
        
        logger.info("Registered calculation command handlers")
    
    async def _handle_calculate_kpi(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle single KPI calculation."""
        payload = command.payload
        kpi_code = payload.get("kpi_code")
        parameters = payload.get("parameters", {})
        time_range = payload.get("time_range")
        filters = payload.get("filters")
        
        logger.info(f"Calculating KPI: {kpi_code}")
        
        try:
            result = await self.calculation_engine.calculate_kpi(
                kpi_code=kpi_code,
                parameters=parameters,
                time_range=time_range,
                filters=filters
            )
            
            return {
                "kpi_code": kpi_code,
                "value": result.get("value"),
                "unit": result.get("unit"),
                "timestamp": result.get("timestamp"),
                "metadata": result.get("metadata", {})
            }
        except Exception as e:
            logger.error(f"Calculation failed for {kpi_code}: {e}")
            raise
    
    async def _handle_calculate_batch(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle batch KPI calculation."""
        payload = command.payload
        kpi_codes = payload.get("kpi_codes", [])
        parameters = payload.get("parameters", {})
        time_range = payload.get("time_range")
        filters = payload.get("filters")
        
        logger.info(f"Calculating batch of {len(kpi_codes)} KPIs")
        
        results = {}
        errors = {}
        
        for kpi_code in kpi_codes:
            try:
                result = await self.calculation_engine.calculate_kpi(
                    kpi_code=kpi_code,
                    parameters=parameters,
                    time_range=time_range,
                    filters=filters
                )
                results[kpi_code] = {
                    "value": result.get("value"),
                    "unit": result.get("unit"),
                    "timestamp": result.get("timestamp")
                }
            except Exception as e:
                errors[kpi_code] = str(e)
        
        return {
            "results": results,
            "errors": errors,
            "total": len(kpi_codes),
            "successful": len(results),
            "failed": len(errors)
        }
    
    async def _handle_health_check(self, command: ServiceCommand) -> Dict[str, Any]:
        """Handle health check."""
        return {
            "service": "calculation_engine",
            "status": "healthy",
            "consumer": self.consumer_name
        }
