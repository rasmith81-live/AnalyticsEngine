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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.555911"},
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
                        76.0,
                        65.9,
                        75.1,
                        68.4,
                        69.8,
                        70.0,
                        67.9,
                        76.5,
                        66.1,
                        65.0,
                        68.6,
                        69.3
                ],
                "unit": "score"
        },
        "current": {
                "value": 69.3,
                "unit": "score",
                "change": 0.7,
                "change_percent": 1.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 69.88,
                "min": 65.0,
                "max": 76.5,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 17.45,
                        "percentage": 25.2
                },
                {
                        "category": "Segment B",
                        "value": 11.36,
                        "percentage": 16.4
                },
                {
                        "category": "Segment C",
                        "value": 7.43,
                        "percentage": 10.7
                },
                {
                        "category": "Segment D",
                        "value": 5.95,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 27.11,
                        "percentage": 39.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.337469",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Security Management System Continuous Improvement Score"
        }
    },
}
