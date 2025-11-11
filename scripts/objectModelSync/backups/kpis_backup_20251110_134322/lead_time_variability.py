"""
Lead Time Variability KPI Definition
"""

LEAD_TIME_VARIABILITY = {
    "code": "LEAD_TIME_VARIABILITY",
    "name": "Lead Time Variability",
    "display_name": "Lead Time Variability",
    "description": "The consistency of lead times provided by suppliers, with lower variability indicating more reliable delivery.",
    "formula": "Standard Deviation of Lead Times / Average Lead Time",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Delivery", "Lead", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
