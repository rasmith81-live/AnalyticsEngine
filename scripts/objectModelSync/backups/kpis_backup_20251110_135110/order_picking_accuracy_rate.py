"""
Order Picking Accuracy Rate

The percentage of orders picked without errors.
"""

ORDER_PICKING_ACCURACY_RATE = {
    "code": "ORDER_PICKING_ACCURACY_RATE",
    "name": "Order Picking Accuracy Rate",
    "description": "The percentage of orders picked without errors.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Picking Accuracy Rate to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.125481"},
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
                        68.17,
                        75.91,
                        76.79,
                        70.22,
                        62.65,
                        59.96,
                        67.63,
                        74.12,
                        60.19,
                        74.74,
                        77.12,
                        68.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.33,
                "unit": "%",
                "change": -8.79,
                "change_percent": -11.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 69.65,
                "min": 59.96,
                "max": 77.12,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 16.02,
                        "percentage": 23.4
                },
                {
                        "category": "Category B",
                        "value": 15.16,
                        "percentage": 22.2
                },
                {
                        "category": "Category C",
                        "value": 12.62,
                        "percentage": 18.5
                },
                {
                        "category": "Category D",
                        "value": 2.64,
                        "percentage": 3.9
                },
                {
                        "category": "Other",
                        "value": 21.89,
                        "percentage": 32.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.753934",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Order Picking Accuracy Rate"
        }
    },
}
