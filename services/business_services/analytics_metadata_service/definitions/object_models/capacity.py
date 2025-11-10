"""
Capacity Object Model

Represents production and supply chain capacity.
Critical for supply chain flexibility metrics.

Key SCOR Metrics Enabled:
- AG.1.1: Upside Supply Chain Flexibility (capacity expansion)
"""

CAPACITY = {
    "code": "CAPACITY",
    "name": "Capacity",
    "description": "Production and supply chain capacity tracking",
    "table_schema": {"table_name": "capacity", "class_name": "Capacity", "columns": [{"name": "capacity_id", "type": "Integer", "primary_key": True, "autoincrement": True}, {"name": "facility_id", "type": "Integer", "nullable": False, "index": True}, {"name": "capacity_type", "type": "String", "length": 50, "index": True, "description": "production, storage, transportation"}, {"name": "measurement_date", "type": "DateTime", "nullable": False, "index": True}, {"name": "maximum_capacity", "type": "Float", "nullable": False}, {"name": "current_capacity", "type": "Float"}, {"name": "utilization_percent", "type": "Float"}, {"name": "unit_of_measure", "type": "String", "length": 20}, {"name": "can_expand", "type": "Boolean"}, {"name": "expansion_time_days", "type": "Integer", "description": "Days to expand by 20%"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}]},
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN"], "related_kpis": ["UPSIDE_SUPPLY_CHAIN_FLEXIBILITY"]},
}
