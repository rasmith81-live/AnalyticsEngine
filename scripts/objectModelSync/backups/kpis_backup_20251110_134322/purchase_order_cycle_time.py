"""
Purchase Order Cycle Time KPI Definition
"""

PURCHASE_ORDER_CYCLE_TIME = {
    "code": "PURCHASE_ORDER_CYCLE_TIME",
    "name": "Purchase Order Cycle Time",
    "display_name": "Purchase Order Cycle Time",
    "description": "The total time taken from the creation of a purchase order to the receipt of the goods or services ordered.",
    "formula": "Total Time for All Purchase Orders / Number of Purchase Orders",
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
