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
                        11.4,
                        9.0,
                        11.9,
                        9.5,
                        7.2,
                        9.0,
                        9.7,
                        7.3,
                        6.0,
                        12.7,
                        12.9,
                        13.0
                ],
                "unit": "days"
        },
        "current": {
                "value": 13.0,
                "unit": "days",
                "change": 0.1,
                "change_percent": 0.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 9.97,
                "min": 6.0,
                "max": 13.0,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 4.4,
                        "percentage": 33.8
                },
                {
                        "category": "Segment B",
                        "value": 2.21,
                        "percentage": 17.0
                },
                {
                        "category": "Segment C",
                        "value": 2.1,
                        "percentage": 16.2
                },
                {
                        "category": "Segment D",
                        "value": 0.65,
                        "percentage": 5.0
                },
                {
                        "category": "Other",
                        "value": 3.64,
                        "percentage": 28.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.335627",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Order to Delivery Lead Time"
        }
    },
}
