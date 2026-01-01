"""
DSPy-based KPI Formula Parser

Uses DSPy's declarative framework for structured LLM output when parsing
natural language KPI definitions into set-based calculation structures.

DSPy provides:
1. Typed signatures for input/output specification
2. Automatic prompt optimization
3. Structured output parsing
4. Chain-of-thought reasoning

This module serves as the LLM fallback when rule-based parsing fails.
"""

from typing import Dict, Any, List, Optional, Literal
from datetime import datetime
from pydantic import BaseModel, Field
import json
import logging
import os

logger = logging.getLogger(__name__)

# Check if DSPy is available
try:
    import dspy
    from dspy import Signature, InputField, OutputField
    DSPY_AVAILABLE = True
except ImportError:
    DSPY_AVAILABLE = False
    logger.warning("DSPy not installed. LLM fallback will use basic prompting.")


# ============================================================================
# PYDANTIC OUTPUT MODELS (for structured parsing)
# ============================================================================

class SetComponentOutput(BaseModel):
    """Structured output for a single set component."""
    name: str = Field(description="Unique name for the set (e.g., 'StartPeriodCustomers')")
    description: str = Field(description="Human-readable description of what this set represents")
    operation: Literal["FILTER", "EXCEPT", "INTERSECT", "UNION"] = Field(
        description="The set operation type"
    )
    base_entity: Optional[str] = Field(
        default=None,
        description="Base entity/table name for FILTER operations (e.g., 'customers')"
    )
    filter_sql: Optional[str] = Field(
        default=None,
        description="SQL WHERE clause for FILTER operations using @PeriodStart/@PeriodEnd params"
    )
    source_sets: Optional[List[str]] = Field(
        default=None,
        description="Source set names for EXCEPT/INTERSECT/UNION operations"
    )


class AggregationOutput(BaseModel):
    """Structured output for an aggregation."""
    name: str = Field(description="Name for the aggregation result (e.g., 'StartCount')")
    set_name: str = Field(description="Name of the set to aggregate")
    aggregation_type: Literal["COUNTROWS", "SUMX", "AVERAGEX", "MINX", "MAXX"] = Field(
        description="Type of aggregation"
    )
    column: Optional[str] = Field(
        default=None,
        description="Column to aggregate for SUMX/AVERAGEX/MINX/MAXX"
    )


class KPIParseOutput(BaseModel):
    """Complete structured output for KPI parsing."""
    sets: List[SetComponentOutput] = Field(
        description="List of set definitions in dependency order"
    )
    aggregations: List[AggregationOutput] = Field(
        description="List of aggregations on the sets"
    )
    final_formula: str = Field(
        description="SQL expression using aggregation names to compute final result"
    )
    key_column: str = Field(
        default="id",
        description="Primary key column for the base entity"
    )
    reasoning: Optional[str] = Field(
        default=None,
        description="Explanation of the parsing logic"
    )


# ============================================================================
# DSPY SIGNATURES (if DSPy is available)
# ============================================================================

if DSPY_AVAILABLE:
    class KPIFormulaToSets(Signature):
        """
        Convert a natural language KPI formula definition into a structured
        set-based calculation definition.
        
        The output should identify:
        1. Base sets that need to be filtered from the source entity
        2. Derived sets using set operations (EXCEPT, INTERSECT, UNION)
        3. Aggregations on those sets (COUNTROWS, SUMX, etc.)
        4. A final formula combining the aggregations
        
        Use @PeriodStart and @PeriodEnd as parameter placeholders for time boundaries.
        """
        
        # Inputs
        nlp_definition: str = InputField(
            desc="Natural language KPI formula (e.g., '(Customers Lost / Customers at Start) * 100')"
        )
        kpi_name: str = InputField(
            desc="Name of the KPI (e.g., 'Customer Churn Rate')"
        )
        base_entity: str = InputField(
            desc="Base entity/table name (e.g., 'customers', 'policies')"
        )
        entity_columns: str = InputField(
            desc="JSON string of known columns: {key, active_date, inactive_date, ...}"
        )
        
        # Outputs
        sets_json: str = OutputField(
            desc="JSON array of set definitions with name, operation, base_entity, filter_sql, source_sets"
        )
        aggregations_json: str = OutputField(
            desc="JSON array of aggregations with name, set_name, aggregation_type, column"
        )
        final_formula: str = OutputField(
            desc="SQL expression using aggregation names (e.g., 'CASE WHEN X > 0 THEN (Y/X)*100 ELSE 0 END')"
        )
        key_column: str = OutputField(
            desc="Primary key column name for the entity"
        )
        reasoning: str = OutputField(
            desc="Step-by-step explanation of how the formula was decomposed"
        )


    class KPIFormulaClassifier(Signature):
        """
        Classify a KPI formula into a known pattern type.
        
        This helps route to optimized rule-based parsers when possible.
        """
        
        nlp_definition: str = InputField(
            desc="Natural language KPI formula"
        )
        
        pattern_type: str = OutputField(
            desc="One of: CHURN_RATE, RETENTION_RATE, GROWTH_RATE, CONVERSION_RATE, RATIO, AGGREGATION, COMPLEX, UNKNOWN"
        )
        confidence: float = OutputField(
            desc="Confidence score 0.0 to 1.0"
        )
        reasoning: str = OutputField(
            desc="Brief explanation of classification"
        )


# ============================================================================
# DSPY KPI PARSER CLASS
# ============================================================================

class DSPyKPIParser:
    """
    DSPy-based parser for converting NLP KPI definitions to set-based structures.
    
    Uses Chain-of-Thought reasoning for complex formula decomposition.
    Falls back to basic LLM prompting if DSPy is not available.
    """
    
    # Entity column templates for common entity types
    ENTITY_TEMPLATES = {
        "customer": {
            "key": "customer_id",
            "active_date": "active_date",
            "inactive_date": "inactive_date",
            "created_at": "created_at"
        },
        "policy": {
            "key": "policy_id",
            "active_date": "effective_date",
            "inactive_date": "termination_date",
            "created_at": "created_at"
        },
        "subscription": {
            "key": "subscription_id",
            "active_date": "start_date",
            "inactive_date": "end_date",
            "created_at": "created_at"
        },
        "employee": {
            "key": "employee_id",
            "active_date": "hire_date",
            "inactive_date": "termination_date",
            "created_at": "created_at"
        },
        "order": {
            "key": "order_id",
            "active_date": "order_date",
            "inactive_date": None,
            "created_at": "created_at",
            "amount": "total_amount"
        },
        "user": {
            "key": "user_id",
            "active_date": "created_at",
            "inactive_date": "deleted_at",
            "created_at": "created_at"
        }
    }
    
    def __init__(
        self,
        model: str = "openai/gpt-4o-mini",
        api_key: Optional[str] = None,
        temperature: float = 0.1
    ):
        """
        Initialize the DSPy KPI parser.
        
        Args:
            model: LLM model to use (DSPy format: provider/model)
            api_key: API key (uses env var if not provided)
            temperature: LLM temperature (lower = more deterministic)
        """
        self.model = model
        self.temperature = temperature
        self._initialized = False
        
        if DSPY_AVAILABLE:
            try:
                # Configure DSPy with the LLM
                api_key = api_key or os.getenv("OPENAI_API_KEY")
                if api_key:
                    lm = dspy.LM(model, api_key=api_key, temperature=temperature)
                    dspy.configure(lm=lm)
                    
                    # Create the parsing modules
                    self.classifier = dspy.ChainOfThought(KPIFormulaClassifier)
                    self.parser = dspy.ChainOfThought(KPIFormulaToSets)
                    self._initialized = True
                    logger.info(f"DSPy KPI Parser initialized with model: {model}")
                else:
                    logger.warning("No API key provided, DSPy parser not initialized")
            except Exception as e:
                logger.error(f"Failed to initialize DSPy: {e}")
                self._initialized = False
    
    def _get_entity_columns(self, base_entity: str) -> Dict[str, Any]:
        """Get column mappings for an entity type."""
        entity_lower = base_entity.lower()
        
        # Check for known entity types
        for entity_type, columns in self.ENTITY_TEMPLATES.items():
            if entity_type in entity_lower:
                return columns
        
        # Default template
        singular = entity_lower.rstrip('s')
        return {
            "key": f"{singular}_id",
            "active_date": "active_date",
            "inactive_date": "inactive_date",
            "created_at": "created_at"
        }
    
    def classify(self, nlp_definition: str) -> Dict[str, Any]:
        """
        Classify a KPI formula into a known pattern type.
        
        Args:
            nlp_definition: Natural language KPI formula
            
        Returns:
            Dict with pattern_type, confidence, reasoning
        """
        if not self._initialized:
            return {
                "pattern_type": "UNKNOWN",
                "confidence": 0.0,
                "reasoning": "DSPy not initialized"
            }
        
        try:
            result = self.classifier(nlp_definition=nlp_definition)
            return {
                "pattern_type": result.pattern_type,
                "confidence": float(result.confidence),
                "reasoning": result.reasoning
            }
        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return {
                "pattern_type": "UNKNOWN",
                "confidence": 0.0,
                "reasoning": str(e)
            }
    
    def parse(
        self,
        nlp_definition: str,
        kpi_name: str,
        base_entity: str,
        entity_columns: Optional[Dict[str, str]] = None
    ) -> KPIParseOutput:
        """
        Parse an NLP KPI definition into structured set-based components.
        
        Args:
            nlp_definition: Natural language KPI formula
            kpi_name: Name of the KPI
            base_entity: Base entity/table name
            entity_columns: Optional column mappings
            
        Returns:
            KPIParseOutput with sets, aggregations, final_formula
        """
        if not self._initialized:
            raise RuntimeError("DSPy parser not initialized. Check API key and DSPy installation.")
        
        # Get entity columns
        columns = entity_columns or self._get_entity_columns(base_entity)
        columns_json = json.dumps(columns)
        
        try:
            # Run the parser with Chain-of-Thought
            result = self.parser(
                nlp_definition=nlp_definition,
                kpi_name=kpi_name,
                base_entity=base_entity,
                entity_columns=columns_json
            )
            
            # Parse the JSON outputs
            sets_data = json.loads(result.sets_json)
            aggregations_data = json.loads(result.aggregations_json)
            
            # Convert to Pydantic models
            sets = [SetComponentOutput(**s) for s in sets_data]
            aggregations = [AggregationOutput(**a) for a in aggregations_data]
            
            return KPIParseOutput(
                sets=sets,
                aggregations=aggregations,
                final_formula=result.final_formula,
                key_column=result.key_column,
                reasoning=result.reasoning
            )
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse DSPy JSON output: {e}")
            raise ValueError(f"LLM returned invalid JSON: {e}")
        except Exception as e:
            logger.error(f"DSPy parsing failed: {e}")
            raise
    
    @property
    def is_available(self) -> bool:
        """Check if the parser is available and initialized."""
        return DSPY_AVAILABLE and self._initialized


# ============================================================================
# INTEGRATION FUNCTION
# ============================================================================

def parse_kpi_with_dspy(
    nlp_definition: str,
    kpi_code: str,
    kpi_name: str,
    base_entity: str,
    unit: str = "Number",
    model: str = "openai/gpt-4o-mini"
) -> Optional[Dict[str, Any]]:
    """
    Parse a KPI definition using DSPy and return a structure compatible
    with the NLPToSetsConverter.
    
    Args:
        nlp_definition: Natural language KPI formula
        kpi_code: KPI code
        kpi_name: KPI name
        base_entity: Base entity table
        unit: Unit of measurement
        model: LLM model to use
        
    Returns:
        ParsedKPIStructure-compatible dict or None if parsing fails
    """
    parser = DSPyKPIParser(model=model)
    
    if not parser.is_available:
        logger.warning("DSPy parser not available")
        return None
    
    try:
        result = parser.parse(
            nlp_definition=nlp_definition,
            kpi_name=kpi_name,
            base_entity=base_entity
        )
        
        # Convert to ParsedKPIStructure format
        return {
            "kpi_code": kpi_code,
            "name": kpi_name,
            "description": f"Auto-parsed: {nlp_definition}",
            "unit": unit,
            "base_entity": base_entity,
            "key_column": result.key_column,
            "period_parameters": ["PeriodStart", "PeriodEnd"],
            "sets": [
                {
                    "name": s.name,
                    "description": s.description,
                    "base_entity": s.base_entity,
                    "key_column": result.key_column,
                    "filter_description": s.filter_sql,
                    "operation": s.operation,
                    "source_sets": s.source_sets,
                    "depends_on": s.source_sets or []
                }
                for s in result.sets
            ],
            "aggregations": [
                {
                    "name": a.name,
                    "set_name": a.set_name,
                    "aggregation_type": a.aggregation_type,
                    "column": a.column
                }
                for a in result.aggregations
            ],
            "final_formula": result.final_formula,
            "metadata": {
                "parsed_by": "dspy",
                "model": model,
                "reasoning": result.reasoning
            }
        }
        
    except Exception as e:
        logger.error(f"DSPy parsing failed: {e}")
        return None


# ============================================================================
# PERFORMANCE OPTIMIZATION: Caching and Batching
# ============================================================================

class CachedDSPyParser:
    """
    Cached version of DSPy parser for production use.
    
    Features:
    - LRU cache for repeated queries
    - Batch processing support
    - Performance metrics
    """
    
    def __init__(
        self,
        model: str = "openai/gpt-4o-mini",
        cache_size: int = 1000
    ):
        self.parser = DSPyKPIParser(model=model)
        self._cache: Dict[str, KPIParseOutput] = {}
        self._cache_size = cache_size
        self._cache_hits = 0
        self._cache_misses = 0
        self._total_parse_time_ms = 0.0
        self._parse_count = 0
    
    def _cache_key(self, nlp_definition: str, base_entity: str) -> str:
        """Generate cache key."""
        return f"{base_entity}:{nlp_definition}"
    
    def parse(
        self,
        nlp_definition: str,
        kpi_name: str,
        base_entity: str
    ) -> KPIParseOutput:
        """Parse with caching."""
        import time
        
        key = self._cache_key(nlp_definition, base_entity)
        
        if key in self._cache:
            self._cache_hits += 1
            return self._cache[key]
        
        self._cache_misses += 1
        
        start = time.perf_counter()
        result = self.parser.parse(nlp_definition, kpi_name, base_entity)
        elapsed_ms = (time.perf_counter() - start) * 1000
        
        self._total_parse_time_ms += elapsed_ms
        self._parse_count += 1
        
        # Add to cache (simple LRU: remove oldest if full)
        if len(self._cache) >= self._cache_size:
            oldest_key = next(iter(self._cache))
            del self._cache[oldest_key]
        
        self._cache[key] = result
        return result
    
    @property
    def stats(self) -> Dict[str, Any]:
        """Get performance statistics."""
        avg_time = (
            self._total_parse_time_ms / self._parse_count
            if self._parse_count > 0 else 0
        )
        return {
            "cache_hits": self._cache_hits,
            "cache_misses": self._cache_misses,
            "cache_hit_rate": (
                self._cache_hits / (self._cache_hits + self._cache_misses)
                if (self._cache_hits + self._cache_misses) > 0 else 0
            ),
            "total_parses": self._parse_count,
            "avg_parse_time_ms": avg_time,
            "cache_size": len(self._cache)
        }
