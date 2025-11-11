"""
Referral Rate KPI Definition
"""

REFERRAL_RATE = {
    "code": "REFERRAL_RATE",
    "name": "Referral Rate",
    "display_name": "Referral Rate",
    "description": "The percentage of new business that comes from referrals by existing customers, which can indicate customer satisfaction and advocacy.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
