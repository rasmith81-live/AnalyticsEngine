"""
Critical Incident Recovery Time

The average time it takes to recover from a critical security incident in the supply chain, demonstrating the resilience of the supply chain operations.
"""

CRITICAL_INCIDENT_RECOVERY_TIME = {
    "code": "CRITICAL_INCIDENT_RECOVERY_TIME",
    "name": "Critical Incident Recovery Time",
    "description": "The average time it takes to recover from a critical security incident in the supply chain, demonstrating the resilience of the supply chain operations.",
    "formula": "Sum of Recovery Times for Critical Incidents / Number of Critical Incidents",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Critical Incident Recovery Time to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.189265"},
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
                        163,
                        164,
                        116,
                        135,
                        146,
                        124,
                        146,
                        142,
                        122,
                        153,
                        142,
                        120
                ],
                "unit": "count"
        },
        "current": {
                "value": 120,
                "unit": "count",
                "change": -22,
                "change_percent": -15.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 139.42,
                "min": 116,
                "max": 164,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.98,
                        "percentage": 15.8
                },
                {
                        "category": "Category B",
                        "value": 29.44,
                        "percentage": 24.5
                },
                {
                        "category": "Category C",
                        "value": 23.28,
                        "percentage": 19.4
                },
                {
                        "category": "Category D",
                        "value": 10.22,
                        "percentage": 8.5
                },
                {
                        "category": "Other",
                        "value": 38.08,
                        "percentage": 31.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.189265",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Critical Incident Recovery Time"
        }
    },
}
