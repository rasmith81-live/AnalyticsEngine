"""
Supplier Diversity KPI Definition
"""

SUPPLIER_DIVERSITY = {
    "code": "SUPPLIER_DIVERSITY",
    "name": "Supplier Diversity",
    "display_name": "Supplier Diversity",
    "description": "The diversity of the company",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
