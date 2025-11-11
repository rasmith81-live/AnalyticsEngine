"""
Average Lead Score

The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.
"""

LEAD_SCORE = {
    "code": "LEAD_SCORE",
    "name": "Average Lead Score",
    "description": "The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.",
    "formula": "Sum of All Lead Scores / Total Number of Leads",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Lead Score to be added.",
    "trend_analysis": "Trend analysis to be defined.",
    "diagnostic_questions": """
* What factors are influencing this metric?
* Are there any anomalies in the data?
    """,
    "actionable_tips": """
* Monitor this KPI regularly
* Set appropriate targets and thresholds
    """,
    "visualization_suggestions": """
* Line chart for time series analysis
* Bar chart for comparisons
    """,
    "risk_warnings": "* Monitor for significant deviations from expected values",
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": "* Integrate with related business metrics",
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "QualityMetric"], "last_validated": "2025-11-10T13:43:23.595293"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        125,
                        110,
                        148,
                        124,
                        120,
                        113,
                        135,
                        147,
                        118,
                        137,
                        128,
                        108
                ],
                "unit": "count"
        },
        "current": {
                "value": 108,
                "unit": "count",
                "change": -20,
                "change_percent": -15.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 126.08,
                "min": 108,
                "max": 148,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 25.65,
                        "percentage": 23.8
                },
                {
                        "category": "Category B",
                        "value": 21.2,
                        "percentage": 19.6
                },
                {
                        "category": "Category C",
                        "value": 16.53,
                        "percentage": 15.3
                },
                {
                        "category": "Category D",
                        "value": 6.56,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 38.06,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.595293",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Lead Score"
        }
    },
}
