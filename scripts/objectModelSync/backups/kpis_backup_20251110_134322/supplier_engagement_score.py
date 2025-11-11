"""
Supplier Engagement Score KPI Definition
"""

SUPPLIER_ENGAGEMENT_SCORE = {
    "code": "SUPPLIER_ENGAGEMENT_SCORE",
    "name": "Supplier Engagement Score",
    "display_name": "Supplier Engagement Score",
    "description": "The level of supplier involvement in sustainability initiatives, supporting the goals of ISO 20400.",
    "formula": "",
    "unit": "count",
    "category": "Iso 20400",
    "metadata_": {
        "modules": ["ISO_20400"],
        "required_objects": ["PurchaseOrder", "Supplier"]
    },
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
}
