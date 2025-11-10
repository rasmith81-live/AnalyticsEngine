"""
Sales Team Response Time KPI

Module: Business Development
"""

from analytics_models import KPI

SALES_TEAM_RESPONSE_TIME = KPI(
    name="Sales Team Response Time",
    code="SALES_TEAM_RESPONSE_TIME",
    description="The average time it takes for a sales representative to follow up on a lead or customer inquiry.",
    
    # Definition & Context
    kpi_definition="The average time it takes for a sales representative to follow up on a lead or customer inquiry.",
    expected_business_insights="Indicates the sales team's responsiveness and can impact customer satisfaction and conversion rates.",
    measurement_approach="Considers the average response time of the sales team to customer inquiries.",
    
    # Calculation
    formula="Average Time Taken by Sales Team to Respond to Inquiries",
    
    # Analysis
    trend_analysis="A decreasing response time may indicate improved sales team efficiency and customer service. An increasing response time could signal overwhelmed sales teams or ineffective lead management processes.",
    diagnostic_questions=['Are there specific types of leads or inquiries that consistently take longer to follow up on?', 'How does our average response time compare to industry standards or customer expectations?'],
    actionable_steps={
        "operational": ['Implement lead management software to automate and prioritize follow-up tasks.'],
        "strategic": ['Provide ongoing training and coaching to sales representatives on effective communication and time management.', 'Establish clear escalation processes for high-priority leads or urgent customer inquiries.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing average response time over different time periods (e.g., daily, weekly, monthly).', 'Scatter plots to identify outliers in response time for individual sales representatives.']
    ],
    risk_warnings=['Long response times can result in lost sales opportunities and dissatisfied customers.', 'Consistently short response times may lead to burnout and decreased sales team morale.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) systems with lead tracking and automated follow-up capabilities.', 'Sales performance analytics tools to identify bottlenecks in the lead management process.'],
    integration_points=['Integrate response time tracking with customer feedback systems to correlate response times with customer satisfaction.', 'Link response time data with sales forecasting to understand the impact on future revenue.'],
    
    # Impact
    change_impact="Improving response time can lead to increased customer retention and loyalty. However, overly aggressive response time targets may sacrifice the quality of interactions with leads and customers.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_PERFORMANCE"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Lead Qualification", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
