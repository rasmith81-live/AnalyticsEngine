"""
Packaging Efficiency Rate KPI Definition
"""

PACKAGING_EFFICIENCY_RATE = {
    "code": "PACKAGING_EFFICIENCY_RATE",
    "name": "Packaging Efficiency Rate",
    "display_name": "Packaging Efficiency Rate",
    "description": "The percentage of packaging operations completed within a set time frame, indicating the effectiveness of packing processes in fulfilling orders swiftly.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Order"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
