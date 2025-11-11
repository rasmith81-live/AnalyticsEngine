"""
Order to Delivery Lead Time KPI Definition
"""

ORDER_TO_DELIVERY_LEAD_TIME = {
    "code": "ORDER_TO_DELIVERY_LEAD_TIME",
    "name": "Order to Delivery Lead Time",
    "display_name": "Order to Delivery Lead Time",
    "description": "The total time taken from when an order is placed to when it is delivered.",
    "formula": "Average Time from Order Placement to Delivery",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "Lead", "Order"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
