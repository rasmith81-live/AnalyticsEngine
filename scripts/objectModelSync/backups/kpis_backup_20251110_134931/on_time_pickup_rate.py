"""
On-time Pickup Rate

The percentage of pickups that occur at the scheduled time.
"""

ON_TIME_PICKUP_RATE = {
    "code": "ON_TIME_PICKUP_RATE",
    "name": "On-time Pickup Rate",
    "description": "The percentage of pickups that occur at the scheduled time.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for On-time Pickup Rate to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": [], "last_validated": "2025-11-10T13:43:23.722829"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        54.09,
                        45.86,
                        42.89,
                        53.78,
                        47.21,
                        50.07,
                        49.42,
                        48.74,
                        52.44,
                        52.98,
                        46.65,
                        37.27
                ],
                "unit": "%"
        },
        "current": {
                "value": 37.27,
                "unit": "%",
                "change": -9.38,
                "change_percent": -20.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 48.45,
                "min": 37.27,
                "max": 54.09,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 10.59,
                        "percentage": 28.4
                },
                {
                        "category": "Category B",
                        "value": 6.0,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 4.19,
                        "percentage": 11.2
                },
                {
                        "category": "Category D",
                        "value": 3.07,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 13.42,
                        "percentage": 36.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.722829",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "On-time Pickup Rate"
        }
    },
}
