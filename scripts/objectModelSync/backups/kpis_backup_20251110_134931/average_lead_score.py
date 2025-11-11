"""
Average Lead Score

The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.
"""

AVERAGE_LEAD_SCORE = {
    "code": "AVERAGE_LEAD_SCORE",
    "name": "Average Lead Score",
    "description": "The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.",
    "formula": "Sum of All Lead Scores / Total Number of Leads",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Lead Score to be added.",
    "trend_analysis": "An increasing average lead score may indicate that the business development team is effectively targeting higher quality leads. A decreasing average lead score could signal a decline in lead quality or a need for reassessment of lead scoring criteria.",
    "diagnostic_questions": ["What criteria are used to score leads, and are they still relevant and effective?", "How does the average lead score compare to conversion rates and actual sales, and are there discrepancies that need to be addressed?"],
    "actionable_tips": """
* Monitor this KPI regularly
* Set appropriate targets and thresholds
    """,
    "visualization_suggestions": """
* Line chart for time series analysis
* Bar chart for comparisons
    """,
    "risk_warnings": ["A consistently low average lead score may lead to wasted resources and efforts on pursuing low-quality leads.", "An excessively high average lead score may indicate a narrow focus that misses potential opportunities in other segments."],
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": ["Integrate lead scoring data with sales performance metrics to identify correlations and optimize lead quality.", "Link lead scoring with marketing campaign data to assess the effectiveness of different lead generation channels."],
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUS_DEV", "SALES_DEVELOPMENT"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "required_objects": ["Lead", "Lead Qualification", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.024999"},
    "required_objects": [],
    "modules": ["BUS_DEV", "SALES_DEVELOPMENT"],
    "module_code": "BUS_DEV",
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
                        460,
                        472,
                        497,
                        455,
                        476,
                        486,
                        489,
                        501,
                        490,
                        499,
                        501,
                        493
                ],
                "unit": "count"
        },
        "current": {
                "value": 493,
                "unit": "count",
                "change": -8,
                "change_percent": -1.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 484.92,
                "min": 455,
                "max": 501,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 145.54,
                        "percentage": 29.5
                },
                {
                        "category": "Category B",
                        "value": 74.14,
                        "percentage": 15.0
                },
                {
                        "category": "Category C",
                        "value": 67.24,
                        "percentage": 13.6
                },
                {
                        "category": "Category D",
                        "value": 57.14,
                        "percentage": 11.6
                },
                {
                        "category": "Other",
                        "value": 148.94,
                        "percentage": 30.2
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.024999",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Lead Score"
        }
    },
}
