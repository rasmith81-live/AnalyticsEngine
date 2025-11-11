"""
Customer Onboarding Efficacy

The effectiveness of the onboarding process for new customers, measured by their time to value and overall satisfaction.
"""

CUSTOMER_ONBOARDING_EFFICACY = {
    "code": "CUSTOMER_ONBOARDING_EFFICACY",
    "name": "Customer Onboarding Efficacy",
    "description": "The effectiveness of the onboarding process for new customers, measured by their time to value and overall satisfaction.",
    "formula": "(Number of Successfully Onboarded Customers / Total Number of New Customers) * 100",
    "calculation_formula": "(Number of Successfully Onboarded Customers / Total Number of New Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Customer Onboarding Efficacy to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:32.852893"},
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
                        58.29,
                        49.53,
                        52.54,
                        55.81,
                        51.78,
                        64.2,
                        58.58,
                        45.57,
                        50.84,
                        51.47,
                        45.53,
                        47.85
                ],
                "unit": "%"
        },
        "current": {
                "value": 47.85,
                "unit": "%",
                "change": 2.32,
                "change_percent": 5.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 52.67,
                "min": 45.53,
                "max": 64.2,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 9.45,
                        "percentage": 19.7
                },
                {
                        "category": "Existing Customers",
                        "value": 13.37,
                        "percentage": 27.9
                },
                {
                        "category": "VIP Customers",
                        "value": 5.65,
                        "percentage": 11.8
                },
                {
                        "category": "At-Risk Customers",
                        "value": 5.79,
                        "percentage": 12.1
                },
                {
                        "category": "Other",
                        "value": 13.59,
                        "percentage": 28.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.732381",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Customer Onboarding Efficacy"
        }
    },
}
