"""
Contract Compliance Rate KPI Definition
"""

CONTRACT_COMPLIANCE_RATE = {
    "code": "CONTRACT_COMPLIANCE_RATE",
    "name": "Contract Compliance Rate",
    "display_name": "Contract Compliance Rate",
    "description": "The percentage of orders placed that are in compliance with the terms of the company",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Contract", "Order", "Supplier"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
