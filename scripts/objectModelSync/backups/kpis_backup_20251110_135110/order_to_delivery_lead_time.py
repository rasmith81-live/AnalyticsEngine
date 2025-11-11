"""
Order to Delivery Lead Time

The total time taken from when an order is placed to when it is delivered.
"""

ORDER_TO_DELIVERY_LEAD_TIME = {
    "code": "ORDER_TO_DELIVERY_LEAD_TIME",
    "name": "Order to Delivery Lead Time",
    "description": "The total time taken from when an order is placed to when it is delivered.",
    "formula": "Average Time from Order Placement to Delivery",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order to Delivery Lead Time to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "Lead", "Order"], "last_validated": "2025-11-10T13:49:33.129449"},
    "required_objects": [],
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
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
                        12.6,
                        9.5,
                        13.8,
                        7.4,
                        6.7,
                        11.6,
                        10.4,
                        12.9,
                        11.9,
                        10.5,
                        9.6,
                        13.2
                ],
                "unit": "days"
        },
        "current": {
                "value": 13.2,
                "unit": "days",
                "change": 3.6,
                "change_percent": 37.5,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 10.84,
                "min": 6.7,
                "max": 13.8,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.03,
                        "percentage": 23.0
                },
                {
                        "category": "Category B",
                        "value": 3.46,
                        "percentage": 26.2
                },
                {
                        "category": "Category C",
                        "value": 2.35,
                        "percentage": 17.8
                },
                {
                        "category": "Category D",
                        "value": 1.21,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 3.15,
                        "percentage": 23.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.761838",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Order to Delivery Lead Time"
        }
    },
}
