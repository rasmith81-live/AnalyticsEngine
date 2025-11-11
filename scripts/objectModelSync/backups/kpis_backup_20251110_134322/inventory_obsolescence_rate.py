"""
Inventory Obsolescence Rate KPI Definition
"""

INVENTORY_OBSOLESCENCE_RATE = {
    "code": "INVENTORY_OBSOLESCENCE_RATE",
    "name": "Inventory Obsolescence Rate",
    "display_name": "Inventory Obsolescence Rate",
    "description": "The percentage of inventory that becomes obsolete before it is sold or used, reflecting product lifecycle management effectiveness.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Inventory", "Product"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
