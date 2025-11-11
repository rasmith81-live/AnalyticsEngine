"""
Shipment Integrity Incidents KPI Definition
"""

SHIPMENT_INTEGRITY_INCIDENTS = {
    "code": "SHIPMENT_INTEGRITY_INCIDENTS",
    "name": "Shipment Integrity Incidents",
    "display_name": "Shipment Integrity Incidents",
    "description": "The number of incidents where a shipment",
    "formula": "Total Number of Shipment Integrity Incidents",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder", "Shipment"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
