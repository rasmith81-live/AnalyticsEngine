"""
Picking Productivity KPI Definition
"""

PICKING_PRODUCTIVITY = {
    "code": "PICKING_PRODUCTIVITY",
    "name": "Picking Productivity",
    "display_name": "Picking Productivity",
    "description": "The rate at which items are picked and processed for orders.",
    "formula": "Total Items Picked / Total Picking Hours",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
