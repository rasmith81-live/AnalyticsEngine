"""
Vehicle Maintenance Costs per Mile KPI Definition
"""

VEHICLE_MAINTENANCE_COSTS_PER_MILE = {
    "code": "VEHICLE_MAINTENANCE_COSTS_PER_MILE",
    "name": "Vehicle Maintenance Costs per Mile",
    "display_name": "Vehicle Maintenance Costs per Mile",
    "description": "The cost incurred for maintaining a vehicle per mile driven.",
    "formula": "Total Vehicle Maintenance Costs / Total Miles Driven",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": []
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
