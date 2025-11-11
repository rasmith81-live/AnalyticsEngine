"""
Early Payment Discounts Captured KPI Definition
"""

EARLY_PAYMENT_DISCOUNTS_CAPTURED = {
    "code": "EARLY_PAYMENT_DISCOUNTS_CAPTURED",
    "name": "Early Payment Discounts Captured",
    "display_name": "Early Payment Discounts Captured",
    "description": "The percentage of available early payment discounts that are successfully obtained.",
    "formula": "Total Amount of Discounts for Early Payments / Total Number of Payments",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Payment"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
