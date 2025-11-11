"""
Packing Error Resolution Time

The average time taken to resolve packing errors, impacting customer satisfaction and operational efficiency.
"""

PACKING_ERROR_RESOLUTION_TIME = {
    "code": "PACKING_ERROR_RESOLUTION_TIME",
    "name": "Packing Error Resolution Time",
    "description": "The average time taken to resolve packing errors, impacting customer satisfaction and operational efficiency.",
    "formula": "Total Time to Resolve Errors / Total Number of Errors",
    "calculation_formula": "To be defined",
    "category": "Packing",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Packing Error Resolution Time to be added.",
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
    "metadata_": {"modules": ["PACKING"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:33.157930"},
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
                        380,
                        371,
                        402,
                        401,
                        409,
                        390,
                        380,
                        399,
                        375,
                        416,
                        377,
                        405
                ],
                "unit": "count"
        },
        "current": {
                "value": 405,
                "unit": "count",
                "change": 28,
                "change_percent": 7.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 392.08,
                "min": 371,
                "max": 416,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 99.89,
                        "percentage": 24.7
                },
                {
                        "category": "Segment B",
                        "value": 55.87,
                        "percentage": 13.8
                },
                {
                        "category": "Segment C",
                        "value": 72.42,
                        "percentage": 17.9
                },
                {
                        "category": "Segment D",
                        "value": 31.42,
                        "percentage": 7.8
                },
                {
                        "category": "Other",
                        "value": 145.4,
                        "percentage": 35.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.400293",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Packing Error Resolution Time"
        }
    },
}
