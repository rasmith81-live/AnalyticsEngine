"""
Supplier Lead Time KPI Definition
"""

SUPPLIER_LEAD_TIME = {
    "code": "SUPPLIER_LEAD_TIME",
    "name": "Supplier Lead Time",
    "display_name": "Supplier Lead Time",
    "description": "The amount of time between when an order is placed with a supplier and when the order is received.",
    "formula": "Average Time from Order Placement to Receipt",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Lead", "Order", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
