"""
Linehaul Efficiency KPI Definition
"""

LINEHAUL_EFFICIENCY = {
    "code": "LINEHAUL_EFFICIENCY",
    "name": "Linehaul Efficiency",
    "display_name": "Linehaul Efficiency",
    "description": "The efficiency of transportation between two points excluding pickup and delivery operations.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "PurchaseOrder"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
