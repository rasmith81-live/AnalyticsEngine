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
                        12.4,
                        11.8,
                        17.0,
                        14.9,
                        9.8,
                        14.1,
                        11.1,
                        16.8,
                        13.3,
                        11.3,
                        16.4,
                        14.2
                ],
                "unit": "days"
        },
        "current": {
                "value": 14.2,
                "unit": "days",
                "change": -2.2,
                "change_percent": -13.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 13.59,
                "min": 9.8,
                "max": 17.0,
                "unit": "days"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 2.82,
                        "percentage": 19.9
                },
                {
                        "category": "Channel Sales",
                        "value": 3.38,
                        "percentage": 23.8
                },
                {
                        "category": "Online Sales",
                        "value": 2.49,
                        "percentage": 17.5
                },
                {
                        "category": "Enterprise Sales",
                        "value": 1.29,
                        "percentage": 9.1
                },
                {
                        "category": "Other",
                        "value": 4.22,
                        "percentage": 29.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.243445",
                "data_points": 12,
                "kpi_type": "time",
                "kpi_name": "Sales Team Response Time"
        }
    },
}
