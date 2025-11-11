"""
Lead Response Time KPI Definition
"""

LEAD_RESPONSE_TIME = {
    "code": "LEAD_RESPONSE_TIME",
    "name": "Lead Response Time",
    "display_name": "Lead Response Time",
    "description": "The time it takes for a sales representative to respond to a new lead.",
    "formula": "Total Time Taken to Respond to Leads / Total Number of Leads",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
