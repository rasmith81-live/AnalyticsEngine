"""
Order Cycle Time Variability KPI Definition
"""

ORDER_CYCLE_TIME_VARIABILITY = {
    "code": "ORDER_CYCLE_TIME_VARIABILITY",
    "name": "Order Cycle Time Variability",
    "display_name": "Order Cycle Time Variability",
    "description": "The variation in the time it takes to complete different orders, indicating the consistency of the buying process.",
    "formula": "Standard Deviation of Order Cycle Time / Average Order Cycle Time",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Order"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
