"""
Qualified Leads per Month KPI

Module: Business Development
"""

from analytics_models import KPI

QUALIFIED_LEADS_PER_MONTH = KPI(
    name="Qualified Leads per Month",
    code="QUALIFIED_LEADS_PER_MONTH",
    description="The number of leads that meet certain criteria set by the sales team, indicating a higher probability of converting into customers.",
    
    # Definition & Context
    kpi_definition="The number of leads that meet certain criteria set by the sales team, indicating a higher probability of converting into customers.",
    expected_business_insights="Assesses the success of lead generation efforts and helps forecast potential sales.",
    measurement_approach="Counts the number of leads that meet the criteria to be considered qualified for the sales process.",
    
    # Calculation
    formula="Total Number of Qualified Leads in a Month",
    
    # Analysis
    trend_analysis="Increasing qualified leads per month may indicate improved marketing strategies or a growing market for the product or service. A decreasing trend could signal a need for reevaluation of lead qualification criteria or a decline in market demand.",
    diagnostic_questions=['Are there specific lead sources or channels that consistently generate higher quality leads?', 'How do our qualified leads per month compare with industry benchmarks or seasonal fluctuations?'],
    actionable_steps={
        "operational": ['Refine lead qualification criteria based on feedback from the sales team and customer conversion data.'],
        "strategic": ['Implement targeted marketing campaigns to attract higher quality leads.', 'Provide additional training and resources to the sales team to improve lead conversion rates.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the monthly trend of qualified leads.', 'Pie charts comparing the distribution of qualified leads by source or channel.']
    ],
    risk_warnings=['Low quality leads may result in wasted sales efforts and resources.', 'Overemphasis on lead quantity over quality can lead to a high volume of unproductive leads.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software to track lead sources and qualification criteria.', 'Marketing automation platforms to streamline lead nurturing and qualification processes.'],
    integration_points=['Integrate lead qualification data with sales performance metrics to assess the effectiveness of lead quality on conversion rates.', 'Link lead qualification criteria with marketing campaign data to optimize lead generation efforts.'],
    
    # Impact
    change_impact="Improving lead quality can lead to higher conversion rates and increased sales revenue. However, a focus on higher quality leads may result in a lower volume of leads, impacting overall sales pipeline size.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "SALES_DEVELOPMENT"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Lead", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
