"""
Referral Rate

The percentage of new business that comes from referrals by existing customers, which can indicate customer satisfaction and advocacy.
"""

REFERRAL_RATE = {
    "code": "REFERRAL_RATE",
    "name": "Referral Rate",
    "description": "The percentage of new business that comes from referrals by existing customers, which can indicate customer satisfaction and advocacy.",
    "formula": "(Number of New Customers from Referrals / Total Number of New Customers) * 100",
    "calculation_formula": "(Number of New Customers from Referrals / Total Number of New Customers) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Referral Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:49:33.325298"},
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
                        63.14,
                        53.17,
                        53.64,
                        47.33,
                        50.38,
                        47.99,
                        52.28,
                        49.88,
                        60.05,
                        58.48,
                        57.57,
                        61.97
                ],
                "unit": "%"
        },
        "current": {
                "value": 61.97,
                "unit": "%",
                "change": 4.4,
                "change_percent": 7.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 54.66,
                "min": 47.33,
                "max": 63.14,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "New Customers",
                        "value": 10.85,
                        "percentage": 17.5
                },
                {
                        "category": "Existing Customers",
                        "value": 9.05,
                        "percentage": 14.6
                },
                {
                        "category": "VIP Customers",
                        "value": 9.68,
                        "percentage": 15.6
                },
                {
                        "category": "At-Risk Customers",
                        "value": 4.43,
                        "percentage": 7.1
                },
                {
                        "category": "Other",
                        "value": 27.96,
                        "percentage": 45.1
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.765173",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Referral Rate"
        }
    },
}
