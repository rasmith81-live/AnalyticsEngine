"""
Security Incident Impact Scale

A scale that rates the impact of security incidents, helping to prioritize response efforts and allocate resources effectively.
"""

SECURITY_INCIDENT_IMPACT_SCALE = {
    "code": "SECURITY_INCIDENT_IMPACT_SCALE",
    "name": "Security Incident Impact Scale",
    "description": "A scale that rates the impact of security incidents, helping to prioritize response efforts and allocate resources effectively.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Incident Impact Scale to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:24.711499"},
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
                        646.25,
                        562.56,
                        570.05,
                        653.24,
                        704.49,
                        607.71,
                        604.78,
                        619.47,
                        581.21,
                        653.37,
                        566.34,
                        570.14
                ],
                "unit": "units"
        },
        "current": {
                "value": 570.14,
                "unit": "units",
                "change": 3.8,
                "change_percent": 0.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 611.63,
                "min": 562.56,
                "max": 704.49,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 104.78,
                        "percentage": 18.4
                },
                {
                        "category": "Category B",
                        "value": 142.33,
                        "percentage": 25.0
                },
                {
                        "category": "Category C",
                        "value": 107.29,
                        "percentage": 18.8
                },
                {
                        "category": "Category D",
                        "value": 56.64,
                        "percentage": 9.9
                },
                {
                        "category": "Other",
                        "value": 159.1,
                        "percentage": 27.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.711499",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Security Incident Impact Scale"
        }
    },
}
