"""
Order Fulfillment Lead Time

The total time from order receipt to packing and shipping, crucial for assessing the efficiency of order processing.
"""

ORDER_FULFILLMENT_LEAD_TIME = {
    "code": "ORDER_FULFILLMENT_LEAD_TIME",
    "name": "Order Fulfillment Lead Time",
    "description": "The total time from order receipt to packing and shipping, crucial for assessing the efficiency of order processing.",
    "formula": "Total Order Fulfillment Time / Total Number of Orders",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Fulfillment Lead Time to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Lead", "Order"], "last_validated": "2025-11-10T13:43:23.745760"},
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
                        224,
                        212,
                        187,
                        178,
                        185,
                        227,
                        209,
                        215,
                        215,
                        195,
                        196,
                        189
                ],
                "unit": "count"
        },
        "current": {
                "value": 189,
                "unit": "count",
                "change": -7,
                "change_percent": -3.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 202.67,
                "min": 178,
                "max": 227,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 60.12,
                        "percentage": 31.8
                },
                {
                        "category": "Category B",
                        "value": 27.07,
                        "percentage": 14.3
                },
                {
                        "category": "Category C",
                        "value": 15.92,
                        "percentage": 8.4
                },
                {
                        "category": "Category D",
                        "value": 17.13,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 68.76,
                        "percentage": 36.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.745760",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Order Fulfillment Lead Time"
        }
    },
}
