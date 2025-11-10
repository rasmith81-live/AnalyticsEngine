"""
Cost per Opportunity KPI

Module: Business Development
"""

from analytics_models import KPI

COST_PER_OPPORTUNITY = KPI(
    name="Cost per Opportunity",
    code="COST_PER_OPPORTUNITY",
    description="The average cost incurred to turn a lead into a sales opportunity.",
    
    # Definition & Context
    kpi_definition="The average cost incurred to turn a lead into a sales opportunity.",
    expected_business_insights="Assists in evaluating the effectiveness of lead nurturing and the cost-efficiency of the sales process.",
    measurement_approach="Measures the cost associated with converting a lead into a sales opportunity.",
    
    # Calculation
    formula="Total Cost of Sales and Marketing / Total Number of Opportunities",
    
    # Analysis
    trend_analysis="Increasing cost per opportunity may indicate inefficiencies in the lead conversion process or rising marketing expenses. A decreasing cost per opportunity could signal improved targeting, better lead quality, or more effective sales tactics.",
    diagnostic_questions=['Are there specific marketing channels or campaigns that result in higher or lower cost per opportunity?', 'How does our cost per opportunity compare with industry benchmarks or with different sales teams within the organization?'],
    actionable_steps={
        "operational": ['Refine lead qualification criteria to focus on higher potential opportunities.'],
        "strategic": ['Implement sales automation tools to streamline the lead nurturing and conversion process.', 'Regularly review and optimize marketing and sales expenses to ensure cost-effectiveness.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of cost per opportunity over time.', 'Pareto charts to identify the most significant factors contributing to the cost per opportunity.']
    ],
    risk_warnings=['High cost per opportunity can lead to reduced profitability and ROI on sales and marketing efforts.', 'Significant fluctuations in cost per opportunity may indicate instability in the lead generation and sales processes.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software to track and analyze lead conversion costs.', 'Marketing automation platforms to optimize lead nurturing and engagement.'],
    integration_points=['Integrate cost per opportunity analysis with financial reporting to understand the impact on overall profitability.', 'Link with customer relationship management systems to track the quality of leads and their conversion costs.'],
    
    # Impact
    change_impact="Reducing cost per opportunity may lead to increased sales efficiency and profitability, but could also require upfront investments in technology and process improvements. Conversely, a high cost per opportunity can strain the sales budget and impact the ability to scale the sales operation.",
    
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
