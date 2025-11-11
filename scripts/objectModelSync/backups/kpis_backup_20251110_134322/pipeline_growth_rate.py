"""
Pipeline Growth Rate KPI Definition
"""

PIPELINE_GROWTH_RATE = {
    "code": "PIPELINE_GROWTH_RATE",
    "name": "Pipeline Growth Rate",
    "display_name": "Pipeline Growth Rate",
    "description": "The rate at which the sales pipeline is growing, indicating the potential for future sales.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
