"""
Days of Inventory KPI Definition
"""

DAYS_OF_INVENTORY = {
    "code": "DAYS_OF_INVENTORY",
    "name": "Days of Inventory",
    "display_name": "Days of Inventory",
    "description": "How many days of sales the inventory can support. The KPI is calculated as the average inventory value over a period of time divided by the average daily cost of goods sold.",
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
