"""
Packing Error Resolution Time KPI Definition
"""

PACKING_ERROR_RESOLUTION_TIME = {
    "code": "PACKING_ERROR_RESOLUTION_TIME",
    "name": "Packing Error Resolution Time",
    "display_name": "Packing Error Resolution Time",
    "description": "The average time taken to resolve packing errors, impacting customer satisfaction and operational efficiency.",
    "formula": "Total Time to Resolve Errors / Total Number of Errors",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Customer"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
