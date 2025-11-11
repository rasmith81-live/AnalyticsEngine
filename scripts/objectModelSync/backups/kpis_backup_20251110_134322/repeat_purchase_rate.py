"""
Repeat Purchase Rate KPI Definition
"""

REPEAT_PURCHASE_RATE = {
    "code": "REPEAT_PURCHASE_RATE",
    "name": "Repeat Purchase Rate",
    "display_name": "Repeat Purchase Rate",
    "description": "The percentage of customers who make more than one purchase, which can indicate customer loyalty and satisfaction with a company",
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
