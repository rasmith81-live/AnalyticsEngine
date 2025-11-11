"""
Cost per Order Picked KPI Definition
"""

COST_PER_ORDER_PICKED = {
    "code": "COST_PER_ORDER_PICKED",
    "name": "Cost per Order Picked",
    "display_name": "Cost per Order Picked",
    "description": "The cost associated with picking each order.",
    "formula": "Total Picking Costs / Total Number of Orders Picked",
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
