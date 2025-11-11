"""
Packing Flexibility KPI Definition
"""

PACKING_FLEXIBILITY = {
    "code": "PACKING_FLEXIBILITY",
    "name": "Packing Flexibility",
    "display_name": "Packing Flexibility",
    "description": "A measure of the ability to adapt packing operations to changes in demand or product types, indicating operational agility.",
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
