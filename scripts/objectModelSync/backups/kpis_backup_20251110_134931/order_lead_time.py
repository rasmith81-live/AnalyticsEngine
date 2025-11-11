"""
Order Lead Time

The time it takes to fulfill an order, from the moment it is placed to the moment it is delivered to the customer. It helps assess the efficiency of inventory management and order processing.
"""

ORDER_LEAD_TIME = {
    "code": "ORDER_LEAD_TIME",
    "name": "Order Lead Time",
    "description": "The time it takes to fulfill an order, from the moment it is placed to the moment it is delivered to the customer. It helps assess the efficiency of inventory management and order processing.",
    "formula": "Total Time from Order Placement to Delivery / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Lead Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Delivery", "Inventory", "Lead", "Order"], "last_validated": "2025-11-10T13:43:23.747450"},
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
                        315,
                        321,
                        313,
                        355,
                        355,
                        326,
                        328,
                        314,
                        344,
                        351,
                        329,
                        329
                ],
                "unit": "count"
        },
        "current": {
                "value": 329,
                "unit": "count",
                "change": 0,
                "change_percent": 0.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 331.67,
                "min": 313,
                "max": 355,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 75.76,
                        "percentage": 23.0
                },
                {
                        "category": "Category B",
                        "value": 42.26,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 44.62,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 29.96,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 136.4,
                        "percentage": 41.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.747450",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Order Lead Time"
        }
    },
}
