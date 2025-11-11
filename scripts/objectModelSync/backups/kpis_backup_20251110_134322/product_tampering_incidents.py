"""
Product Tampering Incidents KPI Definition
"""

PRODUCT_TAMPERING_INCIDENTS = {
    "code": "PRODUCT_TAMPERING_INCIDENTS",
    "name": "Product Tampering Incidents",
    "display_name": "Product Tampering Incidents",
    "description": "The number of product tampering incidents detected, which affects consumer safety and brand reputation.",
    "formula": "Total Number of Product Tampering Incidents",
    "unit": "count",
    "category": "Iso 28000",
    "aggregation_methods": ["sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Product"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}
