"""
Upsell and Cross-Sell Rate KPI

The percentage of customers who purchase additional products or services from the company. This KPI measures the effectiveness of the Customer Success Team in identifying opportunities for upselling or cross-selling.
"""

from analytics_models import KPI

UPSELL_AND_CROSS_SELL_RATE = KPI(
    name="Upsell and Cross-Sell Rate",
    code="UPSELL_AND_CROSS_SELL_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The percentage of customers who purchase additional products or services from the company. This KPI measures the effectiveness of the Customer Success Team in identifying opportunities for upselling or cross-selling.",
    kpi_definition="The percentage of customers who purchase additional products or services from the company. This KPI measures the effectiveness of the Customer Success Team in identifying opportunities for upselling or cross-selling.",
    expected_business_insights="Indicates the effectiveness of sales strategies and the additional value provided to customers.",
    measurement_approach="Measures the success rate of selling additional or complementary products to existing customers.",
    
    # Formula
    formula="(Number of Successful Upsell/Cross-Sell Transactions / Total Number of Sales Opportunities) * 100",
    calculation_formula="(Number of Successful Upsell/Cross-Sell Transactions / Total Number of Sales Opportunities) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing upsell/cross-sell rate may indicate improved customer engagement and satisfaction, leading to more opportunities for additional sales.
    * A decreasing rate could signal a need for better product knowledge or a shift in customer preferences, requiring adjustments in the sales approach.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or industries that are more receptive to upsell/cross-sell offers?
    * How effective are our current upsell/cross-sell strategies, and what feedback have we received from customers?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Train the sales team to identify customer needs and pain points to better position upsell/cross-sell opportunities.
    * Utilize customer data and analytics to personalize and target upsell/cross-sell offers for maximum relevance.
    * Implement a proactive communication strategy to educate customers about additional products or services that complement their existing purchases.
    """,
    visualization_suggestions="""
    * Line charts showing the upsell/cross-sell rate over time to identify seasonal or trend-based patterns.
    * Pie charts to visualize the distribution of additional purchases by product or service category.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low upsell/cross-sell rate may indicate missed revenue opportunities and underutilization of the customer base.
    * Pushing irrelevant or excessive upsell/cross-sell offers can lead to customer annoyance and potential churn.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify upsell/cross-sell opportunities.
    * Marketing automation platforms to personalize and automate upsell/cross-sell campaigns based on customer behavior.
    """,
    integration_points="""
    * Integrate upsell/cross-sell data with sales performance metrics to evaluate the impact on overall revenue and customer lifetime value.
    * Link customer feedback and satisfaction scores with upsell/cross-sell efforts to understand the relationship between customer experience and additional purchases.
    """,
    change_impact_analysis="""
    * An increase in the upsell/cross-sell rate can positively impact revenue and customer lifetime value, but it may also require adjustments in sales strategies and resources.
    * Conversely, a decrease in the rate may signal a need for reevaluation of customer engagement tactics and product relevance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS", "INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Purchase History", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
