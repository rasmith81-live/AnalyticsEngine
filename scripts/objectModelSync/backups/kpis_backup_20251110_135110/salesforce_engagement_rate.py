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
                        49.57,
                        48.98,
                        43.39,
                        48.12,
                        52.01,
                        34.78,
                        33.88,
                        45.27,
                        49.76,
                        43.91,
                        45.32,
                        36.17
                ],
                "unit": "%"
        },
        "current": {
                "value": 36.17,
                "unit": "%",
                "change": -9.15,
                "change_percent": -20.2,
                "trend": "decreasing"
        },
        "statistics": {
                "average": 44.26,
                "min": 33.88,
                "max": 52.01,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 8.46,
                        "percentage": 23.4
                },
                {
                        "category": "Category B",
                        "value": 5.18,
                        "percentage": 14.3
                },
                {
                        "category": "Category C",
                        "value": 5.67,
                        "percentage": 15.7
                },
                {
                        "category": "Category D",
                        "value": 2.98,
                        "percentage": 8.2
                },
                {
                        "category": "Other",
                        "value": 13.88,
                        "percentage": 38.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:24.696043",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Salesforce Engagement Rate"
        }
    },
}
