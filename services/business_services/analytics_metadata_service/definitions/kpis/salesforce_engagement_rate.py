"""
Salesforce Engagement Rate

The level of active use of the salesforce automation tools by the sales team, reflecting on tool adoption and efficiency.
"""

SALESFORCE_ENGAGEMENT_RATE = {
    "code": "SALESFORCE_ENGAGEMENT_RATE",
    "name": "Salesforce Engagement Rate",
    "description": "The level of active use of the salesforce automation tools by the sales team, reflecting on tool adoption and efficiency.",
    "formula": "(Number of Active Users on Salesforce / Total Number of Sales Representatives) * 100",
    "calculation_formula": "(Number of Active Users on Salesforce / Total Number of Sales Representatives) * 100",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Salesforce Engagement Rate to be added.",
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
    "metadata_": {"modules": ["BUSINESS_DEVELOPMENT"], "required_objects": [], "last_validated": "2025-11-10T13:49:33.542662"},
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
                        70.52,
                        58.18,
                        60.61,
                        57.18,
                        71.4,
                        67.05,
                        64.81,
                        65.36,
                        66.1,
                        63.46,
                        67.78,
                        57.94
                ],
                "unit": "%"
        },
        "current": {
                "value": 57.94,
                "unit": "%",
                "change": -9.84,
                "change_percent": -14.5,
                "trend": "stable"
        },
        "statistics": {
                "average": 64.2,
                "min": 57.18,
                "max": 71.4,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 8.85,
                        "percentage": 15.3
                },
                {
                        "category": "Channel Sales",
                        "value": 11.83,
                        "percentage": 20.4
                },
                {
                        "category": "Online Sales",
                        "value": 9.0,
                        "percentage": 15.5
                },
                {
                        "category": "Enterprise Sales",
                        "value": 5.34,
                        "percentage": 9.2
                },
                {
                        "category": "Other",
                        "value": 22.92,
                        "percentage": 39.6
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.304103",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Salesforce Engagement Rate"
        }
    },
}
