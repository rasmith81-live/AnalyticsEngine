"""
Picking Accuracy KPI Definition
"""

PICKING_ACCURACY = {
    "code": "PICKING_ACCURACY",
    "name": "Picking Accuracy",
    "display_name": "Picking Accuracy",
    "description": "The percentage of orders picked without errors from inventory.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Inventory", "Order"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
