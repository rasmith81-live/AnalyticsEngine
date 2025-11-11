"""
Strategic Account Contact Frequency KPI

The frequency of contact or touchpoints with strategic accounts over a given time period.
"""

STRATEGIC_ACCOUNT_CONTACT_FREQUENCY = {
    "code": "STRATEGIC_ACCOUNT_CONTACT_FREQUENCY",
    "name": "Strategic Account Contact Frequency",
    "description": "The frequency of contact or touchpoints with strategic accounts over a given time period.",
    "formula": "Total Number of Contacts with Account / Specified Time Period",
    "calculation_formula": "Total Number of Contacts with Account / Specified Time Period",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The frequency of contact or touchpoints with strategic accounts over a given time period.",
    "expected_business_insights": "Ensures proper engagement levels with strategic accounts, potentially leading to increased satisfaction and revenue.",
    "measurement_approach": "Measures how often key accounts are contacted by account managers.",
    "trend_analysis": """
    * An increasing contact frequency may indicate a proactive approach to account management and stronger relationships with key accounts.
    * A decreasing contact frequency could signal potential disengagement or neglect of strategic accounts, leading to missed opportunities or customer dissatisfaction.
    """,
    "diagnostic_questions": """
    * Are there specific strategic accounts that receive significantly more or less contact than others?
    * How does our contact frequency compare with industry standards or best practices in key account management?
    """,
    "actionable_tips": """
    * Implement a structured account management plan with defined touchpoints and communication schedules for each strategic account.
    * Leverage customer relationship management (CRM) software to track and schedule interactions with key accounts.
    * Regularly review and adjust contact frequency based on the evolving needs and priorities of strategic accounts.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of contact frequency over time for each strategic account.
    * Comparison bar charts displaying the average contact frequency across different segments or regions.
    """,
    "risk_warnings": """
    * Low contact frequency may result in missed sales opportunities or reduced customer loyalty.
    * Excessive contact without adding value can lead to customer fatigue and potential disengagement.
    """,
    "tracking_tools": """
    * CRM systems like Salesforce or HubSpot for tracking and managing interactions with strategic accounts.
    * Marketing automation platforms to personalize and automate communication with key accounts based on their preferences and behavior.
    """,
    "integration_points": """
    * Integrate contact frequency data with sales performance metrics to understand the impact of account management on revenue generation.
    * Link contact frequency with customer feedback and satisfaction scores to gauge the effectiveness of key account management efforts.
    """,
    "change_impact_analysis": """
    * Increasing contact frequency may lead to better customer retention and increased sales, but it could also require additional resources and time from the sales team.
    * Conversely, reducing contact frequency to focus on more profitable accounts may result in short-term gains but could harm long-term relationships and customer lifetime value.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Strategic Initiative", "Strategic Review"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
