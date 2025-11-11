"""
Customer Retention Rate KPI Definition
"""

CUSTOMER_RETENTION_RATE = {
    "code": "CUSTOMER_RETENTION_RATE",
    "name": "Customer Retention Rate",
    "display_name": "Customer Retention Rate",
    "description": "The percentage of customers who remain with the company over a specified period, indicating the success of customer satisfaction and retention strategies.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
