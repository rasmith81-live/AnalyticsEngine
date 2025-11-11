"""
Supply Chain Flexibility KPI Definition
"""

SUPPLY_CHAIN_FLEXIBILITY = {
    "code": "SUPPLY_CHAIN_FLEXIBILITY",
    "name": "Supply Chain Flexibility",
    "display_name": "Supply Chain Flexibility",
    "description": "The ability of the supply chain to adapt to changes in demand, supply, and market conditions without significant performance degradation.",
    "formula": "Scored on a predetermined flexibility scale",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["min"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": []
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
