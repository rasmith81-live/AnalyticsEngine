"""
Local Sourcing Percentage KPI Definition
"""

LOCAL_SOURCING_PERCENTAGE = {
    "code": "LOCAL_SOURCING_PERCENTAGE",
    "name": "Local Sourcing Percentage",
    "display_name": "Local Sourcing Percentage",
    "description": "The proportion of materials and services sourced locally, supporting local economies and reducing transportation emissions as suggested by ISO 20400.",
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
