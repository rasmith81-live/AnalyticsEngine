"""
Inventory Accuracy KPI Definition
"""

INVENTORY_ACCURACY = {
    "code": "INVENTORY_ACCURACY",
    "name": "Inventory Accuracy",
    "display_name": "Inventory Accuracy",
    "description": "How well the inventory records match the physical inventory. The KPI is calculated as the number of items in inventory that match the records divided by the total number of items in inventory.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Inventory", "Product"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
