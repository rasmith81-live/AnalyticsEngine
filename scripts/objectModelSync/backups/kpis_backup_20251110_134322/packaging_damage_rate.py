"""
Packaging Damage Rate KPI Definition
"""

PACKAGING_DAMAGE_RATE = {
    "code": "PACKAGING_DAMAGE_RATE",
    "name": "Packaging Damage Rate",
    "display_name": "Packaging Damage Rate",
    "description": "The percentage of packages that are damaged during packing or transit, indicating the need for improved packing materials or processes.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": []
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
