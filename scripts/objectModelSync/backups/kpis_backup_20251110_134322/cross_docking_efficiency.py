"""
Cross-docking Efficiency KPI Definition
"""

CROSS_DOCKING_EFFICIENCY = {
    "code": "CROSS_DOCKING_EFFICIENCY",
    "name": "Cross-docking Efficiency",
    "display_name": "Cross-docking Efficiency",
    "description": "The effectiveness of moving incoming goods directly to outbound shipping with no storage time.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Product"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
