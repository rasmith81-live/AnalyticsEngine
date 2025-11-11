"""
Labor Cost per Picking Hour KPI Definition
"""

LABOR_COST_PER_PICKING_HOUR = {
    "code": "LABOR_COST_PER_PICKING_HOUR",
    "name": "Labor Cost per Picking Hour",
    "display_name": "Labor Cost per Picking Hour",
    "description": "The labor cost associated with one hour of picking orders.",
    "formula": "Total Labor Costs / Total Picking Hours",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
