"""
Transportation Cost per Unit KPI Definition
"""

TRANSPORTATION_COST_PER_UNIT = {
    "code": "TRANSPORTATION_COST_PER_UNIT",
    "name": "Transportation Cost per Unit",
    "display_name": "Transportation Cost per Unit",
    "description": "The cost of transportation per unit of product shipped. A lower cost indicates more efficient transportation operations.",
    "formula": "Total Transportation Costs / Total Number of Units Shipped",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Product", "PurchaseOrder"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
