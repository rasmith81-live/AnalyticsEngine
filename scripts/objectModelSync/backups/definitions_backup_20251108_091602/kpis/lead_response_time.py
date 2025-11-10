"""
Lead Response Time KPI

Module: Business Development
"""

from analytics_models import KPI

LEAD_RESPONSE_TIME = KPI(
    name="Lead Response Time",
    code="LEAD_RESPONSE_TIME",
    description="The time it takes for a sales representative to respond to a new lead.",
    
    # Definition & Context
    kpi_definition="The time it takes for a sales representative to respond to a new lead.",
    expected_business_insights="Indicates the responsiveness of the sales team and can impact the rate of lead conversion.",
    measurement_approach="Considers the average time taken by sales teams to respond to leads.",
    
    # Calculation
    formula="Total Time Taken to Respond to Leads / Total Number of Leads",
    
    # Analysis
    trend_analysis="Shortening lead response times may indicate improved sales team efficiency and effectiveness in engaging with new leads. An increasing lead response time could signal a need for additional sales resources or a breakdown in lead management processes.",
    diagnostic_questions=['What are the current average lead response times for different sales representatives or teams?', 'How do our lead response times compare with industry benchmarks or customer expectations?'],
    actionable_steps={
        "operational": ['Implement automated lead assignment and notification systems to ensure prompt follow-up on new leads.'],
        "strategic": ['Provide ongoing training and coaching to sales representatives on effective lead engagement and response strategies.', 'Utilize customer relationship management (CRM) software to track and prioritize lead follow-ups.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing lead response times over time for individual sales representatives or teams.', 'Scatter plots to identify any correlation between lead response time and conversion rates.']
    ],
    risk_warnings=['Delayed lead responses can result in lost opportunities and potential revenue.', "Consistently slow lead response times may damage the company's reputation and brand image."],
    
    # Tools & Integration
    suggested_tracking_tools=['CRM systems with lead tracking and automated notification features.', 'Lead management software to streamline lead distribution and follow-up processes.'],
    integration_points=['Integrate lead response time data with sales performance metrics to understand the impact on conversion rates and revenue generation.', 'Link lead response time tracking with customer relationship management systems for a comprehensive view of customer interactions.'],
    
    # Impact
    change_impact="Improving lead response times can lead to increased customer satisfaction and loyalty, ultimately impacting long-term sales performance. However, a focus solely on response time may impact the quality of interactions and the ability to personalize the sales process.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_ENABLEMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY", "SALES_TRAINING_COACHING"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Deal", "Lead", "Lead Qualification", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
