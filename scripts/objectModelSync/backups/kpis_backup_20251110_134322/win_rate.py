"""
Win Rate KPI Definition
"""

WIN_RATE = {
    "code": "WIN_RATE",
    "name": "Win Rate",
    "display_name": "Win Rate",
    "description": "The percentage of deals won out of the total number of opportunities.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Deal", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
