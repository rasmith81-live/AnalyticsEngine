"""
Customer Engagement KPI

A metric that measures how frequently and deeply customers interact with a product or service. This KPI measures the effectiveness of the Customer Success Team in building strong relationships with customers.
"""

from analytics_models import KPI

CUSTOMER_ENGAGEMENT = KPI(
    name="Customer Engagement",
    code="CUSTOMER_ENGAGEMENT",
    category="Customer Success",
    
    # Core Definition
    description="A metric that measures how frequently and deeply customers interact with a product or service. This KPI measures the effectiveness of the Customer Success Team in building strong relationships with customers.",
    kpi_definition="A metric that measures how frequently and deeply customers interact with a product or service. This KPI measures the effectiveness of the Customer Success Team in building strong relationships with customers.",
    expected_business_insights="Provides insight into customer involvement and the potential for upselling, cross-selling, and advocacy.",
    measurement_approach="Measures the degree to which customers interact with the company\'s product, service or brand across various touchpoints.",
    
    # Formula
    formula="Total Number of Customer Interactions / Total Number of Customers",
    calculation_formula="Total Number of Customer Interactions / Total Number of Customers",
    
    # Analysis
    trend_analysis="""
    * An increasing customer engagement may indicate a positive trend in customer satisfaction and loyalty.
    * A decreasing engagement could signal potential issues in product usage, customer support, or overall satisfaction.
    """,
    diagnostic_questions="""
    * Are there specific features or aspects of the product/service that customers engage with more frequently?
    * How does the customer engagement compare with industry benchmarks or with competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly solicit feedback from customers to understand their needs and preferences.
    * Provide targeted training or resources to help customers maximize the value they get from the product/service.
    * Personalize communication and engagement efforts based on individual customer behaviors and preferences.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer engagement over time.
    * Heat maps to identify patterns of engagement based on different customer segments or product features.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer engagement may lead to higher churn rates and decreased customer lifetime value.
    * Inconsistent or sporadic engagement could indicate a lack of perceived value in the product/service.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer interactions.
    * Customer feedback and survey tools to gather insights on engagement levels and satisfaction.
    """,
    integration_points="""
    * Integrate customer engagement data with sales and marketing systems to align efforts and messaging.
    * Link engagement metrics with product development and improvement processes to address customer needs.
    """,
    change_impact_analysis="""
    * Improving customer engagement can lead to increased customer retention and advocacy.
    * However, a focus solely on engagement metrics may overlook other aspects of customer success, such as product quality and support.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Product", "Product Adoption", "Product Usage", "Prospect Engagement", "Sales Team", "Service Level Agreement"]
    }
)
