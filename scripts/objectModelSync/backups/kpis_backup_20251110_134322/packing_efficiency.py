"""
Packing Efficiency KPI Definition
"""

PACKING_EFFICIENCY = {
    "code": "PACKING_EFFICIENCY",
    "name": "Packing Efficiency",
    "display_name": "Packing Efficiency",
    "description": "The speed and accuracy with which items are packed for shipment.",
    "formula": "Total Time Taken for Packing / Total Number of Orders Packed",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order", "Product", "Shipment"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
