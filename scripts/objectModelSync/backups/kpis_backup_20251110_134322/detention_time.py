"""
Detention Time KPI Definition
"""

DETENTION_TIME = {
    "code": "DETENTION_TIME",
    "name": "Detention Time",
    "display_name": "Detention Time",
    "description": "The time a vehicle spends waiting at a facility beyond the expected loading or unloading time.",
    "formula": "Total Detention Time / Number of Deliveries",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": []
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
