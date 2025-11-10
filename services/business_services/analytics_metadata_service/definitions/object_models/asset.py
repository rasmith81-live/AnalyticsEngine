"""
Asset Object Model

Represents fixed assets used in supply chain operations.
Critical for Return on Supply Chain Fixed Assets calculation.

Key SCOR Metrics Enabled:
- PR.1.1: Return on Supply Chain Fixed Assets
"""

from analytics_models import ObjectModel

ASSET = ObjectModel(
    name="Asset",
    code="ASSET",
    description="Fixed assets used in supply chain operations",

    table_schema={
        "table_name": "assets",
        "class_name": "Asset",
        "columns": [
            {"name": "asset_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "asset_code", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True},
            {"name": "asset_name", "type": "String", "length": 200, "nullable": False},
            {"name": "asset_type", "type": "String", "length": 50, "index": True, "description": "warehouse, equipment, vehicle, etc."},
            {"name": "asset_category", "type": "String", "length": 50, "description": "supply_chain, manufacturing, logistics"},
            {"name": "facility_id", "type": "Integer", "index": True},
            {"name": "purchase_date", "type": "DateTime"},
            {"name": "purchase_cost", "type": "Float"},
            {"name": "current_value", "type": "Float"},
            {"name": "accumulated_depreciation", "type": "Float", "default": 0},
            {"name": "net_book_value", "type": "Float"},
            {"name": "useful_life_years", "type": "Integer"},
            {"name": "is_supply_chain_asset", "type": "Boolean", "default": True, "description": "Include in ROSCFA calculation"},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False},
            {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}
        ]
    },

    schema_definition="""
    @startuml
    Asset "*" -- "0..1" Facility : located_at
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"],
        "related_kpis": ["RETURN_ON_SUPPLY_CHAIN_FIXED_ASSETS"],
        "scor_metrics": {
            "PR.1.1": {"name": "Return on Supply Chain Fixed Assets", "calculation": "(Revenue - COGS - OpEx) / SC Fixed Assets"}
        }
    }
)
