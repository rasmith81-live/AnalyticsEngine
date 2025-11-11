"""
Inventory Turnover Ratio KPI Definition
"""

INVENTORY_TURNOVER_RATIO = {
    "code": "INVENTORY_TURNOVER_RATIO",
    "name": "Inventory Turnover Ratio",
    "display_name": "Inventory Turnover Ratio",
    "description": "The rate at which inventory is used and replaced over a certain period.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Inventory"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
