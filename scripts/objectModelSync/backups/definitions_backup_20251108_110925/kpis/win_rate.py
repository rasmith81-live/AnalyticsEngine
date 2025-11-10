"""
Win Rate KPI

The percentage of deals won out of the total number of opportunities.
"""

from analytics_models import KPI

WIN_RATE = KPI(
    name="Win Rate",
    code="WIN_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The percentage of deals won out of the total number of opportunities.",
    kpi_definition="The percentage of deals won out of the total number of opportunities.",
    expected_business_insights="Assesses the effectiveness of channel partners in closing deals and informs sales strategy improvements.",
    measurement_approach="Calculates the percentage of sales opportunities that result in a successful sale by channel partners.",
    
    # Formula
    formula="(Number of Opportunities Won by Partners / Total Number of Opportunities) * 100",
    calculation_formula="(Number of Opportunities Won by Partners / Total Number of Opportunities) * 100",
    
    # Analysis
    trend_analysis="""
    * A rising win rate may indicate improved sales strategies, better product-market fit, or increased customer satisfaction.
    * A decreasing win rate could signal increased competition, ineffective sales tactics, or declining product quality.
    """,
    diagnostic_questions="""
    * Are there specific sales channels or regions where the win rate is consistently higher or lower?
    * How does our win rate compare with industry benchmarks or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training and support to improve the effectiveness of the sales team.
    * Regularly review and update the sales process to ensure it aligns with customer needs and market trends.
    * Implement a lead scoring system to prioritize high-potential opportunities and improve win rates.
    """,
    visualization_suggestions="""
    * Line charts showing win rates over time to identify trends and seasonality.
    * Pie charts comparing win rates across different sales channels or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low win rate can lead to decreased revenue and market share.
    * A high win rate without corresponding revenue growth may indicate pricing or profitability issues.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze sales performance and customer interactions.
    * Sales enablement platforms to provide sales teams with the necessary tools and resources to improve win rates.
    """,
    integration_points="""
    * Integrate win rate data with customer feedback and satisfaction metrics to understand the correlation between sales performance and customer experience.
    * Link win rate tracking with marketing and lead generation efforts to identify the most effective lead sources.
    """,
    change_impact_analysis="""
    * Improving the win rate can lead to increased revenue and market share, but may also require additional resources and investment in sales and marketing.
    * A declining win rate can impact overall business performance and may require strategic adjustments in sales and marketing strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lost Sale", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
