"""
Order Lead Time KPI Definition
"""

ORDER_LEAD_TIME = {
    "code": "ORDER_LEAD_TIME",
    "name": "Order Lead Time",
    "display_name": "Order Lead Time",
    "description": "The time it takes to fulfill an order, from the moment it is placed to the moment it is delivered to the customer. It helps assess the efficiency of inventory management and order processing.",
    "formula": "Total Time from Order Placement to Delivery / Total Number of Orders",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Customer", "Delivery", "Inventory", "Lead", "Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
