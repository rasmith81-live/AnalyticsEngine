"""
Fulfillment Cost per Order KPI Definition
"""

FULFILLMENT_COST_PER_ORDER = {
    "code": "FULFILLMENT_COST_PER_ORDER",
    "name": "Fulfillment Cost per Order",
    "display_name": "Fulfillment Cost per Order",
    "description": "The total cost to fulfill an average order, including labor, materials, and overhead.",
    "formula": "Total Fulfillment Costs / Total Number of Orders Fulfilled",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
