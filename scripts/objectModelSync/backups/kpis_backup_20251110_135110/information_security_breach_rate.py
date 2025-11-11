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
                        66.19,
                        60.42,
                        78.74,
                        61.3,
                        74.76,
                        69.2,
                        68.87,
                        76.75,
                        79.71,
                        76.5,
                        66.87,
                        68.02
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.02,
                "unit": "%",
                "change": 1.15,
                "change_percent": 1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 70.61,
                "min": 60.42,
                "max": 79.71,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 19.47,
                        "percentage": 28.6
                },
                {
                        "category": "Category B",
                        "value": 12.77,
                        "percentage": 18.8
                },
                {
                        "category": "Category C",
                        "value": 6.76,
                        "percentage": 9.9
                },
                {
                        "category": "Category D",
                        "value": 7.25,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 21.77,
                        "percentage": 32.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.522946",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Information Security Breach Rate"
        }
    },
}
