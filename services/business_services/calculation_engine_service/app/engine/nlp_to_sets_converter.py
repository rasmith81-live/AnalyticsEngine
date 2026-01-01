"""
NLP to Set-Based Definition Converter

Converts natural language KPI definitions into structured set-based calculation
definitions that the calculation engine can execute.

Example Input (NLP Definition):
    "Churn Rate = (Number of Customers Lost During Period / Number of Customers at Start of Period) * 100"

Example Output:
    SetBasedKPIDefinition with steps for:
    - StartPeriodCustomers (FILTER)
    - EndPeriodCustomers (FILTER)
    - LostDuringPeriodCustomers (EXCEPT)
    - Aggregations (COUNTROWS)
    - Final formula
"""

from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pydantic import BaseModel, Field
import json
import re
import logging
import httpx

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
    register_set_based_kpi,
)

logger = logging.getLogger(__name__)


class ParsedSetComponent(BaseModel):
    """Intermediate representation of a parsed set from NLP."""
    name: str
    description: str
    base_entity: Optional[str] = None
    key_column: str = "id"
    filter_description: Optional[str] = None
    operation: Optional[str] = None  # FILTER, EXCEPT, INTERSECT, UNION
    source_sets: Optional[List[str]] = None
    depends_on: List[str] = Field(default_factory=list)


class ParsedAggregation(BaseModel):
    """Intermediate representation of a parsed aggregation."""
    name: str
    set_name: str
    aggregation_type: str  # COUNTROWS, SUMX, AVERAGEX
    column: Optional[str] = None


class ParsedKPIStructure(BaseModel):
    """Complete parsed structure from NLP definition."""
    kpi_code: str
    name: str
    description: str
    unit: str = "Number"
    base_entity: str
    key_column: str = "id"
    period_parameters: List[str] = Field(default_factory=lambda: ["PeriodStart", "PeriodEnd"])
    sets: List[ParsedSetComponent]
    aggregations: List[ParsedAggregation]
    final_formula: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


class NLPToSetsConverter:
    """
    Converts natural language KPI definitions to set-based calculation definitions.
    
    Uses LLM to parse the NLP definition and extract:
    1. Required sets and their filter conditions
    2. Set operations (EXCEPT, INTERSECT, UNION)
    3. Aggregations (COUNTROWS, SUMX, etc.)
    4. Final formula
    
    Can also use rule-based parsing for common patterns.
    """
    
    # Common KPI patterns that can be parsed without LLM
    COMMON_PATTERNS = {
        "churn_rate": {
            "pattern": r"(customers?\s+lost|churned?\s+customers?).*(customers?\s+at\s+start|starting\s+customers?)",
            "template": "churn_rate"
        },
        "retention_rate": {
            "pattern": r"(customers?\s+retained|retained\s+customers?).*(customers?\s+at\s+start|starting\s+customers?)",
            "template": "retention_rate"
        },
        "growth_rate": {
            "pattern": r"(new\s+customers?|customers?\s+gained).*(customers?\s+at\s+start|starting\s+customers?)",
            "template": "growth_rate"
        },
        "conversion_rate": {
            "pattern": r"(converted|conversions?).*(total|all)\s+(leads?|visitors?|prospects?)",
            "template": "conversion_rate"
        }
    }
    
    # Entity column mappings for common entities
    ENTITY_COLUMN_MAPPINGS = {
        "customer": {"key": "customer_id", "active_date": "active_date", "inactive_date": "inactive_date"},
        "policy": {"key": "policy_id", "active_date": "effective_date", "inactive_date": "termination_date"},
        "subscription": {"key": "subscription_id", "active_date": "start_date", "inactive_date": "end_date"},
        "employee": {"key": "employee_id", "active_date": "hire_date", "inactive_date": "termination_date"},
        "member": {"key": "member_id", "active_date": "join_date", "inactive_date": "leave_date"},
        "account": {"key": "account_id", "active_date": "opened_date", "inactive_date": "closed_date"},
        "contract": {"key": "contract_id", "active_date": "start_date", "inactive_date": "end_date"},
        "user": {"key": "user_id", "active_date": "created_at", "inactive_date": "deleted_at"},
    }
    
    def __init__(
        self,
        llm_service_url: Optional[str] = None,
        use_llm: bool = True
    ):
        """
        Initialize the converter.
        
        Args:
            llm_service_url: URL for LLM service (conversation service)
            use_llm: Whether to use LLM for parsing (falls back to rules if False)
        """
        self.llm_service_url = llm_service_url
        self.use_llm = use_llm and llm_service_url is not None
        self._http_client: Optional[httpx.AsyncClient] = None
    
    async def _get_http_client(self) -> httpx.AsyncClient:
        """Get or create HTTP client."""
        if self._http_client is None:
            self._http_client = httpx.AsyncClient(timeout=60.0)
        return self._http_client
    
    async def convert(
        self,
        nlp_definition: str,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        unit: str = "Number",
        metadata: Optional[Dict[str, Any]] = None
    ) -> SetBasedKPIDefinition:
        """
        Convert an NLP KPI definition to a SetBasedKPIDefinition.
        
        Args:
            nlp_definition: Natural language definition of the KPI
                Example: "(Number of Customers Lost During Period / Number of Customers at Start of Period) * 100"
            kpi_code: Code for the KPI (e.g., "CHURN_RATE")
            kpi_name: Human-readable name (e.g., "Customer Churn Rate")
            base_entity: The primary entity (e.g., "customers", "policies")
            unit: Unit of measurement (e.g., "Percentage", "Count")
            metadata: Additional metadata
            
        Returns:
            SetBasedKPIDefinition ready for the calculation engine
        """
        # First try rule-based parsing for common patterns
        parsed = self._try_rule_based_parsing(nlp_definition, kpi_code, kpi_name, base_entity, unit)
        
        if parsed:
            return self._build_definition_from_parsed(parsed, metadata)
        
        # Fall back to LLM parsing
        if self.use_llm:
            parsed = await self._llm_parse(nlp_definition, kpi_code, kpi_name, base_entity, unit)
            if parsed:
                return self._build_definition_from_parsed(parsed, metadata)
        
        # If all else fails, try to build a basic structure
        raise ValueError(f"Could not parse NLP definition: {nlp_definition}")
    
    def _try_rule_based_parsing(
        self,
        nlp_definition: str,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        unit: str
    ) -> Optional[ParsedKPIStructure]:
        """
        Try to parse using rule-based patterns for common KPIs.
        """
        nlp_lower = nlp_definition.lower()
        
        # Detect entity and get column mappings
        entity_key = self._detect_entity(base_entity)
        columns = self.ENTITY_COLUMN_MAPPINGS.get(entity_key, {
            "key": f"{entity_key}_id",
            "active_date": "active_date",
            "inactive_date": "inactive_date"
        })
        
        # Check for churn rate pattern
        if self._matches_churn_pattern(nlp_lower):
            return self._build_churn_structure(kpi_code, kpi_name, base_entity, columns, unit)
        
        # Check for retention rate pattern
        if self._matches_retention_pattern(nlp_lower):
            return self._build_retention_structure(kpi_code, kpi_name, base_entity, columns, unit)
        
        # Check for growth rate pattern
        if self._matches_growth_pattern(nlp_lower):
            return self._build_growth_structure(kpi_code, kpi_name, base_entity, columns, unit)
        
        # Check for generic ratio pattern
        ratio_match = self._parse_ratio_pattern(nlp_definition)
        if ratio_match:
            return self._build_ratio_structure(kpi_code, kpi_name, base_entity, columns, unit, ratio_match)
        
        return None
    
    def _detect_entity(self, base_entity: str) -> str:
        """Detect the entity type from the base entity name."""
        entity_lower = base_entity.lower()
        
        # Check for known entity types
        for entity_type in self.ENTITY_COLUMN_MAPPINGS.keys():
            if entity_type in entity_lower:
                return entity_type
        
        # Default to singular form
        if entity_lower.endswith('s'):
            return entity_lower[:-1]
        return entity_lower
    
    def _matches_churn_pattern(self, text: str) -> bool:
        """Check if text matches churn rate pattern."""
        churn_indicators = ["churn", "lost", "cancelled", "terminated", "left", "departed"]
        period_indicators = ["during period", "in period", "over period", "within period"]
        start_indicators = ["at start", "beginning", "initial", "starting"]
        
        has_churn = any(ind in text for ind in churn_indicators)
        has_period = any(ind in text for ind in period_indicators) or "lost during" in text
        has_start = any(ind in text for ind in start_indicators)
        
        return has_churn and (has_period or has_start)
    
    def _matches_retention_pattern(self, text: str) -> bool:
        """Check if text matches retention rate pattern."""
        retention_indicators = ["retain", "kept", "stayed", "remained", "continuing"]
        return any(ind in text for ind in retention_indicators)
    
    def _matches_growth_pattern(self, text: str) -> bool:
        """Check if text matches growth rate pattern."""
        growth_indicators = ["growth", "new", "acquired", "gained", "added"]
        return any(ind in text for ind in growth_indicators) and "rate" in text
    
    def _parse_ratio_pattern(self, text: str) -> Optional[Dict[str, str]]:
        """Parse a generic ratio pattern like (A / B) * 100."""
        # Match patterns like "(X / Y) * 100" or "X divided by Y"
        ratio_pattern = r'\(?\s*([^/]+)\s*/\s*([^)]+)\s*\)?\s*\*?\s*(\d+)?'
        match = re.search(ratio_pattern, text, re.IGNORECASE)
        
        if match:
            return {
                "numerator": match.group(1).strip(),
                "denominator": match.group(2).strip(),
                "multiplier": match.group(3) or "1"
            }
        return None
    
    def _build_churn_structure(
        self,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        columns: Dict[str, str],
        unit: str
    ) -> ParsedKPIStructure:
        """Build structure for churn rate KPI."""
        key_col = columns["key"]
        active_col = columns["active_date"]
        inactive_col = columns["inactive_date"]
        
        return ParsedKPIStructure(
            kpi_code=kpi_code,
            name=kpi_name,
            description=f"Percentage of {base_entity} lost during the period",
            unit=unit,
            base_entity=base_entity,
            key_column=key_col,
            sets=[
                ParsedSetComponent(
                    name="StartPeriodSet",
                    description=f"All {base_entity} active at the start of the period",
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description=f"{active_col} <= @PeriodStart AND ({inactive_col} IS NULL OR {inactive_col} >= @PeriodStart)",
                    operation="FILTER"
                ),
                ParsedSetComponent(
                    name="EndPeriodSet",
                    description=f"All {base_entity} active at the end of the period",
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description=f"{active_col} <= @PeriodEnd AND ({inactive_col} IS NULL OR {inactive_col} >= @PeriodEnd)",
                    operation="FILTER",
                    depends_on=["StartPeriodSet"]
                ),
                ParsedSetComponent(
                    name="LostDuringPeriodSet",
                    description=f"{base_entity} who were active at start but not at end",
                    key_column=key_col,
                    operation="EXCEPT",
                    source_sets=["StartPeriodSet", "EndPeriodSet"],
                    depends_on=["StartPeriodSet", "EndPeriodSet"]
                )
            ],
            aggregations=[
                ParsedAggregation(
                    name="StartCount",
                    set_name="StartPeriodSet",
                    aggregation_type="COUNTROWS"
                ),
                ParsedAggregation(
                    name="LostCount",
                    set_name="LostDuringPeriodSet",
                    aggregation_type="COUNTROWS"
                )
            ],
            final_formula="CASE WHEN StartCount > 0 THEN (LostCount::float / StartCount::float) * 100 ELSE 0 END"
        )
    
    def _build_retention_structure(
        self,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        columns: Dict[str, str],
        unit: str
    ) -> ParsedKPIStructure:
        """Build structure for retention rate KPI."""
        key_col = columns["key"]
        active_col = columns["active_date"]
        inactive_col = columns["inactive_date"]
        
        return ParsedKPIStructure(
            kpi_code=kpi_code,
            name=kpi_name,
            description=f"Percentage of {base_entity} retained during the period",
            unit=unit,
            base_entity=base_entity,
            key_column=key_col,
            sets=[
                ParsedSetComponent(
                    name="StartPeriodSet",
                    description=f"All {base_entity} active at the start of the period",
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description=f"{active_col} <= @PeriodStart AND ({inactive_col} IS NULL OR {inactive_col} >= @PeriodStart)",
                    operation="FILTER"
                ),
                ParsedSetComponent(
                    name="EndPeriodSet",
                    description=f"All {base_entity} active at the end of the period",
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description=f"{active_col} <= @PeriodEnd AND ({inactive_col} IS NULL OR {inactive_col} >= @PeriodEnd)",
                    operation="FILTER",
                    depends_on=["StartPeriodSet"]
                ),
                ParsedSetComponent(
                    name="RetainedSet",
                    description=f"{base_entity} who were active at both start and end",
                    key_column=key_col,
                    operation="INTERSECT",
                    source_sets=["StartPeriodSet", "EndPeriodSet"],
                    depends_on=["StartPeriodSet", "EndPeriodSet"]
                )
            ],
            aggregations=[
                ParsedAggregation(
                    name="StartCount",
                    set_name="StartPeriodSet",
                    aggregation_type="COUNTROWS"
                ),
                ParsedAggregation(
                    name="RetainedCount",
                    set_name="RetainedSet",
                    aggregation_type="COUNTROWS"
                )
            ],
            final_formula="CASE WHEN StartCount > 0 THEN (RetainedCount::float / StartCount::float) * 100 ELSE 0 END"
        )
    
    def _build_growth_structure(
        self,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        columns: Dict[str, str],
        unit: str
    ) -> ParsedKPIStructure:
        """Build structure for growth rate KPI."""
        key_col = columns["key"]
        active_col = columns["active_date"]
        inactive_col = columns["inactive_date"]
        
        return ParsedKPIStructure(
            kpi_code=kpi_code,
            name=kpi_name,
            description=f"Percentage growth in {base_entity} during the period",
            unit=unit,
            base_entity=base_entity,
            key_column=key_col,
            sets=[
                ParsedSetComponent(
                    name="StartPeriodSet",
                    description=f"All {base_entity} active at the start of the period",
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description=f"{active_col} <= @PeriodStart AND ({inactive_col} IS NULL OR {inactive_col} >= @PeriodStart)",
                    operation="FILTER"
                ),
                ParsedSetComponent(
                    name="NewDuringPeriodSet",
                    description=f"New {base_entity} acquired during the period",
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description=f"{active_col} > @PeriodStart AND {active_col} <= @PeriodEnd",
                    operation="FILTER",
                    depends_on=["StartPeriodSet"]
                )
            ],
            aggregations=[
                ParsedAggregation(
                    name="StartCount",
                    set_name="StartPeriodSet",
                    aggregation_type="COUNTROWS"
                ),
                ParsedAggregation(
                    name="NewCount",
                    set_name="NewDuringPeriodSet",
                    aggregation_type="COUNTROWS"
                )
            ],
            final_formula="CASE WHEN StartCount > 0 THEN (NewCount::float / StartCount::float) * 100 ELSE 0 END"
        )
    
    def _build_ratio_structure(
        self,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        columns: Dict[str, str],
        unit: str,
        ratio_match: Dict[str, str]
    ) -> ParsedKPIStructure:
        """Build structure for a generic ratio KPI."""
        key_col = columns["key"]
        multiplier = ratio_match.get("multiplier", "1")
        
        return ParsedKPIStructure(
            kpi_code=kpi_code,
            name=kpi_name,
            description=f"Ratio calculation for {base_entity}",
            unit=unit,
            base_entity=base_entity,
            key_column=key_col,
            sets=[
                ParsedSetComponent(
                    name="NumeratorSet",
                    description=ratio_match["numerator"],
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description="/* Requires manual filter definition */",
                    operation="FILTER"
                ),
                ParsedSetComponent(
                    name="DenominatorSet",
                    description=ratio_match["denominator"],
                    base_entity=base_entity,
                    key_column=key_col,
                    filter_description="/* Requires manual filter definition */",
                    operation="FILTER"
                )
            ],
            aggregations=[
                ParsedAggregation(
                    name="NumeratorCount",
                    set_name="NumeratorSet",
                    aggregation_type="COUNTROWS"
                ),
                ParsedAggregation(
                    name="DenominatorCount",
                    set_name="DenominatorSet",
                    aggregation_type="COUNTROWS"
                )
            ],
            final_formula=f"CASE WHEN DenominatorCount > 0 THEN (NumeratorCount::float / DenominatorCount::float) * {multiplier} ELSE 0 END"
        )
    
    async def _llm_parse(
        self,
        nlp_definition: str,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        unit: str
    ) -> Optional[ParsedKPIStructure]:
        """
        Use LLM to parse the NLP definition into structured components.
        
        Uses DSPy for structured output parsing when available,
        falls back to raw HTTP prompting otherwise.
        """
        # Try DSPy first (preferred - structured output)
        try:
            from .dspy_kpi_parser import parse_kpi_with_dspy
            
            dspy_result = parse_kpi_with_dspy(
                nlp_definition=nlp_definition,
                kpi_code=kpi_code,
                kpi_name=kpi_name,
                base_entity=base_entity,
                unit=unit
            )
            
            if dspy_result:
                logger.info(f"DSPy parsing successful for {kpi_code}")
                return ParsedKPIStructure(**dspy_result)
            else:
                logger.warning("DSPy parsing returned None, falling back to HTTP")
        except ImportError:
            logger.warning("DSPy parser not available, using HTTP fallback")
        except Exception as e:
            logger.warning(f"DSPy parsing failed: {e}, falling back to HTTP")
        
        # Fallback to raw HTTP prompting
        if not self.llm_service_url:
            logger.warning("No LLM service URL configured")
            return None
            
        prompt = self._build_llm_prompt(nlp_definition, kpi_code, kpi_name, base_entity, unit)
        
        try:
            client = await self._get_http_client()
            
            response = await client.post(
                f"{self.llm_service_url}/api/v1/llm/complete",
                json={
                    "messages": [
                        {"role": "system", "content": self._get_system_prompt()},
                        {"role": "user", "content": prompt}
                    ],
                    "json_mode": True,
                    "temperature": 0.1
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result.get("content", "{}")
                parsed_data = json.loads(content)
                return ParsedKPIStructure(**parsed_data)
            else:
                logger.warning(f"LLM request failed: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"LLM parsing failed: {e}")
            return None
    
    def _get_system_prompt(self) -> str:
        """Get the system prompt for LLM parsing."""
        return """You are an expert at converting natural language KPI definitions into structured set-based calculations.

Given a KPI definition, you must identify:
1. The sets needed (with their filter conditions)
2. Set operations (FILTER, EXCEPT, INTERSECT, UNION)
3. Aggregations (COUNTROWS, SUMX, AVERAGEX)
4. The final formula

For temporal KPIs (like churn rate), you must identify:
- Start-of-period sets (entities active at @PeriodStart)
- End-of-period sets (entities active at @PeriodEnd)
- Derived sets (using EXCEPT, INTERSECT, etc.)

Use @PeriodStart and @PeriodEnd as parameter placeholders for period boundaries.

Return a JSON object with this structure:
{
    "kpi_code": "string",
    "name": "string",
    "description": "string",
    "unit": "string",
    "base_entity": "string",
    "key_column": "string",
    "period_parameters": ["PeriodStart", "PeriodEnd"],
    "sets": [
        {
            "name": "string",
            "description": "string",
            "base_entity": "string or null",
            "key_column": "string",
            "filter_description": "SQL-like filter or null",
            "operation": "FILTER|EXCEPT|INTERSECT|UNION",
            "source_sets": ["set_name"] or null,
            "depends_on": ["set_name"]
        }
    ],
    "aggregations": [
        {
            "name": "string",
            "set_name": "string",
            "aggregation_type": "COUNTROWS|SUMX|AVERAGEX",
            "column": "string or null"
        }
    ],
    "final_formula": "SQL expression using aggregation names"
}"""
    
    def _build_llm_prompt(
        self,
        nlp_definition: str,
        kpi_code: str,
        kpi_name: str,
        base_entity: str,
        unit: str
    ) -> str:
        """Build the user prompt for LLM parsing."""
        return f"""Convert this KPI definition to a set-based calculation structure:

KPI Code: {kpi_code}
KPI Name: {kpi_name}
Base Entity: {base_entity}
Unit: {unit}

Natural Language Definition:
{nlp_definition}

Identify all required sets, their filter conditions, any set operations needed, 
aggregations, and the final formula. Use standard column naming conventions 
(e.g., active_date, inactive_date for temporal boundaries)."""
    
    def _build_definition_from_parsed(
        self,
        parsed: ParsedKPIStructure,
        metadata: Optional[Dict[str, Any]] = None
    ) -> SetBasedKPIDefinition:
        """
        Convert ParsedKPIStructure to SetBasedKPIDefinition.
        """
        steps = []
        step_number = 0
        
        # Build set definition steps
        for set_comp in parsed.sets:
            step_number += 1
            
            if set_comp.operation == "FILTER":
                # Build filter conditions from description
                filter_group = self._parse_filter_description(
                    set_comp.filter_description,
                    parsed.key_column
                )
                
                set_def = SetDefinition(
                    name=set_comp.name,
                    description=set_comp.description,
                    base_entity=set_comp.base_entity or parsed.base_entity,
                    key_column=set_comp.key_column or parsed.key_column,
                    filter_conditions=filter_group
                )
            else:
                # Set operation (EXCEPT, INTERSECT, UNION)
                set_def = SetDefinition(
                    name=set_comp.name,
                    description=set_comp.description,
                    operation=SetOperationType(set_comp.operation),
                    source_sets=set_comp.source_sets,
                    key_column=set_comp.key_column or parsed.key_column
                )
            
            steps.append(CalculationStep(
                step_number=step_number,
                name=set_comp.name,
                description=set_comp.description,
                set_definition=set_def,
                depends_on=set_comp.depends_on
            ))
        
        # Build aggregation steps
        for agg in parsed.aggregations:
            step_number += 1
            
            set_agg = SetAggregation(
                name=agg.name,
                set_name=agg.set_name,
                aggregation_type=AggregationType(agg.aggregation_type),
                column=agg.column
            )
            
            steps.append(CalculationStep(
                step_number=step_number,
                name=agg.name,
                description=f"{agg.aggregation_type} of {agg.set_name}",
                aggregation=set_agg,
                depends_on=[agg.set_name]
            ))
        
        return SetBasedKPIDefinition(
            kpi_code=parsed.kpi_code,
            name=parsed.name,
            description=parsed.description,
            unit=parsed.unit,
            period_parameters=parsed.period_parameters,
            steps=steps,
            final_formula=parsed.final_formula,
            metadata=metadata or parsed.metadata
        )
    
    def _parse_filter_description(
        self,
        filter_desc: str,
        key_column: str
    ) -> Optional[FilterGroup]:
        """
        Parse a filter description string into FilterGroup.
        
        Handles patterns like:
        - "active_date <= @PeriodStart AND (inactive_date IS NULL OR inactive_date >= @PeriodStart)"
        """
        if not filter_desc or filter_desc.startswith("/*"):
            return None
        
        conditions = []
        
        # Parse AND conditions at top level
        and_parts = re.split(r'\s+AND\s+', filter_desc, flags=re.IGNORECASE)
        
        for part in and_parts:
            part = part.strip()
            
            # Check for OR group (parenthesized)
            if part.startswith('(') and part.endswith(')'):
                inner = part[1:-1]
                or_conditions = self._parse_or_conditions(inner)
                if or_conditions:
                    conditions.append(FilterGroup(
                        conditions=or_conditions,
                        logical_operator=LogicalOperator.OR
                    ))
            else:
                # Single condition
                cond = self._parse_single_condition(part)
                if cond:
                    conditions.append(cond)
        
        if conditions:
            return FilterGroup(
                conditions=conditions,
                logical_operator=LogicalOperator.AND
            )
        return None
    
    def _parse_or_conditions(self, text: str) -> List[FilterCondition]:
        """Parse OR-separated conditions."""
        conditions = []
        or_parts = re.split(r'\s+OR\s+', text, flags=re.IGNORECASE)
        
        for part in or_parts:
            cond = self._parse_single_condition(part.strip())
            if cond:
                conditions.append(cond)
        
        return conditions
    
    def _parse_single_condition(self, text: str) -> Optional[FilterCondition]:
        """Parse a single condition like 'column >= @Value' or 'column IS NULL'."""
        text = text.strip()
        
        # IS NULL / IS NOT NULL
        is_null_match = re.match(r'(\w+)\s+IS\s+(NOT\s+)?NULL', text, re.IGNORECASE)
        if is_null_match:
            column = is_null_match.group(1)
            is_not = is_null_match.group(2) is not None
            return FilterCondition(
                column=column,
                operator=ComparisonOperator.IS_NOT_NULL if is_not else ComparisonOperator.IS_NULL
            )
        
        # Comparison operators
        comp_match = re.match(r'(\w+)\s*(<=|>=|<>|!=|<|>|=)\s*(.+)', text)
        if comp_match:
            column = comp_match.group(1)
            op_str = comp_match.group(2)
            value = comp_match.group(3).strip()
            
            op_map = {
                '=': ComparisonOperator.EQ,
                '!=': ComparisonOperator.NE,
                '<>': ComparisonOperator.NE,
                '<': ComparisonOperator.LT,
                '<=': ComparisonOperator.LE,
                '>': ComparisonOperator.GT,
                '>=': ComparisonOperator.GE,
            }
            
            return FilterCondition(
                column=column,
                operator=op_map.get(op_str, ComparisonOperator.EQ),
                value=value
            )
        
        return None
    
    async def close(self):
        """Clean up resources."""
        if self._http_client:
            await self._http_client.aclose()
            self._http_client = None


async def convert_nlp_to_set_definition(
    nlp_definition: str,
    kpi_code: str,
    kpi_name: str,
    base_entity: str,
    unit: str = "Number",
    metadata: Optional[Dict[str, Any]] = None,
    llm_service_url: Optional[str] = None,
    register: bool = False
) -> SetBasedKPIDefinition:
    """
    Convenience function to convert an NLP KPI definition to a SetBasedKPIDefinition.
    
    Args:
        nlp_definition: Natural language definition of the KPI
        kpi_code: Code for the KPI
        kpi_name: Human-readable name
        base_entity: The primary entity table
        unit: Unit of measurement
        metadata: Additional metadata
        llm_service_url: Optional URL for LLM service
        register: If True, register the definition in the global registry
        
    Returns:
        SetBasedKPIDefinition
        
    Example:
        definition = await convert_nlp_to_set_definition(
            nlp_definition="(Number of Customers Lost During Period / Number of Customers at Start of Period) * 100",
            kpi_code="CUSTOMER_CHURN_RATE",
            kpi_name="Customer Churn Rate",
            base_entity="customers",
            unit="Percentage"
        )
    """
    converter = NLPToSetsConverter(llm_service_url=llm_service_url)
    
    try:
        definition = await converter.convert(
            nlp_definition=nlp_definition,
            kpi_code=kpi_code,
            kpi_name=kpi_name,
            base_entity=base_entity,
            unit=unit,
            metadata=metadata
        )
        
        if register:
            register_set_based_kpi(definition)
        
        return definition
    finally:
        await converter.close()


def convert_nlp_to_set_definition_sync(
    nlp_definition: str,
    kpi_code: str,
    kpi_name: str,
    base_entity: str,
    unit: str = "Number",
    metadata: Optional[Dict[str, Any]] = None,
    register: bool = False
) -> SetBasedKPIDefinition:
    """
    Synchronous version of convert_nlp_to_set_definition.
    Uses only rule-based parsing (no LLM).
    
    Args:
        nlp_definition: Natural language definition of the KPI
        kpi_code: Code for the KPI
        kpi_name: Human-readable name
        base_entity: The primary entity table
        unit: Unit of measurement
        metadata: Additional metadata
        register: If True, register the definition in the global registry
        
    Returns:
        SetBasedKPIDefinition
    """
    converter = NLPToSetsConverter(use_llm=False)
    
    parsed = converter._try_rule_based_parsing(
        nlp_definition=nlp_definition,
        kpi_code=kpi_code,
        kpi_name=kpi_name,
        base_entity=base_entity,
        unit=unit
    )
    
    if not parsed:
        raise ValueError(f"Could not parse NLP definition using rules: {nlp_definition}")
    
    definition = converter._build_definition_from_parsed(parsed, metadata)
    
    if register:
        register_set_based_kpi(definition)
    
    return definition
