"""
Order Cycle Time Variability

The variation in the time it takes to complete different orders, indicating the consistency of the buying process.
"""

ORDER_CYCLE_TIME_VARIABILITY = {
    "code": "ORDER_CYCLE_TIME_VARIABILITY",
    "name": "Order Cycle Time Variability",
    "description": "The variation in the time it takes to complete different orders, indicating the consistency of the buying process.",
    "formula": "Standard Deviation of Order Cycle Time / Average Order Cycle Time",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Cycle Time Variability to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:43:23.742063"},
    "required_objects": [],
    "modules": ["SOURCING"],
    "module_code": "SOURCING",
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
                        30.7,
                        32.0,
                        27.4,
                        30.0,
                        27.3,
                        27.8,
                        30.9,
                        29.7,
                        32.5,
                        31.9,
                        32.2,
                        28.9
                ],
                "unit": "days"
        },
        "current": {
                "value": 28.9,
                "unit": "days",
                "change": -3.3,
                "change_percent": -10.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 30.11,
                "min": 27.3,
                "max": 32.5,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.9,
                        "percentage": 34.3
                },
                {
                        "category": "Category B",
                        "value": 4.26,
                        "percentage": 14.7
                },
                {
                        "category": "Category C",
                        "value": 3.87,
                        "percentage": 13.4
                },
                {
                        "category": "Category D",
                        "value": 1.46,
                        "percentage": 5.1
                },
                {
                        "category": "Other",
                        "value": 9.41,
                        "percentage": 32.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.742063",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Order Cycle Time Variability"
        }
    },
}
