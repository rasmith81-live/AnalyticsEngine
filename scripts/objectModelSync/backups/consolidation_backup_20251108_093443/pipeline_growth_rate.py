"""
Pipeline Growth Rate KPI

Module: Business Development
"""

from analytics_models import KPI

PIPELINE_GROWTH_RATE = KPI(
    name="Pipeline Growth Rate",
    code="PIPELINE_GROWTH_RATE",
    description="The rate at which the sales pipeline is growing, indicating the potential for future sales.",
    
    # Definition & Context
    kpi_definition="The rate at which the sales pipeline is growing, indicating the potential for future sales.",
    expected_business_insights="Indicates the health of the sales pipeline and potential future revenue growth.",
    measurement_approach="Measures the increase in the number of opportunities in the sales pipeline over a period.",
    
    # Calculation
    formula="((Number of Opportunities at End of Period - Number of Opportunities at Start of Period) / Number of Opportunities at Start of Period) * 100",
    
    # Analysis
    trend_analysis="Increasing pipeline growth rate may indicate successful lead generation and marketing efforts. A decreasing rate could signal challenges in lead qualification or a lack of new opportunities entering the pipeline.",
    diagnostic_questions=['What are the main sources of leads entering the pipeline, and are they sufficient to sustain growth?', 'How effective is our lead nurturing process in converting leads into opportunities?'],
    actionable_steps={
        "operational": ['Invest in targeted marketing campaigns to attract more qualified leads.'],
        "strategic": ['Implement a robust lead scoring system to prioritize high-potential opportunities.', 'Train sales teams on effective lead qualification and conversion techniques.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the monthly or quarterly growth rate of the sales pipeline.', 'Funnel charts to visualize the conversion rates at each stage of the sales pipeline.']
    ],
    risk_warnings=['A stagnant or declining pipeline growth rate may lead to a future sales shortfall.', 'Rapidly increasing pipeline growth without proper qualification may lead to inefficiencies in the sales process.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software to track and manage leads and opportunities.', 'Sales intelligence tools to identify and target potential leads more effectively.'],
    integration_points=['Integrate pipeline growth rate with sales performance metrics to identify areas for improvement in the sales process.', 'Link with marketing automation systems to ensure a steady flow of qualified leads into the pipeline.'],
    
    # Impact
    change_impact="Increasing pipeline growth rate can lead to higher sales volume and revenue. However, rapid growth without proper management can strain resources and lead to decreased conversion rates.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Pipeline", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
