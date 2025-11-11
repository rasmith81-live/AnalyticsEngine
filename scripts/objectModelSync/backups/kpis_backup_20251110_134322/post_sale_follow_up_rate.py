"""
Post-Sale Follow-Up Rate KPI Definition
"""

POST_SALE_FOLLOW_UP_RATE = {
    "code": "POST_SALE_FOLLOW_UP_RATE",
    "name": "Post-Sale Follow-Up Rate",
    "display_name": "Post-Sale Follow-Up Rate",
    "description": "The rate at which the sales team follows up with customers after a sale has been completed, which can impact customer retention and repeat business.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
