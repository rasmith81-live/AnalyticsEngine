"""
Account Penetration Rate

The percentage of a customer account
"""

ACCOUNT_PENETRATION_RATE = {
    "code": "ACCOUNT_PENETRATION_RATE",
    "name": "Account Penetration Rate",
    "description": "The percentage of a customer account",
    "formula": "(Number of Products or Services Sold to an Account / Total Number of Available Offerings) * 100",
    "calculation_formula": "(Number of Products or Services Sold to an Account / Total Number of Available Offerings) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Account Penetration Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:43:22.994657"},
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
                        52.21,
                        44.36,
                        49.14,
                        47.06,
                        55.32,
                        50.8,
                        56.82,
                        47.55,
                        46.2,
                        44.02,
                        55.71,
                        56.45
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.45,
                "unit": "%",
                "change": 0.74,
                "change_percent": 1.3,
                "trend": "increasing"
        },
        "statistics": {
                "average": 50.47,
                "min": 44.02,
                "max": 56.82,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.97,
                        "percentage": 15.9
                },
                {
                        "category": "Category B",
                        "value": 7.71,
                        "percentage": 13.7
                },
                {
                        "category": "Category C",
                        "value": 10.6,
                        "percentage": 18.8
                },
                {
                        "category": "Category D",
                        "value": 5.24,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 23.93,
                        "percentage": 42.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:22.994657",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Penetration Rate"
        }
    },
}
