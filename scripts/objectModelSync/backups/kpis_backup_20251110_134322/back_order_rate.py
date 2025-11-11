"""
Back Order Rate KPI Definition
"""

BACK_ORDER_RATE = {
    "code": "BACK_ORDER_RATE",
    "name": "Back Order Rate",
    "display_name": "Back Order Rate",
    "description": "The percentage of orders that cannot be filled at the time of customer order.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Customer", "Order", "Product"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
