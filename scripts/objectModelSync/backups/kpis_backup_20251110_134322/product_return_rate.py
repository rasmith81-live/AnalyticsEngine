"""
Product Return Rate KPI Definition
"""

PRODUCT_RETURN_RATE = {
    "code": "PRODUCT_RETURN_RATE",
    "name": "Product Return Rate",
    "display_name": "Product Return Rate",
    "description": "The percentage of products that are returned by customers, which can signal issues with product satisfaction or quality.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Product", "QualityMetric", "Return"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
