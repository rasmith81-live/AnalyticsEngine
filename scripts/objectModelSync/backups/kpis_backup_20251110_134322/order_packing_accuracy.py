"""
Order Packing Accuracy KPI Definition
"""

ORDER_PACKING_ACCURACY = {
    "code": "ORDER_PACKING_ACCURACY",
    "name": "Order Packing Accuracy",
    "display_name": "Order Packing Accuracy",
    "description": "The percentage of orders packed correctly according to customer specifications, indicating the precision of packing operations.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Customer", "Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
