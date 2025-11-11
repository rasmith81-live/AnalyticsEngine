"""
Perfect Order Rate KPI Definition
"""

PERFECT_ORDER_RATE = {
    "code": "PERFECT_ORDER_RATE",
    "name": "Perfect Order Rate",
    "display_name": "Perfect Order Rate",
    "description": "The percentage of orders that are delivered on time, complete, and without damage, indicating flawless execution.",
    "formula": "",
    "unit": "count",
    "category": "Iso 22004",
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Order"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
