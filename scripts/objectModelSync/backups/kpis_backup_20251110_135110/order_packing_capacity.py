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
                        765.13,
                        756.87,
                        809.5,
                        698.41,
                        727.75,
                        698.82,
                        687.67,
                        707.91,
                        765.96,
                        735.87,
                        695.09,
                        782.95
                ],
                "unit": "units"
        },
        "current": {
                "value": 782.95,
                "unit": "units",
                "change": 87.86,
                "change_percent": 12.6,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 735.99,
                "min": 687.67,
                "max": 809.5,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 213.91,
                        "percentage": 27.3
                },
                {
                        "category": "Category B",
                        "value": 96.28,
                        "percentage": 12.3
                },
                {
                        "category": "Category C",
                        "value": 80.46,
                        "percentage": 10.3
                },
                {
                        "category": "Category D",
                        "value": 97.19,
                        "percentage": 12.4
                },
                {
                        "category": "Other",
                        "value": 295.11,
                        "percentage": 37.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.751726",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Order Packing Capacity"
        }
    },
}
