"""
Pickup and Delivery Productivity KPI Definition
"""

PICKUP_AND_DELIVERY_PRODUCTIVITY = {
    "code": "PICKUP_AND_DELIVERY_PRODUCTIVITY",
    "name": "Pickup and Delivery Productivity",
    "display_name": "Pickup and Delivery Productivity",
    "description": "The number of pickups and deliveries made in a given period relative to the resource used.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "Product"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
