"""
Base Calculation Handler - Abstract base class for calculation handlers.

Defines the interface for the DynamicCalculationHandler and any future specialized handlers.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
from pydantic import BaseModel
import hashlib
import json


class CalculationParams(BaseModel):
    """Standard calculation parameters."""
    kpi_code: str
    filters: Dict[str, Any] = {}
    aggregation: str = "sum"  # sum, average, count, min, max
    time_period: str = "monthly"  # daily, weekly, monthly, quarterly, annually
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    dimensions: List[str] = []  # e.g., ["region", "product"]
    metadata: Dict[str, Any] = {}


class CalculationResult(BaseModel):
    """Standard calculation result."""
    kpi_code: str
    value: float
    unit: str
    timestamp: datetime
    calculation_time_ms: float
    cached: bool = False
    metadata: Dict[str, Any] = {}
    components: Optional[List[Dict[str, Any]]] = None  # For composite KPIs


class BaseCalculationHandler(ABC):
    """
    Abstract base class for all value chain calculation handlers.
    
    Handlers implement this interface to provide calculation logic 
    while maintaining a consistent API.
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
        """
        Initialize calculation handler.
        
        Args:
            value_chain_code: Value chain identifier (e.g., "SUPPLY_CHAIN", "FINANCE")
            database_service_url: URL for database service
            messaging_service_url: URL for messaging service
            metadata_service_url: URL for metadata service
            cache_enabled: Enable result caching
            cache_ttl: Cache TTL in seconds
        """
        self.value_chain_code = value_chain_code
        self.database_service_url = database_service_url
        self.messaging_service_url = messaging_service_url
        self.metadata_service_url = metadata_service_url
        self.cache_enabled = cache_enabled
        self.cache_ttl = cache_ttl
        
        # Initialized by subclasses
        self.schema_name = f"{value_chain_code.lower()}_data"
    
    @abstractmethod
    async def calculate(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Calculate KPI value.
        
        This is the main calculation method that must be implemented
        by each value chain handler.
        
        Args:
            params: Calculation parameters
            
        Returns:
            CalculationResult with computed value
            
        Raises:
            ValueError: If parameters are invalid
            CalculationError: If calculation fails
        """
        pass
    
    @abstractmethod
    async def validate_params(
        self,
        params: CalculationParams
    ) -> bool:
        """
        Validate calculation parameters.
        
        Args:
            params: Parameters to validate
            
        Returns:
            True if valid
            
        Raises:
            ValueError: If parameters are invalid
        """
        pass
    
    @abstractmethod
    def get_cache_key(
        self,
        params: CalculationParams
    ) -> str:
        """
        Generate cache key for calculation result.
        
        Args:
            params: Calculation parameters
            
        Returns:
            Cache key string
        """
        pass
    
    async def get_kpi_definition(self, kpi_code: str) -> Dict[str, Any]:
        """
        Fetch KPI definition from metadata service.
        
        Args:
            kpi_code: KPI code
            
        Returns:
            KPI definition dictionary
        """
        # Implementation calls metadata_service_url
        # This is a common method used by all handlers
        pass
    
    async def query_data(
        self,
        table_name: str,
        filters: Dict[str, Any],
        columns: List[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Query data from value chain schema.
        
        Args:
            table_name: Table name in value chain schema
            filters: Query filters
            columns: Columns to select
            
        Returns:
            Query results
        """
        # Implementation calls database_service_url
        # This is a common method used by all handlers
        pass
    
    async def publish_result(
        self,
        result: CalculationResult
    ):
        """
        Publish calculation result to messaging service.
        
        Args:
            result: Calculation result to publish
        """
        # Implementation calls messaging_service_url
        # This is a common method used by all handlers
        pass
    
    def _generate_cache_key_base(
        self,
        params: CalculationParams
    ) -> str:
        """
        Generate base cache key from parameters.
        
        Subclasses can override get_cache_key() for custom logic,
        or use this helper method.
        
        Args:
            params: Calculation parameters
            
        Returns:
            Cache key string
        """
        key_data = {
            "value_chain": self.value_chain_code,
            "kpi": params.kpi_code,
            "filters": params.filters,
            "aggregation": params.aggregation,
            "time_period": params.time_period,
            "start_date": params.start_date.isoformat() if params.start_date else None,
            "end_date": params.end_date.isoformat() if params.end_date else None,
            "dimensions": sorted(params.dimensions)
        }
        
        key_string = json.dumps(key_data, sort_keys=True)
        return hashlib.sha256(key_string.encode()).hexdigest()
    
    async def calculate_with_cache(
        self,
        params: CalculationParams
    ) -> CalculationResult:
        """
        Calculate with caching support.
        
        This is a template method that handles caching logic.
        Subclasses implement calculate() for actual computation.
        
        Args:
            params: Calculation parameters
            
        Returns:
            CalculationResult (from cache or fresh calculation)
        """
        if not self.cache_enabled:
            return await self.calculate(params)
        
        # Check cache
        cache_key = self.get_cache_key(params)
        cached_result = await self._get_from_cache(cache_key)
        
        if cached_result:
            cached_result.cached = True
            return cached_result
        
        # Calculate fresh
        result = await self.calculate(params)
        
        # Store in cache
        await self._store_in_cache(cache_key, result)
        
        return result
    
    async def _get_from_cache(self, cache_key: str) -> Optional[CalculationResult]:
        """Get result from cache."""
        # Implementation uses Redis via messaging_service
        pass
    
    async def _store_in_cache(self, cache_key: str, result: CalculationResult):
        """Store result in cache."""
        # Implementation uses Redis via messaging_service
        pass


class CalculationError(Exception):
    """Raised when calculation fails."""
    pass
