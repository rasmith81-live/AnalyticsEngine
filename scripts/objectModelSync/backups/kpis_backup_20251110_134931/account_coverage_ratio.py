"""
Account Coverage Ratio

The ratio of accounts actively managed by the sales team compared to the total number of target accounts.
"""

ACCOUNT_COVERAGE_RATIO = {
    "code": "ACCOUNT_COVERAGE_RATIO",
    "name": "Account Coverage Ratio",
    "description": "The ratio of accounts actively managed by the sales team compared to the total number of target accounts.",
    "formula": "(Number of Accounts Managed by Sales Rep / Total Target Accounts) * 100",
    "calculation_formula": "(Number of Accounts Managed by Sales Rep / Total Target Accounts) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Coverage Ratio to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:43:22.981091"},
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
                        62.4,
                        49.11,
                        46.33,
                        59.7,
                        60.87,
                        51.28,
                        61.83,
                        50.34,
                        55.24,
                        51.2,
                        57.15,
                        59.33
                ],
                "unit": "%"
        },
        "current": {
                "value": 59.33,
                "unit": "%",
                "change": 2.18,
                "change_percent": 3.8,
                "trend": "increasing"
        },
        "statistics": {
                "average": 55.4,
                "min": 46.33,
                "max": 62.4,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.07,
                        "percentage": 28.8
                },
                {
                        "category": "Category B",
                        "value": 14.38,
                        "percentage": 24.2
                },
                {
                        "category": "Category C",
                        "value": 5.75,
                        "percentage": 9.7
                },
                {
                        "category": "Category D",
                        "value": 3.57,
                        "percentage": 6.0
                },
                {
                        "category": "Other",
                        "value": 18.56,
                        "percentage": 31.3
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:22.981091",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Coverage Ratio"
        }
    },
}
