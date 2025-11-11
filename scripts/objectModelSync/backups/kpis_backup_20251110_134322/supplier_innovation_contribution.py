"""
Supplier Innovation Contribution KPI Definition
"""

SUPPLIER_INNOVATION_CONTRIBUTION = {
    "code": "SUPPLIER_INNOVATION_CONTRIBUTION",
    "name": "Supplier Innovation Contribution",
    "display_name": "Supplier Innovation Contribution",
    "description": "The extent to which suppliers contribute to innovation in products, processes, or services, enhancing competitiveness and value creation.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Product", "Supplier"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
