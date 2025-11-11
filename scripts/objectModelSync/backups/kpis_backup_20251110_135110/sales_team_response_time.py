"""
Sales Team Response Time

The average time it takes for a sales representative to follow up on a lead or customer inquiry.
"""

SALES_TEAM_RESPONSE_TIME = {
    "code": "SALES_TEAM_RESPONSE_TIME",
    "name": "Sales Team Response Time",
    "description": "The average time it takes for a sales representative to follow up on a lead or customer inquiry.",
    "formula": "Average Time Taken by Sales Team to Respond to Inquiries",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Sales Team Response Time to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": ["Customer", "Lead", "PurchaseOrder"], "last_validated": "2025-11-10T13:49:33.513657"},
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
                        17.2,
                        19.9,
                        14.9,
                        14.7,
                        13.5,
                        16.3,
                        17.0,
                        19.9,
                        14.9,
                        12.7,
                        18.1,
                        19.2
                ],
                "unit": "days"
        },
        "current": {
                "value": 19.2,
                "unit": "days",
                "change": 1.1,
                "change_percent": 6.1,
                "trend": "stable"
        },
        "statistics": {
                "average": 16.52,
                "min": 12.7,
                "max": 19.9,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 6.63,
                        "percentage": 34.5
                },
                {
                        "category": "Category B",
                        "value": 2.9,
                        "percentage": 15.1
                },
                {
                        "category": "Category C",
                        "value": 2.96,
                        "percentage": 15.4
                },
                {
                        "category": "Category D",
                        "value": 0.83,
                        "percentage": 4.3
                },
                {
                        "category": "Other",
                        "value": 5.88,
                        "percentage": 30.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.644896",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Sales Team Response Time"
        }
    },
}
