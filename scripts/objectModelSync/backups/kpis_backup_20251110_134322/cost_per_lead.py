"""
Cost per Lead KPI Definition
"""

COST_PER_LEAD = {
    "code": "COST_PER_LEAD",
    "name": "Cost per Lead",
    "display_name": "Cost per Lead",
    "description": "The average cost incurred to generate one lead, which helps to evaluate the efficiency of marketing campaigns.",
    "formula": "Total Cost of Lead Generation / Total Number of Leads",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
