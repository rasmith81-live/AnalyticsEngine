"""
Packing Lead Time KPI Definition
"""

PACKING_LEAD_TIME = {
    "code": "PACKING_LEAD_TIME",
    "name": "Packing Lead Time",
    "display_name": "Packing Lead Time",
    "description": "The time taken from initiating packing operations to the completion of packing, critical for timely deliveries.",
    "formula": "Total Packing Time / Total Orders Packed",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Lead", "Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
