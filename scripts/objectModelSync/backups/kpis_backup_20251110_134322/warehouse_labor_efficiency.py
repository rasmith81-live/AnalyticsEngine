"""
Warehouse Labor Efficiency KPI Definition
"""

WAREHOUSE_LABOR_EFFICIENCY = {
    "code": "WAREHOUSE_LABOR_EFFICIENCY",
    "name": "Warehouse Labor Efficiency",
    "display_name": "Warehouse Labor Efficiency",
    "description": "The overall efficiency of warehouse staff based on output over input.",
    "formula": "Total Number of Orders Fulfilled / Total Labor Hours",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Employee", "Order", "Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
