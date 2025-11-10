"""
Market Penetration Rate KPI

The rate at which new clients are acquired in new or existing markets, indicating expansion success.
"""

MARKET_PENETRATION_RATE = {
    "code": "MARKET_PENETRATION_RATE",
    "name": "Market Penetration Rate",
    "description": "The rate at which new clients are acquired in new or existing markets, indicating expansion success.",
    "formula": "(Number of Customers in Target Market / Total Size of Target Market) * 100",
    "calculation_formula": "(Number of Customers in Target Market / Total Size of Target Market) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The rate at which new clients are acquired in new or existing markets, indicating expansion success.",
    "expected_business_insights": "Helps assess the effectiveness of marketing and sales strategies in reaching the desired market segment.",
    "measurement_approach": "Calculates the percentage of a target market that has been captured by the company.",
    "trend_analysis": """
    * Increasing market penetration rate may indicate successful expansion efforts or improved sales strategies.
    * A decreasing rate could signal market saturation or ineffective sales tactics.
    """,
    "diagnostic_questions": """
    * Are there specific regions or demographics where market penetration is particularly low?
    * How does our market penetration rate compare with competitors or industry benchmarks?
    """,
    "actionable_tips": """
    * Invest in targeted marketing campaigns to reach untapped markets.
    * Provide additional sales training or resources to sales teams operating in underperforming markets.
    * Regularly review and adjust sales strategies to adapt to changing market conditions.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of market penetration rate over time for different markets.
    * Geospatial maps to visually represent market penetration by region or territory.
    """,
    "risk_warnings": """
    * Low market penetration rates may lead to missed revenue opportunities and hinder overall company growth.
    * Rapidly expanding into new markets without proper research and planning can result in wasted resources and potential brand damage.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track sales activities and customer interactions in different markets.
    * Data analytics tools to identify market trends and opportunities for expansion.
    """,
    "integration_points": """
    * Integrate market penetration data with customer relationship management systems to better understand customer behavior in different markets.
    * Link market penetration rate with inventory and supply chain systems to ensure adequate product availability in new markets.
    """,
    "change_impact_analysis": """
    * Increasing market penetration can lead to higher sales volume and revenue, but may also require additional resources for customer support and fulfillment.
    * Decreasing market penetration may result in reduced market share and potential loss of competitive advantage.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Penetration", "Channel Market", "Customer", "Customer Success Manager", "Expansion Opportunity", "Market Segment", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
}
