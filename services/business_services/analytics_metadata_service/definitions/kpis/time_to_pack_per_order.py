"""
Time to Pack per Order

The average time taken to pack a single order, providing insight into the speed and efficiency of packing operations.
"""

TIME_TO_PACK_PER_ORDER = {
    "code": "TIME_TO_PACK_PER_ORDER",
    "name": "Time to Pack per Order",
    "description": "The average time taken to pack a single order, providing insight into the speed and efficiency of packing operations.",
    "formula": "Total Packing Time / Total Orders Packed",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Pack per Order to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Order"], "last_validated": "2025-11-10T13:49:33.715974"},
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
                        8.4,
                        10.9,
                        7.1,
                        3.6,
                        6.0,
                        3.7,
                        9.4,
                        6.3,
                        10.7,
                        6.6,
                        4.5,
                        6.3
                ],
                "unit": "days"
        },
        "current": {
                "value": 6.3,
                "unit": "days",
                "change": 1.8,
                "change_percent": 40.0,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 6.96,
                "min": 3.6,
                "max": 10.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 2.17,
                        "percentage": 34.4
                },
                {
                        "category": "Segment B",
                        "value": 1.36,
                        "percentage": 21.6
                },
                {
                        "category": "Segment C",
                        "value": 0.46,
                        "percentage": 7.3
                },
                {
                        "category": "Segment D",
                        "value": 0.48,
                        "percentage": 7.6
                },
                {
                        "category": "Other",
                        "value": 1.83,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.773274",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time to Pack per Order"
        }
    },
}
