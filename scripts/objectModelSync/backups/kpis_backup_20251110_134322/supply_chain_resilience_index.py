"""
Supply Chain Resilience Index KPI Definition
"""

SUPPLY_CHAIN_RESILIENCE_INDEX = {
    "code": "SUPPLY_CHAIN_RESILIENCE_INDEX",
    "name": "Supply Chain Resilience Index",
    "display_name": "Supply Chain Resilience Index",
    "description": "A measure of the supply chain",
    "formula": "Supply Chain Resilience Score",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": []
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
