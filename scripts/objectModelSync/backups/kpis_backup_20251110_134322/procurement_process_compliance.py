"""
Procurement Process Compliance KPI Definition
"""

PROCUREMENT_PROCESS_COMPLIANCE = {
    "code": "PROCUREMENT_PROCESS_COMPLIANCE",
    "name": "Procurement Process Compliance",
    "display_name": "Procurement Process Compliance",
    "description": "The adherence to established procurement policies and procedures.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
