"""
Inventory Health Index KPI Definition
"""

INVENTORY_HEALTH_INDEX = {
    "code": "INVENTORY_HEALTH_INDEX",
    "name": "Inventory Health Index",
    "display_name": "Inventory Health Index",
    "description": "A composite measure assessing the health of inventory including age, turnover, and obsolescence.",
    "formula": "Sum of weighted inventory metrics / Total number of inventory metrics",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "PurchaseOrder"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
