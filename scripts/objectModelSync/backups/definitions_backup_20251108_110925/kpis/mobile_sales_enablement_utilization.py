"""
Mobile Sales Enablement Utilization KPI

Module: Business Development
"""

from analytics_models import KPI

MOBILE_SALES_ENABLEMENT_UTILIZATION = KPI(
    name="Mobile Sales Enablement Utilization",
    code="MOBILE_SALES_ENABLEMENT_UTILIZATION",
    description="The percentage of the sales team that uses mobile tools and applications to enable sales activities.",
    
    # Definition & Context
    kpi_definition="The percentage of the sales team that uses mobile tools and applications to enable sales activities.",
    expected_business_insights="Indicates the adaptability of the sales team to technology and can correlate to increased productivity.",
    measurement_approach="Tracks the usage rate of mobile tools and applications by the sales team.",
    
    # Calculation
    formula="(Number of Sales Representatives Using Mobile Tools / Total Number of Sales Representatives) * 100",
    
    # Analysis
    trend_analysis="Increasing utilization may indicate a positive shift towards mobile sales enablement and improved sales productivity. Decreasing utilization could signal resistance to adopting mobile tools or a lack of effectiveness in the current applications.",
    diagnostic_questions=['What are the primary reasons for not using mobile tools for sales activities?', 'How does the utilization of mobile sales enablement tools vary across different segments of the sales team?'],
    actionable_steps={
        "operational": ['Provide training and support to ensure the sales team is proficient in using mobile sales enablement tools.'],
        "strategic": ["Regularly update and customize mobile applications to better align with the sales team's needs and feedback.", 'Incentivize the use of mobile tools through recognition and rewards for top performers.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend in utilization over time.', 'Pie charts to compare the distribution of mobile tool usage across the sales team.']
    ],
    risk_warnings=['Low utilization may lead to missed sales opportunities and reduced efficiency in sales processes.', 'Resistance to mobile tools could indicate broader issues with technology adoption and change management within the sales team.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Sales enablement platforms like Salesforce or HubSpot for tracking and analyzing mobile sales enablement utilization.', 'Mobile analytics tools to gather insights on how the sales team interacts with mobile applications.'],
    integration_points=['Integrate mobile sales enablement utilization data with CRM systems to understand the impact on sales performance and customer interactions.', 'Link utilization metrics with training and development platforms to identify areas for improvement in sales enablement training.'],
    
    # Impact
    change_impact="Improving mobile sales enablement utilization can lead to increased sales efficiency and potentially higher revenue. However, a lack of utilization may result in missed opportunities and reduced competitiveness in the market.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Enablement Feedback", "Enablement Platform", "Product Usage", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
