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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Lead", "QualityMetric"], "last_validated": "2025-11-10T13:49:33.010575"},
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
                        73.5,
                        68.7,
                        76.5,
                        74.2,
                        70.1,
                        71.4,
                        67.4,
                        74.3,
                        74.0,
                        77.9,
                        79.1,
                        70.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 70.5,
                "unit": "score",
                "change": -8.6,
                "change_percent": -10.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 73.13,
                "min": 67.4,
                "max": 79.1,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 18.0,
                        "percentage": 25.5
                },
                {
                        "category": "Segment B",
                        "value": 8.27,
                        "percentage": 11.7
                },
                {
                        "category": "Segment C",
                        "value": 9.28,
                        "percentage": 13.2
                },
                {
                        "category": "Segment D",
                        "value": 5.48,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 29.47,
                        "percentage": 41.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.119812",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Lead Quality Score"
        }
    },
}
