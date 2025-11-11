"""
Time-to-order KPI Definition
"""

TIME_TO_ORDER = {
    "code": "TIME_TO_ORDER",
    "name": "Time-to-order",
    "display_name": "Time-to-order",
    "description": "The time it takes for the buying function to process a purchase request and place an order with a supplier. A shorter time-to-order indicates more efficient processing of requests.",
    "formula": "Total Time for All Identified Needs to Order Placement / Number of Orders",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Order", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
