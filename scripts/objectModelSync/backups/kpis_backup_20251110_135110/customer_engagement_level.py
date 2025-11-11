"""
Customer Engagement Level

The degree to which customers interact with the brand through various channels and activities, indicating their interest and loyalty.
"""

CUSTOMER_ENGAGEMENT_LEVEL = {
    "code": "CUSTOMER_ENGAGEMENT_LEVEL",
    "name": "Customer Engagement Level",
    "description": "The degree to which customers interact with the brand through various channels and activities, indicating their interest and loyalty.",
    "formula": "(Various metrics depending on the engagement channels used)",
    "calculation_formula": "(Various metrics depending on the engagement channels used)",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Engagement Level to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:32.822563"},
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
                        529.48,
                        633.61,
                        554.43,
                        546.11,
                        601.15,
                        620.49,
                        520.65,
                        566.48,
                        542.85,
                        504.95,
                        588.15,
                        526.92
                ],
                "unit": "units"
        },
        "current": {
                "value": 526.92,
                "unit": "units",
                "change": -61.23,
                "change_percent": -10.4,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 561.27,
                "min": 504.95,
                "max": 633.61,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 83.47,
                        "percentage": 15.8
                },
                {
                        "category": "Category B",
                        "value": 84.92,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 82.74,
                        "percentage": 15.7
                },
                {
                        "category": "Category D",
                        "value": 45.42,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 230.37,
                        "percentage": 43.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.246808",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Engagement Level"
        }
    },
}
