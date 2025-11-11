"""
Returns Processing Efficiency KPI Definition
"""

RETURNS_PROCESSING_EFFICIENCY = {
    "code": "RETURNS_PROCESSING_EFFICIENCY",
    "name": "Returns Processing Efficiency",
    "display_name": "Returns Processing Efficiency",
    "description": "The effectiveness of handling and processing returned items.",
    "formula": "Total Time Taken for Processing Returns / Total Number of Returned Items",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Product", "Return"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
