"""
Lead Time Reduction KPI Definition
"""

LEAD_TIME_REDUCTION = {
    "code": "LEAD_TIME_REDUCTION",
    "name": "Lead Time Reduction",
    "display_name": "Lead Time Reduction",
    "description": "The amount by which the time from order placement to delivery is reduced, improving supply chain responsiveness.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Delivery", "Lead", "Order", "PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
