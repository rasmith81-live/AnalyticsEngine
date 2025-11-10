"""
Transportation Object Model

Represents transportation activities and their environmental impact.
Critical for carbon emissions from logistics.

Key SCOR Metrics Enabled:
- EV.1.1: Carbon Emissions per Unit (transportation emissions)
"""

from analytics_models import ObjectModel

TRANSPORTATION = ObjectModel(
    name="Transportation",
    code="TRANSPORTATION",
    description="Transportation activities and environmental impact",

    table_schema={
        "table_name": "transportation",
        "class_name": "Transportation",
        "columns": [
            {"name": "transportation_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "shipment_id", "type": "Integer", "foreign_key": "shipments.shipment_id", "index": True},
            {"name": "transportation_date", "type": "DateTime", "nullable": False, "index": True},
            {"name": "mode", "type": "String", "length": 50, "index": True, "description": "truck, rail, air, ocean"},
            {"name": "carrier", "type": "String", "length": 100},
            {"name": "distance_km", "type": "Float"},
            {"name": "weight_kg", "type": "Float"},
            {"name": "fuel_consumed_liters", "type": "Float"},
            {"name": "carbon_emissions_kg", "type": "Float"},
            {"name": "cost", "type": "Float"},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}
        ]
    },

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "LOGISTICS", "SUSTAINABILITY"],
        "related_kpis": ["CARBON_EMISSIONS_PER_UNIT"]
    }
)
