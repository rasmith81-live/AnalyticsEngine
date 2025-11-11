"""
Time to Close

The time it takes to close a deal from the initial contact with a lead.
"""

TIME_TO_CLOSE = {
    "code": "TIME_TO_CLOSE",
    "name": "Time to Close",
    "description": "The time it takes to close a deal from the initial contact with a lead.",
    "formula": "Total Time Taken to Close All Sales / Total Number of Sales Closed",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Time to Close to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal", "Lead"], "last_validated": "2025-11-10T13:43:25.013320"},
    "required_objects": [],
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
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
                        118,
                        87,
                        117,
                        108,
                        96,
                        100,
                        112,
                        127,
                        127,
                        87,
                        122,
                        85
                ],
                "unit": "count"
        },
        "current": {
                "value": 85,
                "unit": "count",
                "change": -37,
                "change_percent": -30.3,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 107.17,
                "min": 85,
                "max": 127,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 29.4,
                        "percentage": 34.6
                },
                {
                        "category": "Category B",
                        "value": 15.37,
                        "percentage": 18.1
                },
                {
                        "category": "Category C",
                        "value": 8.86,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 7.01,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 24.36,
                        "percentage": 28.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.013320",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Close"
        }
    },
}
