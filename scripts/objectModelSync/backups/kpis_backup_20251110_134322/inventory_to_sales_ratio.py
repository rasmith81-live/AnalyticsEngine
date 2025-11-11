"""
Inventory to Sales Ratio KPI Definition
"""

INVENTORY_TO_SALES_RATIO = {
    "code": "INVENTORY_TO_SALES_RATIO",
    "name": "Inventory to Sales Ratio",
    "display_name": "Inventory to Sales Ratio",
    "description": "The ratio of inventory on hand to the number of sales orders fulfilled.",
    "formula": "Average Inventory Value / Total Sales",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
