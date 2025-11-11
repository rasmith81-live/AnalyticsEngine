"""
Stockout Frequency KPI Definition
"""

STOCKOUT_FREQUENCY = {
    "code": "STOCKOUT_FREQUENCY",
    "name": "Stockout Frequency",
    "display_name": "Stockout Frequency",
    "description": "The frequency with which inventory items are out of stock.",
    "formula": "Total Number of Stockouts / Total Number of Inventory Checks",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
