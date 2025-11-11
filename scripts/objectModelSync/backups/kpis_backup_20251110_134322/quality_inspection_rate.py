"""
Quality Inspection Rate KPI Definition
"""

QUALITY_INSPECTION_RATE = {
    "code": "QUALITY_INSPECTION_RATE",
    "name": "Quality Inspection Rate",
    "display_name": "Quality Inspection Rate",
    "description": "The percentage of incoming goods that undergo quality inspection.",
    "formula": "",
    "unit": "count",
    "category": "Inventory Management",
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Product", "QualityMetric"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
