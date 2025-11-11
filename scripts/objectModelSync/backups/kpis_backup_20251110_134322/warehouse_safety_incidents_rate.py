"""
Warehouse Safety Incidents Rate KPI Definition
"""

WAREHOUSE_SAFETY_INCIDENTS_RATE = {
    "code": "WAREHOUSE_SAFETY_INCIDENTS_RATE",
    "name": "Warehouse Safety Incidents Rate",
    "display_name": "Warehouse Safety Incidents Rate",
    "description": "The number of safety incidents recorded in a warehouse per time unit.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Warehouse"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
