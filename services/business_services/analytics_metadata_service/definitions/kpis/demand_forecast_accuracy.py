"""
Demand Forecast Accuracy

The accuracy of prediction for future demand compared to actual demand, impacting inventory levels and customer satisfaction.
"""

DEMAND_FORECAST_ACCURACY = {
    "code": "DEMAND_FORECAST_ACCURACY",
    "name": "Demand Forecast Accuracy",
    "description": "The accuracy of prediction for future demand compared to actual demand, impacting inventory levels and customer satisfaction.",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Iso 22004",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Demand Forecast Accuracy to be added.",
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
    "metadata_": {"modules": ["ISO_22004"], "required_objects": ["Customer", "Inventory"], "last_validated": "2025-11-10T13:49:32.922827"},
    "required_objects": [],
    "modules": ["ISO_22004"],
    "module_code": "ISO_22004",
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
                        453.81,
                        415.23,
                        452.67,
                        487.13,
                        426.14,
                        408.54,
                        361.14,
                        351.98,
                        463.08,
                        426.4,
                        378.68,
                        351.74
                ],
                "unit": "units"
        },
        "current": {
                "value": 351.74,
                "unit": "units",
                "change": -26.94,
                "change_percent": -7.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 414.71,
                "min": 351.74,
                "max": 487.13,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 116.22,
                        "percentage": 33.0
                },
                {
                        "category": "Segment B",
                        "value": 65.46,
                        "percentage": 18.6
                },
                {
                        "category": "Segment C",
                        "value": 26.97,
                        "percentage": 7.7
                },
                {
                        "category": "Segment D",
                        "value": 36.4,
                        "percentage": 10.3
                },
                {
                        "category": "Other",
                        "value": 106.69,
                        "percentage": 30.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.914445",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Demand Forecast Accuracy"
        }
    },
}
