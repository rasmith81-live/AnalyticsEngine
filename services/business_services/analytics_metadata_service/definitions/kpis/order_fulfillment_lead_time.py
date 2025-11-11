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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Lead", "Order"], "last_validated": "2025-11-10T13:49:33.119600"},
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
                        303,
                        319,
                        334,
                        291,
                        333,
                        303,
                        319,
                        302,
                        336,
                        313,
                        317,
                        299
                ],
                "unit": "count"
        },
        "current": {
                "value": 299,
                "unit": "count",
                "change": -18,
                "change_percent": -5.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 314.08,
                "min": 291,
                "max": 336,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 50.89,
                        "percentage": 17.0
                },
                {
                        "category": "Segment B",
                        "value": 64.43,
                        "percentage": 21.5
                },
                {
                        "category": "Segment C",
                        "value": 44.42,
                        "percentage": 14.9
                },
                {
                        "category": "Segment D",
                        "value": 23.45,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 115.81,
                        "percentage": 38.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.312675",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Order Fulfillment Lead Time"
        }
    },
}
