"""
Average Warehouse Efficiency KPI Definition
"""

WAREHOUSE_EFFICIENCY = {
    "code": "WAREHOUSE_EFFICIENCY",
    "name": "Average Warehouse Efficiency",
    "display_name": "Average Warehouse Efficiency",
    "description": "The overall efficiency of warehouse operations based on output over input.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Inventory", "Order", "Warehouse"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
