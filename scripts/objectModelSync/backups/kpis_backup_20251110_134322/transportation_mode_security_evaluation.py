"""
Transportation Mode Security Evaluation KPI Definition
"""

TRANSPORTATION_MODE_SECURITY_EVALUATION = {
    "code": "TRANSPORTATION_MODE_SECURITY_EVALUATION",
    "name": "Transportation Mode Security Evaluation",
    "display_name": "Transportation Mode Security Evaluation",
    "description": "The evaluation of security measures specific to different modes of transportation within the supply chain.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
