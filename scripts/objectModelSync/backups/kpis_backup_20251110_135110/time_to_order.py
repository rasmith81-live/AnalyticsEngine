"""
Time-to-order

The time it takes for the buying function to process a purchase request and place an order with a supplier. A shorter time-to-order indicates more efficient processing of requests.
"""

TIME_TO_ORDER = {
    "code": "TIME_TO_ORDER",
    "name": "Time-to-order",
    "description": "The time it takes for the buying function to process a purchase request and place an order with a supplier. A shorter time-to-order indicates more efficient processing of requests.",
    "formula": "Total Time for All Identified Needs to Order Placement / Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Sourcing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time-to-order to be added.",
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
    "metadata_": {"modules": ["SOURCING"], "required_objects": ["Order", "Supplier"], "last_validated": "2025-11-10T13:49:33.714023"},
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
                        377,
                        366,
                        371,
                        367,
                        355,
                        346,
                        372,
                        352,
                        371,
                        389,
                        365,
                        382
                ],
                "unit": "count"
        },
        "current": {
                "value": 382,
                "unit": "count",
                "change": 17,
                "change_percent": 4.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 367.75,
                "min": 346,
                "max": 389,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 82.9,
                        "percentage": 21.7
                },
                {
                        "category": "Category B",
                        "value": 90.61,
                        "percentage": 23.7
                },
                {
                        "category": "Category C",
                        "value": 49.48,
                        "percentage": 13.0
                },
                {
                        "category": "Category D",
                        "value": 28.52,
                        "percentage": 7.5
                },
                {
                        "category": "Other",
                        "value": 130.49,
                        "percentage": 34.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.029709",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time-to-order"
        }
    },
}
