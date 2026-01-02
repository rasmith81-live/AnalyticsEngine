"""
Set-Based Calculation Handler

Handles complex KPI calculations that require multiple intermediate sets
to produce a final result. Extends the base calculation handler to support
set operations like FILTER, EXCEPT, INTERSECT, and aggregations.

Example Use Case: Churn Rate
- Requires StartPeriodCustomers, EndPeriodCustomers, LostCustomers sets
- Final calculation: (COUNTROWS(LostCustomers) / COUNTROWS(StartPeriodCustomers)) * 100
"""

from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
import asyncio
import json

from ..base_handler import (
    BaseCalculationHandler,
    CalculationParams,
    CalculationResult,
    CalculationError
)
from ..engine.set_operations import (
    SetBasedKPIDefinition,
    SetBasedSQLGenerator,
    get_set_based_kpi_definition,
    SET_BASED_KPI_REGISTRY
)
from ..clients.database_client_pubsub import DatabaseClientPubSub
from ..clients.metadata_client_pubsub import MetadataClientPubSub

logger = logging.getLogger(__name__)


class SetBasedCalculationHandler(BaseCalculationHandler):
    """
    Calculation handler for set-based KPI computations.
    
    This handler:
    1. Looks up set-based KPI definitions from registry or metadata service
    2. Generates SQL using CTEs for intermediate sets
    3. Executes the query against TimescaleDB
    4. Returns the calculated result
    
    Supports complex calculations like:
    - Churn Rate (requires EXCEPT operation)
    - Retention Rate (requires INTERSECT operation)
    - Cohort Analysis (requires multiple filtered sets)
    - Period-over-Period comparisons
    """
    
    def __init__(
        self,
        value_chain_code: str,
        redis_url: str,
        cache_enabled: bool = True,
        cache_ttl: int = 300,
        schema_name: str = "analytics_data",
        service_name: str = "calculation_engine"
    ):
        super().__init__(
            value_chain_code=value_chain_code,
            database_service_url="",  # Not used - using pub/sub
            messaging_service_url="",  # Not used - using pub/sub
            metadata_service_url="",  # Not used - using pub/sub
            cache_enabled=cache_enabled,
            cache_ttl=cache_ttl
        )
        self.redis_url = redis_url
        self.sql_generator = SetBasedSQLGenerator(schema_name=schema_name)
        
        # Pub/sub clients for event-driven communication
        self._database_client: Optional[DatabaseClientPubSub] = None
        self._metadata_client: Optional[MetadataClientPubSub] = None
        self._service_name = service_name
    
    async def _get_database_client(self) -> DatabaseClientPubSub:
        """Get or create database pub/sub client."""
        if self._database_client is None:
            self._database_client = DatabaseClientPubSub(
                redis_url=self.redis_url,
                service_name=self._service_name
            )
            await self._database_client.connect()
        return self._database_client
    
    async def _get_metadata_client(self) -> MetadataClientPubSub:
        """Get or create metadata pub/sub client."""
        if self._metadata_client is None:
            self._metadata_client = MetadataClientPubSub(
                redis_url=self.redis_url,
                service_name=self._service_name
            )
            await self._metadata_client.connect()
        return self._metadata_client
    
    async def calculate(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Execute a set-based KPI calculation.
        
        Args:
            params: Calculation parameters including KPI code, date range, filters
            
        Returns:
            CalculationResult with the computed value
        """
        start_time = datetime.utcnow()
        
        # 1. Get set-based KPI definition
        kpi_def = await self._get_kpi_definition(params.kpi_code)
        
        if not kpi_def:
            raise CalculationError(
                f"Set-based KPI definition not found for: {params.kpi_code}"
            )
        
        # 2. Validate required parameters
        if not params.start_date or not params.end_date:
            raise CalculationError(
                "Start date and end date are required for set-based calculations"
            )
        
        # 3. Generate SQL
        try:
            sql, sql_params = self.sql_generator.generate_sql(
                kpi_def=kpi_def,
                period_start=params.start_date,
                period_end=params.end_date,
                additional_filters=params.filters
            )
            logger.debug(f"Generated SQL for {params.kpi_code}:\n{sql}")
        except Exception as e:
            raise CalculationError(f"SQL generation failed: {e}")
        
        # 4. Execute query
        try:
            result_value = await self._execute_query(sql, sql_params)
        except Exception as e:
            raise CalculationError(f"Query execution failed: {e}")
        
        # 5. Build result
        calculation_time = (datetime.utcnow() - start_time).total_seconds() * 1000
        
        return CalculationResult(
            kpi_code=params.kpi_code,
            value=result_value,
            unit=kpi_def.unit,
            timestamp=datetime.utcnow(),
            calculation_time_ms=calculation_time,
            metadata={
                "calculation_type": "set_based",
                "steps_count": len(kpi_def.steps),
                "period_start": params.start_date.isoformat(),
                "period_end": params.end_date.isoformat(),
                "sql_generated": sql,
                "final_formula": kpi_def.final_formula
            }
        )
    
    async def _get_kpi_definition(
        self,
        kpi_code: str
    ) -> Optional[SetBasedKPIDefinition]:
        """
        Get set-based KPI definition from registry or metadata service.
        
        First checks local registry, then falls back to metadata service via pub/sub.
        """
        # Check local registry first
        local_def = get_set_based_kpi_definition(kpi_code)
        if local_def:
            logger.debug(f"Found {kpi_code} in local registry")
            return local_def
        
        # Try metadata service via pub/sub
        try:
            metadata_client = await self._get_metadata_client()
            data = await metadata_client.get_metric_definition(kpi_code)
            
            if data and data.get("calculation_type") == "set_based":
                return self._parse_metadata_to_definition(data)
                    
        except Exception as e:
            logger.warning(f"Failed to fetch KPI definition from metadata service: {e}")
        
        return None
    
    def _parse_metadata_to_definition(
        self,
        metadata: Dict[str, Any]
    ) -> SetBasedKPIDefinition:
        """
        Parse metadata service response into SetBasedKPIDefinition.
        
        The metadata service stores set-based KPI definitions in a JSON structure
        that can be converted to our Pydantic models.
        """
        # The metadata should contain a 'set_based_definition' field
        # with the full definition structure
        set_def = metadata.get("set_based_definition", {})
        
        return SetBasedKPIDefinition(
            kpi_code=metadata.get("code", ""),
            name=metadata.get("name", ""),
            description=metadata.get("description"),
            unit=metadata.get("unit", "Number"),
            steps=set_def.get("steps", []),
            final_formula=set_def.get("final_formula", ""),
            metadata=metadata.get("metadata_", {})
        )
    
    async def _execute_query(
        self,
        sql: str,
        params: Dict[str, Any]
    ) -> float:
        """
        Execute SQL query against the database via pub/sub.
        
        Uses the database service via request/reply pattern.
        """
        try:
            db_client = await self._get_database_client()
            
            # Serialize datetime params
            serialized_params = {
                k: v.isoformat() if isinstance(v, datetime) else v 
                for k, v in params.items()
            }
            
            # Execute query via pub/sub
            result = await db_client.execute_query(
                query=sql,
                parameters=serialized_params
            )
            
            # Extract the result value from the response
            rows = result.get("rows", [])
            if rows and len(rows) > 0:
                return float(rows[0].get("result", 0))
            return 0.0
                
        except Exception as e:
            logger.error(f"Database query failed: {e}")
            raise CalculationError(f"Database query failed: {e}")
    
    async def validate_params(self, params: CalculationParams) -> bool:
        """Validate calculation parameters for set-based calculations."""
        if not params.start_date:
            raise ValueError("start_date is required for set-based calculations")
        if not params.end_date:
            raise ValueError("end_date is required for set-based calculations")
        if params.start_date >= params.end_date:
            raise ValueError("start_date must be before end_date")
        return True
    
    def get_cache_key(self, params: CalculationParams) -> str:
        """Generate cache key for set-based calculation."""
        return f"set_based:{self.value_chain_code}:{self._generate_cache_key_base(params)}"
    
    def get_supported_kpis(self) -> List[str]:
        """Get list of KPI codes supported by this handler."""
        return list(SET_BASED_KPI_REGISTRY.keys())
    
    async def close(self):
        """Clean up resources."""
        if self._http_client:
            await self._http_client.aclose()
            self._http_client = None


class SetBasedCalculationEngine:
    """
    High-level engine for executing set-based calculations.
    
    Provides a simpler interface for running set-based KPI calculations
    without needing to manage handlers directly.
    
    Performance Optimizations for 1-second SLA:
    ============================================
    1. **Pre-compiled SQL**: KPI definitions are converted to SQL at registration time,
       not at query time. The SQL generator caches CTE structures.
    
    2. **Connection Pooling**: HTTP client uses connection pooling with keep-alive
       to minimize connection overhead (~50-100ms savings per request).
    
    3. **Result Caching**: Recent calculation results are cached with TTL.
       Cache key = kpi_code + period_start + period_end + filters_hash.
    
    4. **Query Optimization**: Generated SQL uses CTEs which PostgreSQL/TimescaleDB
       optimizes into a single execution plan. No multiple round-trips.
    
    5. **Timeout Configuration**: Aggressive timeouts ensure fast failure.
    
    Performance Breakdown (target: <1000ms total):
    - HTTP overhead: ~20-50ms (with connection pooling)
    - SQL generation: ~1-5ms (pre-compiled templates)
    - Database execution: ~100-800ms (depends on data size, indexed)
    - Response serialization: ~5-10ms
    
    Note: NLP-to-Set conversion is a ONE-TIME operation during KPI definition,
    NOT during calculation. LLM calls (1-5 seconds) only happen at definition time.
    """
    
    # Class-level cache for SQL templates (shared across instances)
    _sql_cache: Dict[str, str] = {}
    
    # Result cache with TTL
    _result_cache: Dict[str, Dict[str, Any]] = {}
    _cache_ttl_seconds: int = 60  # 1 minute default TTL
    _cache_timestamps: Dict[str, datetime] = {}
    
    def __init__(
        self,
        redis_url: str,
        schema_name: str = "analytics_data",
        cache_ttl_seconds: int = 60,
        query_timeout_seconds: float = 0.8,  # Leave 200ms buffer for overhead
        service_name: str = "calculation_engine"
    ):
        self.redis_url = redis_url
        self.schema_name = schema_name
        self.sql_generator = SetBasedSQLGenerator(schema_name=schema_name)
        self._database_client: Optional[DatabaseClientPubSub] = None
        self._cache_ttl_seconds = cache_ttl_seconds
        self._query_timeout = query_timeout_seconds
        self._service_name = service_name
        
        # Performance metrics
        self._metrics = {
            "total_calculations": 0,
            "cache_hits": 0,
            "cache_misses": 0,
            "avg_calculation_time_ms": 0.0,
            "max_calculation_time_ms": 0.0,
            "sla_violations": 0  # Calculations > 1000ms
        }
    
    async def _get_database_client(self) -> DatabaseClientPubSub:
        """
        Get or create database pub/sub client.
        
        Uses request/reply pattern over Redis for event-driven architecture.
        """
        if self._database_client is None:
            self._database_client = DatabaseClientPubSub(
                redis_url=self.redis_url,
                service_name=self._service_name,
                default_timeout=self._query_timeout + 0.5  # Add buffer for pub/sub overhead
            )
            await self._database_client.connect()
        return self._database_client
    
    def _get_cache_key(
        self,
        kpi_code: str,
        period_start: datetime,
        period_end: datetime,
        filters: Optional[Dict[str, Any]] = None
    ) -> str:
        """Generate cache key for calculation result."""
        import hashlib
        filters_str = json.dumps(filters or {}, sort_keys=True)
        key_str = f"{kpi_code}:{period_start.isoformat()}:{period_end.isoformat()}:{filters_str}"
        return hashlib.md5(key_str.encode()).hexdigest()
    
    def _check_cache(self, cache_key: str) -> Optional[Dict[str, Any]]:
        """Check if result is in cache and not expired."""
        if cache_key in self._result_cache:
            timestamp = self._cache_timestamps.get(cache_key)
            if timestamp and (datetime.utcnow() - timestamp).total_seconds() < self._cache_ttl_seconds:
                self._metrics["cache_hits"] += 1
                return self._result_cache[cache_key]
            else:
                # Expired - remove from cache
                del self._result_cache[cache_key]
                if cache_key in self._cache_timestamps:
                    del self._cache_timestamps[cache_key]
        self._metrics["cache_misses"] += 1
        return None
    
    def _store_cache(self, cache_key: str, result: Dict[str, Any]):
        """Store result in cache."""
        # Simple LRU: remove oldest if cache is too large
        if len(self._result_cache) > 1000:
            oldest_key = min(self._cache_timestamps, key=self._cache_timestamps.get)
            del self._result_cache[oldest_key]
            del self._cache_timestamps[oldest_key]
        
        self._result_cache[cache_key] = result
        self._cache_timestamps[cache_key] = datetime.utcnow()
    
    def _update_metrics(self, calculation_time_ms: float):
        """Update performance metrics."""
        self._metrics["total_calculations"] += 1
        
        # Update average
        n = self._metrics["total_calculations"]
        old_avg = self._metrics["avg_calculation_time_ms"]
        self._metrics["avg_calculation_time_ms"] = old_avg + (calculation_time_ms - old_avg) / n
        
        # Update max
        if calculation_time_ms > self._metrics["max_calculation_time_ms"]:
            self._metrics["max_calculation_time_ms"] = calculation_time_ms
        
        # Check SLA violation
        if calculation_time_ms > 1000:
            self._metrics["sla_violations"] += 1
            logger.warning(f"SLA violation: calculation took {calculation_time_ms:.2f}ms (>1000ms)")
    
    async def calculate(
        self,
        kpi_code: str,
        period_start: datetime,
        period_end: datetime,
        filters: Optional[Dict[str, Any]] = None,
        use_cache: bool = True
    ) -> Dict[str, Any]:
        """
        Calculate a set-based KPI.
        
        Performance target: <1000ms total response time.
        
        Args:
            kpi_code: The KPI code (e.g., "CHURN_RATE")
            period_start: Start of the calculation period
            period_end: End of the calculation period
            filters: Optional additional filters
            use_cache: Whether to use result caching (default: True)
            
        Returns:
            Dictionary with calculation result and metadata
        """
        import time
        start_time = time.perf_counter()
        
        # Check cache first (if enabled)
        cache_key = self._get_cache_key(kpi_code, period_start, period_end, filters)
        if use_cache:
            cached_result = self._check_cache(cache_key)
            if cached_result:
                cached_result["from_cache"] = True
                cached_result["calculation_time_ms"] = (time.perf_counter() - start_time) * 1000
                return cached_result
        
        # Get KPI definition
        kpi_def = get_set_based_kpi_definition(kpi_code)
        if not kpi_def:
            raise ValueError(f"Unknown set-based KPI: {kpi_code}")
        
        # Generate SQL (fast - uses cached templates)
        sql_start = time.perf_counter()
        sql, params = self.sql_generator.generate_sql(
            kpi_def=kpi_def,
            period_start=period_start,
            period_end=period_end,
            additional_filters=filters
        )
        sql_time_ms = (time.perf_counter() - sql_start) * 1000
        
        # Execute query via pub/sub
        query_start = time.perf_counter()
        try:
            db_client = await self._get_database_client()
            
            # Serialize datetime params
            serialized_params = {
                k: v.isoformat() if isinstance(v, datetime) else v 
                for k, v in params.items()
            }
            
            result = await db_client.execute_query(
                query=sql,
                parameters=serialized_params,
                timeout=self._query_timeout
            )
            
            rows = result.get("rows", [])
            value = float(rows[0].get("result", 0)) if rows else 0.0
                
        except asyncio.TimeoutError:
            raise CalculationError("Query timeout - SLA exceeded")
        except Exception as e:
            raise CalculationError(f"Database query failed: {e}")
        
        query_time_ms = (time.perf_counter() - query_start) * 1000
        total_time_ms = (time.perf_counter() - start_time) * 1000
        
        # Update metrics
        self._update_metrics(total_time_ms)
        
        result = {
            "kpi_code": kpi_code,
            "name": kpi_def.name,
            "value": value,
            "unit": kpi_def.unit,
            "period_start": period_start.isoformat(),
            "period_end": period_end.isoformat(),
            "calculation_time_ms": total_time_ms,
            "from_cache": False,
            "performance": {
                "sql_generation_ms": sql_time_ms,
                "query_execution_ms": query_time_ms,
                "total_ms": total_time_ms,
                "sla_met": total_time_ms < 1000
            },
            "sql": sql,
            "steps": [
                {
                    "step": step.step_number,
                    "name": step.name,
                    "description": step.description
                }
                for step in kpi_def.steps
            ]
        }
        
        # Store in cache
        if use_cache:
            self._store_cache(cache_key, result)
        
        return result
    
    async def explain(
        self,
        kpi_code: str,
        period_start: datetime,
        period_end: datetime
    ) -> Dict[str, Any]:
        """
        Get explanation of how a KPI would be calculated.
        
        Returns the SQL and step breakdown without executing.
        """
        kpi_def = get_set_based_kpi_definition(kpi_code)
        if not kpi_def:
            raise ValueError(f"Unknown set-based KPI: {kpi_code}")
        
        sql, params = self.sql_generator.generate_sql(
            kpi_def=kpi_def,
            period_start=period_start,
            period_end=period_end
        )
        
        return {
            "kpi_code": kpi_code,
            "name": kpi_def.name,
            "description": kpi_def.description,
            "unit": kpi_def.unit,
            "sql": sql,
            "parameters": {k: v.isoformat() if isinstance(v, datetime) else v 
                          for k, v in params.items()},
            "steps": [
                {
                    "step": step.step_number,
                    "name": step.name,
                    "description": step.description,
                    "type": "set_definition" if step.set_definition else 
                            "aggregation" if step.aggregation else "formula",
                    "depends_on": step.depends_on
                }
                for step in kpi_def.steps
            ],
            "final_formula": kpi_def.final_formula
        }
    
    def list_available_kpis(self) -> List[Dict[str, str]]:
        """List all available set-based KPIs."""
        return [
            {
                "code": kpi_def.kpi_code,
                "name": kpi_def.name,
                "description": kpi_def.description,
                "unit": kpi_def.unit
            }
            for kpi_def in SET_BASED_KPI_REGISTRY.values()
        ]
    
    def get_metrics(self) -> Dict[str, Any]:
        """
        Get performance metrics for monitoring.
        
        Returns:
            Dictionary with performance statistics including:
            - total_calculations: Total number of calculations performed
            - cache_hits/misses: Cache performance
            - avg_calculation_time_ms: Average calculation time
            - max_calculation_time_ms: Maximum calculation time
            - sla_violations: Number of calculations exceeding 1000ms
            - sla_compliance_rate: Percentage of calculations meeting SLA
        """
        total = self._metrics["total_calculations"]
        violations = self._metrics["sla_violations"]
        
        return {
            **self._metrics,
            "cache_hit_rate": (
                self._metrics["cache_hits"] / 
                (self._metrics["cache_hits"] + self._metrics["cache_misses"])
                if (self._metrics["cache_hits"] + self._metrics["cache_misses"]) > 0
                else 0.0
            ),
            "sla_compliance_rate": (
                (total - violations) / total if total > 0 else 1.0
            ),
            "cache_size": len(self._result_cache)
        }
    
    def clear_cache(self):
        """Clear the result cache."""
        self._result_cache.clear()
        self._cache_timestamps.clear()
        logger.info("Result cache cleared")
    
    async def close(self):
        """Clean up resources."""
        if self._database_client:
            await self._database_client.close()
            self._database_client = None
        self.clear_cache()
