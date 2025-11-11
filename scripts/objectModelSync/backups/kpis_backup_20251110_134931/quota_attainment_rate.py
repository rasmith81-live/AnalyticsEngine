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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.039217"},
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
                        75.2,
                        80.5,
                        79.43,
                        80.7,
                        75.43,
                        67.57,
                        82.35,
                        73.96,
                        83.32,
                        69.26,
                        73.7,
                        84.72
                ],
                "unit": "%"
        },
        "current": {
                "value": 84.72,
                "unit": "%",
                "change": 11.02,
                "change_percent": 15.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 77.18,
                "min": 67.57,
                "max": 84.72,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 22.5,
                        "percentage": 26.6
                },
                {
                        "category": "Category B",
                        "value": 14.61,
                        "percentage": 17.2
                },
                {
                        "category": "Category C",
                        "value": 8.74,
                        "percentage": 10.3
                },
                {
                        "category": "Category D",
                        "value": 10.93,
                        "percentage": 12.9
                },
                {
                        "category": "Other",
                        "value": 27.94,
                        "percentage": 33.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.039217",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Quota Attainment Rate"
        }
    },
}
