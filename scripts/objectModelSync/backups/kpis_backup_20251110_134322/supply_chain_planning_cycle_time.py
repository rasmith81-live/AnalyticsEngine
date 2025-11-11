"""
Supply Chain Planning Cycle Time KPI Definition
"""

SUPPLY_CHAIN_PLANNING_CYCLE_TIME = {
    "code": "SUPPLY_CHAIN_PLANNING_CYCLE_TIME",
    "name": "Supply Chain Planning Cycle Time",
    "display_name": "Supply Chain Planning Cycle Time",
    "description": "The time required to create a supply chain plan, with shorter cycles allowing for more agility and responsiveness to changes.",
    "formula": "Total Planning Cycle Time",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
