"""
Supplier Security Incident Rate KPI Definition
"""

SUPPLIER_SECURITY_INCIDENT_RATE = {
    "code": "SUPPLIER_SECURITY_INCIDENT_RATE",
    "name": "Supplier Security Incident Rate",
    "display_name": "Supplier Security Incident Rate",
    "description": "The frequency of security incidents originating from suppliers, indicating the security performance of upstream supply chain partners.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Supplier"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
