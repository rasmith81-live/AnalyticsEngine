"""
Strategic Initiative Progress

A measure of the progress of key business initiatives against strategic goals.
"""

STRATEGIC_INITIATIVE_PROGRESS = {
    "code": "STRATEGIC_INITIATIVE_PROGRESS",
    "name": "Strategic Initiative Progress",
    "description": "A measure of the progress of key business initiatives against strategic goals.",
    "formula": "(Sum of Completed Milestones or Objectives / Total Planned Milestones or Objectives) * 100",
    "calculation_formula": "(Sum of Completed Milestones or Objectives / Total Planned Milestones or Objectives) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Strategic Initiative Progress to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.606394"},
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
                        47.78,
                        48.13,
                        44.04,
                        59.02,
                        48.84,
                        43.04,
                        48.73,
                        50.39,
                        42.59,
                        48.76,
                        48.54,
                        53.51
                ],
                "unit": "%"
        },
        "current": {
                "value": 53.51,
                "unit": "%",
                "change": 4.97,
                "change_percent": 10.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 48.61,
                "min": 42.59,
                "max": 59.02,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.09,
                        "percentage": 22.6
                },
                {
                        "category": "Segment B",
                        "value": 11.16,
                        "percentage": 20.9
                },
                {
                        "category": "Segment C",
                        "value": 6.21,
                        "percentage": 11.6
                },
                {
                        "category": "Segment D",
                        "value": 5.56,
                        "percentage": 10.4
                },
                {
                        "category": "Other",
                        "value": 18.49,
                        "percentage": 34.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.474659",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Initiative Progress"
        }
    },
}
