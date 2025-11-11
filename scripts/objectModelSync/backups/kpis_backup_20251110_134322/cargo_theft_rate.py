"""
Cargo Theft Rate KPI Definition
"""

CARGO_THEFT_RATE = {
    "code": "CARGO_THEFT_RATE",
    "name": "Cargo Theft Rate",
    "display_name": "Cargo Theft Rate",
    "description": "The frequency of cargo theft incidents per total shipments, illustrating the level of security threats faced by the supply chain.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Shipment"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
