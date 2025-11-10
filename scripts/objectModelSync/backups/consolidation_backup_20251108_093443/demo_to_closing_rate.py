"""
Demo-to-Closing Rate KPI

Module: Business Development
"""

from analytics_models import KPI

DEMO_TO_CLOSING_RATE = KPI(
    name="Demo-to-Closing Rate",
    code="DEMO_TO_CLOSING_RATE",
    description="The percentage of product or service demonstrations that result in a closed sale.",
    
    # Definition & Context
    kpi_definition="The percentage of product or service demonstrations that result in a closed sale.",
    expected_business_insights="Reveals the effectiveness of product demonstrations in the sales process.",
    measurement_approach="Calculates the percentage of demonstrations that result in closed deals.",
    
    # Calculation
    formula="(Number of Closed Deals after a Demo / Number of Demos Conducted) * 100",
    
    # Analysis
    trend_analysis="An increasing demo-to-closing rate may indicate improved product knowledge and sales skills among the sales team. A decreasing rate could signal changes in customer preferences, market saturation, or ineffective sales strategies.",
    diagnostic_questions=['Are there specific products or services that consistently have higher or lower demo-to-closing rates?', 'How does our demo-to-closing rate compare with industry benchmarks or competitors?'],
    actionable_steps={
        "operational": ['Provide additional sales training and resources to improve demonstration and closing techniques.'],
        "strategic": ['Regularly review and update sales scripts and materials to better address customer needs and objections.', 'Implement a lead scoring system to prioritize demonstrations for prospects with higher closing potential.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of demo-to-closing rates over time.', 'Pie charts comparing closing rates for different product or service categories.']
    ],
    risk_warnings=['A consistently low demo-to-closing rate may indicate a need for product or service improvements.', 'High fluctuations in the rate could suggest inconsistent sales processes or customer targeting.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track and analyze demonstration and closing data.', 'Sales enablement platforms to provide sales teams with the necessary resources and content for effective demonstrations.'],
    integration_points=['Integrate demo-to-closing rate data with customer feedback systems to identify areas for improvement.', 'Link with marketing automation platforms to align demonstration efforts with targeted lead generation activities.'],
    
    # Impact
    change_impact="Improving the demo-to-closing rate can lead to increased revenue and customer satisfaction. However, a declining rate may require adjustments in product offerings, sales strategies, or market positioning.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Deal", "Demo", "Lost Sale", "Opportunity", "Product", "Product Adoption", "Product Usage", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
