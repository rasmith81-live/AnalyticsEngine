"""
Quota Attainment Rate

The percentage of sales representatives reaching or exceeding their sales quotas.
"""

QUOTA_ATTAINMENT_RATE = {
    "code": "QUOTA_ATTAINMENT_RATE",
    "name": "Quota Attainment Rate",
    "description": "The percentage of sales representatives reaching or exceeding their sales quotas.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Quota Attainment Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.316272"},
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
                        51.12,
                        55.83,
                        47.44,
                        45.51,
                        49.98,
                        49.67,
                        50.27,
                        42.25,
                        61.7,
                        58.24,
                        43.2,
                        49.14
                ],
                "unit": "%"
        },
        "current": {
                "value": 49.14,
                "unit": "%",
                "change": 5.94,
                "change_percent": 13.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 50.36,
                "min": 42.25,
                "max": 61.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 9.4,
                        "percentage": 19.1
                },
                {
                        "category": "Segment B",
                        "value": 7.23,
                        "percentage": 14.7
                },
                {
                        "category": "Segment C",
                        "value": 7.81,
                        "percentage": 15.9
                },
                {
                        "category": "Segment D",
                        "value": 7.28,
                        "percentage": 14.8
                },
                {
                        "category": "Other",
                        "value": 17.42,
                        "percentage": 35.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.743010",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Quota Attainment Rate"
        }
    },
}
