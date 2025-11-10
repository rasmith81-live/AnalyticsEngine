"""
Conversion Rate KPI

Module: Business Development
"""

from analytics_models import KPI

CONVERSION_RATE = KPI(
    name="Conversion Rate",
    code="CONVERSION_RATE",
    description="The percentage of leads that convert into paying customers.",
    
    # Definition & Context
    kpi_definition="The percentage of leads that convert into paying customers.",
    expected_business_insights="Reflects the effectiveness of the sales funnel and marketing efforts.",
    measurement_approach="Calculates the percentage of leads that convert into customers.",
    
    # Calculation
    formula="(Number of New Customers / Number of Leads) * 100",
    
    # Analysis
    trend_analysis="An increasing conversion rate may indicate improved lead quality or more effective sales strategies. A decreasing rate could signal market saturation or a decline in customer interest.",
    diagnostic_questions=['Are there specific lead sources or channels that consistently result in higher conversion rates?', 'How does our conversion rate compare to industry benchmarks or historical data?'],
    actionable_steps={
        "operational": ['Implement lead nurturing strategies to improve lead quality and engagement.'],
        "strategic": ['Provide sales teams with targeted training and resources to enhance their closing techniques.', 'Regularly review and optimize the sales process to identify and address potential bottlenecks.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the trend of conversion rates over time.', 'Funnel charts to visualize the progression of leads through the sales pipeline.']
    ],
    risk_warnings=['A consistently low conversion rate can lead to wasted resources and reduced ROI on marketing efforts.', 'A sudden drop in conversion rate may indicate a problem with the sales process or product-market fit.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer Relationship Management (CRM) software to track and analyze lead interactions and conversions.', 'Sales enablement platforms to provide sales teams with the tools and content they need to effectively convert leads.'],
    integration_points=['Integrate conversion rate data with marketing analytics to understand the effectiveness of lead generation efforts.', 'Link conversion rate tracking with customer relationship management systems to monitor the impact on customer retention and lifetime value.'],
    
    # Impact
    change_impact="Improving the conversion rate can lead to increased revenue and profitability. However, overly aggressive tactics to boost conversion rates may negatively impact customer satisfaction and long-term brand loyalty.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_STRATEGY"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Lead", "Opportunity", "Quarterly Business Review"]
    }
)
