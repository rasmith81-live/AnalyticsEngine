"""
Security Audit Frequency

The number of security audits conducted in a given period, which assesses the regularity of security evaluations within the supply chain.
"""

SECURITY_AUDIT_FREQUENCY = {
    "code": "SECURITY_AUDIT_FREQUENCY",
    "name": "Security Audit Frequency",
    "description": "The number of security audits conducted in a given period, which assesses the regularity of security evaluations within the supply chain.",
    "formula": "Total Number of Security Audits / Time Period",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Audit Frequency to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.704110"},
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
                        418,
                        408,
                        420,
                        429,
                        451,
                        434,
                        430,
                        415,
                        409,
                        409,
                        423,
                        413
                ],
                "unit": "count"
        },
        "current": {
                "value": 413,
                "unit": "count",
                "change": -10,
                "change_percent": -2.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 421.58,
                "min": 408,
                "max": 451,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 70.21,
                        "percentage": 17.0
                },
                {
                        "category": "Category B",
                        "value": 88.15,
                        "percentage": 21.3
                },
                {
                        "category": "Category C",
                        "value": 58.15,
                        "percentage": 14.1
                },
                {
                        "category": "Category D",
                        "value": 33.25,
                        "percentage": 8.1
                },
                {
                        "category": "Other",
                        "value": 163.24,
                        "percentage": 39.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.704110",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Security Audit Frequency"
        }
    },
}
