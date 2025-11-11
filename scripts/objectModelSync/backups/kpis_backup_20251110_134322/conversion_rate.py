"""
Conversion Rate KPI Definition
"""

CONVERSION_RATE = {
    "code": "CONVERSION_RATE",
    "name": "Conversion Rate",
    "display_name": "Conversion Rate",
    "description": "The percentage of leads that convert into paying customers.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "Lead"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
