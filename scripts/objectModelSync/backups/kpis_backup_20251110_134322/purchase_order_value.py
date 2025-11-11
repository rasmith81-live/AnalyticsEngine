"""
Average Purchase Order Value KPI Definition
"""

PURCHASE_ORDER_VALUE = {
    "code": "PURCHASE_ORDER_VALUE",
    "name": "Average Purchase Order Value",
    "display_name": "Average Purchase Order Value",
    "description": "The average value of purchase orders over a specific period, indicating purchasing patterns or trends.",
    "formula": "Total Spend / Total Number of Purchase Orders",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Order", "PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
