"""
Information Security Breach Rate

The frequency of breaches in information security within the supply chain, hinting at the robustness of cybersecurity measures.
"""

INFORMATION_SECURITY_BREACH_RATE = {
    "code": "INFORMATION_SECURITY_BREACH_RATE",
    "name": "Information Security Breach Rate",
    "description": "The frequency of breaches in information security within the supply chain, hinting at the robustness of cybersecurity measures.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Information Security Breach Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.973139"},
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
                        82.62,
                        67.24,
                        73.45,
                        80.89,
                        76.11,
                        75.68,
                        64.26,
                        70.53,
                        80.58,
                        70.24,
                        69.95,
                        71.71
                ],
                "unit": "%"
        },
        "current": {
                "value": 71.71,
                "unit": "%",
                "change": 1.76,
                "change_percent": 2.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 73.61,
                "min": 64.26,
                "max": 82.62,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 11.79,
                        "percentage": 16.4
                },
                {
                        "category": "Segment B",
                        "value": 11.31,
                        "percentage": 15.8
                },
                {
                        "category": "Segment C",
                        "value": 9.43,
                        "percentage": 13.2
                },
                {
                        "category": "Segment D",
                        "value": 8.74,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 30.44,
                        "percentage": 42.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.035257",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Information Security Breach Rate"
        }
    },
}
