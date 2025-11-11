"""
Warehouse Operating Costs KPI Definition
"""

WAREHOUSE_OPERATING_COSTS = {
    "code": "WAREHOUSE_OPERATING_COSTS",
    "name": "Warehouse Operating Costs",
    "display_name": "Warehouse Operating Costs",
    "description": "The total operating costs of running a warehouse.",
    "formula": "Sum of all Warehouse Operating Costs",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
