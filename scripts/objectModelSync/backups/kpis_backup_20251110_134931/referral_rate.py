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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer"], "last_validated": "2025-11-10T13:43:24.053530"},
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
                        70.17,
                        62.12,
                        74.7,
                        60.0,
                        57.21,
                        71.14,
                        57.73,
                        72.75,
                        68.25,
                        63.77,
                        63.15,
                        67.63
                ],
                "unit": "%"
        },
        "current": {
                "value": 67.63,
                "unit": "%",
                "change": 4.48,
                "change_percent": 7.1,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 65.72,
                "min": 57.21,
                "max": 74.7,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.11,
                        "percentage": 29.7
                },
                {
                        "category": "Category B",
                        "value": 13.16,
                        "percentage": 19.5
                },
                {
                        "category": "Category C",
                        "value": 10.92,
                        "percentage": 16.1
                },
                {
                        "category": "Category D",
                        "value": 2.37,
                        "percentage": 3.5
                },
                {
                        "category": "Other",
                        "value": 21.07,
                        "percentage": 31.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.053530",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Referral Rate"
        }
    },
}
