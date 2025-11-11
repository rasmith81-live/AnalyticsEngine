"""
Loading Efficiency KPI Definition
"""

LOADING_EFFICIENCY = {
    "code": "LOADING_EFFICIENCY",
    "name": "Loading Efficiency",
    "display_name": "Loading Efficiency",
    "description": "The speed and accuracy with which goods are loaded into outbound vehicles.",
    "formula": "Total Time Taken for Loading / Total Number of Shipments Loaded",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Shipment"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
