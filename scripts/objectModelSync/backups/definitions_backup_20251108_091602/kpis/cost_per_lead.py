"""
Cost per Lead KPI

Module: Business Development
"""

from analytics_models import KPI

COST_PER_LEAD = KPI(
    name="Cost per Lead",
    code="COST_PER_LEAD",
    description="The average cost incurred to generate one lead, which helps to evaluate the efficiency of marketing campaigns.",
    
    # Definition & Context
    kpi_definition="The average cost incurred to generate one lead, which helps to evaluate the efficiency of marketing campaigns.",
    expected_business_insights="Helps in budget allocation for marketing campaigns and measures the efficiency of lead generation efforts.",
    measurement_approach="Considers the average cost incurred to generate a lead.",
    
    # Calculation
    formula="Total Cost of Lead Generation / Total Number of Leads",
    
    # Analysis
    trend_analysis="Increasing cost per lead may indicate inefficiencies in marketing campaigns or a decrease in the quality of leads generated. A decreasing cost per lead could signal improved targeting or more effective lead generation strategies.",
    diagnostic_questions=['Are there specific marketing channels or campaigns that are driving higher cost per lead?', 'How does our cost per lead compare to industry benchmarks or historical performance?'],
    actionable_steps={
        "operational": ['Refine audience targeting to focus on higher quality leads.'],
        "strategic": ['Optimize marketing campaigns to improve conversion rates and reduce overall lead generation costs.', 'Implement lead scoring to prioritize and focus on leads with the highest potential for conversion.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of cost per lead over time.', 'Pie charts to compare the distribution of lead costs across different marketing channels or campaigns.']
    ],
    risk_warnings=['High cost per lead can lead to decreased ROI and impact overall profitability.', 'A consistently increasing cost per lead may indicate a need for a strategic shift in marketing approach.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Marketing automation platforms like HubSpot or Marketo to track and analyze lead generation costs.', 'CRM systems to monitor the quality and conversion rates of leads generated.'],
    integration_points=['Integrate cost per lead analysis with sales performance data to understand the impact on revenue and profitability.', 'Link lead cost tracking with customer relationship management systems to assess the quality and value of leads generated.'],
    
    # Impact
    change_impact="Reducing cost per lead may lead to increased lead volume, but could also impact lead quality and conversion rates. Conversely, a high cost per lead can put pressure on sales teams to convert leads at a higher rate to justify the investment.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Lead", "Lead Qualification", "Quarterly Business Review", "Sale"]
    }
)
