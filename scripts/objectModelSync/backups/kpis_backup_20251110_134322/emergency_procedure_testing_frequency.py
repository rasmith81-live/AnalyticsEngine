"""
Emergency Procedure Testing Frequency KPI Definition
"""

EMERGENCY_PROCEDURE_TESTING_FREQUENCY = {
    "code": "EMERGENCY_PROCEDURE_TESTING_FREQUENCY",
    "name": "Emergency Procedure Testing Frequency",
    "display_name": "Emergency Procedure Testing Frequency",
    "description": "The frequency at which emergency procedures are tested, indicating the preparedness for potential supply chain disruptions.",
    "formula": "Total Number of Emergency Tests and Drills / Time Period",
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
