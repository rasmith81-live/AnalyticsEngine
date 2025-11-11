"""
Channel Conflict Rate KPI

The rate at which conflicts arise between channel partners and the company, or between channel partners themselves.
"""

CHANNEL_CONFLICT_RATE = {
    "code": "CHANNEL_CONFLICT_RATE",
    "name": "Channel Conflict Rate",
    "description": "The rate at which conflicts arise between channel partners and the company, or between channel partners themselves.",
    "formula": "(Number of Conflicting Deals / Total Number of Deals) * 100",
    "calculation_formula": "(Number of Conflicting Deals / Total Number of Deals) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The rate at which conflicts arise between channel partners and the company, or between channel partners themselves.",
    "expected_business_insights": "Identifies the level of conflict within the channel ecosystem, which can harm partner relationships and efficiency.",
    "measurement_approach": "Measures the percentage of deals where channel partners compete against each other or the vendor's direct sales.",
    "trend_analysis": """
    * An increasing channel conflict rate may indicate issues with communication or alignment between the company and its channel partners.
    * A decreasing rate could signal improved collaboration and conflict resolution processes.
    """,
    "diagnostic_questions": """
    * What are the common sources of conflict between the company and its channel partners?
    * How do channel conflict rates vary across different regions or product lines?
    """,
    "actionable_tips": """
    * Establish clear and transparent communication channels with channel partners to address issues promptly.
    * Provide training and resources to help channel partners understand the company's policies and procedures.
    * Implement a formal conflict resolution process to address disputes in a timely and fair manner.
    """,
    "visualization_suggestions": """
    * Line charts to track the channel conflict rate over time and identify any seasonal or cyclical patterns.
    * Pie charts to compare the distribution of conflicts across different channel partners or regions.
    """,
    "risk_warnings": """
    * High channel conflict rates can lead to decreased sales and damaged relationships with channel partners.
    * Unresolved conflicts may result in legal disputes or the loss of key channel partners.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems to track interactions and communication with channel partners.
    * Collaboration platforms like Slack or Microsoft Teams to facilitate real-time communication and problem-solving.
    """,
    "integration_points": """
    * Integrate channel conflict rate data with sales performance metrics to understand the impact of conflicts on revenue and market share.
    * Link conflict resolution processes with customer service systems to ensure consistent messaging and support for end customers.
    """,
    "change_impact_analysis": """
    * Reducing channel conflict rates can lead to improved partner satisfaction and loyalty, potentially increasing overall sales performance.
    * However, addressing conflicts may require additional resources and time, impacting operational efficiency and cost management.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
