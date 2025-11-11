"""
Supplier Diversity Rate KPI Definition
"""

SUPPLIER_DIVERSITY_RATE = {
    "code": "SUPPLIER_DIVERSITY_RATE",
    "name": "Supplier Diversity Rate",
    "display_name": "Supplier Diversity Rate",
    "description": "The percentage of the supplier base that is composed of diverse businesses, promoting diversity as per ISO 20400",
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
