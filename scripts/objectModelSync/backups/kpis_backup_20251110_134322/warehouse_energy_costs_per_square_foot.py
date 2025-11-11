"""
Warehouse Energy Costs per Square Foot KPI Definition
"""

WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT = {
    "code": "WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT",
    "name": "Warehouse Energy Costs per Square Foot",
    "display_name": "Warehouse Energy Costs per Square Foot",
    "description": "The cost of energy consumption per square foot of warehouse space.",
    "formula": "Total Energy Costs / Total Square Footage of Warehouse",
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
