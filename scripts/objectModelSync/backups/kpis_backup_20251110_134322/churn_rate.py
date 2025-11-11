"""
Churn Rate KPI Definition
"""

CHURN_RATE = {
    "code": "CHURN_RATE",
    "name": "Churn Rate",
    "display_name": "Churn Rate",
    "description": "The percentage of customers or subscribers who stop using a company",
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
