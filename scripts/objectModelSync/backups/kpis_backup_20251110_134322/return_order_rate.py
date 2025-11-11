"""
Return Order Rate KPI Definition
"""

RETURN_ORDER_RATE = {
    "code": "RETURN_ORDER_RATE",
    "name": "Return Order Rate",
    "display_name": "Return Order Rate",
    "description": "The percentage of orders that are returned by customers.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Customer", "Order", "Return"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
