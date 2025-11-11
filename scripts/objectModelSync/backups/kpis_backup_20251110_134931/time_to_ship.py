"""
Time to Ship

The time it takes from receiving an order to shipping it out.
"""

TIME_TO_SHIP = {
    "code": "TIME_TO_SHIP",
    "name": "Time to Ship",
    "description": "The time it takes from receiving an order to shipping it out.",
    "formula": "Total Time Taken for Shipping / Total Number of Orders Shipped",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Ship to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:43:25.058787"},
    "required_objects": [],
    "modules": ["INVENTORY_MANAGEMENT"],
    "module_code": "INVENTORY_MANAGEMENT",
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
                        229,
                        233,
                        261,
                        256,
                        247,
                        259,
                        229,
                        231,
                        255,
                        242,
                        255,
                        229
                ],
                "unit": "count"
        },
        "current": {
                "value": 229,
                "unit": "count",
                "change": -26,
                "change_percent": -10.2,
                "trend": "stable"
        },
        "statistics": {
                "average": 243.83,
                "min": 229,
                "max": 261,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 77.14,
                        "percentage": 33.7
                },
                {
                        "category": "Category B",
                        "value": 51.23,
                        "percentage": 22.4
                },
                {
                        "category": "Category C",
                        "value": 17.07,
                        "percentage": 7.5
                },
                {
                        "category": "Category D",
                        "value": 9.04,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 74.52,
                        "percentage": 32.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.058787",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Ship"
        }
    },
}
