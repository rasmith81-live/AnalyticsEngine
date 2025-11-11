"""
Cross-selling Rate KPI Definition
"""

CROSS_SELLING_RATE = {
    "code": "CROSS_SELLING_RATE",
    "name": "Cross-selling Rate",
    "display_name": "Cross-selling Rate",
    "description": "The percentage of customers who have been sold additional, complementary products or services.",
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
