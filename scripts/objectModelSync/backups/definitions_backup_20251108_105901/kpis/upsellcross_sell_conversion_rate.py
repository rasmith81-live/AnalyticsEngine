"""
Upsell/Cross-sell Conversion Rate KPI

The success rate of converting existing customers to purchase additional or related products and services.
"""

from analytics_models import KPI

UPSELLCROSS_SELL_CONVERSION_RATE = KPI(
    name="Upsell/Cross-sell Conversion Rate",
    code="UPSELLCROSS_SELL_CONVERSION_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The success rate of converting existing customers to purchase additional or related products and services.",
    kpi_definition="The success rate of converting existing customers to purchase additional or related products and services.",
    expected_business_insights="Helps evaluate the effectiveness of sales strategies and the potential for increasing customer value.",
    measurement_approach="Measures the success rate of converting standard sales into upsells or cross-sells.",
    
    # Formula
    formula="(Number of Upsell/Cross-sell Sales / Total Number of Sales Opportunities) * 100",
    calculation_formula="(Number of Upsell/Cross-sell Sales / Total Number of Sales Opportunities) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing upsell/cross-sell conversion rate may indicate successful sales strategies or improved customer engagement.
    * A decreasing rate could signal a need for better product knowledge among sales teams or a lack of customer interest in additional offerings.
    """,
    diagnostic_questions="""
    * Are there specific products or services that have higher conversion rates for upsell/cross-sell opportunities?
    * How does our upsell/cross-sell conversion rate compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional training to sales teams on product knowledge and effective upselling techniques.
    * Implement targeted marketing campaigns to promote related products or services to existing customers.
    * Create bundled offerings or package deals to make upselling/cross-selling more attractive to customers.
    """,
    visualization_suggestions="""
    * Line charts showing the upsell/cross-sell conversion rate over time.
    * Pie charts comparing conversion rates for different product or service categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low upsell/cross-sell conversion rate may lead to missed revenue opportunities and underutilization of the existing customer base.
    * Pushing too aggressively for upselling or cross-selling may result in customer dissatisfaction and potential churn.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify upsell/cross-sell opportunities.
    * Analytics tools to analyze customer behavior and preferences for targeted upselling/cross-selling.
    """,
    integration_points="""
    * Integrate upsell/cross-sell data with customer support systems to provide personalized recommendations during customer interactions.
    * Link with inventory management systems to ensure availability of additional products or services for upsell/cross-sell opportunities.
    """,
    change_impact_analysis="""
    * An increase in upsell/cross-sell conversion rate can lead to higher revenue and improved customer lifetime value.
    * However, too much focus on upselling/cross-selling may impact the overall customer experience and satisfaction.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Opportunity", "Product", "Purchase History", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
