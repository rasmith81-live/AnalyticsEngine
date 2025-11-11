"""
Ethical Sourcing Index KPI Definition
"""

ETHICAL_SOURCING_INDEX = {
    "code": "ETHICAL_SOURCING_INDEX",
    "name": "Ethical Sourcing Index",
    "display_name": "Ethical Sourcing Index",
    "description": "A measure of the extent to which sourcing policies and practices align with ethical standards, in accordance with ISO 20400.",
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
