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
                        280.5,
                        319.72,
                        360.84,
                        321.1,
                        325.66,
                        401.61,
                        299.87,
                        313.68,
                        328.21,
                        327.82,
                        308.57,
                        392.37
                ],
                "unit": "units"
        },
        "current": {
                "value": 392.37,
                "unit": "units",
                "change": 83.8,
                "change_percent": 27.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 331.66,
                "min": 280.5,
                "max": 401.61,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 87.21,
                        "percentage": 22.2
                },
                {
                        "category": "Segment B",
                        "value": 92.33,
                        "percentage": 23.5
                },
                {
                        "category": "Segment C",
                        "value": 70.74,
                        "percentage": 18.0
                },
                {
                        "category": "Segment D",
                        "value": 18.81,
                        "percentage": 4.8
                },
                {
                        "category": "Other",
                        "value": 123.28,
                        "percentage": 31.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.339148",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Tracking Efficiency"
        }
    },
}
