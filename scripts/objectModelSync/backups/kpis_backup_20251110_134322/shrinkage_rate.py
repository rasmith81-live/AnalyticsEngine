"""
Shrinkage Rate KPI Definition
"""

SHRINKAGE_RATE = {
    "code": "SHRINKAGE_RATE",
    "name": "Shrinkage Rate",
    "display_name": "Shrinkage Rate",
    "description": "The percentage of inventory loss between manufacture and point of sale.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "PurchaseOrder"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
