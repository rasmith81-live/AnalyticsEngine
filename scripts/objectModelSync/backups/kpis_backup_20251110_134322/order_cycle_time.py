"""
Total Order Cycle Time KPI Definition
"""

ORDER_CYCLE_TIME = {
    "code": "ORDER_CYCLE_TIME",
    "name": "Total Order Cycle Time",
    "display_name": "Total Order Cycle Time",
    "description": "The total time from when an order is placed until it",
    "formula": "Sum of Time from Order Placement to Order Delivery / Total Number of Orders",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Customer", "Delivery", "Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
