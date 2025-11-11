"""
Cost per Ton-Mile KPI Definition
"""

COST_PER_TON_MILE = {
    "code": "COST_PER_TON_MILE",
    "name": "Cost per Ton-Mile",
    "display_name": "Cost per Ton-Mile",
    "description": "The cost to transport one ton of material one mile.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["PurchaseOrder", "Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
