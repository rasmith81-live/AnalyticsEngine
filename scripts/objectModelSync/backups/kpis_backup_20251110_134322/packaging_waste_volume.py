"""
Packaging Waste Volume KPI Definition
"""

PACKAGING_WASTE_VOLUME = {
    "code": "PACKAGING_WASTE_VOLUME",
    "name": "Packaging Waste Volume",
    "display_name": "Packaging Waste Volume",
    "description": "The total volume of waste generated from packaging materials, highlighting opportunities for waste reduction and recycling.",
    "formula": "Total Waste Volume / Total Packaging Units",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
