"""
Opportunity Pipeline KPI

Module: Business Development
"""

from analytics_models import KPI

OPPORTUNITY_PIPELINE = KPI(
    name="Opportunity Pipeline",
    code="OPPORTUNITY_PIPELINE",
    description="The number of opportunities in the pipeline and their value.",
    
    # Definition & Context
    kpi_definition="The number of opportunities in the pipeline and their value.",
    expected_business_insights="Provides a visual representation and overview of potential revenue and informs forecasting.",
    measurement_approach="Consists of all sales opportunities at various stages in the sales process.",
    
    # Calculation
    formula="Sum of All Opportunities at Various Stages of the Sales Cycle",
    
    # Analysis
    trend_analysis="An increasing number of opportunities in the pipeline with a decreasing total value may indicate a higher volume of low-value opportunities, potentially impacting overall sales performance. A consistent or decreasing number of opportunities with a steady or increasing total value could signal a healthy pipeline with higher-value opportunities, leading to better conversion rates and revenue generation.",
    diagnostic_questions=['What is the average value of opportunities in the pipeline, and how does it compare to previous periods?', 'Are there specific stages in the sales process where opportunities tend to stall or drop out, impacting the overall pipeline value?'],
    actionable_steps={
        "operational": ['Implement a lead scoring system to prioritize high-value opportunities and focus sales efforts on those with the highest potential return.'],
        "strategic": ['Regularly review and clean the pipeline to remove stale or low-value opportunities, ensuring a more accurate representation of potential revenue.', 'Provide ongoing training and support for sales teams to improve their ability to identify and pursue high-value opportunities.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Stacked bar charts showing the distribution of opportunities by value range within the pipeline.', 'Line charts tracking the total pipeline value over time to identify trends and fluctuations.']
    ],
    risk_warnings=['A high number of low-value opportunities may lead to wasted sales efforts and resources, impacting overall sales efficiency and effectiveness.', 'A declining total pipeline value could indicate a lack of new high-value opportunities entering the pipeline, potentially leading to future revenue shortfalls.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software with robust opportunity tracking and reporting capabilities.', 'Sales analytics tools to identify patterns and trends within the opportunity pipeline and assess the impact of different sales strategies.'],
    integration_points=['Integrate opportunity pipeline data with sales forecasting and resource allocation systems to align sales efforts with expected revenue generation.', 'Link pipeline management with marketing automation platforms to ensure a steady flow of high-quality leads into the pipeline.'],
    
    # Impact
    change_impact="Improving the quality and value distribution of opportunities in the pipeline can lead to more efficient use of sales resources and higher overall revenue. However, a sudden increase in high-value opportunities may require adjustments in sales strategies and resource allocation to effectively capitalize on the potential revenue.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_DEVELOPMENT"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Deal", "Expansion Opportunity", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
