"""
New Business Opportunities Identified KPI

Module: Business Development
"""

from analytics_models import KPI

NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED = KPI(
    name="New Business Opportunities Identified",
    code="NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED",
    description="The number of new business opportunities identified by the team, indicating the potential for revenue growth.",
    
    # Definition & Context
    kpi_definition="The number of new business opportunities identified by the team, indicating the potential for revenue growth.",
    expected_business_insights="Signals the effectiveness of lead generation efforts and market expansion potential.",
    measurement_approach="Counts the number of new potential sales opportunities discovered.",
    
    # Calculation
    formula="Total Number of New Opportunities Identified",
    
    # Analysis
    trend_analysis="An increasing number of new business opportunities identified may indicate a proactive and effective sales team, as well as a growing market. A decreasing trend in new business opportunities could signal market saturation, ineffective lead generation strategies, or a lack of innovation in product offerings.",
    diagnostic_questions=['Are there specific industries or regions where new business opportunities are consistently being identified?', 'How does the conversion rate of identified opportunities compare to previous periods?'],
    actionable_steps={
        "operational": ['Invest in market research and customer segmentation to identify untapped potential in existing markets.'],
        "strategic": ['Provide ongoing training and support for the sales team to enhance their prospecting and lead generation skills.', 'Explore strategic partnerships or collaborations to access new markets and customer segments.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of new business opportunities identified over time.', 'Pie charts to visualize the distribution of identified opportunities by industry or region.']
    ],
    risk_warnings=['A consistently low number of new business opportunities identified may lead to stagnant revenue growth and decreased market share.', 'Relying solely on existing customer base without actively seeking new opportunities can result in vulnerability to market changes and competitive pressures.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software to track and manage leads and opportunities.', 'Data analytics tools to identify patterns and trends in the sources of new business opportunities.'],
    integration_points=['Integrate with marketing automation systems to align lead generation efforts with identified opportunities.', 'Link with financial forecasting and budgeting systems to ensure that resource allocation aligns with the potential revenue from new opportunities.'],
    
    # Impact
    change_impact="An increase in new business opportunities can impact production, supply chain, and customer service operations, requiring adjustments to meet increased demand. Conversely, a decrease in identified opportunities may lead to cost-cutting measures and a focus on retaining existing customers.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Quarterly Business Review", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
