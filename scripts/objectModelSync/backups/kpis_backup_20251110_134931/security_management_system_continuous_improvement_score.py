"""
Security Management System Continuous Improvement Score

A score that evaluates the extent of continuous improvement efforts applied to the security management system within the supply chain.
"""

SECURITY_MANAGEMENT_SYSTEM_CONTINUOUS_IMPROVEMENT_SCORE = {
    "code": "SECURITY_MANAGEMENT_SYSTEM_CONTINUOUS_IMPROVEMENT_SCORE",
    "name": "Security Management System Continuous Improvement Score",
    "description": "A score that evaluates the extent of continuous improvement efforts applied to the security management system within the supply chain.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Management System Continuous Improvement Score to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.724165"},
    "required_objects": [],
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
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
                        63.5,
                        63.8,
                        67.2,
                        69.7,
                        66.2,
                        62.8,
                        66.8,
                        71.3,
                        65.4,
                        66.6,
                        68.8,
                        70.8
                ],
                "unit": "score"
        },
        "current": {
                "value": 70.8,
                "unit": "score",
                "change": 2.0,
                "change_percent": 2.9,
                "trend": "increasing"
        },
        "statistics": {
                "average": 66.91,
                "min": 62.8,
                "max": 71.3,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.38,
                        "percentage": 27.4
                },
                {
                        "category": "Category B",
                        "value": 8.54,
                        "percentage": 12.1
                },
                {
                        "category": "Category C",
                        "value": 14.4,
                        "percentage": 20.3
                },
                {
                        "category": "Category D",
                        "value": 7.84,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 20.64,
                        "percentage": 29.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.724165",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Security Management System Continuous Improvement Score"
        }
    },
}
