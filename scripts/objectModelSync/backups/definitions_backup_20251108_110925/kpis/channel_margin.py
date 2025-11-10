"""
Channel Margin KPI

A measure of the profit margin a company achieves on sales made through channel partners.
"""

from analytics_models import KPI

CHANNEL_MARGIN = KPI(
    name="Channel Margin",
    code="CHANNEL_MARGIN",
    category="Channel Sales",
    
    # Core Definition
    description="A measure of the profit margin a company achieves on sales made through channel partners.",
    kpi_definition="A measure of the profit margin a company achieves on sales made through channel partners.",
    expected_business_insights="Highlights the profitability of channel sales, guiding pricing strategies and partner incentives.",
    measurement_approach="Reflects the difference between the sales price obtained by the channel partner and their cost of procurement.",
    
    # Formula
    formula="(Sales Price - Cost of Procurement) / Sales Price * 100",
    calculation_formula="(Sales Price - Cost of Procurement) / Sales Price * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing channel margin may indicate successful negotiation of better terms with channel partners or a shift towards higher-margin products.
    * Decreasing channel margin could signal increased competition, pricing pressures, or inefficiencies in the channel sales process.
    """,
    diagnostic_questions="""
    * What factors are contributing to changes in channel margin, such as product mix, pricing strategies, or partner performance?
    * Are there specific channel partners or regions where channel margin is consistently higher or lower, and what factors may be influencing this?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and renegotiate terms with channel partners to ensure margins are competitive and sustainable.
    * Provide training and support to channel partners to help them sell higher-margin products or services effectively.
    * Implement pricing strategies that incentivize channel partners to focus on higher-margin offerings.
    """,
    visualization_suggestions="""
    * Line charts showing channel margin trends over time, segmented by product category or partner type.
    * Pareto charts to identify the most significant channel partners contributing to overall margin performance.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Declining channel margins may lead to reduced profitability and financial instability for the organization.
    * High channel margins in certain regions or with specific partners may indicate potential pricing inefficiencies or missed opportunities for growth.
    """,
    tracking_tools="""
    * Financial analysis and reporting software to track and analyze channel margin data in real-time.
    * Partner relationship management (PRM) platforms to monitor and optimize partner performance and margin contributions.
    """,
    integration_points="""
    * Integrate channel margin data with sales and marketing systems to align strategies with margin performance and optimize resource allocation.
    * Link channel margin analysis with supply chain and inventory management systems to ensure efficient fulfillment and minimize margin erosion due to stockouts or overstock situations.
    """,
    change_impact_analysis="""
    * Improving channel margin can positively impact overall profitability and financial health, but may require initial investments in partner enablement and relationship management.
    * Conversely, declining channel margin can lead to reduced resources for innovation and growth, impacting long-term competitiveness and market position.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
