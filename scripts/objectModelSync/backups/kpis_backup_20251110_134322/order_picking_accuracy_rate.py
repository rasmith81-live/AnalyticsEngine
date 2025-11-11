"""
Order Picking Accuracy Rate KPI Definition
"""

ORDER_PICKING_ACCURACY_RATE = {
    "code": "ORDER_PICKING_ACCURACY_RATE",
    "name": "Order Picking Accuracy Rate",
    "display_name": "Order Picking Accuracy Rate",
    "description": "The percentage of orders picked without errors.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
