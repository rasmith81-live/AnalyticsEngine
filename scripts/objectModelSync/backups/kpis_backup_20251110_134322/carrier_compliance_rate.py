"""
Carrier Compliance Rate KPI Definition
"""

CARRIER_COMPLIANCE_RATE = {
    "code": "CARRIER_COMPLIANCE_RATE",
    "name": "Carrier Compliance Rate",
    "display_name": "Carrier Compliance Rate",
    "description": "The percentage of deliveries that comply with the carrier’s requirements and standards.",
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
