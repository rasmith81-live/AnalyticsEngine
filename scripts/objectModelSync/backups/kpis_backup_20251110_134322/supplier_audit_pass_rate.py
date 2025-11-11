"""
Supplier Audit Pass Rate KPI Definition
"""

SUPPLIER_AUDIT_PASS_RATE = {
    "code": "SUPPLIER_AUDIT_PASS_RATE",
    "name": "Supplier Audit Pass Rate",
    "display_name": "Supplier Audit Pass Rate",
    "description": "The rate at which suppliers pass sustainability audits based on criteria established in ISO 20400.",
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
