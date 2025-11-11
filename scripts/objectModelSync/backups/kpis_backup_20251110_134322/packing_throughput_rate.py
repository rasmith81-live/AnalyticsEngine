"""
Packing Throughput Rate KPI Definition
"""

PACKING_THROUGHPUT_RATE = {
    "code": "PACKING_THROUGHPUT_RATE",
    "name": "Packing Throughput Rate",
    "display_name": "Packing Throughput Rate",
    "description": "The number of units packed over a specific period, indicating the volume and efficiency of packing operations.",
    "formula": "Total Orders Packed / Total Packing Time",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
