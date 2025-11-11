"""
Sales Team Response Time KPI Definition
"""

SALES_TEAM_RESPONSE_TIME = {
    "code": "SALES_TEAM_RESPONSE_TIME",
    "name": "Sales Team Response Time",
    "display_name": "Sales Team Response Time",
    "description": "The average time it takes for a sales representative to follow up on a lead or customer inquiry.",
    "formula": "Average Time Taken by Sales Team to Respond to Inquiries",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Lead", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
