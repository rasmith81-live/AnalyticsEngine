"""
Partner Equity Score KPI

A measure of the value channel partners perceive in their relationship with the company, factoring in financial, support, and strategic elements.
"""

from analytics_models import KPI

PARTNER_EQUITY_SCORE = KPI(
    name="Partner Equity Score",
    code="PARTNER_EQUITY_SCORE",
    category="Channel Sales",
    
    # Core Definition
    description="A measure of the value channel partners perceive in their relationship with the company, factoring in financial, support, and strategic elements.",
    kpi_definition="A measure of the value channel partners perceive in their relationship with the company, factoring in financial, support, and strategic elements.",
    expected_business_insights="Ensures the partnership is mutually beneficial, leading to sustained engagement and growth.",
    measurement_approach="Evaluates the perceived value of a partnership to both the company and the partner.",
    
    # Formula
    formula="Qualitative Assessment Score of Partner Equity",
    calculation_formula="Qualitative Assessment Score of Partner Equity",
    
    # Analysis
    trend_analysis="""
    * Increasing partner equity score may indicate improved financial incentives, better support, or more strategic alignment with partners.
    * A decreasing score could signal dissatisfaction with the partnership, lack of support, or changes in the competitive landscape.
    """,
    diagnostic_questions="""
    * What specific elements of the partnership are contributing to the perceived value for our channel partners?
    * Are there any recent changes in our support, financial incentives, or strategic direction that could be impacting partner equity score?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly engage with channel partners to understand their needs and challenges.
    * Provide additional training and resources to help partners maximize the value they receive from the partnership.
    * Align incentives and rewards with the desired behaviors and outcomes for channel partners.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of partner equity score over time.
    * Comparative bar charts to visualize partner equity score across different regions or partner types.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low partner equity score may lead to partners seeking out other, more valuable partnerships.
    * Perceived lack of value in the partnership can result in decreased sales and market share through the channel.
    """,
    tracking_tools="""
    * Partner relationship management (PRM) software to track and analyze partner interactions and satisfaction.
    * Feedback and survey tools to gather input from channel partners on their perception of the partnership.
    """,
    integration_points="""
    * Integrate partner equity score data with sales performance metrics to understand the impact on revenue and market share.
    * Link partner equity score with marketing efforts to ensure alignment in messaging and support for channel partners.
    """,
    change_impact_analysis="""
    * Improving partner equity score can lead to increased sales, market share, and overall channel performance.
    * Conversely, a declining score may result in decreased sales and market share through the channel, impacting overall business performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Partnership", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Strategic Initiative", "Strategic Review", "Support Ticket"]
    }
)
