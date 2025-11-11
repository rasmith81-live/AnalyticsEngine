"""
Packing Error Rate KPI Definition
"""

PACKING_ERROR_RATE = {
    "code": "PACKING_ERROR_RATE",
    "name": "Packing Error Rate",
    "display_name": "Packing Error Rate",
    "description": "The ratio of incorrectly packed items to the total number of items packed, highlighting the accuracy of the packing process.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Order", "Product"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
