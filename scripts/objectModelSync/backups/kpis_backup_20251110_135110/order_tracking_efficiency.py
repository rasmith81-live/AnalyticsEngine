"""
Order Tracking Efficiency

The effectiveness of the system used to track order status throughout the delivery process.
"""

ORDER_TRACKING_EFFICIENCY = {
    "code": "ORDER_TRACKING_EFFICIENCY",
    "name": "Order Tracking Efficiency",
    "description": "The effectiveness of the system used to track order status throughout the delivery process.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Logistics",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Tracking Efficiency to be added.",
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
    "metadata_": {"modules": ["LOGISTICS"], "required_objects": ["Delivery", "Order"], "last_validated": "2025-11-10T13:49:33.130559"},
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
                        466.85,
                        391.11,
                        380.67,
                        468.93,
                        478.31,
                        514.98,
                        476.67,
                        435.38,
                        434.33,
                        380.71,
                        444.16,
                        490.94
                ],
                "unit": "units"
        },
        "current": {
                "value": 490.94,
                "unit": "units",
                "change": 46.78,
                "change_percent": 10.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 446.92,
                "min": 380.67,
                "max": 514.98,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 112.55,
                        "percentage": 22.9
                },
                {
                        "category": "Category B",
                        "value": 92.78,
                        "percentage": 18.9
                },
                {
                        "category": "Category C",
                        "value": 52.18,
                        "percentage": 10.6
                },
                {
                        "category": "Category D",
                        "value": 28.1,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 205.33,
                        "percentage": 41.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.764352",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Tracking Efficiency"
        }
    },
}
