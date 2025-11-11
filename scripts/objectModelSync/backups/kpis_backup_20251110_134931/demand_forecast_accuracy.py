"""
Demand Forecast Accuracy

The accuracy of prediction for future demand compared to actual demand, impacting inventory levels and customer satisfaction.
"""

DEMAND_FORECAST_ACCURACY = {
    "code": "DEMAND_FORECAST_ACCURACY",
    "name": "Demand Forecast Accuracy",
    "description": "The accuracy of prediction for future demand compared to actual demand, impacting inventory levels and customer satisfaction.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Demand Forecast Accuracy to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Customer", "Inventory"], "last_validated": "2025-11-10T13:43:23.431691"},
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
                        422.9,
                        539.16,
                        484.21,
                        452.9,
                        486.29,
                        493.25,
                        463.6,
                        519.31,
                        526.32,
                        509.43,
                        457.63,
                        427.72
                ],
                "unit": "units"
        },
        "current": {
                "value": 427.72,
                "unit": "units",
                "change": -29.91,
                "change_percent": -6.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 481.89,
                "min": 422.9,
                "max": 539.16,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 83.72,
                        "percentage": 19.6
                },
                {
                        "category": "Category B",
                        "value": 62.29,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 66.72,
                        "percentage": 15.6
                },
                {
                        "category": "Category D",
                        "value": 39.5,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 175.49,
                        "percentage": 41.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.431691",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Demand Forecast Accuracy"
        }
    },
}
