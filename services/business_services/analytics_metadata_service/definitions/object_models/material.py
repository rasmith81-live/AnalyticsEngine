"""
Material Object Model

Represents raw materials and components used in production.
Critical for COGS and supply chain flexibility metrics.

Key SCOR Metrics Enabled:
- CO.1.2: Cost of Goods Sold (material costs)
- AG.1.1: Upside Supply Chain Flexibility (material availability)
"""

from analytics_models import ObjectModel

MATERIAL = ObjectModel(
    name="Material",
    code="MATERIAL",
    description="Raw materials and components used in production",

    table_schema={
        "table_name": "materials",
        "class_name": "Material",
        "columns": [
            {"name": "material_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "material_code", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True},
            {"name": "material_name", "type": "String", "length": 200, "nullable": False},
            {"name": "material_type", "type": "String", "length": 50, "index": True},
            {"name": "supplier_id", "type": "Integer", "foreign_key": "suppliers.supplier_id", "index": True},
            {"name": "unit_of_measure", "type": "String", "length": 20},
            {"name": "unit_cost", "type": "Float"},
            {"name": "lead_time_days", "type": "Integer"},
            {"name": "minimum_order_quantity", "type": "Integer"},
            {"name": "is_critical", "type": "Boolean", "default": False},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False},
            {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}
        ]
    },

    schema_definition="""
    @startuml
    Material "*" -- "1" Supplier : supplied_by
    Material "*" -- "0..*" Production : used_in
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "MANUFACTURING"],
        "related_kpis": ["COST_OF_GOODS_SOLD", "UPSIDE_SUPPLY_CHAIN_FLEXIBILITY"]
    }
)
