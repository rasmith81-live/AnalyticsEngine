"""
Stockout Rate


"""

STOCKOUT_RATE = {
    "code": "STOCKOUT_RATE",
    "name": "Stockout Rate",
    "description": "",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "General",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Stockout Rate to be added.",
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
    "metadata_": {"modules": [], "required_objects": [], "last_validated": "2025-11-10T13:43:24.801212"},
    "required_objects": [],
    "modules": [],
    "module_code": "GENERAL",
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
                        60.76,
                        61.09,
                        48.44,
                        55.51,
                        45.51,
                        49.3,
                        61.81,
                        51.75,
                        49.79,
                        48.83,
                        62.14,
                        44.62
                ],
                "unit": "%"
        },
        "current": {
                "value": 44.62,
                "unit": "%",
                "change": -17.52,
                "change_percent": -28.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 53.3,
                "min": 44.62,
                "max": 62.14,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 7.57,
                        "percentage": 17.0
                },
                {
                        "category": "Category B",
                        "value": 11.78,
                        "percentage": 26.4
                },
                {
                        "category": "Category C",
                        "value": 5.12,
                        "percentage": 11.5
                },
                {
                        "category": "Category D",
                        "value": 3.22,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 16.93,
                        "percentage": 37.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.801212",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Stockout Rate"
        }
    },
}
