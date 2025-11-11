"""
Lead Quality Score KPI Definition
"""

LEAD_QUALITY_SCORE = {
    "code": "LEAD_QUALITY_SCORE",
    "name": "Lead Quality Score",
    "display_name": "Lead Quality Score",
    "description": "A score assigned to leads based on their perceived value, taking into account factors like job title, industry, company size, and engagement level.",
    "formula": "",
    "unit": "count",
    "category": "Business Development",
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead", "QualityMetric"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
