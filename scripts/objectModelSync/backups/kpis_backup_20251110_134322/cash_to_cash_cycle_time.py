"""
Cash-to-Cash Cycle Time KPI Definition
"""

CASH_TO_CASH_CYCLE_TIME = {
    "code": "CASH_TO_CASH_CYCLE_TIME",
    "name": "Cash-to-Cash Cycle Time",
    "display_name": "Cash-to-Cash Cycle Time",
    "description": "The time between the outlay of cash for raw materials and receiving cash from customers for product sales, impacting liquidity and cash flow.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Customer", "Inventory", "Product"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
