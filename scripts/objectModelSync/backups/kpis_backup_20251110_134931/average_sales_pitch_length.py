"""
Average Sales Pitch Length

The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.
"""

AVERAGE_SALES_PITCH_LENGTH = {
    "code": "AVERAGE_SALES_PITCH_LENGTH",
    "name": "Average Sales Pitch Length",
    "description": "The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    "formula": "Total Duration of All Sales Pitches / Number of Sales Pitches",
    "calculation_formula": "To be defined",
    "category": "Business Development",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Average Sales Pitch Length to be added.",
    "trend_analysis": "Increasing average sales pitch length may indicate a more detailed and comprehensive approach to presenting products or services. A decreasing average pitch length could suggest a more concise and efficient communication style, but it may also lead to overlooking important details.",
    "diagnostic_questions": ["Are there specific products or services that require longer pitches to effectively convey their value?", "How does the average pitch length correlate with the success rate of closing deals?"],
    "actionable_tips": """
* Monitor this KPI regularly
* Set appropriate targets and thresholds
    """,
    "visualization_suggestions": """
* Line chart for time series analysis
* Bar chart for comparisons
    """,
    "risk_warnings": ["Excessively long pitches may lead to customer disengagement and loss of interest.", "Overly short pitches might result in insufficient information being conveyed, leading to missed sales opportunities."],
    "tracking_tools": "* CRM or analytics platform",
    "integration_points": ["Integrate pitch length data with customer feedback and conversion rates to understand the impact of pitch duration on sales performance.", "Link pitch length analysis with sales training programs to tailor coaching and development efforts based on the findings."],
    "change_impact_analysis": "Changes in this KPI may impact related business processes.",
    "metadata_": {"modules": ["BUS_DEV"], "value_chains": ["SALES_MGMT"], "source": "kpidepot.com", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Prospect Engagement", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "last_validated": "2025-11-10T13:43:23.044635"},
    "required_objects": [],
    "modules": ["BUS_DEV"],
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
                        128,
                        99,
                        97,
                        103,
                        96,
                        127,
                        106,
                        136,
                        111,
                        115,
                        146,
                        132
                ],
                "unit": "count"
        },
        "current": {
                "value": 132,
                "unit": "count",
                "change": -14,
                "change_percent": -9.6,
                "trend": "increasing"
        },
        "statistics": {
                "average": 116.33,
                "min": 96,
                "max": 146,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 31.87,
                        "percentage": 24.1
                },
                {
                        "category": "Category B",
                        "value": 30.91,
                        "percentage": 23.4
                },
                {
                        "category": "Category C",
                        "value": 22.06,
                        "percentage": 16.7
                },
                {
                        "category": "Category D",
                        "value": 12.31,
                        "percentage": 9.3
                },
                {
                        "category": "Other",
                        "value": 34.85,
                        "percentage": 26.4
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.044635",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Average Sales Pitch Length"
        }
    },
}
