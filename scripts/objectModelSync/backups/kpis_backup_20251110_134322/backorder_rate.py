"""
Backorder Rate KPI Definition
"""

BACKORDER_RATE = {
    "code": "BACKORDER_RATE",
    "name": "Backorder Rate",
    "display_name": "Backorder Rate",
    "description": "The percentage of orders that cannot be filled immediately and are placed on backorder.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Inventory", "Order", "Product"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
