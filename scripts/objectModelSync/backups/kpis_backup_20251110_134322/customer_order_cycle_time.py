"""
Customer Order Cycle Time KPI Definition
"""

CUSTOMER_ORDER_CYCLE_TIME = {
    "code": "CUSTOMER_ORDER_CYCLE_TIME",
    "name": "Customer Order Cycle Time",
    "display_name": "Customer Order Cycle Time",
    "description": "The total time taken from receiving a customer order to delivering the product or service, reflecting the speed of the supply chain.",
    "formula": "Time of Order Delivery - Time of Order Placement",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["sum"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Customer", "Delivery", "Order", "Product"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
