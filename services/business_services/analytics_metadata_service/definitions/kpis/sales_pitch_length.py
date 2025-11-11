"""
Average Sales Pitch Length

The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.
"""

SALES_PITCH_LENGTH = {
    "code": "SALES_PITCH_LENGTH",
    "name": "Average Sales Pitch Length",
    "description": "The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    "formula": "Total Duration of All Sales Pitches / Number of Sales Pitches",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Sales Pitch Length to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:33.465610"},
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
                        85,
                        70,
                        64,
                        82,
                        101,
                        68,
                        85,
                        91,
                        94,
                        101,
                        67,
                        102
                ],
                "unit": "count"
        },
        "current": {
                "value": 102,
                "unit": "count",
                "change": 35,
                "change_percent": 52.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 84.17,
                "min": 64,
                "max": 102,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 27.13,
                        "percentage": 26.6
                },
                {
                        "category": "Channel Sales",
                        "value": 13.28,
                        "percentage": 13.0
                },
                {
                        "category": "Online Sales",
                        "value": 11.38,
                        "percentage": 11.2
                },
                {
                        "category": "Enterprise Sales",
                        "value": 7.46,
                        "percentage": 7.3
                },
                {
                        "category": "Other",
                        "value": 42.75,
                        "percentage": 41.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.109646",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Sales Pitch Length"
        }
    },
}
