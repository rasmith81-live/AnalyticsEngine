"""
Fill Rate KPI Definition
"""

FILL_RATE = {
    "code": "FILL_RATE",
    "name": "Fill Rate",
    "display_name": "Fill Rate",
    "description": "The percentage of customer orders that are filled completely and on time. The KPI is calculated as the number of items shipped on time divided by the total number of items ordered.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Customer", "Order", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
