"""
Active Users (MAU) KPI

The number of unique users who engage with a service or product within a selected period.
"""

from analytics_models import KPI

ACTIVE_USERS_MAU = KPI(
    name="Active Users (MAU)",
    code="ACTIVE_USERS_MAU",
    category="Customer Retention",
    
    # Core Definition
    description="The number of unique users who engage with a service or product within a selected period.",
    kpi_definition="The number of unique users who engage with a service or product within a selected period.",
    expected_business_insights="Reflects user engagement levels and the active customer base, useful for trend analysis and growth tracking.",
    measurement_approach="Counts the number of unique users who engage with a service or product within a selected period.",
    
    # Formula
    formula="Total Number of Unique Active Users in a selected period",
    calculation_formula="Total Number of Unique Active Users in a selected period",
    
    # Analysis
    trend_analysis="""
    * An increasing MAU may indicate growing user engagement and interest in the product or service.
    * A decreasing MAU could signal declining interest, potential issues with the product, or increased competition in the market.
    """,
    diagnostic_questions="""
    * Are there specific features or content that are driving user engagement?
    * How does our MAU compare with industry benchmarks or seasonal trends?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update and refresh content or features to maintain user interest and engagement.
    * Invest in targeted marketing or promotional campaigns to attract and retain users.
    * Collect and analyze user feedback to identify areas for improvement and innovation.
    """,
    visualization_suggestions="""
    * Line charts showing monthly trends in MAU over time.
    * Cohort analysis to track the retention of users who joined in specific time periods.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Declining MAU may lead to reduced revenue and market share.
    * High MAU with low conversion rates may indicate issues with the product or service that need to be addressed.
    """,
    tracking_tools="""
    * Analytics platforms like Google Analytics or Mixpanel to track user engagement and behavior.
    * Customer relationship management (CRM) systems to manage and nurture customer relationships for improved retention.
    """,
    integration_points="""
    * Integrate MAU data with marketing automation systems to personalize user experiences and communications.
    * Link MAU with customer support systems to identify and address user concerns or issues proactively.
    """,
    change_impact_analysis="""
    * Increasing MAU can lead to higher revenue and market growth, but may also require scaling up infrastructure and support resources.
    * Decreasing MAU can impact overall business performance and may require strategic shifts in product development or marketing strategies.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]
    }
)
