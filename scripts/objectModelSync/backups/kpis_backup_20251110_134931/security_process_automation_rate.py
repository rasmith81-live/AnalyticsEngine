"""
Security Process Automation Rate

The extent to which security processes are automated, demonstrating the organization
"""

SECURITY_PROCESS_AUTOMATION_RATE = {
    "code": "SECURITY_PROCESS_AUTOMATION_RATE",
    "name": "Security Process Automation Rate",
    "description": "The extent to which security processes are automated, demonstrating the organization",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 28000",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Security Process Automation Rate to be added.",
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
    "metadata_": {"modules": ["ISO_28000"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.731594"},
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
                        60.12,
                        66.76,
                        65.23,
                        72.57,
                        61.9,
                        75.24,
                        70.07,
                        74.51,
                        73.69,
                        64.17,
                        74.2,
                        74.99
                ],
                "unit": "%"
        },
        "current": {
                "value": 74.99,
                "unit": "%",
                "change": 0.79,
                "change_percent": 1.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 69.45,
                "min": 60.12,
                "max": 75.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 21.59,
                        "percentage": 28.8
                },
                {
                        "category": "Category B",
                        "value": 10.82,
                        "percentage": 14.4
                },
                {
                        "category": "Category C",
                        "value": 9.62,
                        "percentage": 12.8
                },
                {
                        "category": "Category D",
                        "value": 7.93,
                        "percentage": 10.6
                },
                {
                        "category": "Other",
                        "value": 25.03,
                        "percentage": 33.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.731594",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Security Process Automation Rate"
        }
    },
}
