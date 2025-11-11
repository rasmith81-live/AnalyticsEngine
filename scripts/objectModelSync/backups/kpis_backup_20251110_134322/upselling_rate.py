"""
Upselling Rate KPI Definition
"""

UPSELLING_RATE = {
    "code": "UPSELLING_RATE",
    "name": "Upselling Rate",
    "display_name": "Upselling Rate",
    "description": "The percentage of customers who have purchased a more expensive version or upgrade of the product or service they initially bought.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Product"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
