"""
Lead Nurturing Success Rate KPI

Module: Business Development
"""

from analytics_models import KPI

LEAD_NURTURING_SUCCESS_RATE = KPI(
    name="Lead Nurturing Success Rate",
    code="LEAD_NURTURING_SUCCESS_RATE",
    description="The percentage of leads that become opportunities as a result of lead nurturing efforts.",
    
    # Definition & Context
    kpi_definition="The percentage of leads that become opportunities as a result of lead nurturing efforts.",
    expected_business_insights="Assesses the effectiveness of lead nurturing programs and content marketing efforts.",
    measurement_approach="Calculates the percentage of nurtured leads that convert into sales opportunities or customers.",
    
    # Calculation
    formula="(Number of Nurtured Leads Converted / Total Number of Nurtured Leads) * 100",
    
    # Analysis
    trend_analysis="An increasing lead nurturing success rate may indicate more effective lead nurturing strategies or a higher quality of leads being generated. A decreasing rate could signal a need for improvements in lead nurturing tactics or a decline in the overall quality of leads.",
    diagnostic_questions=['Are there specific lead nurturing activities or channels that have shown higher success rates?', 'How does our lead nurturing success rate compare with industry benchmarks or with historical data?'],
    actionable_steps={
        "operational": ['Personalize lead nurturing efforts based on the specific needs and interests of different leads.'],
        "strategic": ['Implement lead scoring to prioritize and focus on leads with the highest potential for conversion.', 'Regularly review and optimize lead nurturing workflows and content based on performance data and feedback.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts tracking the lead nurturing success rate over time.', 'Pie charts showing the distribution of lead sources and their corresponding success rates.']
    ],
    risk_warnings=['A low lead nurturing success rate can lead to wasted resources and missed sales opportunities.', 'Consistently low success rates may indicate a need for a reevaluation of lead generation and qualification processes.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track and analyze lead nurturing activities and outcomes.', 'Marketing automation platforms for implementing and optimizing lead nurturing campaigns.'],
    integration_points=['Integrate lead nurturing success rate data with sales performance metrics to understand the impact on overall conversion rates and revenue.', 'Link lead nurturing data with customer relationship management systems to ensure a seamless transition from lead nurturing to sales activities.'],
    
    # Impact
    change_impact="An improved lead nurturing success rate can lead to higher conversion rates and increased sales efficiency. Conversely, a declining success rate may lead to longer sales cycles and decreased revenue.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_DEVELOPMENT", "SALES_OPERATIONS"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer Success Manager", "Lead", "Lead Qualification", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
