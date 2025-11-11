"""
Truck Turnaround Time KPI Definition
"""

TRUCK_TURNAROUND_TIME = {
    "code": "TRUCK_TURNAROUND_TIME",
    "name": "Truck Turnaround Time",
    "display_name": "Truck Turnaround Time",
    "description": "The total time from when a truck arrives at a facility until it departs.",
    "formula": "Average Time from Departure to Return for Each Truck",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Return"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
