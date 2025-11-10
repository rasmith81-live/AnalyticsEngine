"""
Lead-to-Opportunity Conversion Rate KPI

Module: Business Development
"""

from analytics_models import KPI

LEAD_TO_OPPORTUNITY_CONVERSION_RATE = KPI(
    name="Lead-to-Opportunity Conversion Rate",
    code="LEAD_TO_OPPORTUNITY_CONVERSION_RATE",
    description="The percentage of leads that become sales opportunities, indicating the effectiveness of the lead qualification process.",
    
    # Definition & Context
    kpi_definition="The percentage of leads that become sales opportunities, indicating the effectiveness of the lead qualification process.",
    expected_business_insights="Measures the effectiveness of lead qualification processes and the sales team's efficiency.",
    measurement_approach="Tracks the percentage of leads that become qualified sales opportunities.",
    
    # Calculation
    formula="(Number of Leads Converted to Opportunities / Total Number of Leads) * 100",
    
    # Analysis
    trend_analysis="An increasing lead-to-opportunity conversion rate may indicate improved lead qualification processes or a higher demand for the product or service. A decreasing rate could signal issues in lead qualification, changes in market demand, or ineffective sales strategies.",
    diagnostic_questions=['Are there specific lead sources or channels that consistently result in higher conversion rates?', 'How does our lead-to-opportunity conversion rate compare with industry benchmarks or historical data?'],
    actionable_steps={
        "operational": ['Regularly review and update lead qualification criteria to ensure they align with the ideal customer profile.'],
        "strategic": ['Provide ongoing training and support for sales teams to improve their lead nurturing and qualification skills.', 'Implement lead scoring systems to prioritize high-quality leads and allocate resources effectively.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of lead-to-opportunity conversion rates over time.', 'Pie charts comparing conversion rates across different lead sources or channels.']
    ],
    risk_warnings=['A consistently low conversion rate may lead to wasted resources and decreased sales effectiveness.', 'Rapid fluctuations in conversion rates could indicate instability in the sales process or market conditions.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track and analyze lead interactions and conversions.', 'Sales enablement platforms to provide sales teams with the necessary tools and content to improve lead conversion.'],
    integration_points=['Integrate lead-to-opportunity conversion data with marketing automation systems to align marketing efforts with sales goals.', 'Link conversion rate analysis with customer relationship management (CRM) systems to gain insights into customer behavior and preferences.'],
    
    # Impact
    change_impact="Improving the lead-to-opportunity conversion rate can lead to increased sales revenue and improved sales team morale. Conversely, a declining conversion rate may result in missed sales opportunities and decreased confidence in the sales process.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Expansion Opportunity", "Lead", "Lead Qualification", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
