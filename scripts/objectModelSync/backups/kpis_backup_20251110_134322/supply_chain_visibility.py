"""
Supply Chain Visibility KPI Definition
"""

SUPPLY_CHAIN_VISIBILITY = {
    "code": "SUPPLY_CHAIN_VISIBILITY",
    "name": "Supply Chain Visibility",
    "display_name": "Supply Chain Visibility",
    "description": "The degree to which stakeholders can access real-time data and track products throughout the supply chain, improving decision-making and responsiveness.",
    "formula": "Visibility Score based on traceability and transparency criteria",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "min", "max"],
    "time_periods": ["daily", "weekly", "monthly"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Product", "PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
