"""
Supplier Consolidation Rate KPI Definition
"""

SUPPLIER_CONSOLIDATION_RATE = {
    "code": "SUPPLIER_CONSOLIDATION_RATE",
    "name": "Supplier Consolidation Rate",
    "display_name": "Supplier Consolidation Rate",
    "description": "The extent to which the buying organization has decreased its number of suppliers to optimize the supply base.",
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
