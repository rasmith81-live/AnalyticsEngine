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
                        75.26,
                        70.43,
                        65.75,
                        77.25,
                        59.1,
                        77.54,
                        63.29,
                        68.58,
                        64.46,
                        58.92,
                        74.97,
                        60.17
                ],
                "unit": "%"
        },
        "current": {
                "value": 60.17,
                "unit": "%",
                "change": -14.8,
                "change_percent": -19.7,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 67.98,
                "min": 58.92,
                "max": 77.54,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 18.84,
                        "percentage": 31.3
                },
                {
                        "category": "Category B",
                        "value": 13.61,
                        "percentage": 22.6
                },
                {
                        "category": "Category C",
                        "value": 6.78,
                        "percentage": 11.3
                },
                {
                        "category": "Category D",
                        "value": 5.29,
                        "percentage": 8.8
                },
                {
                        "category": "Other",
                        "value": 15.65,
                        "percentage": 26.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.941310",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Post-Sale Follow-Up Rate"
        }
    },
}
