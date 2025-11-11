"""
Equipment Utilization Rate KPI Definition
"""

EQUIPMENT_UTILIZATION_RATE = {
    "code": "EQUIPMENT_UTILIZATION_RATE",
    "name": "Equipment Utilization Rate",
    "display_name": "Equipment Utilization Rate",
    "description": "The percentage of time warehouse equipment is used compared to its availability.",
    "formula": "Total Operating Time of Equipment / Total Available Time",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
