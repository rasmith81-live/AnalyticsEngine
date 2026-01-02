"""KPI Analyzer for the Data Simulator Service.

Looks up KPI definitions to determine what entity data needs to be generated.
Uses the required_objects field already populated during KPI upload.
Uses pub/sub messaging for event-driven metadata access.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple
import logging

from .models import EntityConfig
from .metadata_client_pubsub import MetadataClientPubSub

logger = logging.getLogger(__name__)


class KPIAnalyzer:
    """Analyzes KPI definitions to extract entity requirements for simulation."""
    
    # Sample KPI definitions for fallback when metadata service is unavailable
    SAMPLE_KPIS: Dict[str, Dict[str, Any]] = {
        "REVENUE": {
            "code": "REVENUE",
            "name": "Total Revenue",
            "calculation_type": "simple",
            "required_objects": ["orders", "order_items"],
        },
        "AVG_ORDER_VALUE": {
            "code": "AVG_ORDER_VALUE",
            "name": "Average Order Value",
            "calculation_type": "simple",
            "required_objects": ["orders"],
        },
        "CONVERSION_RATE": {
            "code": "CONVERSION_RATE",
            "name": "Conversion Rate",
            "calculation_type": "set_based",
            "required_objects": ["leads", "opportunities", "deals"],
        },
        "WIN_RATE": {
            "code": "WIN_RATE",
            "name": "Win Rate",
            "calculation_type": "set_based",
            "required_objects": ["opportunities", "deals"],
        },
        "SALES_CYCLE_LENGTH": {
            "code": "SALES_CYCLE_LENGTH",
            "name": "Sales Cycle Length",
            "calculation_type": "simple",
            "required_objects": ["opportunities", "deals"],
        },
        "CHURN_RATE": {
            "code": "CHURN_RATE",
            "name": "Churn Rate",
            "calculation_type": "set_based",
            "required_objects": ["customers"],
        },
        "RETENTION_RATE": {
            "code": "RETENTION_RATE",
            "name": "Retention Rate",
            "calculation_type": "set_based",
            "required_objects": ["customers"],
        },
        "NPS": {
            "code": "NPS",
            "name": "Net Promoter Score",
            "calculation_type": "simple",
            "required_objects": ["customer_surveys"],
        },
        "CSAT": {
            "code": "CSAT",
            "name": "Customer Satisfaction Score",
            "calculation_type": "simple",
            "required_objects": ["customer_surveys"],
        },
        "CLV": {
            "code": "CLV",
            "name": "Customer Lifetime Value",
            "calculation_type": "set_based",
            "required_objects": ["customers", "orders"],
        },
        "CAC": {
            "code": "CAC",
            "name": "Customer Acquisition Cost",
            "calculation_type": "simple",
            "required_objects": ["marketing_spend", "customers"],
        },
        "MQL_COUNT": {
            "code": "MQL_COUNT",
            "name": "Marketing Qualified Leads",
            "calculation_type": "simple",
            "required_objects": ["leads"],
        },
        "CAMPAIGN_ROI": {
            "code": "CAMPAIGN_ROI",
            "name": "Campaign ROI",
            "calculation_type": "set_based",
            "required_objects": ["campaigns", "marketing_spend", "conversions"],
        },
        "ORDER_FULFILLMENT_TIME": {
            "code": "ORDER_FULFILLMENT_TIME",
            "name": "Order Fulfillment Time",
            "calculation_type": "simple",
            "required_objects": ["orders", "shipments"],
        },
        "INVENTORY_TURNOVER": {
            "code": "INVENTORY_TURNOVER",
            "name": "Inventory Turnover",
            "calculation_type": "simple",
            "required_objects": ["inventory", "sales"],
        },
        "GROSS_MARGIN": {
            "code": "GROSS_MARGIN",
            "name": "Gross Margin",
            "calculation_type": "simple",
            "required_objects": ["revenue", "costs"],
        },
        "MRR": {
            "code": "MRR",
            "name": "Monthly Recurring Revenue",
            "calculation_type": "set_based",
            "required_objects": ["subscriptions", "customers"],
        },
        "ARR": {
            "code": "ARR",
            "name": "Annual Recurring Revenue",
            "calculation_type": "set_based",
            "required_objects": ["subscriptions", "customers"],
        },
    }
    
    def __init__(self, redis_url: Optional[str] = None):
        self.redis_url = redis_url
        self._metadata_client: Optional[MetadataClientPubSub] = None
        self._kpi_cache: Dict[str, Dict[str, Any]] = {}
    
    async def _get_metadata_client(self) -> Optional[MetadataClientPubSub]:
        """Get or create metadata pub/sub client."""
        if self._metadata_client is None and self.redis_url:
            self._metadata_client = MetadataClientPubSub(
                redis_url=self.redis_url,
                service_name="data_simulator"
            )
            await self._metadata_client.connect()
        return self._metadata_client
    
    async def close(self) -> None:
        """Close the metadata client."""
        if self._metadata_client:
            await self._metadata_client.close()
            self._metadata_client = None
    
    async def analyze_kpis(
        self,
        kpi_codes: List[str]
    ) -> Tuple[List[EntityConfig], List[Dict[str, Any]]]:
        """
        Analyze a list of KPIs and return the entity configurations needed.
        
        Uses the required_objects field from the KPI definition which was
        populated during KPI upload/ingestion.
        
        Args:
            kpi_codes: List of KPI codes to analyze
            
        Returns:
            Tuple of (entity_configs, kpi_definitions)
            - entity_configs: List of EntityConfig objects for entities to simulate
            - kpi_definitions: List of full KPI definitions for reference
        """
        entities_needed: Dict[str, EntityConfig] = {}
        kpi_definitions: List[Dict[str, Any]] = []
        
        for kpi_code in kpi_codes:
            kpi_def = await self._get_kpi_definition(kpi_code)
            if not kpi_def:
                logger.warning(f"KPI definition not found: {kpi_code}")
                continue
            
            kpi_definitions.append(kpi_def)
            
            # Use required_objects field from KPI definition
            required_objects = kpi_def.get("required_objects", [])
            calculation_type = kpi_def.get("calculation_type", "simple")
            set_based_def = kpi_def.get("set_based_definition")
            
            for entity_code in required_objects:
                if entity_code not in entities_needed:
                    # Build entity config from the entity code
                    entity_config = await self._build_entity_config_from_code(
                        entity_code, 
                        calculation_type,
                        set_based_def
                    )
                    if entity_config:
                        entities_needed[entity_code] = entity_config
        
        return list(entities_needed.values()), kpi_definitions
    
    async def _get_kpi_definition(self, kpi_code: str) -> Optional[Dict[str, Any]]:
        """Fetch KPI definition from metadata service via pub/sub, cache, or fallback to samples."""
        if kpi_code in self._kpi_cache:
            return self._kpi_cache[kpi_code]
        
        # Try metadata service first
        metadata_client = await self._get_metadata_client()
        if metadata_client:
            try:
                kpi_def = await metadata_client.get_metric_definition(kpi_code)
                if kpi_def:
                    self._kpi_cache[kpi_code] = kpi_def
                    return kpi_def
            except Exception as e:
                logger.warning(f"Failed to fetch KPI {kpi_code} from metadata service: {e}")
        
        # Fallback to sample KPIs
        if kpi_code in self.SAMPLE_KPIS:
            logger.info(f"Using sample KPI definition for {kpi_code}")
            sample_def = self.SAMPLE_KPIS[kpi_code]
            self._kpi_cache[kpi_code] = sample_def
            return sample_def
        
        return None
    
    async def _get_entity_definition(self, entity_code: str) -> Optional[Dict[str, Any]]:
        """Fetch entity definition from metadata service via pub/sub."""
        metadata_client = await self._get_metadata_client()
        if metadata_client:
            try:
                return await metadata_client.get_entity_definition(entity_code)
            except Exception as e:
                logger.warning(f"Failed to fetch entity {entity_code}: {e}")
        
        return None
    
    async def _build_entity_config_from_code(
        self,
        entity_code: str,
        calculation_type: str,
        set_based_def: Optional[Dict[str, Any]]
    ) -> Optional[EntityConfig]:
        """
        Build an EntityConfig from an entity code by looking up the entity definition.
        
        Args:
            entity_code: The entity code from required_objects
            calculation_type: "simple" or "set_based"
            set_based_def: The set_based_definition if calculation_type is "set_based"
        """
        # Try to fetch entity definition from metadata service
        entity_def = await self._get_entity_definition(entity_code)
        
        # Extract table schema info if available
        table_name = entity_code.lower()
        key_column = "id"
        attributes = {}
        
        if entity_def:
            # Use table_schema from entity definition
            table_schema = entity_def.get("table_schema", {})
            table_name = table_schema.get("table_name", entity_code.lower())
            
            # Extract columns from schema
            columns = table_schema.get("columns", [])
            for col in columns:
                col_name = col.get("name", "")
                if col.get("primary_key"):
                    key_column = col_name
                elif col_name not in ["created_at", "updated_at"]:
                    attributes[col_name] = self._infer_column_config(col)
        
        # If set_based, extract additional column requirements
        if calculation_type == "set_based" and set_based_def:
            required_columns = self._extract_columns_from_set_def(set_based_def)
            for col in required_columns:
                if col not in attributes and col not in [key_column, "created_at", "updated_at"]:
                    attributes[col] = self._infer_column_type(col)
        
        # Infer rates based on entity type
        churn_rate, growth_rate, conversion_rate = self._infer_rates(entity_code)
        
        return EntityConfig(
            entity_name=entity_code,
            table_name=table_name,
            key_column=key_column,
            initial_count=1000,
            base_churn_rate=churn_rate,
            base_growth_rate=growth_rate,
            base_conversion_rate=conversion_rate,
            attributes=attributes,
        )
    
    def _infer_column_config(self, column_def: Dict[str, Any]) -> Dict[str, Any]:
        """Infer column generation config from a column definition."""
        col_type = column_def.get("data_type", "string").lower()
        col_name = column_def.get("name", "").lower()
        
        if col_type in ["timestamp", "timestamptz", "datetime", "date"]:
            return {"type": "datetime"}
        elif col_type in ["decimal", "numeric", "float", "double", "real"]:
            return {"type": "float", "min": 0.0, "max": 10000.0}
        elif col_type in ["integer", "int", "bigint", "smallint"]:
            return {"type": "int", "min": 1, "max": 1000}
        elif col_type == "boolean":
            return {"type": "bool", "probability": 0.5}
        elif "status" in col_name or "state" in col_name:
            return {"type": "choice", "values": ["active", "pending", "completed", "cancelled"]}
        elif "tier" in col_name or "level" in col_name or "plan" in col_name:
            return {"type": "choice", "values": ["basic", "standard", "premium", "enterprise"]}
        else:
            return {"type": "string"}
    
    def _extract_columns_from_set_def(self, set_def: Dict[str, Any]) -> Set[str]:
        """Extract all column names referenced in a set_based_definition."""
        columns = set()
        
        def extract_from_conditions(conditions: Any):
            if isinstance(conditions, dict):
                if "column" in conditions:
                    columns.add(conditions["column"])
                if "conditions" in conditions:
                    for cond in conditions["conditions"]:
                        extract_from_conditions(cond)
            elif isinstance(conditions, list):
                for cond in conditions:
                    extract_from_conditions(cond)
        
        # Check top-level filter conditions
        filter_conditions = set_def.get("filter_conditions")
        if filter_conditions:
            extract_from_conditions(filter_conditions)
        
        # Check steps
        for step in set_def.get("steps", []):
            step_set_def = step.get("set_definition", {})
            step_filters = step_set_def.get("filter_conditions")
            if step_filters:
                extract_from_conditions(step_filters)
            
            # Check aggregation columns
            aggregation = step.get("aggregation", {})
            if "column" in aggregation:
                columns.add(aggregation["column"])
        
        return columns
    
    def _infer_rates(self, entity_name: str) -> Tuple[float, float, float]:
        """Infer appropriate churn/growth/conversion rates based on entity type."""
        entity_lower = entity_name.lower()
        
        # Default rates
        churn_rate = 0.02  # 2% monthly
        growth_rate = 0.05  # 5% monthly
        conversion_rate = 0.15  # 15%
        
        # Adjust based on entity type
        if "customer" in entity_lower or "client" in entity_lower:
            churn_rate = 0.02
            growth_rate = 0.05
        elif "subscription" in entity_lower:
            churn_rate = 0.03
            growth_rate = 0.08
        elif "policy" in entity_lower:
            churn_rate = 0.015
            growth_rate = 0.03
        elif "lead" in entity_lower:
            churn_rate = 0.10  # Leads expire faster
            growth_rate = 0.20
            conversion_rate = 0.15
        elif "opportunity" in entity_lower:
            churn_rate = 0.05
            growth_rate = 0.10
            conversion_rate = 0.25
        elif "order" in entity_lower or "transaction" in entity_lower:
            churn_rate = 0.0  # Transactions don't churn
            growth_rate = 0.10
        
        return churn_rate, growth_rate, conversion_rate
    
    def _infer_column_type(self, column_name: str) -> Dict[str, Any]:
        """Infer the type and generation config for a column by name."""
        col_lower = column_name.lower()
        
        # Date columns
        if any(x in col_lower for x in ["date", "time", "at", "_on"]):
            return {"type": "datetime"}
        
        # Amount/value columns
        if any(x in col_lower for x in ["amount", "value", "price", "cost", "revenue"]):
            return {"type": "float", "min": 10.0, "max": 10000.0}
        
        # Count columns
        if any(x in col_lower for x in ["count", "quantity", "seats", "users"]):
            return {"type": "int", "min": 1, "max": 100}
        
        # Status columns
        if any(x in col_lower for x in ["status", "state"]):
            return {"type": "choice", "values": ["active", "pending", "completed", "cancelled"]}
        
        # Tier/level columns
        if any(x in col_lower for x in ["tier", "level", "plan"]):
            return {"type": "choice", "values": ["basic", "standard", "premium", "enterprise"]}
        
        # Boolean columns
        if any(x in col_lower for x in ["is_", "has_", "verified", "active"]):
            return {"type": "bool", "probability": 0.7}
        
        # Default to string
        return {"type": "string"}
    
    async def get_kpi_summary(self, kpi_code: str) -> Optional[Dict[str, Any]]:
        """
        Get a summary of a KPI for display in the UI.
        
        Returns:
            Dict with code, name, calculation_type, required_objects
        """
        kpi_def = await self._get_kpi_definition(kpi_code)
        if not kpi_def:
            return None
        
        return {
            "code": kpi_def.get("code"),
            "name": kpi_def.get("name"),
            "calculation_type": kpi_def.get("calculation_type", "simple"),
            "required_objects": kpi_def.get("required_objects", []),
            "formula": kpi_def.get("formula"),
            "category": kpi_def.get("category"),
        }
