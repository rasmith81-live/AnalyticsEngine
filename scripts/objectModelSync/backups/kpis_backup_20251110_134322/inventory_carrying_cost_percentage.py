"""
Inventory Carrying Cost Percentage KPI Definition
"""

INVENTORY_CARRYING_COST_PERCENTAGE = {
    "code": "INVENTORY_CARRYING_COST_PERCENTAGE",
    "name": "Inventory Carrying Cost Percentage",
    "display_name": "Inventory Carrying Cost Percentage",
    "description": "The percentage of total inventory value that represents the cost of holding inventory, including storage, insurance, and obsolescence.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Inventory"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
