"""
Supplier Risk Assessment KPI Definition
"""

SUPPLIER_RISK_ASSESSMENT = {
    "code": "SUPPLIER_RISK_ASSESSMENT",
    "name": "Supplier Risk Assessment",
    "display_name": "Supplier Risk Assessment",
    "description": "The identification and evaluation of risks associated with a supplier",
    "formula": "Qualitative Risk Score based on Predefined Risk Criteria",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
