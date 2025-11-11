"""
Packing Inventory Turnover Rate KPI Definition
"""

PACKING_INVENTORY_TURNOVER_RATE = {
    "code": "PACKING_INVENTORY_TURNOVER_RATE",
    "name": "Packing Inventory Turnover Rate",
    "display_name": "Packing Inventory Turnover Rate",
    "description": "The rate at which packaging materials are used and replenished, indicating inventory management effectiveness.",
    "formula": "Total Packing Materials Used / Average Packing Inventory",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Inventory"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
