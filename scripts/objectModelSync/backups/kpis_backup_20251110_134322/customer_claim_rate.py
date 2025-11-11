"""
Customer Claim Rate KPI Definition
"""

CUSTOMER_CLAIM_RATE = {
    "code": "CUSTOMER_CLAIM_RATE",
    "name": "Customer Claim Rate",
    "display_name": "Customer Claim Rate",
    "description": "The frequency at which customers make claims for undelivered or damaged goods.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Customer"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
