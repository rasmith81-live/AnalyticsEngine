"""
Activity Object Model

Represents supply chain activities for activity-based costing.
Critical for Total Supply Chain Management Cost calculation.

Key SCOR Metrics Enabled:
- CO.1.1: Total Supply Chain Management Cost (activity-based costing)
"""

ACTIVITY = {
    "code": "ACTIVITY",
    "name": "Activity",
    "description": "Supply chain activities for activity-based costing",
    "table_schema": {"table_name": "activities", "class_name": "Activity", "columns": [{"name": "activity_id", "type": "Integer", "primary_key": True, "autoincrement": True}, {"name": "activity_code", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True}, {"name": "activity_name", "type": "String", "length": 200, "nullable": False}, {"name": "activity_type", "type": "String", "length": 50, "index": True}, {"name": "scor_process", "type": "String", "length": 50, "index": True, "description": "Plan, Source, Make, Deliver, Return"}, {"name": "cost_center_id", "type": "Integer", "foreign_key": "cost_centers.cost_center_id", "index": True}, {"name": "cost_driver", "type": "String", "length": 100, "description": "What drives the cost"}, {"name": "is_active", "type": "Boolean", "default": True}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}]},
    "schema_definition": """
    @startuml
    Activity "*" -- "1" CostCenter : belongs_to
    Activity "1" -- "0..*" Cost : incurs
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"], "related_kpis": ["TOTAL_SUPPLY_CHAIN_MANAGEMENT_COST"]},
}
