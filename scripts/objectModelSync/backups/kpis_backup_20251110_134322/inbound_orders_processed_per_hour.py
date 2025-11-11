"""
Inbound Orders Processed per Hour KPI Definition
"""

INBOUND_ORDERS_PROCESSED_PER_HOUR = {
    "code": "INBOUND_ORDERS_PROCESSED_PER_HOUR",
    "name": "Inbound Orders Processed per Hour",
    "display_name": "Inbound Orders Processed per Hour",
    "description": "The number of inbound orders processed per hour.",
    "formula": "Total Inbound Orders Processed / Total Hours Worked",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Order"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
