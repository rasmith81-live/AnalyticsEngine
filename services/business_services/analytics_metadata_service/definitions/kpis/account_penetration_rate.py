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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Product", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:32.631109"},
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
                        62.31,
                        68.71,
                        61.21,
                        72.03,
                        65.15,
                        75.87,
                        68.33,
                        66.36,
                        67.98,
                        70.95,
                        68.85,
                        64.66
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.66,
                "unit": "%",
                "change": -4.19,
                "change_percent": -6.1,
                "trend": "increasing"
        },
        "statistics": {
                "average": 67.7,
                "min": 61.21,
                "max": 75.87,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Enterprise Accounts",
                        "value": 15.59,
                        "percentage": 24.1
                },
                {
                        "category": "Mid-Market",
                        "value": 13.45,
                        "percentage": 20.8
                },
                {
                        "category": "Small Business",
                        "value": 7.28,
                        "percentage": 11.3
                },
                {
                        "category": "Strategic Partners",
                        "value": 5.56,
                        "percentage": 8.6
                },
                {
                        "category": "Other",
                        "value": 22.78,
                        "percentage": 35.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.336477",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Account Penetration Rate"
        }
    },
}
