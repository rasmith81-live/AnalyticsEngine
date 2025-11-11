"""
Environmental Impact of Packaging KPI Definition
"""

ENVIRONMENTAL_IMPACT_OF_PACKAGING = {
    "code": "ENVIRONMENTAL_IMPACT_OF_PACKAGING",
    "name": "Environmental Impact of Packaging",
    "display_name": "Environmental Impact of Packaging",
    "description": "A measure of the environmental footprint of packaging materials, assessing sustainability practices in the supply chain.",
    "formula": "Total Environmental Impact Score / Total Packaging Units",
    "unit": "count",
    "category": "Packing",
    "aggregation_methods": ["sum"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["PACKING"],
        "required_objects": []
    },
    "modules": ["PACKING"],
    "module_code": "PACKING",
}
