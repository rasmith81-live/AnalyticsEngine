"""
Stakeholder Security Confidence Index

A measure of stakeholders
"""

STAKEHOLDER_SECURITY_CONFIDENCE_INDEX = {
    "code": "STAKEHOLDER_SECURITY_CONFIDENCE_INDEX",
    "name": "Stakeholder Security Confidence Index",
    "description": "A measure of stakeholders",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stakeholder Security Confidence Index to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.784382"},
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
                        86.0,
                        94.5,
                        92.3,
                        84.4,
                        91.7,
                        92.8,
                        85.9,
                        84.9,
                        92.4,
                        91.1,
                        90.2,
                        85.3
                ],
                "unit": "score"
        },
        "current": {
                "value": 85.3,
                "unit": "score",
                "change": -4.9,
                "change_percent": -5.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 89.29,
                "min": 84.4,
                "max": 94.5,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.04,
                        "percentage": 18.8
                },
                {
                        "category": "Category B",
                        "value": 14.03,
                        "percentage": 16.4
                },
                {
                        "category": "Category C",
                        "value": 18.35,
                        "percentage": 21.5
                },
                {
                        "category": "Category D",
                        "value": 6.47,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 30.41,
                        "percentage": 35.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.784382",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Stakeholder Security Confidence Index"
        }
    },
}
