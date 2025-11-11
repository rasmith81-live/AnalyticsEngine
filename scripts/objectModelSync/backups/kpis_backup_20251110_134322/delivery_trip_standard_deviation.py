"""
Delivery Trip Standard Deviation KPI Definition
"""

DELIVERY_TRIP_STANDARD_DEVIATION = {
    "code": "DELIVERY_TRIP_STANDARD_DEVIATION",
    "name": "Delivery Trip Standard Deviation",
    "display_name": "Delivery Trip Standard Deviation",
    "description": "The variability in delivery trip duration.",
    "formula": "Standard Deviation of Delivery Trip Distances or Times",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["average", "min", "max"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
