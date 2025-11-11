"""
Supply Chain Training Investment KPI Definition
"""

SUPPLY_CHAIN_TRAINING_INVESTMENT = {
    "code": "SUPPLY_CHAIN_TRAINING_INVESTMENT",
    "name": "Supply Chain Training Investment",
    "display_name": "Supply Chain Training Investment",
    "description": "The amount invested in employee training to improve supply chain skills and knowledge, contributing to performance improvements.",
    "formula": "Total Spend on Supply Chain Training",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Employee"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
