"""
Outbound Orders Processed per Hour KPI Definition
"""

OUTBOUND_ORDERS_PROCESSED_PER_HOUR = {
    "code": "OUTBOUND_ORDERS_PROCESSED_PER_HOUR",
    "name": "Outbound Orders Processed per Hour",
    "display_name": "Outbound Orders Processed per Hour",
    "description": "The number of outbound orders processed per hour.",
    "formula": "Total Outbound Orders Processed / Total Hours Worked",
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
