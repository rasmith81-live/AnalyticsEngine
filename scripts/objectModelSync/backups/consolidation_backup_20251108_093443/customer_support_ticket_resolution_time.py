"""
Customer Support Ticket Resolution Time KPI

Module: Business Development
"""

from analytics_models import KPI

CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME = KPI(
    name="Customer Support Ticket Resolution Time",
    code="CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME",
    description="The average time it takes for the sales or support team to resolve customer issues or support tickets.",
    
    # Definition & Context
    kpi_definition="The average time it takes for the sales or support team to resolve customer issues or support tickets.",
    expected_business_insights="Indicates the efficiency of customer support teams and impacts customer satisfaction.",
    measurement_approach="Considers the average time taken to resolve customer support tickets.",
    
    # Calculation
    formula="Total Time Taken to Resolve Tickets / Number of Tickets Resolved",
    
    # Analysis
    trend_analysis="An increasing resolution time may indicate a growing backlog of customer issues or a decrease in team efficiency. A decreasing resolution time could signal improved processes, better training, or enhanced tools for the sales or support team.",
    diagnostic_questions=['Are there specific types of customer issues that consistently take longer to resolve?', 'How does our resolution time compare with industry benchmarks or customer expectations?'],
    actionable_steps={
        "operational": ['Implement customer relationship management (CRM) software to streamline ticket management and improve response times.'],
        "strategic": ['Provide ongoing training and support for the sales or support team to enhance their problem-solving skills and efficiency.', 'Regularly review and update the knowledge base or resources available to the team to address common customer issues more effectively.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the average resolution time over time to identify trends and patterns.', 'Stacked bar charts comparing resolution times by different customer issue categories.']
    ],
    risk_warnings=['Long resolution times can lead to customer dissatisfaction and potentially lost sales or recurring issues.', 'Consistently high resolution times may indicate underlying issues in team capacity, training, or resource allocation.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Helpdesk or ticketing systems like Zendesk or Freshdesk to track and manage customer support tickets more efficiently.', 'Performance analytics tools to monitor and analyze resolution times and identify areas for improvement.'],
    integration_points=['Integrate customer support ticket data with sales performance metrics to understand the impact of resolution times on customer satisfaction and retention.', 'Link resolution time tracking with customer feedback systems to gather insights on the quality of support provided.'],
    
    # Impact
    change_impact="Improving resolution times can enhance customer satisfaction and loyalty, potentially leading to increased sales and positive word-of-mouth referrals. However, focusing solely on reducing resolution times may risk sacrificing the quality of support provided, impacting long-term customer relationships.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
