"""
Supply Chain Sustainability Index KPI Definition
"""

SUPPLY_CHAIN_SUSTAINABILITY_INDEX = {
    "code": "SUPPLY_CHAIN_SUSTAINABILITY_INDEX",
    "name": "Supply Chain Sustainability Index",
    "display_name": "Supply Chain Sustainability Index",
    "description": "A composite metric that evaluates the environmental and social performance of the supply chain operations.",
    "formula": "Sustainability Score based on predefined criteria",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
