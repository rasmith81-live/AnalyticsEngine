"""
Backorder Level KPI Definition
"""

BACKORDER_LEVEL = {
    "code": "BACKORDER_LEVEL",
    "name": "Backorder Level",
    "display_name": "Backorder Level",
    "description": "The amount of orders that cannot be filled from current inventory.",
    "formula": "Total Number of Backordered Items",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Order", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
