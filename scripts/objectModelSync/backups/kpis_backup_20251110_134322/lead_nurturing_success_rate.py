"""
Lead Nurturing Success Rate KPI Definition
"""

LEAD_NURTURING_SUCCESS_RATE = {
    "code": "LEAD_NURTURING_SUCCESS_RATE",
    "name": "Lead Nurturing Success Rate",
    "display_name": "Lead Nurturing Success Rate",
    "description": "The percentage of leads that become opportunities as a result of lead nurturing efforts.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead", "PurchaseOrder"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
