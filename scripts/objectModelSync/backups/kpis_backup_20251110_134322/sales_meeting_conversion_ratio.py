"""
Sales Meeting Conversion Ratio KPI Definition
"""

SALES_MEETING_CONVERSION_RATIO = {
    "code": "SALES_MEETING_CONVERSION_RATIO",
    "name": "Sales Meeting Conversion Ratio",
    "display_name": "Sales Meeting Conversion Ratio",
    "description": "The proportion of sales meetings or presentations that result in a sale or movement to the next stage of the buying process.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
