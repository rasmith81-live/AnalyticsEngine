"""
Dock to Stock Time KPI Definition
"""

DOCK_TO_STOCK_TIME = {
    "code": "DOCK_TO_STOCK_TIME",
    "name": "Dock to Stock Time",
    "display_name": "Dock to Stock Time",
    "description": "The time it takes for goods to move from the receiving dock to available inventory.",
    "formula": "Total Dock to Stock Time / Total Number of Shipments",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Shipment"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
