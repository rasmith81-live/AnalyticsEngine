"""
Average Training Hours per Employee KPI Definition
"""

TRAINING_HOURS_PER_EMPLOYEE = {
    "code": "TRAINING_HOURS_PER_EMPLOYEE",
    "name": "Average Training Hours per Employee",
    "display_name": "Average Training Hours per Employee",
    "description": "The average number of training hours provided to each warehouse employee.",
    "formula": "Total Training Hours / Total Number of Employees",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Employee", "Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
