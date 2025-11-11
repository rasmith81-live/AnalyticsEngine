"""
Early Payment Discounts Captured

The percentage of available early payment discounts that are successfully obtained.
"""

EARLY_PAYMENT_DISCOUNTS_CAPTURED = {
    "code": "EARLY_PAYMENT_DISCOUNTS_CAPTURED",
    "name": "Early Payment Discounts Captured",
    "description": "The percentage of available early payment discounts that are successfully obtained.",
    "formula": "Total Amount of Discounts for Early Payments / Total Number of Payments",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Early Payment Discounts Captured to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Payment"], "last_validated": "2025-11-10T13:49:32.937326"},
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
                        95,
                        99,
                        90,
                        105,
                        78,
                        81,
                        68,
                        98,
                        69,
                        106,
                        76,
                        74
                ],
                "unit": "count"
        },
        "current": {
                "value": 74,
                "unit": "count",
                "change": -2,
                "change_percent": -2.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 86.58,
                "min": 68,
                "max": 106,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 24.32,
                        "percentage": 32.9
                },
                {
                        "category": "Category B",
                        "value": 10.76,
                        "percentage": 14.5
                },
                {
                        "category": "Category C",
                        "value": 11.81,
                        "percentage": 16.0
                },
                {
                        "category": "Category D",
                        "value": 7.9,
                        "percentage": 10.7
                },
                {
                        "category": "Other",
                        "value": 19.21,
                        "percentage": 26.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.457369",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Early Payment Discounts Captured"
        }
    },
}
