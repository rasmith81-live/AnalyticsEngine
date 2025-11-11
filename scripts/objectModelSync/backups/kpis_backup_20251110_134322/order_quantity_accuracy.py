"""
Order Quantity Accuracy KPI Definition
"""

ORDER_QUANTITY_ACCURACY = {
    "code": "ORDER_QUANTITY_ACCURACY",
    "name": "Order Quantity Accuracy",
    "display_name": "Order Quantity Accuracy",
    "description": "The degree to which the quantity ordered matches the quantity needed, reducing overstock or stockouts.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Inventory", "Order"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
