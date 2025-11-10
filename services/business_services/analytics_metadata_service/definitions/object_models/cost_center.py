"""
Cost Center Object Model

Represents organizational cost centers for cost allocation.
Critical for Total Supply Chain Management Cost calculation.

Key SCOR Metrics Enabled:
- CO.1.1: Total Supply Chain Management Cost
"""

COST_CENTER = {
    "code": "COST_CENTER",
    "name": "Cost Center",
    "description": "Organizational cost centers for cost allocation",
    "table_schema": {"table_name": "cost_centers", "class_name": "CostCenter", "columns": [{"name": "cost_center_id", "type": "Integer", "primary_key": True, "autoincrement": True}, {"name": "cost_center_code", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True}, {"name": "cost_center_name", "type": "String", "length": 200, "nullable": False}, {"name": "scor_process", "type": "String", "length": 50, "index": True, "description": "Plan, Source, Make, Deliver, Return"}, {"name": "department", "type": "String", "length": 100}, {"name": "manager", "type": "String", "length": 100}, {"name": "is_active", "type": "Boolean", "default": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}]},
    "schema_definition": """
    @startuml
    CostCenter "1" -- "0..*" Cost : allocates
    CostCenter "1" -- "0..*" Activity : contains
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"], "related_kpis": ["TOTAL_SUPPLY_CHAIN_MANAGEMENT_COST"]},
}
