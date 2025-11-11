"""
Time to Ship KPI Definition
"""

TIME_TO_SHIP = {
    "code": "TIME_TO_SHIP",
    "name": "Time to Ship",
    "display_name": "Time to Ship",
    "description": "The time it takes from receiving an order to shipping it out.",
    "formula": "Total Time Taken for Shipping / Total Number of Orders Shipped",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
