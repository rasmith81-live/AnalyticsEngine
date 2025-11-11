"""
Average Lead Score KPI Definition
"""

LEAD_SCORE = {
    "code": "LEAD_SCORE",
    "name": "Average Lead Score",
    "display_name": "Average Lead Score",
    "description": "The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.",
    "formula": "Sum of All Lead Scores / Total Number of Leads",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Lead", "QualityMetric"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}
