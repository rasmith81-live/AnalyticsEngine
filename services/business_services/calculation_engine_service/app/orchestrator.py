"""
Calculation Engine Orchestrator

Routes calculation requests to appropriate value chain handlers,
manages parallel execution, and aggregates results.
"""

from typing import Dict, List, Any, Optional
from datetime import datetime
import asyncio
import logging
import hashlib
import json

from .base_handler import (
    BaseCalculationHandler,
    CalculationParams,
    CalculationResult,
    CalculationError
)

logger = logging.getLogger(__name__)


class CalculationOrchestrator:
    """
    Orchestrates calculation requests across multiple value chain handlers.
    
    Responsibilities:
    - Route requests to appropriate handlers
    - Execute calculations in parallel
    - Aggregate multi-KPI results
    - Handle errors and retries
    - Request Coalescing (Single-flight)
    """
    
    def __init__(self):
        """Initialize orchestrator."""
        self.handlers: Dict[str, BaseCalculationHandler] = {}
        self.kpi_to_handler_map: Dict[str, str] = {}
        self._pending_calculations: Dict[str, asyncio.Task] = {}
    
    def register_handler(
        self,
        value_chain_code: str,
        handler: BaseCalculationHandler
    ):
        """
        Register a value chain handler.
        
        Args:
            value_chain_code: Value chain identifier
            handler: Handler instance
        """
        self.handlers[value_chain_code] = handler
        logger.info(f"Registered handler for value chain: {value_chain_code}")
    
    async def load_kpi_mappings(self, metadata_service_url: str):
        """
        Load KPI to value chain mappings from metadata service.
        
        Args:
            metadata_service_url: Metadata service URL
        """
        # Fetch all KPIs and their value chain assignments
        # Build kpi_to_handler_map
        # Example: {"PERFECT_ORDER_FULFILLMENT": "SUPPLY_CHAIN"}
        pass
    
    async def calculate_single(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Calculate a single KPI with Request Coalescing.
        
        If a calculation with the same parameters is already in progress,
        this method will wait for that calculation to complete and return
        the same result, rather than starting a new one.
        
        Args:
            params: Calculation parameters
            
        Returns:
            CalculationResult
            
        Raises:
            ValueError: If KPI not found or handler not registered
            CalculationError: If calculation fails
        """
        key = self._get_request_key(params)
        
        # Check if already running
        if key in self._pending_calculations:
            logger.debug(f"Coalescing request for {params.kpi_code} (key: {key})")
            return await self._pending_calculations[key]
            
        # Create new task
        task = asyncio.create_task(self._execute_calculate_single(params))
        self._pending_calculations[key] = task
        
        try:
            return await task
        finally:
            # Cleanup finished task
            self._pending_calculations.pop(key, None)

    async def _execute_calculate_single(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Internal execution logic for single KPI calculation.
        """
        # Get handler for this KPI
        handler = self._get_handler_for_kpi(params.kpi_code)
        
        if not handler:
            raise ValueError(
                f"No handler registered for KPI: {params.kpi_code}"
            )
        
        # Validate parameters
        await handler.validate_params(params)
        
        # Calculate with caching
        start_time = datetime.utcnow()
        
        try:
            result = await handler.calculate_with_cache(params)
            
            # Add orchestration metadata
            result.metadata["orchestrator"] = {
                "handler": handler.value_chain_code,
                "request_time": start_time.isoformat()
            }
            
            return result
            
        except Exception as e:
            logger.error(
                f"Calculation failed for {params.kpi_code}: {str(e)}"
            )
            raise CalculationError(
                f"Failed to calculate {params.kpi_code}: {str(e)}"
            )
    
    def _get_request_key(self, params: CalculationParams) -> str:
        """Generate a unique key for the calculation request."""
        # Dump model to dict, exclude metadata if it contains transient info
        # For now we include everything as params should be deterministic
        params_dict = params.model_dump(mode='json')
        # Sort keys to ensure consistent hash
        params_json = json.dumps(params_dict, sort_keys=True)
        return hashlib.sha256(params_json.encode()).hexdigest()

    async def calculate_batch(
        self,
        params_list: List[CalculationParams]
    ) -> List[CalculationResult]:
        """
        Calculate multiple KPIs in parallel.
        
        Args:
            params_list: List of calculation parameters
            
        Returns:
            List of CalculationResults
        """
        # Group by handler for optimization
        handler_groups = self._group_by_handler(params_list)
        
        # Execute in parallel per handler
        tasks = []
        for handler_code, params_group in handler_groups.items():
            handler = self.handlers.get(handler_code)
            if handler:
                for params in params_group:
                    tasks.append(
                        self.calculate_single(params)
                    )
        
        # Wait for all calculations
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Filter out errors (or handle them)
        valid_results = [
            r for r in results
            if isinstance(r, CalculationResult)
        ]
        
        return valid_results
    
    async def calculate_dashboard(
        self,
        dashboard_config: Dict[str, Any]
    ) -> Dict[str, CalculationResult]:
        """
        Calculate all KPIs for a dashboard.
        
        Args:
            dashboard_config: Dashboard configuration with KPI list
            
        Returns:
            Dictionary of KPI code to CalculationResult
        """
        # Extract KPI codes from dashboard config
        kpi_codes = dashboard_config.get("kpis", [])
        
        # Build params for each KPI
        params_list = [
            CalculationParams(
                kpi_code=kpi_code,
                filters=dashboard_config.get("filters", {}),
                time_period=dashboard_config.get("time_period", "monthly"),
                start_date=dashboard_config.get("start_date"),
                end_date=dashboard_config.get("end_date")
            )
            for kpi_code in kpi_codes
        ]
        
        # Calculate in parallel
        results = await self.calculate_batch(params_list)
        
        # Return as dictionary
        return {
            result.kpi_code: result
            for result in results
        }
    
    def _get_handler_for_kpi(
        self,
        kpi_code: str
    ) -> Optional[BaseCalculationHandler]:
        """
        Get handler for a specific KPI.
        
        Args:
            kpi_code: KPI code
            
        Returns:
            Handler instance or None
        """
        # Look up value chain for this KPI
        value_chain_code = self.kpi_to_handler_map.get(kpi_code)
        
        if not value_chain_code:
            logger.warning(f"No value chain mapping for KPI: {kpi_code}")
            return None
        
        # Get handler for value chain
        handler = self.handlers.get(value_chain_code)
        
        if not handler:
            logger.warning(
                f"No handler registered for value chain: {value_chain_code}"
            )
            return None
        
        return handler
    
    def _group_by_handler(
        self,
        params_list: List[CalculationParams]
    ) -> Dict[str, List[CalculationParams]]:
        """
        Group calculation parameters by handler.
        
        Args:
            params_list: List of calculation parameters
            
        Returns:
            Dictionary of handler code to params list
        """
        groups: Dict[str, List[CalculationParams]] = {}
        
        for params in params_list:
            handler = self._get_handler_for_kpi(params.kpi_code)
            if handler:
                handler_code = handler.value_chain_code
                if handler_code not in groups:
                    groups[handler_code] = []
                groups[handler_code].append(params)
        
        return groups
    
    def get_handler_stats(self) -> Dict[str, Any]:
        """
        Get statistics about registered handlers.
        
        Returns:
            Dictionary of handler statistics
        """
        return {
            "total_handlers": len(self.handlers),
            "handlers": list(self.handlers.keys()),
            "total_kpis": len(self.kpi_to_handler_map),
            "kpis_per_handler": {
                handler_code: len([
                    k for k, v in self.kpi_to_handler_map.items()
                    if v == handler_code
                ])
                for handler_code in self.handlers.keys()
            }
        }
