"""
Purchase Order Accuracy KPI Definition
"""

PURCHASE_ORDER_ACCURACY = {
    "code": "PURCHASE_ORDER_ACCURACY",
    "name": "Purchase Order Accuracy",
    "display_name": "Purchase Order Accuracy",
    "description": "The degree to which purchase order information is accurate and free from errors.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Order", "PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
