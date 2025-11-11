"""
Cost of Carry KPI Definition
"""

COST_OF_CARRY = {
    "code": "COST_OF_CARRY",
    "name": "Cost of Carry",
    "display_name": "Cost of Carry",
    "description": "The cost associated with holding inventory, including storage, insurance, and taxes.",
    "formula": "Total Carrying Costs / Average Inventory Value",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
