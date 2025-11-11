"""
Percentage of Sustainable Suppliers KPI Definition
"""

PERCENTAGE_OF_SUSTAINABLE_SUPPLIERS = {
    "code": "PERCENTAGE_OF_SUSTAINABLE_SUPPLIERS",
    "name": "Percentage of Sustainable Suppliers",
    "display_name": "Percentage of Sustainable Suppliers",
    "description": "The proportion of suppliers that meet the organization",
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
