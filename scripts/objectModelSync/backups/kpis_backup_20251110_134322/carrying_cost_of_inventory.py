"""
Carrying Cost of Inventory KPI Definition
"""

CARRYING_COST_OF_INVENTORY = {
    "code": "CARRYING_COST_OF_INVENTORY",
    "name": "Carrying Cost of Inventory",
    "display_name": "Carrying Cost of Inventory",
    "description": "The cost of storing and maintaining inventory, including warehousing, insurance, and depreciation. It helps identify opportunities to reduce inventory costs without sacrificing customer service levels.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Customer", "Inventory", "PurchaseOrder"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
