"""
Security Policy Update Frequency KPI Definition
"""

SECURITY_POLICY_UPDATE_FREQUENCY = {
    "code": "SECURITY_POLICY_UPDATE_FREQUENCY",
    "name": "Security Policy Update Frequency",
    "display_name": "Security Policy Update Frequency",
    "description": "The frequency with which security policies are reviewed and updated, showing the organization",
    "formula": "Total Number of Security Policy Updates / Time Period",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
