"""
Procurement Cycle Time KPI Definition
"""

PROCUREMENT_CYCLE_TIME = {
    "code": "PROCUREMENT_CYCLE_TIME",
    "name": "Procurement Cycle Time",
    "display_name": "Procurement Cycle Time",
    "description": "The time taken to complete the procurement process from requisition to purchase order and receiving the goods or services.",
    "formula": "Time of Purchase Order Creation - Time of Requisition",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "min", "max"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Order", "PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
