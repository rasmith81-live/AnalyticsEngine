"""
Inventory Carrying Cost KPI Definition
"""

INVENTORY_CARRYING_COST = {
    "code": "INVENTORY_CARRYING_COST",
    "name": "Inventory Carrying Cost",
    "display_name": "Inventory Carrying Cost",
    "description": "The total cost of holding inventory including storage, insurance, and taxes.",
    "formula": "Sum of All Inventory-Related Costs / Total Value of Inventory",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Inventory"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
