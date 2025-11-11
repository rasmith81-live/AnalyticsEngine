"""
Cross-Border Security Compliance Rate KPI Definition
"""

CROSS_BORDER_SECURITY_COMPLIANCE_RATE = {
    "code": "CROSS_BORDER_SECURITY_COMPLIANCE_RATE",
    "name": "Cross-Border Security Compliance Rate",
    "display_name": "Cross-Border Security Compliance Rate",
    "description": "The rate at which the organization complies with cross-border security regulations, reflecting the ability to operate internationally without security-related disruptions.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Order", "Shipment"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
