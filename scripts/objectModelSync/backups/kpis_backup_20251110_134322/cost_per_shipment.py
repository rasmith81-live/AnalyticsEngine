"""
Cost per Shipment KPI Definition
"""

COST_PER_SHIPMENT = {
    "code": "COST_PER_SHIPMENT",
    "name": "Cost per Shipment",
    "display_name": "Cost per Shipment",
    "description": "The total cost divided by the number of shipments.",
    "formula": "Total Shipping Costs / Total Number of Shipments",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
