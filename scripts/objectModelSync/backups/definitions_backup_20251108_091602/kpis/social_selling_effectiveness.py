"""
Social Selling Effectiveness KPI

Module: Business Development
"""

from analytics_models import KPI

SOCIAL_SELLING_EFFECTIVENESS = KPI(
    name="Social Selling Effectiveness",
    code="SOCIAL_SELLING_EFFECTIVENESS",
    description="A measure of how effectively the sales team uses social media channels to engage with prospects, build relationships, and close deals.",
    
    # Definition & Context
    kpi_definition="A measure of how effectively the sales team uses social media channels to engage with prospects, build relationships, and close deals.",
    expected_business_insights="Highlights the impact of social selling on lead generation and sales conversions.",
    measurement_approach="Measures the success of sales initiatives using social media channels.",
    
    # Calculation
    formula="(Number of Leads or Sales Attributed to Social Media Efforts / Total Number of Leads or Sales) * 100",
    
    # Analysis
    trend_analysis="An increasing social selling effectiveness may indicate better engagement strategies and stronger relationships with prospects. A decreasing effectiveness could signal a need for improved social media tactics or a decline in prospect engagement.",
    diagnostic_questions=['Are there specific social media channels where the sales team is seeing more success in engaging with prospects?', 'How does our social selling effectiveness compare with industry benchmarks or competitors?'],
    actionable_steps={
        "operational": ['Provide social media training and resources to the sales team to improve their social selling skills.'],
        "strategic": ['Encourage the use of personalized and targeted content to engage with prospects on social media.', 'Implement a social selling tool or platform to streamline and track social selling activities.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of social selling effectiveness over time.', 'Comparison bar charts displaying the effectiveness of different social media channels for engaging with prospects.']
    ],
    risk_warnings=['Low social selling effectiveness may lead to missed sales opportunities and decreased revenue.', 'Overemphasis on social selling without a balanced approach may neglect other important sales activities.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Social media management platforms like Hootsuite or Buffer to schedule and analyze social media posts.', 'Customer relationship management (CRM) systems with social selling features to track prospect interactions on social media.'],
    integration_points=['Integrate social selling effectiveness data with customer relationship management (CRM) systems to understand the impact on the sales pipeline.', 'Link social selling metrics with marketing automation platforms to align sales and marketing efforts for better prospect engagement.'],
    
    # Impact
    change_impact="Improving social selling effectiveness can lead to increased lead generation and conversion rates, positively impacting overall sales performance. However, a heavy focus on social selling may divert resources from other sales activities, potentially affecting the overall sales strategy.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "SALES_DEVELOPMENT"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Channel Partner", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
