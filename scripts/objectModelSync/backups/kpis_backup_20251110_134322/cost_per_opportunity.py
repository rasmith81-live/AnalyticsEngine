"""
Cost per Opportunity KPI Definition
"""

COST_PER_OPPORTUNITY = {
    "code": "COST_PER_OPPORTUNITY",
    "name": "Cost per Opportunity",
    "display_name": "Cost per Opportunity",
    "description": "The average cost incurred to turn a lead into a sales opportunity.",
    "formula": "Total Cost of Sales and Marketing / Total Number of Opportunities",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead", "Opportunity", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
