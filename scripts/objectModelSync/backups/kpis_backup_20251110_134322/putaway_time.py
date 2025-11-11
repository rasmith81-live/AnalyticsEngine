"""
Putaway Time KPI Definition
"""

PUTAWAY_TIME = {
    "code": "PUTAWAY_TIME",
    "name": "Putaway Time",
    "display_name": "Putaway Time",
    "description": "The time it takes to store goods in their designated location after receipt.",
    "formula": "Total Time Taken for Putaway / Total Number of Items Putaway",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
