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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:32.624157"},
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
                        64.09,
                        68.67,
                        82.76,
                        66.22,
                        68.89,
                        74.83,
                        79.7,
                        68.19,
                        75.93,
                        68.7,
                        82.28,
                        76.37
                ],
                "unit": "%"
        },
        "current": {
                "value": 76.37,
                "unit": "%",
                "change": -5.91,
                "change_percent": -7.2,
                "trend": "increasing"
        },
        "statistics": {
                "average": 73.05,
                "min": 64.09,
                "max": 82.76,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 11.87,
                        "percentage": 15.5
                },
                {
                        "category": "Mid-Market",
                        "value": 17.66,
                        "percentage": 23.1
                },
                {
                        "category": "Small Business",
                        "value": 8.32,
                        "percentage": 10.9
                },
                {
                        "category": "Strategic Partners",
                        "value": 6.89,
                        "percentage": 9.0
                },
                {
                        "category": "Other",
                        "value": 31.63,
                        "percentage": 41.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.324435",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Coverage Ratio"
        }
    },
}
