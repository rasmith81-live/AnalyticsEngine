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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.585902"},
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
                        78.1,
                        77.4,
                        78.2,
                        82.8,
                        82.7,
                        84.0,
                        81.3,
                        76.6,
                        79.8,
                        81.1,
                        80.8,
                        79.5
                ],
                "unit": "score"
        },
        "current": {
                "value": 79.5,
                "unit": "score",
                "change": -1.3,
                "change_percent": -1.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 80.19,
                "min": 76.6,
                "max": 84.0,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 19.75,
                        "percentage": 24.8
                },
                {
                        "category": "Segment B",
                        "value": 20.0,
                        "percentage": 25.2
                },
                {
                        "category": "Segment C",
                        "value": 8.79,
                        "percentage": 11.1
                },
                {
                        "category": "Segment D",
                        "value": 7.04,
                        "percentage": 8.9
                },
                {
                        "category": "Other",
                        "value": 23.92,
                        "percentage": 30.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.409692",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Stakeholder Security Confidence Index"
        }
    },
}
