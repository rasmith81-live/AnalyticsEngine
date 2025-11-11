"""
Green Procurement Spend Share KPI Definition
"""

GREEN_PROCUREMENT_SPEND_SHARE = {
    "code": "GREEN_PROCUREMENT_SPEND_SHARE",
    "name": "Green Procurement Spend Share",
    "display_name": "Green Procurement Spend Share",
    "description": "The share of total procurement spend that goes towards environmentally friendly products and services, as guided by ISO 20400.",
    "formula": "",
    "unit": "count",
    "category": "Iso 20400",
    "metadata_": {
        "modules": ["ISO_20400"],
        "required_objects": ["Product"]
    },
    "modules": ["ISO_20400"],
    "module_code": "ISO_20400",
}
