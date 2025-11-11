"""
Total Order Cycle Time

The total time from when an order is placed until it
"""

ORDER_CYCLE_TIME = {
    "code": "ORDER_CYCLE_TIME",
    "name": "Total Order Cycle Time",
    "description": "The total time from when an order is placed until it",
    "formula": "Sum of Time from Order Placement to Order Delivery / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Inventory Management",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Total Order Cycle Time to be added.",
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
    "metadata_": {"modules": ["INVENTORY_MANAGEMENT"], "required_objects": ["Customer", "Delivery", "Order"], "last_validated": "2025-11-10T13:43:23.738946"},
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
                        158,
                        130,
                        164,
                        134,
                        139,
                        137,
                        155,
                        155,
                        136,
                        146,
                        172,
                        162
                ],
                "unit": "count"
        },
        "current": {
                "value": 162,
                "unit": "count",
                "change": -10,
                "change_percent": -5.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 149.0,
                "min": 130,
                "max": 172,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 45.67,
                        "percentage": 28.2
                },
                {
                        "category": "Category B",
                        "value": 20.75,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 14.89,
                        "percentage": 9.2
                },
                {
                        "category": "Category D",
                        "value": 20.96,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 59.73,
                        "percentage": 36.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.738946",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Total Order Cycle Time"
        }
    },
}
