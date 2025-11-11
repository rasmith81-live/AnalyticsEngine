"""
Customer Order Cycle Time

The total time taken from receiving a customer order to delivering the product or service, reflecting the speed of the supply chain.
"""

CUSTOMER_ORDER_CYCLE_TIME = {
    "code": "CUSTOMER_ORDER_CYCLE_TIME",
    "name": "Customer Order Cycle Time",
    "description": "The total time taken from receiving a customer order to delivering the product or service, reflecting the speed of the supply chain.",
    "formula": "Time of Order Delivery - Time of Order Placement",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Order Cycle Time to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Customer", "Delivery", "Order", "Product"], "last_validated": "2025-11-10T13:43:23.320472"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        15.3,
                        16.7,
                        21.4,
                        18.0,
                        13.9,
                        18.4,
                        19.4,
                        18.3,
                        15.5,
                        14.9,
                        17.1,
                        20.6
                ],
                "unit": "days"
        },
        "current": {
                "value": 20.6,
                "unit": "days",
                "change": 3.5,
                "change_percent": 20.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 17.46,
                "min": 13.9,
                "max": 21.4,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 3.25,
                        "percentage": 15.8
                },
                {
                        "category": "Category B",
                        "value": 5.18,
                        "percentage": 25.1
                },
                {
                        "category": "Category C",
                        "value": 3.69,
                        "percentage": 17.9
                },
                {
                        "category": "Category D",
                        "value": 2.41,
                        "percentage": 11.7
                },
                {
                        "category": "Other",
                        "value": 6.07,
                        "percentage": 29.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.320472",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Customer Order Cycle Time"
        }
    },
}
