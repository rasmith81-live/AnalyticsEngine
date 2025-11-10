"""
Competitive Win Rate KPI

Module: Business Development
"""

from analytics_models import KPI

COMPETITIVE_WIN_RATE = KPI(
    name="Competitive Win Rate",
    code="COMPETITIVE_WIN_RATE",
    description="The percentage of deals won against competitors, indicating the sales team's effectiveness in competitive situations.",
    
    # Definition & Context
    kpi_definition="The percentage of deals won against competitors, indicating the sales team's effectiveness in competitive situations.",
    expected_business_insights="Signals the company's market competitiveness and sales team effectiveness.",
    measurement_approach="Calculates the percentage of deals won against competitors.",
    
    # Calculation
    formula="(Number of Deals Won Against Competitors / Total Number of Competitive Deals) * 100",
    
    # Analysis
    trend_analysis="An increasing competitive win rate may indicate improved sales strategies, better product positioning, or a stronger understanding of customer needs. A decreasing rate could signal increased competition, ineffective sales tactics, or a shift in customer preferences towards competitors.",
    diagnostic_questions=['What specific factors have contributed to recent wins against competitors?', 'Are there common reasons why deals are lost to competitors, and how can those be addressed?'],
    actionable_steps={
        "operational": ['Invest in ongoing sales training and development to enhance competitive selling skills.'],
        "strategic": ['Conduct regular competitive analysis to understand the strengths and weaknesses of competitors and adjust sales strategies accordingly.', 'Seek feedback from lost deals to identify areas for improvement and address any recurring issues.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the competitive win rate over time to identify trends and fluctuations.', 'Comparison bar charts to visualize the win rate against specific competitors or within different market segments.']
    ],
    risk_warnings=['A consistently low competitive win rate may indicate a need for significant changes in sales strategies or product offerings.', 'Highly fluctuating win rates could signal inconsistency in sales performance or market volatility.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track and analyze competitive win rates and sales activities.', "Competitive intelligence tools to gather insights on competitors' activities and market positioning."],
    integration_points=['Integrate competitive win rate data with sales performance metrics to identify correlations and areas for improvement.', 'Link win rate analysis with customer feedback and satisfaction data to understand the impact of competitive success on customer relationships.'],
    
    # Impact
    change_impact="Improving the competitive win rate can lead to increased market share and revenue growth, but may also require additional resources and investments in sales capabilities. A declining win rate can affect overall sales team morale and confidence, potentially impacting overall sales performance.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "OUTSIDE_SALES"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Competitive Analysis", "Deal", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
