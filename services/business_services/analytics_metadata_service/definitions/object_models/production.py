"""
Production Object Model

Represents manufacturing production runs and operations.
Critical for supply chain flexibility and adaptability metrics.

Production tracks manufacturing activities, capacity utilization, and output,
used to calculate agility metrics for SCOR.

Key SCOR Metrics Enabled:
- AG.1.1: Upside Supply Chain Flexibility (production capacity)
- AG.1.2: Downside Supply Chain Adaptability (production adjustments)
- CO.1.2: Cost of Goods Sold (manufacturing costs)
"""

from analytics_models import ObjectModel

PRODUCTION = ObjectModel(
    name="Production",
    code="PRODUCTION",
    description="Manufacturing production runs and operations",

    table_schema={
        "table_name": "production",
        "class_name": "Production",
        "columns": [
            {"name": "production_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "production_order_number", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True},
            {"name": "product_id", "type": "Integer", "foreign_key": "products.product_id", "nullable": False, "index": True},
            {"name": "facility_id", "type": "Integer", "index": True},
            {"name": "production_line", "type": "String", "length": 100},
            {"name": "start_date", "type": "DateTime", "nullable": False, "index": True},
            {"name": "end_date", "type": "DateTime", "index": True},
            {"name": "planned_quantity", "type": "Integer", "nullable": False},
            {"name": "actual_quantity", "type": "Integer"},
            {"name": "defect_quantity", "type": "Integer", "default": 0},
            {"name": "yield_percent", "type": "Float"},
            {"name": "production_status", "type": "String", "length": 50, "nullable": False, "index": True},
            {"name": "capacity_utilized_percent", "type": "Float"},
            {"name": "production_cost", "type": "Float"},
            {"name": "unit_cost", "type": "Float"},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False},
            {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}
        ]
    },

    schema_definition="""
    @startuml
    Production "*" -- "1" Product : produces
    Production "*" -- "0..*" Material : consumes
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "MANUFACTURING"],
        "related_kpis": ["UPSIDE_SUPPLY_CHAIN_FLEXIBILITY", "DOWNSIDE_SUPPLY_CHAIN_ADAPTABILITY", "COST_OF_GOODS_SOLD"],
        "scor_metrics": {
            "AG.1.1": {"name": "Upside Supply Chain Flexibility", "usage": "Production capacity and scale-up time"},
            "AG.1.2": {"name": "Downside Supply Chain Adaptability", "usage": "Production reduction capability"}
        }
    }
)
