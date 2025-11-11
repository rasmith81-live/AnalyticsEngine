"""
Claims Percentage KPI Definition
"""

CLAIMS_PERCENTAGE = {
    "code": "CLAIMS_PERCENTAGE",
    "name": "Claims Percentage",
    "display_name": "Claims Percentage",
    "description": "The percentage of shipments that result in claims for loss or damage.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
