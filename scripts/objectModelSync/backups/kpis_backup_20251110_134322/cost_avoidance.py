"""
Cost Avoidance KPI Definition
"""

COST_AVOIDANCE = {
    "code": "COST_AVOIDANCE",
    "name": "Cost Avoidance",
    "display_name": "Cost Avoidance",
    "description": "The reduction in costs achieved by negotiating better prices or finding more cost-effective purchasing solutions.",
    "formula": "Projected Cost without Procurement Intervention - Actual Cost Post-Intervention",
    "unit": "count",
    "category": "Sourcing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
