"""
Average Deal Discount KPI Definition
"""

DEAL_DISCOUNT = {
    "code": "DEAL_DISCOUNT",
    "name": "Average Deal Discount",
    "display_name": "Average Deal Discount",
    "description": "The average percentage discount applied to deals, which can reflect the sales team",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Deal"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
