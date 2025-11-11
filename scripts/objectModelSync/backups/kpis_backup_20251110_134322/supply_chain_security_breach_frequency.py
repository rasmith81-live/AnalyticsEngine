"""
Supply Chain Security Breach Frequency KPI Definition
"""

SUPPLY_CHAIN_SECURITY_BREACH_FREQUENCY = {
    "code": "SUPPLY_CHAIN_SECURITY_BREACH_FREQUENCY",
    "name": "Supply Chain Security Breach Frequency",
    "display_name": "Supply Chain Security Breach Frequency",
    "description": "The number of times the security of the supply chain is breached within a given period, indicating the effectiveness of security measures in place.",
    "formula": "Total Number of Supply Chain Security Breaches / Time Period",
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
