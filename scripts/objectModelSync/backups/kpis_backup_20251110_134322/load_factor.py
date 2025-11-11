"""
Load Factor KPI Definition
"""

LOAD_FACTOR = {
    "code": "LOAD_FACTOR",
    "name": "Load Factor",
    "display_name": "Load Factor",
    "description": "The percentage of a transport vehicle’s available capacity that is being used.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["PurchaseOrder", "Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
