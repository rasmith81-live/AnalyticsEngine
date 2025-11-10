"""
Email Click-Through Rate (CTR) KPI

The percentage of recipients who click on a link contained in a sales email.
"""

EMAIL_CLICK_THROUGH_RATE_CTR = {
    "code": "EMAIL_CLICK_THROUGH_RATE_CTR",
    "name": "Email Click-Through Rate (CTR)",
    "description": "The percentage of recipients who click on a link contained in a sales email.",
    "formula": "(Number of Clicks / Number of Delivered Emails) * 100",
    "calculation_formula": "(Number of Clicks / Number of Delivered Emails) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The percentage of recipients who click on a link contained in a sales email.",
    "expected_business_insights": "Evaluates the effectiveness of email marketing content in driving engagement.",
    "measurement_approach": "The percentage of email recipients who click on one or more links contained in an email.",
    "trend_analysis": """
    * A rising email click-through rate may indicate more engaging email content or improved targeting of recipients.
    * A decreasing rate could signal email fatigue among recipients or a need for better segmentation and personalization.
    """,
    "diagnostic_questions": """
    * Are there specific types of content or subject lines that consistently result in higher click-through rates?
    * How does our email click-through rate compare with industry benchmarks or with different segments of our target audience?
    """,
    "actionable_tips": """
    * Experiment with different types of content, visuals, and calls-to-action in emails to see what resonates best with recipients.
    * Segment email lists based on recipient behavior and interests to deliver more personalized and relevant content.
    * Regularly clean and update email lists to remove inactive or unengaged recipients.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of click-through rates over time.
    * Heat maps to identify which links within emails are generating the most clicks.
    """,
    "risk_warnings": """
    * A consistently low click-through rate may lead to decreased sales opportunities and revenue.
    * High click-through rates without corresponding conversion rates may indicate a disconnect between email content and the sales process.
    """,
    "tracking_tools": """
    * Email marketing platforms like Mailchimp or HubSpot that provide detailed analytics on email performance.
    * A/B testing tools to experiment with different email elements and measure their impact on click-through rates.
    """,
    "integration_points": """
    * Integrate email click-through rate data with CRM systems to track the impact on lead generation and sales opportunities.
    * Link with marketing automation platforms to adjust email content and targeting based on recipient behavior and engagement.
    """,
    "change_impact_analysis": """
    * Improving the email click-through rate can lead to increased lead generation and sales opportunities, but may also require investment in content creation and audience segmentation.
    * Conversely, a declining click-through rate can signal the need for a reassessment of email marketing strategies and potentially impact overall marketing ROI.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Email", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
    "module_code": "INSIDE_SALES",
}
