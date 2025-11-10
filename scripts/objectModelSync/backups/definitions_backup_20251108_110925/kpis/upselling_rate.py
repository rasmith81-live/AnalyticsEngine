"""
Upselling Rate KPI

Module: Business Development
"""

from analytics_models import KPI

UPSELLING_RATE = KPI(
    name="Upselling Rate",
    code="UPSELLING_RATE",
    description="The percentage of customers who have purchased a more expensive version or upgrade of the product or service they initially bought.",
    
    # Definition & Context
    kpi_definition="The percentage of customers who have purchased a more expensive version or upgrade of the product or service they initially bought.",
    expected_business_insights="Highlights the effectiveness of upselling strategies and can suggest how much more revenue existing customers could generate.",
    measurement_approach="Tracks the percentage of customers who purchased additional features or higher-tier products compared to all customers who made a purchase.",
    
    # Calculation
    formula="(Number of Customers Who Purchased Additional Services or Products / Total Number of Customers) * 100",
    
    # Analysis
    trend_analysis="An increasing upselling rate may indicate successful sales strategies or a growing customer base willing to invest in higher-tier products. A decreasing rate could signal missed opportunities for upselling, ineffective sales techniques, or a shift in customer preferences towards lower-priced options.",
    diagnostic_questions=['Are there specific products or services that have a higher success rate for upselling?', 'How does our upselling rate compare with industry benchmarks or with historical data?'],
    actionable_steps={
        "operational": ['Train sales teams to effectively communicate the value of higher-tier products or services.'],
        "strategic": ['Implement targeted marketing campaigns to promote upgrades and premium features to existing customers.', 'Offer incentives or discounts for customers to upgrade to a more expensive version.']
    },
    
    # Visualization
    visualization_suggestions=[
        {"type": "chart", "description": viz} for viz in ['Line charts showing the upselling rate over time to identify trends and seasonal patterns.', 'Pie charts to compare the distribution of customers who have upgraded by product or service category.']
    ],
    risk_warnings=['A low upselling rate may result in missed revenue opportunities and underutilization of premium product features.', 'Overemphasis on upselling may lead to customer dissatisfaction or resistance to future purchases.'],
    
    # Tools & Integration
    suggested_tracking_tools=['Customer relationship management (CRM) software to track customer interactions and identify upselling opportunities.', 'Data analytics tools to segment customers and personalize upselling strategies based on their preferences and behavior.'],
    integration_points=['Integrate upselling rate data with sales performance metrics to evaluate the effectiveness of upselling efforts by individual sales representatives.', 'Link upselling rate with customer feedback systems to understand the impact of upselling on customer satisfaction and loyalty.'],
    
    # Impact
    change_impact="Improving the upselling rate can lead to increased revenue and customer lifetime value, but it may also require additional resources for training and marketing. A declining upselling rate may indicate a need for product or service adjustments to better align with customer needs and preferences.",
    
    # Metadata
    category="Business Development",
    is_active=True,
    metadata_={
        "modules": ["BUS_DEV"],
        "value_chains": ["SALES_MGMT"],
        "source": "kpidepot.com",
        "required_objects": ["Customer", "Product", "Product Adoption", "Product Usage", "Purchase History", "Quarterly Business Review", "Service Level Agreement"]
    }
)
