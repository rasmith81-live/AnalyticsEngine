"""
Average Deal Discount

The average percentage discount applied to deals, which can reflect the sales team
"""

DEAL_DISCOUNT = {
    "code": "DEAL_DISCOUNT",
    "name": "Average Deal Discount",
    "description": "The average percentage discount applied to deals, which can reflect the sales team",
    "formula": "To be defined",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Deal Discount to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Deal"], "last_validated": "2025-11-10T13:49:32.910015"},
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
                        481.54,
                        473.42,
                        522.86,
                        531.28,
                        536.98,
                        509.39,
                        485.83,
                        511.48,
                        519.77,
                        572.19,
                        462.81,
                        577.35
                ],
                "unit": "units"
        },
        "current": {
                "value": 577.35,
                "unit": "units",
                "change": 114.54,
                "change_percent": 24.7,
                "trend": "increasing"
        },
        "statistics": {
                "average": 515.41,
                "min": 462.81,
                "max": 577.35,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 124.33,
                        "percentage": 21.5
                },
                {
                        "category": "Category B",
                        "value": 132.6,
                        "percentage": 23.0
                },
                {
                        "category": "Category C",
                        "value": 104.4,
                        "percentage": 18.1
                },
                {
                        "category": "Category D",
                        "value": 53.19,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 162.83,
                        "percentage": 28.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.405937",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Average Deal Discount"
        }
    },
}
