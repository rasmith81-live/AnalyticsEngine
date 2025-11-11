"""
Critical Incident Response Time

The time taken to respond to and address critical incidents in the supply chain, affecting continuity and resilience.
"""

CRITICAL_INCIDENT_RESPONSE_TIME = {
    "code": "CRITICAL_INCIDENT_RESPONSE_TIME",
    "name": "Critical Incident Response Time",
    "description": "The time taken to respond to and address critical incidents in the supply chain, affecting continuity and resilience.",
    "formula": "Time of Incident Resolution - Time of Incident Identification",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Critical Incident Response Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["PurchaseOrder"], "last_validated": "2025-11-10T13:43:23.190271"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        23.4,
                        18.9,
                        18.1,
                        17.5,
                        20.7,
                        24.2,
                        16.6,
                        18.8,
                        20.1,
                        20.6,
                        17.6,
                        19.5
                ],
                "unit": "days"
        },
        "current": {
                "value": 19.5,
                "unit": "days",
                "change": 1.9,
                "change_percent": 10.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 19.67,
                "min": 16.6,
                "max": 24.2,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.4,
                        "percentage": 17.4
                },
                {
                        "category": "Category B",
                        "value": 5.4,
                        "percentage": 27.7
                },
                {
                        "category": "Category C",
                        "value": 1.79,
                        "percentage": 9.2
                },
                {
                        "category": "Category D",
                        "value": 2.38,
                        "percentage": 12.2
                },
                {
                        "category": "Other",
                        "value": 6.53,
                        "percentage": 33.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.190271",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Critical Incident Response Time"
        }
    },
}
