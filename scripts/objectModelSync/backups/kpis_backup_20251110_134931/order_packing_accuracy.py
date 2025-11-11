"""
Order Packing Accuracy

The percentage of orders packed correctly according to customer specifications, indicating the precision of packing operations.
"""

ORDER_PACKING_ACCURACY = {
    "code": "ORDER_PACKING_ACCURACY",
    "name": "Order Packing Accuracy",
    "description": "The percentage of orders packed correctly according to customer specifications, indicating the precision of packing operations.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Packing Accuracy to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer", "Order"], "last_validated": "2025-11-10T13:43:23.749524"},
    "required_objects": [],
    "modules": ["PACKING"],
    "module_code": "PACKING",
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
                        481.55,
                        444.45,
                        463.31,
                        352.38,
                        465.39,
                        396.65,
                        378.02,
                        401.76,
                        337.76,
                        438.49,
                        452.87,
                        444.95
                ],
                "unit": "units"
        },
        "current": {
                "value": 444.95,
                "unit": "units",
                "change": -7.92,
                "change_percent": -1.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 421.46,
                "min": 337.76,
                "max": 481.55,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 96.89,
                        "percentage": 21.8
                },
                {
                        "category": "Category B",
                        "value": 64.8,
                        "percentage": 14.6
                },
                {
                        "category": "Category C",
                        "value": 78.32,
                        "percentage": 17.6
                },
                {
                        "category": "Category D",
                        "value": 57.34,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 147.6,
                        "percentage": 33.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.749524",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Packing Accuracy"
        }
    },
}
