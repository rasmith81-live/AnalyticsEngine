"""
Packaging Sustainability Score KPI Definition
"""

PACKAGING_SUSTAINABILITY_SCORE = {
    "code": "PACKAGING_SUSTAINABILITY_SCORE",
    "name": "Packaging Sustainability Score",
    "display_name": "Packaging Sustainability Score",
    "description": "A composite score measuring various sustainability factors such as recyclability, biodegradability, and carbon footprint of packaging materials.",
    "formula": "",
    "unit": "count",
    "category": "Packing",
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
