"""
Cost Savings KPI Definition
"""

COST_SAVINGS = {
    "code": "COST_SAVINGS",
    "name": "Cost Savings",
    "display_name": "Cost Savings",
    "description": "The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management.",
    "formula": "Baseline Spend - Current Spend",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": []
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
