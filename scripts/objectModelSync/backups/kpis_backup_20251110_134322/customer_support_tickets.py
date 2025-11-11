"""
Customer Support Tickets KPI

The number of support tickets or customer service inquiries received within a specific period.
"""

CUSTOMER_SUPPORT_TICKETS = {
    "code": "CUSTOMER_SUPPORT_TICKETS",
    "name": "Customer Support Tickets",
    "description": "The number of support tickets or customer service inquiries received within a specific period.",
    "formula": "Total Number of Customer Support Tickets Received",
    "calculation_formula": "Total Number of Customer Support Tickets Received",
    "category": "Customer Retention",
    "is_active": True,
    "kpi_definition": "The number of support tickets or customer service inquiries received within a specific period.",
    "expected_business_insights": "Tracks the volume of customer support needs and can indicate product/service issues.",
    "measurement_approach": "Counts the number of support tickets or customer service inquiries received.",
    "trend_analysis": """
    * An increasing number of customer support tickets may indicate product or service quality issues that need to be addressed.
    * A decreasing trend in support tickets could signal improved customer satisfaction or product reliability.
    """,
    "diagnostic_questions": """
    * Are there recurring issues or common themes in the support tickets received?
    * How do our customer support ticket volumes compare to industry benchmarks or historical data?
    """,
    "actionable_tips": """
    * Implement proactive customer education to reduce common support ticket issues.
    * Invest in product or service improvements based on the feedback received through support tickets.
    * Train customer support staff to efficiently handle and resolve inquiries to reduce ticket volumes.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend in support ticket volumes over time.
    * Pareto charts to identify the most common reasons for support tickets.
    """,
    "risk_warnings": """
    * High support ticket volumes can lead to customer frustration and dissatisfaction, impacting retention.
    * Ignoring support ticket trends may result in a decline in customer loyalty and retention.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track and analyze support ticket data.
    * Help desk software to efficiently manage and respond to customer inquiries.
    """,
    "integration_points": """
    * Integrate support ticket data with product development teams to address recurring issues.
    * Link support ticket metrics with customer satisfaction surveys to gain a comprehensive view of customer experience.
    """,
    "change_impact_analysis": """
    * Reducing support ticket volumes can lead to improved customer satisfaction and loyalty.
    * However, a sudden decrease in support tickets may also indicate a lack of customer engagement or feedback, which could impact product development and innovation.
    """,
    "metadata_": {"modules": ["CUSTOMER_RETENTION"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Service Level Agreement", "Support Ticket"]},
    "modules": ["CUSTOMER_RETENTION"],
    "module_code": "CUSTOMER_RETENTION",
}
