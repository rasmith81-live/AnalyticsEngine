"""
Email Open Rate KPI

The percentage of sales emails sent that are opened by recipients.
"""

EMAIL_OPEN_RATE = {
    "code": "EMAIL_OPEN_RATE",
    "name": "Email Open Rate",
    "description": "The percentage of sales emails sent that are opened by recipients.",
    "formula": "(Number of Emails Opened / Number of Emails Sent) * 100",
    "calculation_formula": "(Number of Emails Opened / Number of Emails Sent) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The percentage of sales emails sent that are opened by recipients.",
    "expected_business_insights": "Gauges the effectiveness of email subject lines and the overall engagement level of an email campaign.",
    "measurement_approach": "The percentage of email recipients who open an email.",
    "trend_analysis": """
    * A rising email open rate may indicate improved email subject lines or more engaging content.
    * A decreasing rate could signal email deliverability issues or a decline in recipient interest.
    """,
    "diagnostic_questions": """
    * Are there specific types of emails (e.g., promotional, informational) that have higher or lower open rates?
    * How does our email open rate compare with industry benchmarks or with different segments of our target audience?
    """,
    "actionable_tips": """
    * Optimize email subject lines and content to increase recipient engagement.
    * Regularly clean and update email lists to improve deliverability and engagement.
    * Segment email lists and tailor content to different audience preferences and behaviors.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of email open rates over time.
    * Comparison bar charts displaying open rates for different types of emails or audience segments.
    """,
    "risk_warnings": """
    * Low email open rates can lead to reduced sales opportunities and lower ROI on email marketing efforts.
    * Consistently declining open rates may indicate broader issues with email marketing strategy or audience targeting.
    """,
    "tracking_tools": """
    * Email marketing platforms like Mailchimp or HubSpot for tracking and analyzing open rates.
    * Data cleansing tools to maintain accurate and engaged email lists.
    """,
    "integration_points": """
    * Integrate email open rate data with CRM systems to better understand the impact on sales and customer engagement.
    * Link with marketing automation platforms to adjust email content and timing based on open rate performance.
    """,
    "change_impact_analysis": """
    * Improving email open rates can lead to increased sales opportunities and better ROI on marketing efforts.
    * However, changes in email content or frequency may impact overall email deliverability and engagement metrics.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Email", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "INSIDE_SALES",
}
