"""
On-time Shipment Rate KPI Definition
"""

ON_TIME_SHIPMENT_RATE = {
    "code": "ON_TIME_SHIPMENT_RATE",
    "name": "On-time Shipment Rate",
    "display_name": "On-time Shipment Rate",
    "description": "The percentage of orders shipped on or before the requested ship date.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order", "Shipment"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
