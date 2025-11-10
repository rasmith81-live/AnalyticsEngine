"""
Channel Partner Growth Rate KPI

The rate at which individual channel partners grow in terms of their business with the company, which can be measured in sales or other metrics.
"""

CHANNEL_PARTNER_GROWTH_RATE = {
    "code": "CHANNEL_PARTNER_GROWTH_RATE",
    "name": "Channel Partner Growth Rate",
    "description": "The rate at which individual channel partners grow in terms of their business with the company, which can be measured in sales or other metrics.",
    "formula": "((Number of Active Partners at End of Period - Number at Beginning of Period) / Number at Beginning of Period) * 100",
    "calculation_formula": "((Number of Active Partners at End of Period - Number at Beginning of Period) / Number at Beginning of Period) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The rate at which individual channel partners grow in terms of their business with the company, which can be measured in sales or other metrics.",
    "expected_business_insights": "Provides insight into the expansion of the channel network and the effectiveness of partner recruitment strategies.",
    "measurement_approach": "Calculates the percentage increase in the number of active channel partners over a specific period.",
    "trend_analysis": """
    * Increasing channel partner growth rate may indicate successful onboarding and support programs for new partners.
    * A decreasing growth rate could signal dissatisfaction among existing partners or increased competition in the market.
    """,
    "diagnostic_questions": """
    * Are there specific regions or industries where channel partner growth is particularly strong or weak?
    * What factors contribute to the success of high-growth channel partners, and how can those strategies be replicated?
    """,
    "actionable_tips": """
    * Provide additional training and resources to underperforming channel partners to help them grow their business.
    * Regularly review and update the channel partner program to ensure it remains competitive and attractive.
    * Implement a referral program to incentivize existing partners to bring in new business.
    """,
    "visualization_suggestions": """
    * Line charts showing the growth rate of individual channel partners over time.
    * Pie charts comparing the distribution of high-growth, moderate-growth, and low-growth partners.
    """,
    "risk_warnings": """
    * Rapid growth in a few partners may lead to overreliance on a small number of channels, increasing vulnerability to market changes.
    * Slow growth across the board may indicate a lack of competitiveness or support for the channel partner program.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track partner interactions and identify growth opportunities.
    * Partner Relationship Management (PRM) platforms to streamline partner onboarding, training, and support.
    """,
    "integration_points": """
    * Integrate channel partner growth data with sales performance metrics to understand the impact of partner growth on overall revenue.
    * Link growth rate analysis with marketing efforts to identify which campaigns or initiatives are driving partner success.
    """,
    "change_impact_analysis": """
    * Increasing channel partner growth can lead to expanded market reach and increased sales, but may also require additional resources for support and management.
    * A decline in partner growth may signal the need for strategic adjustments to the partner program or market approach.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
