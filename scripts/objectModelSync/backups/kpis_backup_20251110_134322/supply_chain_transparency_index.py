"""
Supply Chain Transparency Index KPI Definition
"""

SUPPLY_CHAIN_TRANSPARENCY_INDEX = {
    "code": "SUPPLY_CHAIN_TRANSPARENCY_INDEX",
    "name": "Supply Chain Transparency Index",
    "display_name": "Supply Chain Transparency Index",
    "description": "A measure of the visibility and traceability of products and materials throughout the supply chain, as recommended by ISO 20400.",
    "formula": "",
    "unit": "count",
    "category": "Iso 20400",
    "metadata_": {
        "modules": ["ISO_20400"],
        "required_objects": ["Product"]
    },
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
}
