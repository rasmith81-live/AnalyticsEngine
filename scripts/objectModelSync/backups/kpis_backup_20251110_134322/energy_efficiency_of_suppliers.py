"""
Energy Efficiency of Suppliers KPI Definition
"""

ENERGY_EFFICIENCY_OF_SUPPLIERS = {
    "code": "ENERGY_EFFICIENCY_OF_SUPPLIERS",
    "name": "Energy Efficiency of Suppliers",
    "display_name": "Energy Efficiency of Suppliers",
    "description": "The average level of energy efficiency among suppliers, reflecting adherence to ISO 20400",
    "formula": "",
    "unit": "count",
    "category": "Iso 20400",
    "metadata_": {
        "modules": ["ISO_20400"],
        "required_objects": ["Supplier"]
    },
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
}
