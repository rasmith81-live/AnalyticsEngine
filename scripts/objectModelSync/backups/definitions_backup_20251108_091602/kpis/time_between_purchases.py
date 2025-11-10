"""
Time Between Purchases KPI

The average time interval between purchases made by a repeat customer.
"""

from analytics_models import KPI

TIME_BETWEEN_PURCHASES = KPI(
    name="Time Between Purchases",
    code="TIME_BETWEEN_PURCHASES",
    category="Customer Retention",
    
    # Core Definition
    description="The average time interval between purchases made by a repeat customer.",
    kpi_definition="The average time interval between purchases made by a repeat customer.",
    expected_business_insights="Indicates buying habits and can help in timing marketing campaigns and customer engagement efforts.",
    measurement_approach="Tracks the average duration between purchases made by a customer.",
    
    # Formula
    formula="Average Time Span Between Customer Purchases",
    calculation_formula="Average Time Span Between Customer Purchases",
    
    # Analysis
    trend_analysis="""
    * Shortening time between purchases may indicate improved customer satisfaction and loyalty.
    * An increasing time interval could signal declining interest in products or services.
    """,
    diagnostic_questions="""
    * Are there specific products or services that are driving longer intervals between purchases?
    * How does our time between purchases compare with industry averages or benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance customer engagement and communication to maintain interest and encourage repeat purchases.
    * Offer loyalty programs or incentives to incentivize more frequent purchases.
    * Regularly analyze customer feedback and adjust product or service offerings to meet changing needs and preferences.
    """,
    visualization_suggestions="""
    * Line charts showing the average time between purchases over time.
    * Cohort analysis to compare the purchasing behavior of different customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Longer time between purchases may lead to decreased customer lifetime value and revenue.
    * It could indicate a need to reevaluate the product or service offering to maintain relevance in the market.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer behavior and preferences.
    * Data analytics tools to identify patterns and trends in customer purchasing behavior.
    """,
    integration_points="""
    * Integrate with marketing automation platforms to personalize and target communications based on customer purchasing patterns.
    * Link with inventory management systems to ensure product availability and timely delivery for repeat purchases.
    """,
    change_impact_analysis="""
    * Shortening the time between purchases can increase revenue and customer lifetime value.
    * However, it may also require increased marketing and operational costs to maintain customer engagement.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Representative"]
    }
)
