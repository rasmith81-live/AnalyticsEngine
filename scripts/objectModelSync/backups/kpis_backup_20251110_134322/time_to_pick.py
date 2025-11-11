"""
Time to Pick KPI Definition
"""

TIME_TO_PICK = {
    "code": "TIME_TO_PICK",
    "name": "Time to Pick",
    "display_name": "Time to Pick",
    "description": "The time it takes to collect items for an order from the warehouse.",
    "formula": "Total Time Taken for Picking / Total Number of Orders Picked",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order", "Product", "Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
