"""
Average Sales Pitch Length KPI

Module: Business Development
"""

from analytics_models import KPI

AVERAGE_SALES_PITCH_LENGTH = KPI(
    name="Average Sales Pitch Length",
    code="AVERAGE_SALES_PITCH_LENGTH",
    description="The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    
    # Definition & Context
    kpi_definition="The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
    expected_business_insights="Provides insights into the efficiency of the sales process and potential customer engagement levels.",
    measurement_approach="Considers the average duration of sales presentations or meetings.",
    
    # Calculation
    formula="Total Duration of All Sales Pitches / Number of Sales Pitches",
    
    # Analysis
    trend_analysis="Increasing average sales pitch length may indicate a more detailed and comprehensive approach to presenting products or services. A decreasing average pitch length could suggest a more concise and efficient communication style, but it may also lead to overlooking important details.",
    diagnostic_questions=['Are there specific products or services that require longer pitches to effectively convey their value?', 'How does the average pitch length correlate with the success rate of closing deals?'],
    actionable_steps={
        "operational": ['Provide sales training to ensure that pitches are informative but also engaging and concise.'],
        "strategic": ['Utilize technology such as presentation software to create visually appealing and impactful pitches without unnecessary length.', 'Regularly review and refine the pitch content to focus on key value propositions and address customer pain points efficiently.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the average pitch length over time to identify any significant fluctuations.', 'Comparison bar charts to visualize the average pitch length for different products or sales representatives.']
    ],
    risk_warnings=['Excessively long pitches may lead to customer disengagement and loss of interest.', 'Overly short pitches might result in insufficient information being conveyed, leading to missed sales opportunities.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track the length of pitches and their outcomes.', 'Video recording tools to analyze and improve the delivery and content of sales pitches.'],
    integration_points=['Integrate pitch length data with customer feedback and conversion rates to understand the impact of pitch duration on sales performance.', 'Link pitch length analysis with sales training programs to tailor coaching and development efforts based on the findings.'],
    
    # Impact
    change_impact="Shorter, more effective pitches can lead to higher sales conversion rates and improved customer satisfaction. However, a significant reduction in pitch length may also raise concerns about the depth of product knowledge and understanding conveyed to customers.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Prospect Engagement", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
