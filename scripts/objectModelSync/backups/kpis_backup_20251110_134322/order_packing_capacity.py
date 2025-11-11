"""
Order Packing Capacity KPI Definition
"""

ORDER_PACKING_CAPACITY = {
    "code": "ORDER_PACKING_CAPACITY",
    "name": "Order Packing Capacity",
    "display_name": "Order Packing Capacity",
    "description": "The maximum number of orders that can be packed within a given time frame, indicating the capability of packing operations.",
    "formula": "Total Orders Packed / Total Packing Time",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum", "max", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
