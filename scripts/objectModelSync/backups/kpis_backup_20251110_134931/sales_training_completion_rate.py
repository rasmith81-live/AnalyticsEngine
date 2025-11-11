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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.679527"},
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
                        61.34,
                        48.28,
                        63.72,
                        54.9,
                        53.92,
                        57.42,
                        53.37,
                        66.24,
                        60.1,
                        63.48,
                        62.48,
                        56.53
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.53,
                "unit": "%",
                "change": -5.95,
                "change_percent": -9.5,
                "trend": "increasing"
        },
        "statistics": {
                "average": 58.48,
                "min": 48.28,
                "max": 66.24,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 15.48,
                        "percentage": 27.4
                },
                {
                        "category": "Category B",
                        "value": 6.7,
                        "percentage": 11.9
                },
                {
                        "category": "Category C",
                        "value": 5.9,
                        "percentage": 10.4
                },
                {
                        "category": "Category D",
                        "value": 3.51,
                        "percentage": 6.2
                },
                {
                        "category": "Other",
                        "value": 24.94,
                        "percentage": 44.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.679527",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Sales Training Completion Rate"
        }
    },
}
