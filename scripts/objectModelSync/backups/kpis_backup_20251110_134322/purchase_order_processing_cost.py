"""
Purchase Order Processing Cost KPI Definition
"""

PURCHASE_ORDER_PROCESSING_COST = {
    "code": "PURCHASE_ORDER_PROCESSING_COST",
    "name": "Purchase Order Processing Cost",
    "display_name": "Purchase Order Processing Cost",
    "description": "The total cost associated with processing each purchase order, including labor, overhead, and technology.",
    "formula": "Total Cost of Processing Purchase Orders / Total Number of Purchase Orders",
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
