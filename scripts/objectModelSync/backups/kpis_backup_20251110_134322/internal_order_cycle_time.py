"""
Internal Order Cycle Time KPI Definition
"""

INTERNAL_ORDER_CYCLE_TIME = {
    "code": "INTERNAL_ORDER_CYCLE_TIME",
    "name": "Internal Order Cycle Time",
    "display_name": "Internal Order Cycle Time",
    "description": "The time it takes for the internal warehouse process from order receipt to shipment.",
    "formula": "Total Time for Internal Order Fulfillment / Total Number of Internal Orders",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order", "Shipment", "Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
