"""
Deal Size KPI Definition
"""

DEAL_SIZE = {
    "code": "DEAL_SIZE",
    "name": "Deal Size",
    "display_name": "Deal Size",
    "description": "The average value of closed deals.",
    "formula": "Total Revenue from Closed Deals / Number of Closed Deals",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Deal"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
