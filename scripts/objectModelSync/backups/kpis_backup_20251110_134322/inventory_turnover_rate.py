"""
Inventory Turnover Rate KPI Definition
"""

INVENTORY_TURNOVER_RATE = {
    "code": "INVENTORY_TURNOVER_RATE",
    "name": "Inventory Turnover Rate",
    "display_name": "Inventory Turnover Rate",
    "description": "How many times inventory is sold and replaced within a given period. It helps determine if inventory levels are too high or too low, and if adjustments are needed to optimize inventory management.",
    "formula": "Cost of Goods Sold / Average Inventory Value",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["average", "min"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
