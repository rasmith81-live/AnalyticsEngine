"""
Supplier Compliance Rate KPI Definition
"""

SUPPLIER_COMPLIANCE_RATE = {
    "code": "SUPPLIER_COMPLIANCE_RATE",
    "name": "Supplier Compliance Rate",
    "display_name": "Supplier Compliance Rate",
    "description": "The percentage of suppliers that comply with the sustainability standards and requirements set out in ISO 20400.",
    "formula": "",
    "unit": "count",
    "category": "Iso 20400",
    "metadata_": {
        "modules": ["ISO_20400"],
        "required_objects": ["Supplier"]
    },
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
}
