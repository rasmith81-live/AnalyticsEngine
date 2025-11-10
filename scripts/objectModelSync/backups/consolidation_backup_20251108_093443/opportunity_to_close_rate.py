"""
Opportunity-to-Close Rate KPI

Module: Business Development
"""

from analytics_models import KPI

OPPORTUNITY_TO_CLOSE_RATE = KPI(
    name="Opportunity-to-Close Rate",
    code="OPPORTUNITY_TO_CLOSE_RATE",
    description="The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team's closing abilities.",
    
    # Definition & Context
    kpi_definition="The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team's closing abilities.",
    expected_business_insights="Measures the effectiveness of the sales process and closing abilities of the sales team.",
    measurement_approach="Calculates the percentage of sales opportunities that are converted into actual sales.",
    
    # Calculation
    formula="(Number of Opportunities Closed as Wins / Total Number of Opportunities) * 100",
    
    # Analysis
    trend_analysis="An increasing opportunity-to-close rate may indicate improved sales tactics or a growing demand for the product. A decreasing rate could signal ineffective sales strategies or a decline in market interest.",
    diagnostic_questions=['Are there specific stages in the sales process where opportunities are frequently lost?', 'How does our opportunity-to-close rate compare with industry benchmarks or competitors?'],
    actionable_steps={
        "operational": ['Provide additional sales training and support to improve closing techniques.'],
        "strategic": ['Implement a lead scoring system to prioritize high-potential opportunities.', 'Regularly review and refine the sales process to identify and address bottlenecks.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Funnel charts to visualize the progression of opportunities through the sales pipeline.', 'Time series graphs to track changes in the opportunity-to-close rate over time.']
    ],
    risk_warnings=['A consistently low opportunity-to-close rate can lead to missed revenue targets and decreased morale among the sales team.', 'An excessively high rate may indicate that the sales team is being too aggressive, potentially leading to customer dissatisfaction.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track and manage sales opportunities.', 'Sales analytics tools to identify patterns and trends in the opportunity-to-close rate.'],
    integration_points=['Integrate the opportunity-to-close rate with marketing automation systems to align sales and marketing efforts.', 'Link with customer feedback platforms to gather insights on why certain opportunities are not converting.'],
    
    # Impact
    change_impact="Improving the opportunity-to-close rate can lead to increased revenue and customer satisfaction. However, overly aggressive tactics to boost the rate may negatively impact the overall customer experience.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Deal", "Expansion Opportunity", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
