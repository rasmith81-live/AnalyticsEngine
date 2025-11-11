"""
Sales Cycle Length KPI Definition
"""

SALES_CYCLE_LENGTH = {
    "code": "SALES_CYCLE_LENGTH",
    "name": "Sales Cycle Length",
    "display_name": "Sales Cycle Length",
    "description": "The length of time it takes for a lead to become a customer.",
    "formula": "Average Time from First Contact to Deal Closure",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Deal", "Lead"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
