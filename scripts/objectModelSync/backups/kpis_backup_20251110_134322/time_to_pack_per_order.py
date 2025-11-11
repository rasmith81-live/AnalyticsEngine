"""
Time to Pack per Order KPI Definition
"""

TIME_TO_PACK_PER_ORDER = {
    "code": "TIME_TO_PACK_PER_ORDER",
    "name": "Time to Pack per Order",
    "display_name": "Time to Pack per Order",
    "description": "The average time taken to pack a single order, providing insight into the speed and efficiency of packing operations.",
    "formula": "Total Packing Time / Total Orders Packed",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
