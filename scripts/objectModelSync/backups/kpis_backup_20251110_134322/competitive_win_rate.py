"""
Competitive Win Rate KPI Definition
"""

COMPETITIVE_WIN_RATE = {
    "code": "COMPETITIVE_WIN_RATE",
    "name": "Competitive Win Rate",
    "display_name": "Competitive Win Rate",
    "description": "The percentage of deals won against competitors, indicating the sales team",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Deal"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
