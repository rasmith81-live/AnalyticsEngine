"""
Maverick Spend KPI Definition
"""

MAVERICK_SPEND = {
    "code": "MAVERICK_SPEND",
    "name": "Maverick Spend",
    "display_name": "Maverick Spend",
    "description": "The percentage of total spend that occurs outside of pre-negotiated contracts or preferred suppliers.",
    "formula": "Total Maverick Spend / Total Spend",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Contract", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
