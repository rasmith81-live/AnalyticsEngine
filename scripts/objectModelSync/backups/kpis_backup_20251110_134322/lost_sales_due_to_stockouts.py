"""
Lost Sales Due to Stockouts KPI Definition
"""

LOST_SALES_DUE_TO_STOCKOUTS = {
    "code": "LOST_SALES_DUE_TO_STOCKOUTS",
    "name": "Lost Sales Due to Stockouts",
    "display_name": "Lost Sales Due to Stockouts",
    "description": "The estimated sales lost due to items being out of stock.",
    "formula": "Estimated Sales Value of Stockout Items",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Inventory", "Product"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
