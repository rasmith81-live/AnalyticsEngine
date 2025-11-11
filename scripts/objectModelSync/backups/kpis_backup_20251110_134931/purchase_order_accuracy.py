"""
Purchase Order Accuracy

The degree to which purchase order information is accurate and free from errors.
"""

PURCHASE_ORDER_ACCURACY = {
    "code": "PURCHASE_ORDER_ACCURACY",
    "name": "Purchase Order Accuracy",
    "description": "The degree to which purchase order information is accurate and free from errors.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Purchase Order Accuracy to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:24.009111"},
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
                        793.58,
                        750.94,
                        858.43,
                        831.74,
                        766.32,
                        793.13,
                        744.03,
                        730.81,
                        785.75,
                        796.93,
                        840.2,
                        715.16
                ],
                "unit": "units"
        },
        "current": {
                "value": 715.16,
                "unit": "units",
                "change": -125.04,
                "change_percent": -14.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 783.92,
                "min": 715.16,
                "max": 858.43,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 146.42,
                        "percentage": 20.5
                },
                {
                        "category": "Category B",
                        "value": 149.83,
                        "percentage": 21.0
                },
                {
                        "category": "Category C",
                        "value": 132.77,
                        "percentage": 18.6
                },
                {
                        "category": "Category D",
                        "value": 40.03,
                        "percentage": 5.6
                },
                {
                        "category": "Other",
                        "value": 246.11,
                        "percentage": 34.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.009111",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Purchase Order Accuracy"
        }
    },
}
