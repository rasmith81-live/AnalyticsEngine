"""
Category Management Effectiveness KPI Definition
"""

CATEGORY_MANAGEMENT_EFFECTIVENESS = {
    "code": "CATEGORY_MANAGEMENT_EFFECTIVENESS",
    "name": "Category Management Effectiveness",
    "display_name": "Category Management Effectiveness",
    "description": "The performance of procurement in managing different categories of goods and services.",
    "formula": "Sum of Performance Metrics within a Category / Total Number of Metrics for Category",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": []
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
