"""
Fleet Utilization Rate KPI Definition
"""

FLEET_UTILIZATION_RATE = {
    "code": "FLEET_UTILIZATION_RATE",
    "name": "Fleet Utilization Rate",
    "display_name": "Fleet Utilization Rate",
    "description": "The percentage of time a fleet is used compared to its availability for use.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
