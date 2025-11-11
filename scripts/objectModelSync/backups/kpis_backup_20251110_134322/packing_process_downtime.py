"""
Packing Process Downtime KPI Definition
"""

PACKING_PROCESS_DOWNTIME = {
    "code": "PACKING_PROCESS_DOWNTIME",
    "name": "Packing Process Downtime",
    "display_name": "Packing Process Downtime",
    "description": "The total time when packing operations are halted due to equipment failure or other disruptions, impacting operational efficiency.",
    "formula": "Total Downtime / Total Packing Time",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": []
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
