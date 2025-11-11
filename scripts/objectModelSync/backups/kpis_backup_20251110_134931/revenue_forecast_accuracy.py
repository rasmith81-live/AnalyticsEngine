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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:24.108646"},
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
                        53450.2,
                        53601.65,
                        45380.38,
                        39810.2,
                        47766.14,
                        48935.66,
                        51640.12,
                        40111.58,
                        49981.13,
                        49673.22,
                        51558.42,
                        52550.66
                ],
                "unit": "$"
        },
        "current": {
                "value": 52550.66,
                "unit": "$",
                "change": 992.24,
                "change_percent": 1.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 48704.95,
                "min": 39810.2,
                "max": 53601.65,
                "unit": "$"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 11160.52,
                        "percentage": 21.2
                },
                {
                        "category": "Category B",
                        "value": 10756.14,
                        "percentage": 20.5
                },
                {
                        "category": "Category C",
                        "value": 8959.56,
                        "percentage": 17.0
                },
                {
                        "category": "Category D",
                        "value": 5121.18,
                        "percentage": 9.7
                },
                {
                        "category": "Other",
                        "value": 16553.26,
                        "percentage": 31.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.108646",
                "data_points": 12,
                "kpi_type": "currency",
                "kpi_name": "Revenue Forecast Accuracy"
        }
    },
}
