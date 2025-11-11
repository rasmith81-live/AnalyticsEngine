"""
Market Share Growth KPI

The increase in a company's sales volume in relation to the total sales volume of all competitors in the market, indicating the company's growing dominance in the market.
"""

MARKET_SHARE_GROWTH = {
    "code": "MARKET_SHARE_GROWTH",
    "name": "Market Share Growth",
    "description": "The increase in a company's sales volume in relation to the total sales volume of all competitors in the market, indicating the company's growing dominance in the market.",
    "formula": "((Current Market Share - Previous Market Share) / Previous Market Share) * 100",
    "calculation_formula": "((Current Market Share - Previous Market Share) / Previous Market Share) * 100",
    "category": "Channel Sales",
    "is_active": True,
    "kpi_definition": "The increase in a company's sales volume in relation to the total sales volume of all competitors in the market, indicating the company's growing dominance in the market.",
    "expected_business_insights": "Reflects the impact of channel strategy on competitive positioning within the market.",
    "measurement_approach": "Evaluates the increase in the company’s market share due to channel sales.",
    "trend_analysis": """
    * Market share growth tends to show a gradual increase over time as the company gains traction in the market.
    * Positive performance shifts may be indicated by consistent, steady growth in market share, while negative shifts could be seen in stagnant or declining growth rates.
    """,
    "diagnostic_questions": """
    * What specific strategies or initiatives have contributed to the increase in market share?
    * Are there any external factors or market conditions that could be influencing the market share growth?
    """,
    "actionable_tips": """
    * Invest in targeted marketing and sales efforts to capture a larger share of the market.
    * Focus on product differentiation and innovation to attract more customers and increase market share.
    * Explore strategic partnerships or acquisitions to expand market presence and gain a competitive edge.
    """,
    "visualization_suggestions": """
    * Line charts to visually represent the steady increase in market share over time.
    * Pie charts to compare the company's market share with that of competitors in a specific timeframe.
    """,
    "risk_warnings": """
    * Rapid market share growth may lead to increased competition and potential price wars.
    * Overreliance on a specific market segment for growth could pose risks if that segment becomes saturated or experiences a downturn.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and analyze customer acquisition and retention efforts.
    * Competitor analysis tools to monitor and compare market share data with industry competitors.
    """,
    "integration_points": """
    * Integrate market share data with sales and marketing systems to align strategies with growth opportunities.
    * Link market share metrics with financial systems to assess the impact of market share growth on revenue and profitability.
    """,
    "change_impact_analysis": """
    * Increasing market share can lead to economies of scale and potentially lower production costs.
    * However, aggressive tactics to gain market share may impact brand reputation and customer loyalty if not managed carefully.
    """,
    "metadata_": {"modules": ["CHANNEL_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["CHANNEL_SALES"],
    "module_code": "CHANNEL_SALES",
}
