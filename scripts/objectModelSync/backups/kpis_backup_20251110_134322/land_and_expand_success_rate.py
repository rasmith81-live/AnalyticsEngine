"""
Land-and-Expand Success Rate KPI Definition
"""

LAND_AND_EXPAND_SUCCESS_RATE = {
    "code": "LAND_AND_EXPAND_SUCCESS_RATE",
    "name": "Land-and-Expand Success Rate",
    "display_name": "Land-and-Expand Success Rate",
    "description": "The success rate at which initial sales to new customers lead to subsequent sales within the same account, often through additional products or user licenses.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Lead", "Product"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
