"""
Account Penetration Rate KPI Definition
"""

ACCOUNT_PENETRATION_RATE = {
    "code": "ACCOUNT_PENETRATION_RATE",
    "name": "Account Penetration Rate",
    "display_name": "Account Penetration Rate",
    "description": "The percentage of a customer account",
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
