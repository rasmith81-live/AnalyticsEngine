"""
Dock-to-stock Cycle Time KPI Definition
"""

DOCK_TO_STOCK_CYCLE_TIME = {
    "code": "DOCK_TO_STOCK_CYCLE_TIME",
    "name": "Dock-to-stock Cycle Time",
    "display_name": "Dock-to-stock Cycle Time",
    "description": "The time taken to move goods from the receiving dock to the storage area.",
    "formula": "Average Time from Goods Receipt to Warehouse Stocking",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Inventory", "Warehouse"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
