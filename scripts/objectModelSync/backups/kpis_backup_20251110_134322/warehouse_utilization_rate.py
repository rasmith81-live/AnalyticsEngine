"""
Warehouse Utilization Rate KPI Definition
"""

WAREHOUSE_UTILIZATION_RATE = {
    "code": "WAREHOUSE_UTILIZATION_RATE",
    "name": "Warehouse Utilization Rate",
    "display_name": "Warehouse Utilization Rate",
    "description": "The percentage of warehouse capacity that is currently being used, indicating the effectiveness of space management.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Warehouse"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
