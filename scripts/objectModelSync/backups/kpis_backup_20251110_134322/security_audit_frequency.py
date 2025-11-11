"""
Security Audit Frequency KPI Definition
"""

SECURITY_AUDIT_FREQUENCY = {
    "code": "SECURITY_AUDIT_FREQUENCY",
    "name": "Security Audit Frequency",
    "display_name": "Security Audit Frequency",
    "description": "The number of security audits conducted in a given period, which assesses the regularity of security evaluations within the supply chain.",
    "formula": "Total Number of Security Audits / Time Period",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": []
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
