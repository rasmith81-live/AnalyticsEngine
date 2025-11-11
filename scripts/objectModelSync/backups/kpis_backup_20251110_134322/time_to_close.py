"""
Time to Close KPI Definition
"""

TIME_TO_CLOSE = {
    "code": "TIME_TO_CLOSE",
    "name": "Time to Close",
    "display_name": "Time to Close",
    "description": "The time it takes to close a deal from the initial contact with a lead.",
    "formula": "Total Time Taken to Close All Sales / Total Number of Sales Closed",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Deal", "Lead"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
