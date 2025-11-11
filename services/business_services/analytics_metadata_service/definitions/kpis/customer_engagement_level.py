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
                        1017.19,
                        1063.65,
                        978.23,
                        981.31,
                        955.49,
                        1063.95,
                        985.16,
                        917.92,
                        1004.96,
                        974.3,
                        1063.15,
                        970.1
                ],
                "unit": "units"
        },
        "current": {
                "value": 970.1,
                "unit": "units",
                "change": -93.05,
                "change_percent": -8.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 997.95,
                "min": 917.92,
                "max": 1063.95,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 265.87,
                        "percentage": 27.4
                },
                {
                        "category": "Existing Customers",
                        "value": 193.97,
                        "percentage": 20.0
                },
                {
                        "category": "VIP Customers",
                        "value": 111.22,
                        "percentage": 11.5
                },
                {
                        "category": "At-Risk Customers",
                        "value": 79.64,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 319.4,
                        "percentage": 32.9
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.639974",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Engagement Level"
        }
    },
}
