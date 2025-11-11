"""
Transportation Cost per Unit Shipped KPI Definition
"""

TRANSPORTATION_COST_PER_UNIT_SHIPPED = {
    "code": "TRANSPORTATION_COST_PER_UNIT_SHIPPED",
    "name": "Transportation Cost per Unit Shipped",
    "display_name": "Transportation Cost per Unit Shipped",
    "description": "The average cost associated with transporting a single unit of product, with lower costs indicating a more efficient transportation strategy.",
    "formula": "Total Transportation Costs / Total Units Shipped",
    "unit": "count",
    "category": "Iso 22004",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["ISO_22004"],
        "required_objects": ["Product", "PurchaseOrder"]
    },
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
}
