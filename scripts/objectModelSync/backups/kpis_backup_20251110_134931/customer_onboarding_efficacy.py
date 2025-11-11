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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:43:23.310300"},
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
                        697.19,
                        736.93,
                        718.96,
                        767.63,
                        810.01,
                        774.54,
                        787.9,
                        735.4,
                        736.74,
                        731.22,
                        801.75,
                        793.32
                ],
                "unit": "units"
        },
        "current": {
                "value": 793.32,
                "unit": "units",
                "change": -8.43,
                "change_percent": -1.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 757.63,
                "min": 697.19,
                "max": 810.01,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 256.65,
                        "percentage": 32.4
                },
                {
                        "category": "Category B",
                        "value": 127.66,
                        "percentage": 16.1
                },
                {
                        "category": "Category C",
                        "value": 84.53,
                        "percentage": 10.7
                },
                {
                        "category": "Category D",
                        "value": 45.06,
                        "percentage": 5.7
                },
                {
                        "category": "Other",
                        "value": 279.42,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.310300",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Customer Onboarding Efficacy"
        }
    },
}
