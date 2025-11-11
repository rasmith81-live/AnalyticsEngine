"""
Supplier Lead Time Variability KPI Definition
"""

SUPPLIER_LEAD_TIME_VARIABILITY = {
    "code": "SUPPLIER_LEAD_TIME_VARIABILITY",
    "name": "Supplier Lead Time Variability",
    "display_name": "Supplier Lead Time Variability",
    "description": "The consistency of supplier lead times over a period, with lower variability indicating more reliable delivery schedules.",
    "formula": "Standard Deviation of Supplier Lead Time",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "min", "max"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Delivery", "Lead", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
