"""
Customer Satisfaction with Delivery KPI Definition
"""

CUSTOMER_SATISFACTION_WITH_DELIVERY = {
    "code": "CUSTOMER_SATISFACTION_WITH_DELIVERY",
    "name": "Customer Satisfaction with Delivery",
    "display_name": "Customer Satisfaction with Delivery",
    "description": "Customer satisfaction with the company",
    "formula": "Average of Customer Delivery Satisfaction Scores",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Customer", "Delivery", "Order"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
