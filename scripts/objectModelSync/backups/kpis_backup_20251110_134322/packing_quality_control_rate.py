"""
Packing Quality Control Rate KPI Definition
"""

PACKING_QUALITY_CONTROL_RATE = {
    "code": "PACKING_QUALITY_CONTROL_RATE",
    "name": "Packing Quality Control Rate",
    "display_name": "Packing Quality Control Rate",
    "description": "The percentage of packed items that pass quality control checks, ensuring product integrity and customer satisfaction.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Customer", "Order", "Product", "QualityMetric"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
