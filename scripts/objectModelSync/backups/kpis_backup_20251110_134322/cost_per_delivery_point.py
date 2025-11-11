"""
Cost per Delivery Point KPI Definition
"""

COST_PER_DELIVERY_POINT = {
    "code": "COST_PER_DELIVERY_POINT",
    "name": "Cost per Delivery Point",
    "display_name": "Cost per Delivery Point",
    "description": "The cost incurred for delivering goods to each individual point.",
    "formula": "Total Delivery Costs / Total Number of Delivery Points",
    "unit": "count",
    "category": "Logistics",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["Delivery", "PurchaseOrder"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}
