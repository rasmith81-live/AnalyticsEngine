"""
Procurement ROI KPI Definition
"""

PROCUREMENT_ROI = {
    "code": "PROCUREMENT_ROI",
    "name": "Procurement ROI",
    "display_name": "Procurement ROI",
    "description": "The return on investment for procurement activities, measuring the cost-effectiveness of the procurement function.",
    "formula": "",
    "unit": "count",
    "category": "Sourcing",
    "metadata_": {
        "modules": ["SOURCING"],
        "required_objects": ["Return"]
    },
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
}
