"""
Sales Opportunity Scorecard KPI

A tool that evaluates and scores sales opportunities based on various criteria like deal size, likelihood of close, etc.
"""

from analytics_models import KPI

SALES_OPPORTUNITY_SCORECARD = KPI(
    name="Sales Opportunity Scorecard",
    code="SALES_OPPORTUNITY_SCORECARD",
    category="Key Account Management",
    
    # Core Definition
    description="A tool that evaluates and scores sales opportunities based on various criteria like deal size, likelihood of close, etc.",
    kpi_definition="A tool that evaluates and scores sales opportunities based on various criteria like deal size, likelihood of close, etc.",
    expected_business_insights="Helps prioritize sales efforts on the most promising opportunities to maximize revenue.",
    measurement_approach="Utilizes a set of criteria to score sales opportunities based on potential value and likelihood to close.",
    
    # Formula
    formula="Custom scoring based on criteria like budget, decision-maker accessibility, timeline, etc.",
    calculation_formula="Custom scoring based on criteria like budget, decision-maker accessibility, timeline, etc.",
    
    # Analysis
    trend_analysis="""
    * Increasing sales opportunity scores may indicate a more effective sales process or a higher quality of leads.
    * Decreasing scores could signal a need for sales team training or a shift in the market that requires a different approach.
    """,
    diagnostic_questions="""
    * Are there common characteristics among opportunities with high scores?
    * What factors have historically led to successful closures of high-scoring opportunities?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update the criteria used to score sales opportunities to ensure they align with current market conditions and customer needs.
    * Provide ongoing training and support for the sales team to improve their ability to identify and pursue high-scoring opportunities.
    * Implement a lead nurturing strategy to increase the likelihood of closing opportunities with lower scores.
    """,
    visualization_suggestions="""
    * Line charts showing the average opportunity score over time to identify trends.
    * Pie charts to compare the distribution of scores across different sales territories or product lines.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on the opportunity score without considering other factors may result in missed opportunities or lost revenue.
    * Inaccurate scoring criteria could lead to misallocation of resources and ineffective sales efforts.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software with built-in opportunity scoring functionality.
    * Data analytics tools to identify patterns and correlations between opportunity scores and eventual outcomes.
    """,
    integration_points="""
    * Integrate sales opportunity scoring with performance management systems to align sales team incentives with the pursuit of high-scoring opportunities.
    * Link opportunity scoring with marketing automation platforms to ensure a consistent approach to lead qualification and nurturing.
    """,
    change_impact_analysis="""
    * Improving opportunity scores can lead to increased revenue and market share, but may also require adjustments in resource allocation and sales strategies.
    * Lowering opportunity scores may indicate a need to realign sales and marketing efforts, potentially impacting short-term performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Deal", "Deal", "Expansion Opportunity", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Partner Performance Scorecard", "Performance Scorecard", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
