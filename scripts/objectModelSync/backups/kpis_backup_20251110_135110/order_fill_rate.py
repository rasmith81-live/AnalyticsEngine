"""
Order Fill Rate

The percentage of orders that are filled completely and on time. A high fill rate indicates good relationships with suppliers and efficient order processing.
"""

ORDER_FILL_RATE = {
    "code": "ORDER_FILL_RATE",
    "name": "Order Fill Rate",
    "description": "The percentage of orders that are filled completely and on time. A high fill rate indicates good relationships with suppliers and efficient order processing.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Fill Rate to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "Supplier"], "last_validated": "2025-11-10T13:49:33.118008"},
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
                        51.69,
                        48.66,
                        49.65,
                        31.86,
                        39.67,
                        51.48,
                        35.26,
                        50.27,
                        33.15,
                        42.12,
                        43.16,
                        39.53
                ],
                "unit": "%"
        },
        "current": {
                "value": 39.53,
                "unit": "%",
                "change": -3.63,
                "change_percent": -8.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 43.04,
                "min": 31.86,
                "max": 51.69,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 9.94,
                        "percentage": 25.1
                },
                {
                        "category": "Category B",
                        "value": 8.1,
                        "percentage": 20.5
                },
                {
                        "category": "Category C",
                        "value": 5.19,
                        "percentage": 13.1
                },
                {
                        "category": "Category D",
                        "value": 2.31,
                        "percentage": 5.8
                },
                {
                        "category": "Other",
                        "value": 13.99,
                        "percentage": 35.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.744206",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Order Fill Rate"
        }
    },
}
