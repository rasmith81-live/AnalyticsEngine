"""
Lead-to-Opportunity Conversion Rate KPI Definition
"""

LEAD_TO_OPPORTUNITY_CONVERSION_RATE = {
    "code": "LEAD_TO_OPPORTUNITY_CONVERSION_RATE",
    "name": "Lead-to-Opportunity Conversion Rate",
    "display_name": "Lead-to-Opportunity Conversion Rate",
    "description": "The percentage of leads that become sales opportunities, indicating the effectiveness of the lead qualification process.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead", "Opportunity", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
