"""
Supplier Compliance to Quality Standards KPI Definition
"""

SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS = {
    "code": "SUPPLIER_COMPLIANCE_TO_QUALITY_STANDARDS",
    "name": "Supplier Compliance to Quality Standards",
    "display_name": "Supplier Compliance to Quality Standards",
    "description": "The percentage of suppliers that comply with predefined quality standards, ensuring consistency and reliability in the supply chain.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["QualityMetric", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
