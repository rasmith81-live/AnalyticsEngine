"""
SCOR Calculation Handler

Implements BaseCalculationHandler for SCOR (Supply Chain Operations Reference) KPIs.
"""

from typing import Dict, Any
from datetime import datetime
import logging

from ..base_handler import (
    BaseCalculationHandler,
    CalculationParams,
    CalculationResult,
    CalculationError
)

logger = logging.getLogger(__name__)


class SCORCalculationHandler(BaseCalculationHandler):
    """
    SCOR-specific calculation handler.
    
    Handles calculation of SCOR KPIs like:
    - Perfect Order Fulfillment (RL.1.1)
    - Order Fulfillment Cycle Time (RS.1.1)
    - Cash-to-Cash Cycle Time (AM.1.1)
    - Total Supply Chain Management Cost (CO.1.1)
    - etc.
    """
    
    def __init__(
        self,
        database_service_url: str,
        messaging_service_url: str,
        metadata_service_url: str,
        cache_enabled: bool = True,
        cache_ttl: int = 3600  # SCOR calcs are expensive, cache longer
    ):
        """Initialize SCOR handler."""
        super().__init__(
            value_chain_code="SUPPLY_CHAIN",
            database_service_url=database_service_url,
            messaging_service_url=messaging_service_url,
            metadata_service_url=metadata_service_url,
            cache_enabled=cache_enabled,
            cache_ttl=cache_ttl
        )
        
        # SCOR-specific configuration
        self.schema_name = "scor_data"
        
        # Map KPI codes to calculation methods
        self.kpi_calculators = {
            "PERFECT_ORDER_FULFILLMENT": self._calculate_perfect_order,
            "ORDER_FULFILLMENT_CYCLE_TIME": self._calculate_cycle_time,
            "CASH_TO_CASH_CYCLE_TIME": self._calculate_cash_to_cash,
            "TOTAL_SUPPLY_CHAIN_COST": self._calculate_total_cost,
            # ... more KPIs
        }
    
    async def calculate(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Calculate SCOR KPI.
        
        Routes to specific calculation method based on KPI code.
        """
        start_time = datetime.utcnow()
        
        # Get calculation method
        calculator = self.kpi_calculators.get(params.kpi_code)
        
        if not calculator:
            raise CalculationError(
                f"Unknown SCOR KPI: {params.kpi_code}"
            )
        
        # Execute calculation
        try:
            value, metadata = await calculator(params)
            
            calculation_time = (
                datetime.utcnow() - start_time
            ).total_seconds() * 1000
            
            return CalculationResult(
                kpi_code=params.kpi_code,
                value=value,
                unit=metadata.get("unit", "Percentage"),
                timestamp=datetime.utcnow(),
                calculation_time_ms=calculation_time,
                metadata=metadata
            )
            
        except Exception as e:
            logger.error(
                f"SCOR calculation failed for {params.kpi_code}: {str(e)}"
            )
            raise CalculationError(str(e))
    
    async def validate_params(
        self,
        params: CalculationParams
    ) -> bool:
        """Validate SCOR calculation parameters."""
        # Check required filters
        if params.kpi_code == "PERFECT_ORDER_FULFILLMENT":
            # Requires date range
            if not params.start_date or not params.end_date:
                raise ValueError(
                    "Perfect Order Fulfillment requires start_date and end_date"
                )
        
        # Add more validation as needed
        return True
    
    def get_cache_key(
        self,
        params: CalculationParams
    ) -> str:
        """Generate cache key for SCOR calculations."""
        return f"scor:{self._generate_cache_key_base(params)}"
    
    # ========================================================================
    # SCOR-Specific Calculation Methods
    # ========================================================================
    
    async def _calculate_perfect_order(
        self,
        params: CalculationParams
    ) -> tuple[float, Dict[str, Any]]:
        """
        Calculate Perfect Order Fulfillment (RL.1.1).
        
        Formula: (Total perfect orders / Total orders) × 100%
        
        An order is perfect if:
        - Delivered in full (RL.2.1)
        - On time (RL.2.2)
        - Perfect documentation (RL.2.3)
        - Perfect condition (RL.2.4)
        """
        # Query orders from scor_data schema
        orders = await self.query_data(
            table_name="orders",
            filters={
                "order_date": {
                    "gte": params.start_date,
                    "lte": params.end_date
                },
                **params.filters
            }
        )
        
        total_orders = len(orders)
        
        if total_orders == 0:
            return 0.0, {"unit": "Percentage", "total_orders": 0}
        
        # Count perfect orders
        perfect_orders = sum(
            1 for order in orders
            if self._is_perfect_order(order)
        )
        
        # Calculate percentage
        value = (perfect_orders / total_orders) * 100
        
        metadata = {
            "unit": "Percentage",
            "total_orders": total_orders,
            "perfect_orders": perfect_orders,
            "components": {
                "RL.2.1": "Delivered in Full",
                "RL.2.2": "On Time Delivery",
                "RL.2.3": "Perfect Documentation",
                "RL.2.4": "Perfect Condition"
            }
        }
        
        return value, metadata
    
    async def _calculate_cycle_time(
        self,
        params: CalculationParams
    ) -> tuple[float, Dict[str, Any]]:
        """
        Calculate Order Fulfillment Cycle Time (RS.1.1).
        
        Formula: Average time from order receipt to customer receipt
        """
        # Query orders with delivery data
        orders = await self.query_data(
            table_name="orders",
            filters={
                "order_date": {
                    "gte": params.start_date,
                    "lte": params.end_date
                },
                "status": "delivered",
                **params.filters
            },
            columns=["order_date", "delivery_date"]
        )
        
        if not orders:
            return 0.0, {"unit": "Days", "order_count": 0}
        
        # Calculate cycle times
        cycle_times = [
            (order["delivery_date"] - order["order_date"]).days
            for order in orders
            if order.get("delivery_date")
        ]
        
        if not cycle_times:
            return 0.0, {"unit": "Days", "order_count": 0}
        
        # Calculate average
        avg_cycle_time = sum(cycle_times) / len(cycle_times)
        
        metadata = {
            "unit": "Days",
            "order_count": len(cycle_times),
            "min_cycle_time": min(cycle_times),
            "max_cycle_time": max(cycle_times),
            "aggregation": params.aggregation
        }
        
        return avg_cycle_time, metadata
    
    async def _calculate_cash_to_cash(
        self,
        params: CalculationParams
    ) -> tuple[float, Dict[str, Any]]:
        """
        Calculate Cash-to-Cash Cycle Time (AM.1.1).
        
        Formula: DIO + DSO - DPO
        Where:
        - DIO = Days Inventory Outstanding
        - DSO = Days Sales Outstanding
        - DPO = Days Payable Outstanding
        """
        # Calculate components
        dio = await self._calculate_dio(params)
        dso = await self._calculate_dso(params)
        dpo = await self._calculate_dpo(params)
        
        # Calculate cash-to-cash
        cash_to_cash = dio + dso - dpo
        
        metadata = {
            "unit": "Days",
            "components": {
                "DIO": dio,
                "DSO": dso,
                "DPO": dpo
            },
            "formula": "DIO + DSO - DPO"
        }
        
        return cash_to_cash, metadata
    
    async def _calculate_total_cost(
        self,
        params: CalculationParams
    ) -> tuple[float, Dict[str, Any]]:
        """
        Calculate Total Supply Chain Management Cost (CO.1.1).
        
        Sum of all supply chain costs.
        """
        # Query costs from scor_data schema
        costs = await self.query_data(
            table_name="costs",
            filters={
                "cost_date": {
                    "gte": params.start_date,
                    "lte": params.end_date
                },
                **params.filters
            },
            columns=["cost_amount", "cost_category"]
        )
        
        # Sum costs
        total_cost = sum(cost["cost_amount"] for cost in costs)
        
        # Break down by category
        cost_by_category = {}
        for cost in costs:
            category = cost.get("cost_category", "Other")
            cost_by_category[category] = (
                cost_by_category.get(category, 0) + cost["cost_amount"]
            )
        
        metadata = {
            "unit": "Currency",
            "cost_count": len(costs),
            "breakdown": cost_by_category
        }
        
        return total_cost, metadata
    
    # ========================================================================
    # Helper Methods
    # ========================================================================
    
    def _is_perfect_order(self, order: Dict[str, Any]) -> bool:
        """Check if order meets all perfect order criteria."""
        return (
            order.get("delivered_in_full", False) and
            order.get("delivered_on_time", False) and
            order.get("documentation_complete", False) and
            order.get("condition_perfect", False)
        )
    
    async def _calculate_dio(self, params: CalculationParams) -> float:
        """
        Calculate Days Inventory Outstanding.
        Formula: (Average Inventory / Cost of Goods Sold) * Days in Period
        """
        # Query inventory and COGS data
        query = f"""
            SELECT 
                AVG(inventory_value) as avg_inventory,
                SUM(cogs) as total_cogs
            FROM {self.schema_name}.inventory_summary
            WHERE date >= %(start_date)s 
              AND date <= %(end_date)s
        """
        
        result = await self._execute_query(query, params.filters)
        
        if not result or not result[0]["total_cogs"]:
            return 0.0
        
        avg_inventory = result[0]["avg_inventory"] or 0
        total_cogs = result[0]["total_cogs"]
        days = (params.time_period["end_date"] - params.time_period["start_date"]).days
        
        if total_cogs > 0:
            dio = (avg_inventory / total_cogs) * days
            return round(dio, 2)
        
        return 0.0
    
    async def _calculate_dso(self, params: CalculationParams) -> float:
        """
        Calculate Days Sales Outstanding.
        Formula: (Average Accounts Receivable / Total Credit Sales) * Days in Period
        """
        query = f"""
            SELECT 
                AVG(accounts_receivable) as avg_ar,
                SUM(credit_sales) as total_sales
            FROM {self.schema_name}.financial_summary
            WHERE date >= %(start_date)s 
              AND date <= %(end_date)s
        """
        
        result = await self._execute_query(query, params.filters)
        
        if not result or not result[0]["total_sales"]:
            return 0.0
        
        avg_ar = result[0]["avg_ar"] or 0
        total_sales = result[0]["total_sales"]
        days = (params.time_period["end_date"] - params.time_period["start_date"]).days
        
        if total_sales > 0:
            dso = (avg_ar / total_sales) * days
            return round(dso, 2)
        
        return 0.0
    
    async def _calculate_dpo(self, params: CalculationParams) -> float:
        """
        Calculate Days Payable Outstanding.
        Formula: (Average Accounts Payable / Cost of Goods Sold) * Days in Period
        """
        query = f"""
            SELECT 
                AVG(accounts_payable) as avg_ap,
                SUM(cogs) as total_cogs
            FROM {self.schema_name}.financial_summary
            WHERE date >= %(start_date)s 
              AND date <= %(end_date)s
        """
        
        result = await self._execute_query(query, params.filters)
        
        if not result or not result[0]["total_cogs"]:
            return 0.0
        
        avg_ap = result[0]["avg_ap"] or 0
        total_cogs = result[0]["total_cogs"]
        days = (params.time_period["end_date"] - params.time_period["start_date"]).days
        
        if total_cogs > 0:
            dpo = (avg_ap / total_cogs) * days
            return round(dpo, 2)
        
        return 0.0
