"""
Packing Cost Variance KPI Definition
"""

PACKING_COST_VARIANCE = {
    "code": "PACKING_COST_VARIANCE",
    "name": "Packing Cost Variance",
    "display_name": "Packing Cost Variance",
    "description": "The difference between projected and actual packing costs, important for budget management and cost control.",
    "formula": "Actual Packing Costs - Budgeted Packing Costs",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
