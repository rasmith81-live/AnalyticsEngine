"""
Calculation Engine Core Components

Provides the core calculation engine components including:
- FormulaParser: Parses string-based KPI formulas into ASTs
- SQLGenerator: Compiles ASTs into optimized TimescaleDB SQL queries
- DependencyGraph: Manages dependencies between metrics
- SetBasedSQLGenerator: Generates SQL for set-based calculations
- Set operation models and definitions
"""

from .parser import FormulaParser
from .sql_generator import SQLGenerator
from .dependency_graph import DependencyGraph
from .set_operations import (
    SetOperationType,
    AggregationType,
    ComparisonOperator,
    LogicalOperator,
    FilterCondition,
    FilterGroup,
    SetDefinition,
    SetAggregation,
    CalculationStep,
    SetBasedKPIDefinition,
    SetBasedSQLGenerator,
    CHURN_RATE_DEFINITION,
    RETENTION_RATE_DEFINITION,
    SET_BASED_KPI_REGISTRY,
    get_set_based_kpi_definition,
    register_set_based_kpi,
)
from .nlp_to_sets_converter import (
    NLPToSetsConverter,
    ParsedKPIStructure,
    ParsedSetComponent,
    ParsedAggregation,
    convert_nlp_to_set_definition,
    convert_nlp_to_set_definition_sync,
)
from .dspy_kpi_parser import (
    DSPyKPIParser,
    CachedDSPyParser,
    KPIParseOutput,
    SetComponentOutput,
    AggregationOutput,
    parse_kpi_with_dspy,
    DSPY_AVAILABLE,
)

__all__ = [
    # Core components
    "FormulaParser",
    "SQLGenerator",
    "DependencyGraph",
    # Set-based components
    "SetOperationType",
    "AggregationType",
    "ComparisonOperator",
    # NLP converter
    "NLPToSetsConverter",
    "ParsedKPIStructure",
    "ParsedSetComponent",
    "ParsedAggregation",
    "convert_nlp_to_set_definition",
    "convert_nlp_to_set_definition_sync",
    "LogicalOperator",
    "FilterCondition",
    "FilterGroup",
    "SetDefinition",
    "SetAggregation",
    "CalculationStep",
    "SetBasedKPIDefinition",
    "SetBasedSQLGenerator",
    # Pre-built definitions
    "CHURN_RATE_DEFINITION",
    "RETENTION_RATE_DEFINITION",
    "SET_BASED_KPI_REGISTRY",
    # Functions
    "get_set_based_kpi_definition",
    "register_set_based_kpi",
    # DSPy parser
    "DSPyKPIParser",
    "CachedDSPyParser",
    "KPIParseOutput",
    "SetComponentOutput",
    "AggregationOutput",
    "parse_kpi_with_dspy",
    "DSPY_AVAILABLE",
]
