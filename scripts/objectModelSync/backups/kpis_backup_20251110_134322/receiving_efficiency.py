"""
Receiving Efficiency KPI Definition
"""

RECEIVING_EFFICIENCY = {
    "code": "RECEIVING_EFFICIENCY",
    "name": "Receiving Efficiency",
    "display_name": "Receiving Efficiency",
    "description": "The speed and accuracy of processing incoming goods into the warehouse.",
    "formula": "Total Time Taken for Receiving / Total Number of Shipments Received",
    "unit": "count",
    "category": "Inventory Management",
    "aggregation_methods": ["sum", "min", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["INVENTORY_MANAGEMENT"],
        "required_objects": ["Shipment", "Warehouse"]
    },
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
}
