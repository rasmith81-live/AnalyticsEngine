"""
Demo-to-Closing Rate KPI Definition
"""

DEMO_TO_CLOSING_RATE = {
    "code": "DEMO_TO_CLOSING_RATE",
    "name": "Demo-to-Closing Rate",
    "display_name": "Demo-to-Closing Rate",
    "description": "The percentage of product or service demonstrations that result in a closed sale.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Deal", "Product"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
