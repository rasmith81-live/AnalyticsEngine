"""
Order Tracking Efficiency KPI Definition
"""

ORDER_TRACKING_EFFICIENCY = {
    "code": "ORDER_TRACKING_EFFICIENCY",
    "name": "Order Tracking Efficiency",
    "display_name": "Order Tracking Efficiency",
    "description": "The effectiveness of the system used to track order status throughout the delivery process.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "Order"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
