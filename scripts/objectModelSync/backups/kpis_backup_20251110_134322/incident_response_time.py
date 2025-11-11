"""
Incident Response Time KPI Definition
"""

INCIDENT_RESPONSE_TIME = {
    "code": "INCIDENT_RESPONSE_TIME",
    "name": "Incident Response Time",
    "display_name": "Incident Response Time",
    "description": "The average time it takes for the organization to respond to a supply chain security incident, reflecting the efficiency and preparedness of the response team.",
    "formula": "Sum of Response Times for All Incidents / Number of Incidents",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
