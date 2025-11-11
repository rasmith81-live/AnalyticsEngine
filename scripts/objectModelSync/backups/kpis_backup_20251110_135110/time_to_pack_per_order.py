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
                        13.3,
                        15.0,
                        13.7,
                        18.3,
                        15.2,
                        14.7,
                        15.0,
                        14.9,
                        13.8,
                        17.5,
                        12.0,
                        15.1
                ],
                "unit": "days"
        },
        "current": {
                "value": 15.1,
                "unit": "days",
                "change": 3.1,
                "change_percent": 25.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 14.88,
                "min": 12.0,
                "max": 18.3,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 2.81,
                        "percentage": 18.6
                },
                {
                        "category": "Category B",
                        "value": 4.17,
                        "percentage": 27.6
                },
                {
                        "category": "Category C",
                        "value": 2.36,
                        "percentage": 15.6
                },
                {
                        "category": "Category D",
                        "value": 1.09,
                        "percentage": 7.2
                },
                {
                        "category": "Other",
                        "value": 4.67,
                        "percentage": 30.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.035576",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Time to Pack per Order"
        }
    },
}
