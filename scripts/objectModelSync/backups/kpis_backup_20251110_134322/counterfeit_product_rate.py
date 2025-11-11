"""
Counterfeit Product Rate KPI Definition
"""

COUNTERFEIT_PRODUCT_RATE = {
    "code": "COUNTERFEIT_PRODUCT_RATE",
    "name": "Counterfeit Product Rate",
    "display_name": "Counterfeit Product Rate",
    "description": "The rate at which counterfeit products are identified within the supply chain, indicating the effectiveness of security measures to protect product authenticity.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Product"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
