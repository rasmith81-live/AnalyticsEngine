"""
Post-Sale Follow-Up Rate

The rate at which the sales team follows up with customers after a sale has been completed, which can impact customer retention and repeat business.
"""

POST_SALE_FOLLOW_UP_RATE = {
    "code": "POST_SALE_FOLLOW_UP_RATE",
    "name": "Post-Sale Follow-Up Rate",
    "description": "The rate at which the sales team follows up with customers after a sale has been completed, which can impact customer retention and repeat business.",
    "formula": "(Number of Completed Sales with Follow-Up / Total Number of Completed Sales) * 100",
    "calculation_formula": "(Number of Completed Sales with Follow-Up / Total Number of Completed Sales) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Post-Sale Follow-Up Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.247544"},
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
                        54.58,
                        50.85,
                        61.51,
                        43.46,
                        47.42,
                        48.83,
                        50.13,
                        43.98,
                        53.14,
                        51.09,
                        56.77,
                        56.17
                ],
                "unit": "%"
        },
        "current": {
                "value": 56.17,
                "unit": "%",
                "change": -0.6,
                "change_percent": -1.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 51.49,
                "min": 43.46,
                "max": 61.51,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 10.06,
                        "percentage": 17.9
                },
                {
                        "category": "Channel Sales",
                        "value": 7.05,
                        "percentage": 12.6
                },
                {
                        "category": "Online Sales",
                        "value": 11.24,
                        "percentage": 20.0
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.7,
                        "percentage": 8.4
                },
                {
                        "category": "Other",
                        "value": 23.12,
                        "percentage": 41.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:12.583843",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Post-Sale Follow-Up Rate"
        }
    },
}
