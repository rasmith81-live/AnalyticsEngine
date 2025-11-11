"""
Security Incident Impact Scale KPI Definition
"""

SECURITY_INCIDENT_IMPACT_SCALE = {
    "code": "SECURITY_INCIDENT_IMPACT_SCALE",
    "name": "Security Incident Impact Scale",
    "display_name": "Security Incident Impact Scale",
    "description": "A scale that rates the impact of security incidents, helping to prioritize response efforts and allocate resources effectively.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
