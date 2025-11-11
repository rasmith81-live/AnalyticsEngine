"""
Non-Compliant Spend KPI Definition
"""

NON_COMPLIANT_SPEND = {
    "code": "NON_COMPLIANT_SPEND",
    "name": "Non-Compliant Spend",
    "display_name": "Non-Compliant Spend",
    "description": "The amount of spending that does not comply with procurement policies or contracts.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Contract", "PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
