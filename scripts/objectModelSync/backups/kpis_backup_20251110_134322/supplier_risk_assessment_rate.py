"""
Supplier Risk Assessment Rate KPI Definition
"""

SUPPLIER_RISK_ASSESSMENT_RATE = {
    "code": "SUPPLIER_RISK_ASSESSMENT_RATE",
    "name": "Supplier Risk Assessment Rate",
    "display_name": "Supplier Risk Assessment Rate",
    "description": "The frequency at which suppliers are evaluated for risks such as financial stability, geopolitical factors, and natural disasters.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["PurchaseOrder", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
