"""
New Business Opportunities Identified KPI Definition
"""

NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED = {
    "code": "NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED",
    "name": "New Business Opportunities Identified",
    "display_name": "New Business Opportunities Identified",
    "description": "The number of new business opportunities identified by the team, indicating the potential for revenue growth.",
    "formula": "Total Number of New Opportunities Identified",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
