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
                        66.28,
                        80.78,
                        70.53,
                        76.07,
                        81.05,
                        83.25,
                        78.5,
                        66.68,
                        77.07,
                        74.76,
                        74.56,
                        65.42
                ],
                "unit": "%"
        },
        "current": {
                "value": 65.42,
                "unit": "%",
                "change": -9.14,
                "change_percent": -12.3,
                "trend": "stable"
        },
        "statistics": {
                "average": 74.58,
                "min": 65.42,
                "max": 83.25,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.51,
                        "percentage": 34.4
                },
                {
                        "category": "Category B",
                        "value": 10.81,
                        "percentage": 16.5
                },
                {
                        "category": "Category C",
                        "value": 4.89,
                        "percentage": 7.5
                },
                {
                        "category": "Category D",
                        "value": 7.36,
                        "percentage": 11.3
                },
                {
                        "category": "Other",
                        "value": 19.85,
                        "percentage": 30.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.821348",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Strategic Initiative Progress"
        }
    },
}
