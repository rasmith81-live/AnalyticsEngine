"""
Up-sell and Cross-sell Conversion Rate KPI

The success rate of sales strategies aimed at selling additional or complementary products to existing customers.
"""

from analytics_models import KPI

UP_SELL_AND_CROSS_SELL_CONVERSION_RATE = KPI(
    name="Up-sell and Cross-sell Conversion Rate",
    code="UP_SELL_AND_CROSS_SELL_CONVERSION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The success rate of sales strategies aimed at selling additional or complementary products to existing customers.",
    kpi_definition="The success rate of sales strategies aimed at selling additional or complementary products to existing customers.",
    expected_business_insights="Illuminates the effectiveness of sales strategies focused on increasing customer spend and loyalty.",
    measurement_approach="Measures the success rate of converting opportunities into additional sales with existing customers.",
    
    # Formula
    formula="(Number of Successful Up-sell/Cross-sell Deals / Total Number of Opportunities) * 100",
    calculation_formula="(Number of Successful Up-sell/Cross-sell Deals / Total Number of Opportunities) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing up-sell and cross-sell conversion rate may indicate successful sales strategies or a growing understanding of customer needs.
    * A decreasing rate could signal ineffective sales approaches, lack of product knowledge among sales teams, or changing customer preferences.
    """,
    diagnostic_questions="""
    * Are there specific products or services that have higher conversion rates for up-sell and cross-sell opportunities?
    * How does our conversion rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide regular training and product knowledge sessions for sales teams to better understand the full range of offerings.
    * Implement targeted marketing campaigns to educate existing customers about complementary products or services.
    * Offer incentives or rewards for sales representatives who successfully execute up-sell and cross-sell strategies.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of conversion rates over time.
    * Pie charts to visualize the distribution of up-sell and cross-sell opportunities across different product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low conversion rate may lead to missed revenue opportunities and underutilization of the existing customer base.
    * Pushing too aggressively for up-sell and cross-sell opportunities could result in customer dissatisfaction and potential churn.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems with built-in analytics to track customer behavior and preferences.
    * Sales enablement platforms that provide insights into customer interactions and buying patterns.
    """,
    integration_points="""
    * Integrate up-sell and cross-sell data with customer relationship management systems to create personalized recommendations for each customer.
    * Link sales performance data with inventory management systems to ensure the availability of complementary products.
    """,
    change_impact_analysis="""
    * Improving up-sell and cross-sell conversion rates can lead to increased revenue and customer lifetime value.
    * However, overly aggressive tactics may impact customer satisfaction and long-term loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Success Manager", "Deal", "Enablement Feedback", "Enablement Platform", "Lead", "Opportunity", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
