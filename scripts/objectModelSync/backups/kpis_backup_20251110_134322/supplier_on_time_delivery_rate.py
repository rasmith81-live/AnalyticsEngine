"""
Supplier On-time Delivery Rate KPI Definition
"""

SUPPLIER_ON_TIME_DELIVERY_RATE = {
    "code": "SUPPLIER_ON_TIME_DELIVERY_RATE",
    "name": "Supplier On-time Delivery Rate",
    "display_name": "Supplier On-time Delivery Rate",
    "description": "The percentage of orders delivered by suppliers on or before the promised delivery date, indicating their reliability and efficiency.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Delivery", "Order", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
