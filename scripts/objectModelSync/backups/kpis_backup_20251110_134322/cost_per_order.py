"""
Cost per Order KPI Definition
"""

COST_PER_ORDER = {
    "code": "COST_PER_ORDER",
    "name": "Cost per Order",
    "display_name": "Cost per Order",
    "description": "The total cost of processing a purchase order, including any fees or charges associated with placing the order. A lower cost per order indicates more efficient use of resources.",
    "formula": "Total Cost of Procurement Operations / Total Number of Orders",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Order", "PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
