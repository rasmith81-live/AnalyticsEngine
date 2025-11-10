"""
Lost Deal Analysis KPI

Module: Business Development
"""

from analytics_models import KPI

LOST_DEAL_ANALYSIS = KPI(
    name="Lost Deal Analysis",
    code="LOST_DEAL_ANALYSIS",
    description="The systematic examination of lost deals to understand why they were not won and to implement improvements.",
    
    # Definition & Context
    kpi_definition="The systematic examination of lost deals to understand why they were not won and to implement improvements.",
    expected_business_insights="Provides insights into sales strategy inefficiencies and competitive disadvantages, offering areas for improvement.",
    measurement_approach="Involves the examination of reasons and trends behind lost deals.",
    
    # Calculation
    formula="(Qualitative analysis based on deal feedback and data)",
    
    # Analysis
    trend_analysis="An increasing number of lost deals may indicate issues with the sales process, product quality, or competitive pricing. A decreasing trend in lost deals could signal improved sales strategies, product enhancements, or better market positioning.",
    diagnostic_questions=['Are there common reasons why deals are being lost, such as pricing, product features, or customer service?', 'How do our lost deal reasons compare with industry benchmarks or competitor offerings?'],
    actionable_steps={
        "operational": ['Implement regular win/loss analysis meetings to gather insights from the sales team about lost deals.'],
        "strategic": ['Provide additional sales training or resources to address common reasons for lost deals.', 'Consider adjusting pricing, product features, or sales processes based on the analysis of lost deals.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Pie charts to visualize the distribution of reasons for lost deals.', 'Trend line graphs to track changes in lost deals over time.']
    ],
    risk_warnings=['High numbers of lost deals can impact revenue and market share.', 'Repeatedly losing deals for the same reasons may indicate systemic issues that need to be addressed.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software to track and analyze lost deals.', 'Sales analytics tools to identify patterns and trends in lost deals data.'],
    integration_points=['Integrate lost deal analysis with sales performance evaluations to identify areas for improvement.', 'Link lost deal data with product development and marketing strategies to address identified weaknesses.'],
    
    # Impact
    change_impact="Reducing the number of lost deals can lead to increased revenue and market share. However, changes to address lost deals may require investment in product development, sales training, or marketing efforts.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Channel Deal", "Competitive Analysis", "Customer Feedback", "Deal", "Enablement Feedback", "Lost Sale", "Quarterly Business Review"]
    }
)
