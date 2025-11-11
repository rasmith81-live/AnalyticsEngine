"""
Yield per Mile KPI Definition
"""

YIELD_PER_MILE = {
    "code": "YIELD_PER_MILE",
    "name": "Yield per Mile",
    "display_name": "Yield per Mile",
    "description": "The revenue or profit generated for each mile of transportation.",
    "formula": "Total Revenue / Total Miles Driven",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
