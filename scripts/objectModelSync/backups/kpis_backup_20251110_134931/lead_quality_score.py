"""
Lead Quality Score

A score assigned to leads based on their perceived value, taking into account factors like job title, industry, company size, and engagement level.
"""

LEAD_QUALITY_SCORE = {
    "code": "LEAD_QUALITY_SCORE",
    "name": "Lead Quality Score",
    "description": "A score assigned to leads based on their perceived value, taking into account factors like job title, industry, company size, and engagement level.",
    "formula": "(Various metrics depending on the lead scoring criteria used)",
    "calculation_formula": "(Various metrics depending on the lead scoring criteria used)",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Lead Quality Score to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "QualityMetric"], "last_validated": "2025-11-10T13:43:23.590546"},
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
                        85.4,
                        84.9,
                        81.3,
                        77.5,
                        87.5,
                        81.4,
                        80.5,
                        82.9,
                        88.1,
                        90.2,
                        83.2,
                        79.8
                ],
                "unit": "score"
        },
        "current": {
                "value": 79.8,
                "unit": "score",
                "change": -3.4,
                "change_percent": -4.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 83.56,
                "min": 77.5,
                "max": 90.2,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21.91,
                        "percentage": 27.5
                },
                {
                        "category": "Category B",
                        "value": 18.07,
                        "percentage": 22.6
                },
                {
                        "category": "Category C",
                        "value": 9.84,
                        "percentage": 12.3
                },
                {
                        "category": "Category D",
                        "value": 8.35,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 21.63,
                        "percentage": 27.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.590546",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Lead Quality Score"
        }
    },
}
