"""
Security Incident Root Cause Analysis Frequency KPI Definition
"""

SECURITY_INCIDENT_ROOT_CAUSE_ANALYSIS_FREQUENCY = {
    "code": "SECURITY_INCIDENT_ROOT_CAUSE_ANALYSIS_FREQUENCY",
    "name": "Security Incident Root Cause Analysis Frequency",
    "display_name": "Security Incident Root Cause Analysis Frequency",
    "description": "The regularity with which root cause analyses are conducted following security incidents, which is critical for preventing future occurrences.",
    "formula": "Total Number of Root Cause Analyses / Number of Security Incidents",
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
