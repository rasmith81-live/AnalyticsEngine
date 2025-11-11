"""
Contract Renewal Rate KPI Definition
"""

CONTRACT_RENEWAL_RATE = {
    "code": "CONTRACT_RENEWAL_RATE",
    "name": "Contract Renewal Rate",
    "display_name": "Contract Renewal Rate",
    "description": "The percentage of contracts that are renewed at the end of their term, indicating customer satisfaction and the",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Contract", "Customer"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
