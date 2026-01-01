"""
Set-Based Calculation Engine

Provides set operations for complex KPI calculations that require multiple
intermediate sets to produce a final result.

Example: Churn Rate Calculation
- Step 1: Define StartPeriodCustomers (FILTER)
- Step 2: Define EndPeriodCustomers (FILTER)
- Step 3: Define LostCustomers (EXCEPT)
- Step 4: Calculate ChurnRate = (COUNTROWS(LostCustomers) / COUNTROWS(StartPeriodCustomers)) * 100

Supported Operations:
- FILTER: Filter a base set based on conditions
- EXCEPT: Set difference (A - B)
- INTERSECT: Set intersection (A ∩ B)
- UNION: Set union (A ∪ B)
- COUNTROWS: Count rows in a set
- SUMX: Sum a column across a set
- AVERAGEX: Average a column across a set
"""

from typing import Dict, Any, List, Optional, Union
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
import logging

logger = logging.getLogger(__name__)


class SetOperationType(str, Enum):
    """Types of set operations."""
    FILTER = "FILTER"
    EXCEPT = "EXCEPT"
    INTERSECT = "INTERSECT"
    UNION = "UNION"


class AggregationType(str, Enum):
    """Types of aggregation operations on sets."""
    COUNTROWS = "COUNTROWS"
    SUMX = "SUMX"
    AVERAGEX = "AVERAGEX"
    MINX = "MINX"
    MAXX = "MAXX"


class ComparisonOperator(str, Enum):
    """Comparison operators for filter conditions."""
    EQ = "="
    NE = "!="
    LT = "<"
    LE = "<="
    GT = ">"
    GE = ">="
    IS_NULL = "IS NULL"
    IS_NOT_NULL = "IS NOT NULL"
    IN = "IN"
    NOT_IN = "NOT IN"


class LogicalOperator(str, Enum):
    """Logical operators for combining conditions."""
    AND = "AND"
    OR = "OR"


class FilterCondition(BaseModel):
    """A single filter condition."""
    column: str
    operator: ComparisonOperator
    value: Optional[Any] = None  # None for IS NULL / IS NOT NULL
    
    def to_sql(self, param_prefix: str = "p") -> tuple[str, Dict[str, Any]]:
        """Convert condition to SQL fragment with parameters."""
        param_name = f"{param_prefix}_{self.column}"
        
        if self.operator == ComparisonOperator.IS_NULL:
            return f"{self.column} IS NULL", {}
        elif self.operator == ComparisonOperator.IS_NOT_NULL:
            return f"{self.column} IS NOT NULL", {}
        elif self.operator == ComparisonOperator.IN:
            return f"{self.column} = ANY(:{param_name})", {param_name: self.value}
        elif self.operator == ComparisonOperator.NOT_IN:
            return f"{self.column} != ALL(:{param_name})", {param_name: self.value}
        else:
            return f"{self.column} {self.operator.value} :{param_name}", {param_name: self.value}


class FilterGroup(BaseModel):
    """A group of filter conditions combined with a logical operator."""
    conditions: List[Union[FilterCondition, "FilterGroup"]]
    logical_operator: LogicalOperator = LogicalOperator.AND
    
    def to_sql(self, param_prefix: str = "p") -> tuple[str, Dict[str, Any]]:
        """Convert filter group to SQL fragment with parameters."""
        sql_parts = []
        params = {}
        
        for i, condition in enumerate(self.conditions):
            prefix = f"{param_prefix}_{i}"
            sql, cond_params = condition.to_sql(prefix)
            sql_parts.append(f"({sql})")
            params.update(cond_params)
        
        joiner = f" {self.logical_operator.value} "
        return joiner.join(sql_parts), params


# Enable self-reference in FilterGroup
FilterGroup.model_rebuild()


class SetDefinition(BaseModel):
    """
    Defines a named set that can be used in calculations.
    
    A set can be:
    1. A base table/entity with optional filters
    2. The result of a set operation on other sets
    """
    name: str = Field(..., description="Unique name for this set within the calculation")
    description: Optional[str] = None
    
    # For base sets (from a table)
    base_entity: Optional[str] = Field(None, description="Base table/entity name")
    filter_conditions: Optional[FilterGroup] = None
    
    # For derived sets (from set operations)
    operation: Optional[SetOperationType] = None
    source_sets: Optional[List[str]] = Field(None, description="Names of source sets for operations")
    
    # Key column for set operations (e.g., customer_id for customer sets)
    key_column: str = Field(default="id", description="Primary key column for set membership")
    
    def is_base_set(self) -> bool:
        """Check if this is a base set (not derived from operations)."""
        return self.base_entity is not None and self.operation is None


class SetAggregation(BaseModel):
    """
    Defines an aggregation operation on a set.
    """
    name: str = Field(..., description="Name for the aggregation result")
    set_name: str = Field(..., description="Name of the set to aggregate")
    aggregation_type: AggregationType
    column: Optional[str] = Field(None, description="Column to aggregate (for SUMX, AVERAGEX, etc.)")


class CalculationStep(BaseModel):
    """
    A single step in a multi-step calculation.
    
    Can be either:
    1. A set definition
    2. An aggregation
    3. A formula using aggregation results
    """
    step_number: int
    name: str
    description: Optional[str] = None
    
    # One of these should be set
    set_definition: Optional[SetDefinition] = None
    aggregation: Optional[SetAggregation] = None
    formula: Optional[str] = Field(None, description="Formula using previous step results")
    
    # Dependencies on other steps (by name)
    depends_on: List[str] = Field(default_factory=list)


class SetBasedKPIDefinition(BaseModel):
    """
    Complete definition for a set-based KPI calculation.
    
    Example: Churn Rate
    {
        "kpi_code": "CHURN_RATE",
        "name": "Customer Churn Rate",
        "description": "Percentage of customers lost during the period",
        "unit": "Percentage",
        "steps": [
            {
                "step_number": 1,
                "name": "StartPeriodCustomers",
                "set_definition": {
                    "name": "StartPeriodCustomers",
                    "base_entity": "customers",
                    "key_column": "customer_id",
                    "filter_conditions": {
                        "conditions": [
                            {"column": "active_date", "operator": "<=", "value": "@PeriodStart"},
                            {
                                "conditions": [
                                    {"column": "inactive_date", "operator": "IS NULL"},
                                    {"column": "inactive_date", "operator": ">=", "value": "@PeriodStart"}
                                ],
                                "logical_operator": "OR"
                            }
                        ],
                        "logical_operator": "AND"
                    }
                }
            },
            ...
        ],
        "final_formula": "(LostCustomerCount / StartCustomerCount) * 100"
    }
    """
    kpi_code: str
    name: str
    description: Optional[str] = None
    unit: str = "Number"
    
    # Period parameters (injected at runtime)
    period_parameters: List[str] = Field(
        default_factory=lambda: ["PeriodStart", "PeriodEnd"],
        description="Named parameters that will be injected based on the calculation period"
    )
    
    # Calculation steps in order
    steps: List[CalculationStep]
    
    # Final formula combining step results
    final_formula: str = Field(..., description="Formula using step result names as variables")
    
    # Metadata
    metadata: Dict[str, Any] = Field(default_factory=dict)


class SetBasedSQLGenerator:
    """
    Generates SQL for set-based calculations.
    
    Uses CTEs (Common Table Expressions) to build up intermediate sets
    and then combines them for the final calculation.
    """
    
    def __init__(self, schema_name: str = "analytics_data"):
        self.schema_name = schema_name
    
    def generate_sql(
        self,
        kpi_def: SetBasedKPIDefinition,
        period_start: datetime,
        period_end: datetime,
        additional_filters: Optional[Dict[str, Any]] = None
    ) -> tuple[str, Dict[str, Any]]:
        """
        Generate complete SQL for a set-based KPI calculation.
        
        Returns:
            Tuple of (SQL string, parameters dict)
        """
        params = {
            "PeriodStart": period_start,
            "PeriodEnd": period_end
        }
        if additional_filters:
            params.update(additional_filters)
        
        cte_parts = []
        aggregation_selects = []
        
        for step in kpi_def.steps:
            if step.set_definition:
                cte_sql = self._generate_set_cte(step.set_definition, params)
                cte_parts.append(f"{step.name} AS (\n{cte_sql}\n)")
                
            elif step.aggregation:
                agg_sql = self._generate_aggregation_select(step.aggregation)
                aggregation_selects.append(f"{agg_sql} AS {step.name}")
        
        # Build final SQL
        sql_parts = ["WITH"]
        sql_parts.append(",\n".join(cte_parts))
        
        # Final SELECT with aggregations and formula
        final_select = self._generate_final_select(
            kpi_def.final_formula,
            aggregation_selects
        )
        sql_parts.append(final_select)
        
        return "\n".join(sql_parts), params
    
    def _generate_set_cte(
        self,
        set_def: SetDefinition,
        params: Dict[str, Any]
    ) -> str:
        """Generate CTE for a set definition."""
        if set_def.is_base_set():
            return self._generate_base_set_sql(set_def, params)
        else:
            return self._generate_derived_set_sql(set_def)
    
    def _generate_base_set_sql(
        self,
        set_def: SetDefinition,
        params: Dict[str, Any]
    ) -> str:
        """Generate SQL for a base set with filters."""
        table_name = f"{self.schema_name}.{set_def.base_entity}"
        
        sql = f"SELECT {set_def.key_column} FROM {table_name}"
        
        if set_def.filter_conditions:
            where_sql = self._resolve_filter_conditions(
                set_def.filter_conditions,
                params
            )
            sql += f"\nWHERE {where_sql}"
        
        return sql
    
    def _generate_derived_set_sql(self, set_def: SetDefinition) -> str:
        """Generate SQL for a derived set (set operation result)."""
        if not set_def.source_sets or len(set_def.source_sets) < 2:
            raise ValueError(f"Set operation requires at least 2 source sets: {set_def.name}")
        
        set_a = set_def.source_sets[0]
        set_b = set_def.source_sets[1]
        key_col = set_def.key_column
        
        if set_def.operation == SetOperationType.EXCEPT:
            # A EXCEPT B = rows in A but not in B
            return f"""SELECT {key_col} FROM {set_a}
WHERE {key_col} NOT IN (SELECT {key_col} FROM {set_b})"""
        
        elif set_def.operation == SetOperationType.INTERSECT:
            # A INTERSECT B = rows in both A and B
            return f"""SELECT {key_col} FROM {set_a}
WHERE {key_col} IN (SELECT {key_col} FROM {set_b})"""
        
        elif set_def.operation == SetOperationType.UNION:
            # A UNION B = all rows from A and B (deduplicated)
            return f"""SELECT {key_col} FROM {set_a}
UNION
SELECT {key_col} FROM {set_b}"""
        
        else:
            raise ValueError(f"Unsupported set operation: {set_def.operation}")
    
    def _resolve_filter_conditions(
        self,
        filter_group: FilterGroup,
        params: Dict[str, Any]
    ) -> str:
        """Resolve filter conditions, replacing parameter references."""
        sql_parts = []
        
        for condition in filter_group.conditions:
            if isinstance(condition, FilterCondition):
                sql_part = self._resolve_single_condition(condition, params)
                sql_parts.append(f"({sql_part})")
            elif isinstance(condition, FilterGroup):
                nested_sql = self._resolve_filter_conditions(condition, params)
                sql_parts.append(f"({nested_sql})")
        
        joiner = f" {filter_group.logical_operator.value} "
        return joiner.join(sql_parts)
    
    def _resolve_single_condition(
        self,
        condition: FilterCondition,
        params: Dict[str, Any]
    ) -> str:
        """Resolve a single filter condition."""
        if condition.operator == ComparisonOperator.IS_NULL:
            return f"{condition.column} IS NULL"
        elif condition.operator == ComparisonOperator.IS_NOT_NULL:
            return f"{condition.column} IS NOT NULL"
        
        # Resolve value - could be a parameter reference like @PeriodStart
        value = condition.value
        if isinstance(value, str) and value.startswith("@"):
            param_name = value[1:]  # Remove @
            if param_name in params:
                resolved_value = params[param_name]
                if isinstance(resolved_value, datetime):
                    value = f"'{resolved_value.isoformat()}'"
                else:
                    value = f"'{resolved_value}'" if isinstance(resolved_value, str) else resolved_value
            else:
                raise ValueError(f"Unknown parameter reference: {value}")
        elif isinstance(value, str):
            value = f"'{value}'"
        elif isinstance(value, datetime):
            value = f"'{value.isoformat()}'"
        
        return f"{condition.column} {condition.operator.value} {value}"
    
    def _generate_aggregation_select(self, agg: SetAggregation) -> str:
        """Generate SQL for an aggregation."""
        if agg.aggregation_type == AggregationType.COUNTROWS:
            return f"(SELECT COUNT(*) FROM {agg.set_name})"
        elif agg.aggregation_type == AggregationType.SUMX:
            return f"(SELECT SUM({agg.column}) FROM {agg.set_name})"
        elif agg.aggregation_type == AggregationType.AVERAGEX:
            return f"(SELECT AVG({agg.column}) FROM {agg.set_name})"
        elif agg.aggregation_type == AggregationType.MINX:
            return f"(SELECT MIN({agg.column}) FROM {agg.set_name})"
        elif agg.aggregation_type == AggregationType.MAXX:
            return f"(SELECT MAX({agg.column}) FROM {agg.set_name})"
        else:
            raise ValueError(f"Unsupported aggregation type: {agg.aggregation_type}")
    
    def _generate_final_select(
        self,
        formula: str,
        aggregation_selects: List[str]
    ) -> str:
        """Generate the final SELECT statement."""
        # Build subquery for aggregations
        if aggregation_selects:
            agg_sql = ", ".join(aggregation_selects)
            return f"SELECT {formula} AS result FROM (SELECT {agg_sql}) AS aggs"
        else:
            return f"SELECT {formula} AS result"


# Pre-built KPI definitions for common metrics
CHURN_RATE_DEFINITION = SetBasedKPIDefinition(
    kpi_code="CHURN_RATE",
    name="Customer Churn Rate",
    description="Percentage of customers lost during the period. Calculated as (Customers Lost / Customers at Start) * 100",
    unit="Percentage",
    period_parameters=["PeriodStart", "PeriodEnd"],
    steps=[
        # Step 1: Start-of-Period Customer Set
        CalculationStep(
            step_number=1,
            name="StartPeriodCustomers",
            description="All customers active at the start of the period",
            set_definition=SetDefinition(
                name="StartPeriodCustomers",
                base_entity="customers",
                key_column="customer_id",
                filter_conditions=FilterGroup(
                    conditions=[
                        FilterCondition(
                            column="active_date",
                            operator=ComparisonOperator.LE,
                            value="@PeriodStart"
                        ),
                        FilterGroup(
                            conditions=[
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.IS_NULL
                                ),
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.GE,
                                    value="@PeriodStart"
                                )
                            ],
                            logical_operator=LogicalOperator.OR
                        )
                    ],
                    logical_operator=LogicalOperator.AND
                )
            )
        ),
        # Step 2: End-of-Period Customer Set
        CalculationStep(
            step_number=2,
            name="EndPeriodCustomers",
            description="All customers active at the end of the period",
            set_definition=SetDefinition(
                name="EndPeriodCustomers",
                base_entity="customers",
                key_column="customer_id",
                filter_conditions=FilterGroup(
                    conditions=[
                        FilterCondition(
                            column="active_date",
                            operator=ComparisonOperator.LE,
                            value="@PeriodEnd"
                        ),
                        FilterGroup(
                            conditions=[
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.IS_NULL
                                ),
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.GE,
                                    value="@PeriodEnd"
                                )
                            ],
                            logical_operator=LogicalOperator.OR
                        )
                    ],
                    logical_operator=LogicalOperator.AND
                )
            ),
            depends_on=["StartPeriodCustomers"]
        ),
        # Step 3: Lost-During-Period Customer Set (EXCEPT operation)
        CalculationStep(
            step_number=3,
            name="LostDuringPeriodCustomers",
            description="Customers who were active at start but not at end",
            set_definition=SetDefinition(
                name="LostDuringPeriodCustomers",
                operation=SetOperationType.EXCEPT,
                source_sets=["StartPeriodCustomers", "EndPeriodCustomers"],
                key_column="customer_id"
            ),
            depends_on=["StartPeriodCustomers", "EndPeriodCustomers"]
        ),
        # Step 4: Count Start Period Customers
        CalculationStep(
            step_number=4,
            name="StartCustomerCount",
            description="Count of customers at period start",
            aggregation=SetAggregation(
                name="StartCustomerCount",
                set_name="StartPeriodCustomers",
                aggregation_type=AggregationType.COUNTROWS
            ),
            depends_on=["StartPeriodCustomers"]
        ),
        # Step 5: Count Lost Customers
        CalculationStep(
            step_number=5,
            name="LostCustomerCount",
            description="Count of customers lost during period",
            aggregation=SetAggregation(
                name="LostCustomerCount",
                set_name="LostDuringPeriodCustomers",
                aggregation_type=AggregationType.COUNTROWS
            ),
            depends_on=["LostDuringPeriodCustomers"]
        )
    ],
    final_formula="CASE WHEN StartCustomerCount > 0 THEN (LostCustomerCount::float / StartCustomerCount::float) * 100 ELSE 0 END",
    metadata={
        "category": "Customer Retention",
        "business_impact": "High",
        "recommended_frequency": "monthly"
    }
)


# Additional pre-built definitions
RETENTION_RATE_DEFINITION = SetBasedKPIDefinition(
    kpi_code="RETENTION_RATE",
    name="Customer Retention Rate",
    description="Percentage of customers retained during the period. Calculated as 100 - Churn Rate",
    unit="Percentage",
    period_parameters=["PeriodStart", "PeriodEnd"],
    steps=[
        # Reuse the same set definitions as Churn Rate
        CalculationStep(
            step_number=1,
            name="StartPeriodCustomers",
            description="All customers active at the start of the period",
            set_definition=SetDefinition(
                name="StartPeriodCustomers",
                base_entity="customers",
                key_column="customer_id",
                filter_conditions=FilterGroup(
                    conditions=[
                        FilterCondition(
                            column="active_date",
                            operator=ComparisonOperator.LE,
                            value="@PeriodStart"
                        ),
                        FilterGroup(
                            conditions=[
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.IS_NULL
                                ),
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.GE,
                                    value="@PeriodStart"
                                )
                            ],
                            logical_operator=LogicalOperator.OR
                        )
                    ],
                    logical_operator=LogicalOperator.AND
                )
            )
        ),
        CalculationStep(
            step_number=2,
            name="EndPeriodCustomers",
            description="All customers active at the end of the period",
            set_definition=SetDefinition(
                name="EndPeriodCustomers",
                base_entity="customers",
                key_column="customer_id",
                filter_conditions=FilterGroup(
                    conditions=[
                        FilterCondition(
                            column="active_date",
                            operator=ComparisonOperator.LE,
                            value="@PeriodEnd"
                        ),
                        FilterGroup(
                            conditions=[
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.IS_NULL
                                ),
                                FilterCondition(
                                    column="inactive_date",
                                    operator=ComparisonOperator.GE,
                                    value="@PeriodEnd"
                                )
                            ],
                            logical_operator=LogicalOperator.OR
                        )
                    ],
                    logical_operator=LogicalOperator.AND
                )
            ),
            depends_on=["StartPeriodCustomers"]
        ),
        # Retained = INTERSECT (customers in both start and end)
        CalculationStep(
            step_number=3,
            name="RetainedCustomers",
            description="Customers who were active at both start and end",
            set_definition=SetDefinition(
                name="RetainedCustomers",
                operation=SetOperationType.INTERSECT,
                source_sets=["StartPeriodCustomers", "EndPeriodCustomers"],
                key_column="customer_id"
            ),
            depends_on=["StartPeriodCustomers", "EndPeriodCustomers"]
        ),
        CalculationStep(
            step_number=4,
            name="StartCustomerCount",
            aggregation=SetAggregation(
                name="StartCustomerCount",
                set_name="StartPeriodCustomers",
                aggregation_type=AggregationType.COUNTROWS
            ),
            depends_on=["StartPeriodCustomers"]
        ),
        CalculationStep(
            step_number=5,
            name="RetainedCustomerCount",
            aggregation=SetAggregation(
                name="RetainedCustomerCount",
                set_name="RetainedCustomers",
                aggregation_type=AggregationType.COUNTROWS
            ),
            depends_on=["RetainedCustomers"]
        )
    ],
    final_formula="CASE WHEN StartCustomerCount > 0 THEN (RetainedCustomerCount::float / StartCustomerCount::float) * 100 ELSE 0 END",
    metadata={
        "category": "Customer Retention",
        "business_impact": "High",
        "recommended_frequency": "monthly"
    }
)


# Registry of pre-built set-based KPI definitions
SET_BASED_KPI_REGISTRY: Dict[str, SetBasedKPIDefinition] = {
    "CHURN_RATE": CHURN_RATE_DEFINITION,
    "RETENTION_RATE": RETENTION_RATE_DEFINITION,
}


def get_set_based_kpi_definition(kpi_code: str) -> Optional[SetBasedKPIDefinition]:
    """Get a pre-built set-based KPI definition by code."""
    return SET_BASED_KPI_REGISTRY.get(kpi_code.upper())


def register_set_based_kpi(definition: SetBasedKPIDefinition):
    """Register a new set-based KPI definition."""
    SET_BASED_KPI_REGISTRY[definition.kpi_code.upper()] = definition
