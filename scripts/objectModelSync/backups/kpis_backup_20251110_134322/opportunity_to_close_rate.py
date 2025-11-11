"""
Opportunity-to-Close Rate KPI Definition
"""

OPPORTUNITY_TO_CLOSE_RATE = {
    "code": "OPPORTUNITY_TO_CLOSE_RATE",
    "name": "Opportunity-to-Close Rate",
    "display_name": "Opportunity-to-Close Rate",
    "description": "The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Opportunity", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
