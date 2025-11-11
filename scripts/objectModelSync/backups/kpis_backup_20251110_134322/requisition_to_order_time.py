"""
Requisition-to-Order Time KPI Definition
"""

REQUISITION_TO_ORDER_TIME = {
    "code": "REQUISITION_TO_ORDER_TIME",
    "name": "Requisition-to-Order Time",
    "display_name": "Requisition-to-Order Time",
    "description": "The time elapsed from when a purchase requisition is initiated to when the purchase order is created.",
    "formula": "Total Time from Requisition to Purchase Order / Number of Requisitions",
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
