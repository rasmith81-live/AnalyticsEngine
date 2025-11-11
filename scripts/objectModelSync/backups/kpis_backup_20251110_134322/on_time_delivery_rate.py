"""
On-time Delivery Rate KPI Definition
"""

ON_TIME_DELIVERY_RATE = {
    "code": "ON_TIME_DELIVERY_RATE",
    "name": "On-time Delivery Rate",
    "display_name": "On-time Delivery Rate",
    "description": "The percentage of shipments that are delivered on time. A higher rate indicates more efficient and reliable transportation operations.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "PurchaseOrder", "Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
