"""
Packing Cost per Unit KPI Definition
"""

PACKING_COST_PER_UNIT = {
    "code": "PACKING_COST_PER_UNIT",
    "name": "Packing Cost per Unit",
    "display_name": "Packing Cost per Unit",
    "description": "The average cost incurred to pack a single unit, helping to assess cost-efficiency in packing operations.",
    "formula": "Total Packing Costs / Total Units Packed",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["average", "sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": []
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
