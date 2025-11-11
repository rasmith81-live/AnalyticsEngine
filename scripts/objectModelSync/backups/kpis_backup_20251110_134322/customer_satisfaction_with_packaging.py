"""
Customer Satisfaction with Packaging KPI Definition
"""

CUSTOMER_SATISFACTION_WITH_PACKAGING = {
    "code": "CUSTOMER_SATISFACTION_WITH_PACKAGING",
    "name": "Customer Satisfaction with Packaging",
    "display_name": "Customer Satisfaction with Packaging",
    "description": "The level of customer satisfaction with the quality and condition of packaging upon delivery, impacting customer loyalty.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Customer", "Delivery", "PurchaseOrder", "QualityMetric"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
