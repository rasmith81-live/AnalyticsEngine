"""
Number of Active Channel Partners KPI

The number of active channel partners in the network.
"""

NUMBER_OF_ACTIVE_CHANNEL_PARTNERS = {
    "code": "NUMBER_OF_ACTIVE_CHANNEL_PARTNERS",
    "name": "Number of Active Channel Partners",
    "description": "The number of active channel partners in the network.",
    "formula": "Total Count of Active Channel Partners",
    "calculation_formula": "Total Count of Active Channel Partners",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The number of active channel partners in the network.",
    "expected_business_insights": "Shows the breadth of the channel partner network and helps manage and optimize partner relationships.",
    "measurement_approach": "Counts the total number of channel partners actively engaged in selling or promoting products.",
    "trend_analysis": """
    * The number of active channel partners tends to increase as the company expands its market reach or introduces new products/services.
    * A decreasing number of active channel partners may indicate dissatisfaction with the partnership program or increased competition in the market.
    """,
    "diagnostic_questions": """
    * What factors contribute to the onboarding and retention of channel partners?
    * Are there specific regions or industries where the number of active channel partners is declining, and what could be the reasons behind it?
    """,
    "actionable_tips": """
    * Regularly review and update the value proposition for channel partners to ensure it aligns with their needs and market demands.
    * Provide comprehensive training and support to channel partners to help them effectively sell and promote the company's products/services.
    * Implement a robust communication and feedback mechanism to address the concerns and suggestions of channel partners in a timely manner.
    """,
    "visualization_suggestions": """
    * Line charts showing the growth or decline in the number of active channel partners over time.
    * Map visualizations to identify geographical areas with the highest and lowest concentration of active channel partners.
    """,
    "risk_warnings": """
    * A decreasing number of active channel partners can lead to reduced market coverage and missed sales opportunities.
    * An excessively high number of channel partners without proper management can lead to channel conflict and diluted brand representation.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems to track and manage interactions with channel partners.
    * Partner Relationship Management (PRM) software to streamline partner onboarding, training, and collaboration.
    """,
    "integration_points": """
    * Integrate the number of active channel partners with sales performance data to assess the effectiveness of the channel partner network in driving revenue.
    * Link the channel partner KPI with marketing analytics to understand the impact of partner-driven promotions and campaigns.
    """,
    "change_impact_analysis": """
    * An increase in the number of active channel partners can lead to expanded market reach and potentially higher sales volumes.
    * However, a decrease in the number of active channel partners may require a reassessment of the partnership program and its value proposition.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
