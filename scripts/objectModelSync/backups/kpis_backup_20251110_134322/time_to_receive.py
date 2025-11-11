"""
Time to Receive KPI Definition
"""

TIME_TO_RECEIVE = {
    "code": "TIME_TO_RECEIVE",
    "name": "Time to Receive",
    "display_name": "Time to Receive",
    "description": "The time it takes to accept, process, and store incoming goods.",
    "formula": "Total Time Taken for Receiving / Total Number of Deliveries",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "min", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": []
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
