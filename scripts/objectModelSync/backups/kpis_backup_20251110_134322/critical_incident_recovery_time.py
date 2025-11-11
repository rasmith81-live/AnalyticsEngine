"""
Critical Incident Recovery Time KPI Definition
"""

CRITICAL_INCIDENT_RECOVERY_TIME = {
    "code": "CRITICAL_INCIDENT_RECOVERY_TIME",
    "name": "Critical Incident Recovery Time",
    "display_name": "Critical Incident Recovery Time",
    "description": "The average time it takes to recover from a critical security incident in the supply chain, demonstrating the resilience of the supply chain operations.",
    "formula": "Sum of Recovery Times for Critical Incidents / Number of Critical Incidents",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": []
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
