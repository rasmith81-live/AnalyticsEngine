"""
Excess Inventory Rate KPI Definition
"""

EXCESS_INVENTORY_RATE = {
    "code": "EXCESS_INVENTORY_RATE",
    "name": "Excess Inventory Rate",
    "display_name": "Excess Inventory Rate",
    "description": "The percentage of inventory that exceeds the forecasted demand, indicating potential overstock and capital tie-up.",
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
