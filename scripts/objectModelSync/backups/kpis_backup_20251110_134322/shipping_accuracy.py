"""
Shipping Accuracy KPI Definition
"""

SHIPPING_ACCURACY = {
    "code": "SHIPPING_ACCURACY",
    "name": "Shipping Accuracy",
    "display_name": "Shipping Accuracy",
    "description": "The percentage of shipments that are correct per the shipping documentation.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Shipment"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
