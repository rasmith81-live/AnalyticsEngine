"""
Order Fulfillment Lead Time KPI Definition
"""

ORDER_FULFILLMENT_LEAD_TIME = {
    "code": "ORDER_FULFILLMENT_LEAD_TIME",
    "name": "Order Fulfillment Lead Time",
    "display_name": "Order Fulfillment Lead Time",
    "description": "The total time from order receipt to packing and shipping, crucial for assessing the efficiency of order processing.",
    "formula": "Total Order Fulfillment Time / Total Number of Orders",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Lead", "Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
