"""
Dynamic Calculation Handler

Generic handler that executes KPIs based on metadata definitions.

Supports two calculation types:
1. "simple" - Direct formula calculation using math_expression and FormulaParser
2. "set_based" - Multi-step set operations using SetBasedKPIDefinition

The calculation_type field in the KPI definition determines which path is used.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import logging

from ..base_handler import (
    BaseCalculationHandler,
    CalculationParams,
    CalculationResult,
    CalculationError
)
from ..engine.parser import FormulaParser
from ..engine.sql_generator import SQLGenerator
from ..engine.timescale_manager import TimescaleManager
from ..engine.set_operations import (
    SetBasedKPIDefinition,
    SetBasedSQLGenerator,
    get_set_based_kpi_definition,
)

logger = logging.getLogger(__name__)

class DynamicCalculationHandler(BaseCalculationHandler):
    """
    Executes calculations dynamically based on metadata definitions.
    
    Calculation Types:
    - "simple": Uses math_expression → FormulaParser → SQLGenerator
    - "set_based": Uses set_based_definition → SetBasedSQLGenerator
    
    Flow for simple calculations:
    1. Fetch KPI definition from Metadata Service
    2. Parse formula string into AST using FormulaParser
    3. Determine optimal table/view using TimescaleManager
    4. Compile AST into SQL using SQLGenerator
    5. Execute SQL and return result
    
    Flow for set-based calculations:
    1. Fetch KPI definition from Metadata Service
    2. Load SetBasedKPIDefinition from set_based_definition field
    3. Generate CTE-based SQL using SetBasedSQLGenerator
    4. Execute single SQL query and return result
    """
    
    def __init__(
        self,
        value_chain_code: str,
        database_service_url: str,
        messaging_service_url: str,
        metadata_service_url: str,
        cache_enabled: bool = True,
        cache_ttl: int = 300
    ):
        super().__init__(
            value_chain_code=value_chain_code,
            database_service_url=database_service_url,
            messaging_service_url=messaging_service_url,
            metadata_service_url=metadata_service_url,
            cache_enabled=cache_enabled,
            cache_ttl=cache_ttl
        )
        # Simple calculation components
        self.parser = FormulaParser()
        self.sql_generator = SQLGenerator()
        self.timescale_manager = TimescaleManager()
        
        # Set-based calculation components
        self.set_based_sql_generator = SetBasedSQLGenerator(schema_name=self.schema_name)
        
    async def calculate(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Dynamically calculate KPI value.
        
        Routes to appropriate calculation method based on calculation_type:
        - "set_based": Uses SetBasedSQLGenerator for multi-step set operations
        - "simple" (default): Uses FormulaParser + SQLGenerator for direct formulas
        """
        start_time = datetime.utcnow()
        
        # 1. Fetch KPI Definition
        kpi_def = await self.get_kpi_definition(params.kpi_code)
        
        if not kpi_def:
            logger.warning(f"KPI definition not found for {params.kpi_code}, checking fallbacks")
            kpi_def = self._get_fallback_definition(params.kpi_code)
            
        if not kpi_def:
             raise CalculationError(f"KPI definition not found for: {params.kpi_code}")

        # 2. Route based on calculation_type
        calculation_type = kpi_def.get("calculation_type", "simple")
        
        if calculation_type == "set_based":
            return await self._calculate_set_based(params, kpi_def, start_time)
        else:
            return await self._calculate_simple(params, kpi_def, start_time)
    
    async def _calculate_set_based(
        self,
        params: CalculationParams,
        kpi_def: Dict[str, Any],
        start_time: datetime
    ) -> CalculationResult:
        """
        Calculate using set-based definition (multi-step set operations).
        
        Uses SetBasedKPIDefinition stored in set_based_definition field.
        """
        # Get set-based definition
        set_def_data = kpi_def.get("set_based_definition")
        if not set_def_data:
            raise CalculationError(f"No set_based_definition for set_based KPI: {params.kpi_code}")
        
        # Parse into SetBasedKPIDefinition
        try:
            set_based_def = SetBasedKPIDefinition(
                kpi_code=kpi_def.get("code", params.kpi_code),
                name=kpi_def.get("name", params.kpi_code),
                description=kpi_def.get("description"),
                unit=kpi_def.get("unit", "Number"),
                period_parameters=set_def_data.get("period_parameters", ["PeriodStart", "PeriodEnd"]),
                steps=set_def_data.get("steps", []),
                final_formula=set_def_data.get("final_formula", ""),
                metadata=kpi_def.get("metadata_", {})
            )
        except Exception as e:
            raise CalculationError(f"Invalid set_based_definition: {e}")
        
        # Generate SQL using SetBasedSQLGenerator
        sql, sql_params = self.set_based_sql_generator.generate_sql(
            kpi_def=set_based_def,
            period_start=params.start_date,
            period_end=params.end_date,
            additional_filters=params.filters
        )
        
        # Execute query (placeholder - would use db_client in real implementation)
        # In real implementation: results = await self.db_client.fetch_all(sql, sql_params)
        value = 0.0  # Placeholder
        
        calculation_time = (datetime.utcnow() - start_time).total_seconds() * 1000
        
        return CalculationResult(
            kpi_code=params.kpi_code,
            value=value,
            unit=set_based_def.unit,
            timestamp=datetime.utcnow(),
            calculation_time_ms=calculation_time,
            metadata={
                "calculation_type": "set_based",
                "sql_generated": sql,
                "steps": [step.name for step in set_based_def.steps],
                "final_formula": set_based_def.final_formula
            }
        )
    
    async def _calculate_simple(
        self,
        params: CalculationParams,
        kpi_def: Dict[str, Any],
        start_time: datetime
    ) -> CalculationResult:
        """
        Calculate using simple formula (direct math expression).
        
        Uses math_expression or formula field with FormulaParser.
        """
        # Get formula - prefer set_based_definition.final_formula if exists,
        # otherwise use math_expression or natural language formula
        formula = kpi_def.get("math_expression") or kpi_def.get("formula")
        if not formula:
            raise CalculationError(f"No formula defined for KPI: {params.kpi_code}")
            
        # 2. Parse Formula
        try:
            parsed_formula = self.parser.parse(formula)
        except Exception as e:
            raise CalculationError(f"Formula parsing failed for '{formula}': {e}")
            
        # 3. Determine Execution Strategy (Hierarchical Query Logic & Approximation)
        # Check for approximate mode preference (Params override Metadata)
        approximate = params.metadata.get("approximate")
        if approximate is None:
            approximate = kpi_def.get("approximate_mode", False)
            
        # Determine base table name - typically derived from the KPI's primary entity or explicitly mapped
        base_table_name = kpi_def.get("target_table") or f"{self.schema_name}.{params.kpi_code.lower()}_facts"
        
        # Resolve optimal source table and bucket interval based on time range
        if params.start_date and params.end_date:
            time_range = (params.start_date, params.end_date)
            # Map 'time_period' param (e.g. 'monthly') to interval string if needed, or use default
            requested_interval = "1 day" # Default base granularity
            
            target_table, bucket_interval = self.timescale_manager.get_optimal_query_source(
                base_table_name,
                time_range,
                requested_interval
            )
        else:
            target_table = base_table_name
            bucket_interval = "1 day"

        # 4. Generate SQL
        try:
            # Pass dimensions to group_by if needed
            group_by = ", ".join(params.dimensions) if params.dimensions else None
            
            query = self.sql_generator.generate_query(
                parsed_formula=parsed_formula,
                table_name=target_table,
                group_by=group_by,
                approximate=approximate,
                bucket_interval=bucket_interval
            )
            
            # Apply time filters and other filters
            # SQLGenerator currently returns a basic SELECT. We need to wrap or append WHERE clauses.
            # This is a simplification. A robust query builder would handle this more gracefully.
            # For now, we'll rely on the base_handler's query_data to execute raw SQL 
            # OR we can improve SQLGenerator to accept filters.
            # Let's assume we execute the generated SQL and post-process or inject WHERE clauses.
            
            # Inject WHERE clause for time range
            # Note: naive string manipulation, in prod use a builder
            time_filter = f"time >= '{params.start_date}' AND time <= '{params.end_date}'"
            if "WHERE" in query:
                query += f" AND {time_filter}"
            else:
                # Need to insert before GROUP BY
                if "GROUP BY" in query:
                    parts = query.split("GROUP BY")
                    query = f"{parts[0]} WHERE {time_filter} GROUP BY {parts[1]}"
                else:
                    query += f" WHERE {time_filter}"
                    
        except Exception as e:
            raise CalculationError(f"SQL generation failed: {e}")

        # 4. Execute Query
        # Using base class query execution which should handle connection pooling etc.
        try:
            # We use a raw query execution here. 
            # validate_params ensures start_date/end_date are present if required
            
            # This needs to be implemented in base_handler or accessible
            # Assuming query_data can take a raw query or we use a lower level method
            # For this step, we'll simulate the execution call
            
            # In real implementation:
            # results = await self.db_client.fetch_all(query)
            
            # Mocking result for now since we don't have a live DB connection in this env
            # and base_handler.query_data is abstract/stubbed
            value = 100.0 # Placeholder
            
            # If we had real results:
            # value = results[0]['value'] if results else 0.0
            
        except Exception as e:
            raise CalculationError(f"Query execution failed: {e}")

        calculation_time = (datetime.utcnow() - start_time).total_seconds() * 1000
        
        return CalculationResult(
            kpi_code=params.kpi_code,
            value=value,
            unit=kpi_def.get("unit", "Number"),
            timestamp=datetime.utcnow(),
            calculation_time_ms=calculation_time,
            metadata={
                "calculation_type": "simple",
                "formula": formula,
                "sql_generated": query,
                "variables": parsed_formula.get("variables", [])
            }
        )

    async def validate_params(self, params: CalculationParams) -> bool:
        """Validate calculation parameters."""
        if not params.start_date or not params.end_date:
             raise ValueError("Start date and end date are required for dynamic calculation.")
        return True

    def get_cache_key(self, params: CalculationParams) -> str:
        """Generate cache key."""
        return f"dynamic:{self.value_chain_code}:{self._generate_cache_key_base(params)}"

    def _get_fallback_definition(self, kpi_code: str) -> Dict[str, Any]:
        """Temporary hardcoded definitions for bootstrapping/testing."""
        definitions = {
            "EXAMPLE_RATIO_KPI": {
                "formula": "(numerator_metric / denominator_metric) * 100",
                "unit": "Percentage",
                "target_table": "generic_data.metrics"
            },
            "EXAMPLE_DURATION_KPI": {
                "formula": "avg(end_time - start_time)",
                "unit": "Days",
                "target_table": "generic_data.events"
            }
        }
        return definitions.get(kpi_code)
