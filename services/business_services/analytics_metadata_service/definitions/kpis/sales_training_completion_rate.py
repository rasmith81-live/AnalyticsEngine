"""
Sales Training Completion Rate

The percentage of sales representatives who have completed mandatory sales training programs.
"""

SALES_TRAINING_COMPLETION_RATE = {
    "code": "SALES_TRAINING_COMPLETION_RATE",
    "name": "Sales Training Completion Rate",
    "description": "The percentage of sales representatives who have completed mandatory sales training programs.",
    "formula": "(Number of Sales Reps Who Completed Training / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Who Completed Training / Total Number of Sales Reps) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Training Completion Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.533378"},
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
                        50.43,
                        48.71,
                        58.58,
                        48.23,
                        59.16,
                        56.41,
                        52.23,
                        48.98,
                        51.2,
                        55.31,
                        60.53,
                        45.79
                ],
                "unit": "%"
        },
        "current": {
                "value": 45.79,
                "unit": "%",
                "change": -14.74,
                "change_percent": -24.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 52.96,
                "min": 45.79,
                "max": 60.53,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 12.16,
                        "percentage": 26.6
                },
                {
                        "category": "Channel Sales",
                        "value": 10.44,
                        "percentage": 22.8
                },
                {
                        "category": "Online Sales",
                        "value": 6.79,
                        "percentage": 14.8
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.81,
                        "percentage": 10.5
                },
                {
                        "category": "Other",
                        "value": 11.59,
                        "percentage": 25.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.286325",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Training Completion Rate"
        }
    },
}
