"""
Critical Incident Response Time KPI Definition
"""

CRITICAL_INCIDENT_RESPONSE_TIME = {
    "code": "CRITICAL_INCIDENT_RESPONSE_TIME",
    "name": "Critical Incident Response Time",
    "display_name": "Critical Incident Response Time",
    "description": "The time taken to respond to and address critical incidents in the supply chain, affecting continuity and resilience.",
    "formula": "Time of Incident Resolution - Time of Incident Identification",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "min", "max"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
