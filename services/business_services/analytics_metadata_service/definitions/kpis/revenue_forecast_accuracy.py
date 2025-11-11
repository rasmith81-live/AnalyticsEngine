"""
Revenue Forecast Accuracy

The accuracy of the sales team
"""

REVENUE_FORECAST_ACCURACY = {
    "code": "REVENUE_FORECAST_ACCURACY",
    "name": "Revenue Forecast Accuracy",
    "description": "The accuracy of the sales team",
    "formula": "(Absolute Value of (Actual Revenue - Forecasted Revenue) / Actual Revenue) * 100",
    "calculation_formula": "(Absolute Value of (Actual Revenue - Forecasted Revenue) / Actual Revenue) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Revenue Forecast Accuracy to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.357805"},
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
                        60.7,
                        52.11,
                        61.7,
                        46.33,
                        48.82,
                        52.3,
                        47.32,
                        56.54,
                        47.72,
                        61.87,
                        59.0,
                        46.76
                ],
                "unit": "%"
        },
        "current": {
                "value": 46.76,
                "unit": "%",
                "change": -12.24,
                "change_percent": -20.7,
                "trend": "stable"
        },
        "statistics": {
                "average": 53.43,
                "min": 46.33,
                "max": 61.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 12.31,
                        "percentage": 26.3
                },
                {
                        "category": "Channel Sales",
                        "value": 6.32,
                        "percentage": 13.5
                },
                {
                        "category": "Online Sales",
                        "value": 6.31,
                        "percentage": 13.5
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.21,
                        "percentage": 11.1
                },
                {
                        "category": "Other",
                        "value": 16.61,
                        "percentage": 35.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.833696",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Revenue Forecast Accuracy"
        }
    },
}
