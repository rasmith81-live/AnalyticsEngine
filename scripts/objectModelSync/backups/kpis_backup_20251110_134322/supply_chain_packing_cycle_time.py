"""
Supply Chain Packing Cycle Time KPI Definition
"""

SUPPLY_CHAIN_PACKING_CYCLE_TIME = {
    "code": "SUPPLY_CHAIN_PACKING_CYCLE_TIME",
    "name": "Supply Chain Packing Cycle Time",
    "display_name": "Supply Chain Packing Cycle Time",
    "description": "The total time from order placement to packing completion in the supply chain, providing a measure of packing speed and responsiveness.",
    "formula": "Total Packing Cycle Time / Total Orders Packed",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["Order", "PurchaseOrder"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
