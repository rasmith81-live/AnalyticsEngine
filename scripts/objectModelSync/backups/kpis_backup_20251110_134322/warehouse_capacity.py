"""
Average Warehouse Capacity KPI Definition
"""

WAREHOUSE_CAPACITY = {
    "code": "WAREHOUSE_CAPACITY",
    "name": "Average Warehouse Capacity",
    "display_name": "Average Warehouse Capacity",
    "description": "The average amount of inventory a warehouse can hold over a certain period.",
    "formula": "Total Available Warehouse Space for Inventory / Total Warehouse Capacity",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
