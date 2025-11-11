"""
Opportunity Pipeline KPI Definition
"""

OPPORTUNITY_PIPELINE = {
    "code": "OPPORTUNITY_PIPELINE",
    "name": "Opportunity Pipeline",
    "display_name": "Opportunity Pipeline",
    "description": "The number of opportunities in the pipeline and their value.",
    "formula": "Sum of All Opportunities at Various Stages of the Sales Cycle",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Opportunity", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
