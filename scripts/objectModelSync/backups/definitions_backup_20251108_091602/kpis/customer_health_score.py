"""
Customer Health Score KPI

A composite metric that combines various customer data points to indicate the overall health and long-term prospects of a customer relationship.
"""

from analytics_models import KPI

CUSTOMER_HEALTH_SCORE = KPI(
    name="Customer Health Score",
    code="CUSTOMER_HEALTH_SCORE",
    category="Customer Retention",
    
    # Core Definition
    description="A composite metric that combines various customer data points to indicate the overall health and long-term prospects of a customer relationship.",
    kpi_definition="A composite metric that combines various customer data points to indicate the overall health and long-term prospects of a customer relationship.",
    expected_business_insights="Provides a predictive measure of customer retention and identifies customers at risk of churning.",
    measurement_approach="Assigns a value to each customer based on various metrics that reflect their likelihood to continue using the service.",
    
    # Formula
    formula="Sum of Weighted Customer Metrics (such as product usage, satisfaction, etc.)",
    calculation_formula="Sum of Weighted Customer Metrics (such as product usage, satisfaction, etc.)",
    
    # Analysis
    trend_analysis="""
    * Increasing customer health score may indicate stronger engagement and satisfaction with the product or service.
    * Decreasing score could signal potential issues with customer retention and loyalty.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or demographics that consistently show lower health scores?
    * How does the customer health score align with customer feedback and support interactions?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular customer feedback surveys to gauge satisfaction and identify areas for improvement.
    * Provide targeted resources or support to customers with lower health scores to improve their experience.
    * Develop personalized retention strategies based on individual customer health scores.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer health scores over time.
    * Pie charts to visualize the distribution of customer health scores across different segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer health scores may lead to increased churn and reduced lifetime value.
    * Inaccurate or outdated data inputs can skew the customer health score and lead to misinformed decisions.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer interactions and feedback.
    * Customer health score calculators or algorithms to automate the process of determining scores.
    """,
    integration_points="""
    * Integrate customer health scores with sales and marketing systems to tailor outreach and messaging based on customer health.
    * Link customer health scores with customer success platforms to proactively address potential issues and improve retention.
    """,
    change_impact_analysis="""
    * Improving customer health scores can lead to increased customer lifetime value and overall revenue.
    * However, focusing solely on the score without addressing underlying customer issues may lead to short-term improvements but long-term dissatisfaction.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Service Level Agreement"]
    }
)
