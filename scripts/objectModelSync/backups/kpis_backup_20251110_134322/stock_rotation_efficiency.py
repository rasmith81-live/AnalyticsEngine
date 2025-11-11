"""
Stock Rotation Efficiency KPI Definition
"""

STOCK_ROTATION_EFFICIENCY = {
    "code": "STOCK_ROTATION_EFFICIENCY",
    "name": "Stock Rotation Efficiency",
    "display_name": "Stock Rotation Efficiency",
    "description": "The effectiveness of inventory management practices in rotating stock before it becomes outdated or expires.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
