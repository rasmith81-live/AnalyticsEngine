"""
Customer Satisfaction Index KPI Definition
"""

CUSTOMER_SATISFACTION_INDEX = {
    "code": "CUSTOMER_SATISFACTION_INDEX",
    "name": "Customer Satisfaction Index",
    "display_name": "Customer Satisfaction Index",
    "description": "A measure of how satisfied customers are with a company",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Product", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
