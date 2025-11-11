"""
Order Packing Capacity

The maximum number of orders that can be packed within a given time frame, indicating the capability of packing operations.
"""

ORDER_PACKING_CAPACITY = {
    "code": "ORDER_PACKING_CAPACITY",
    "name": "Order Packing Capacity",
    "description": "The maximum number of orders that can be packed within a given time frame, indicating the capability of packing operations.",
    "formula": "Total Orders Packed / Total Packing Time",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Order Packing Capacity to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.124122"},
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
                        724.99,
                        723.26,
                        733.38,
                        728.8,
                        719.24,
                        707.5,
                        802.43,
                        756.19,
                        727.23,
                        773.37,
                        732.82,
                        775.71
                ],
                "unit": "units"
        },
        "current": {
                "value": 775.71,
                "unit": "units",
                "change": 42.89,
                "change_percent": 5.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 742.08,
                "min": 707.5,
                "max": 802.43,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 178.87,
                        "percentage": 23.1
                },
                {
                        "category": "Segment B",
                        "value": 135.47,
                        "percentage": 17.5
                },
                {
                        "category": "Segment C",
                        "value": 98.14,
                        "percentage": 12.7
                },
                {
                        "category": "Segment D",
                        "value": 58.81,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 304.42,
                        "percentage": 39.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.322708",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Packing Capacity"
        }
    },
}
