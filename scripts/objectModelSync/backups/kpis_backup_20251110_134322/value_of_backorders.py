"""
Value of Backorders KPI Definition
"""

VALUE_OF_BACKORDERS = {
    "code": "VALUE_OF_BACKORDERS",
    "name": "Value of Backorders",
    "display_name": "Value of Backorders",
    "description": "The monetary value of all backordered items.",
    "formula": "Sum of Product Prices * Quantity Backordered",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
