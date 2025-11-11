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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal", "Lead"], "last_validated": "2025-11-10T13:49:33.709190"},
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
                        371,
                        367,
                        392,
                        369,
                        368,
                        377,
                        366,
                        383,
                        386,
                        383,
                        387,
                        413
                ],
                "unit": "count"
        },
        "current": {
                "value": 413,
                "unit": "count",
                "change": 26,
                "change_percent": 6.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 380.17,
                "min": 366,
                "max": 413,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 75.58,
                        "percentage": 18.3
                },
                {
                        "category": "Channel Sales",
                        "value": 113.68,
                        "percentage": 27.5
                },
                {
                        "category": "Online Sales",
                        "value": 61.88,
                        "percentage": 15.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 28.22,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 133.64,
                        "percentage": 32.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.752143",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Time to Close"
        }
    },
}
