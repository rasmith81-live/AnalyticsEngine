"""
Churn Rate KPI

The percentage of customers who stop purchasing or subscribing to a service during a given time period.
"""

from analytics_models import KPI

CHURN_RATE = KPI(
    name="Churn Rate",
    code="CHURN_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of customers who stop purchasing or subscribing to a service during a given time period.",
    kpi_definition="The percentage of customers who stop purchasing or subscribing to a service during a given time period.",
    expected_business_insights="Provides insights into customer loyalty and product/service satisfaction, crucial for retention strategies.",
    measurement_approach="Measures the percentage of customers who stop doing business with the company over a specific period.",
    
    # Formula
    formula="(Number of Customers Lost During Period / Number of Customers at the Start of Period) * 100",
    calculation_formula="(Number of Customers Lost During Period / Number of Customers at the Start of Period) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing churn rate may indicate issues with customer satisfaction, product quality, or competition.
    * A decreasing churn rate can signal improved customer retention strategies, product enhancements, or better customer service.
    """,
    diagnostic_questions="""
    * What are the common reasons customers cite for discontinuing our service?
    * How does our churn rate compare with industry benchmarks or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance customer support and engagement to address issues leading to customer churn.
    * Regularly gather and analyze customer feedback to identify areas for improvement.
    * Implement loyalty programs or incentives to encourage customer retention.
    """,
    visualization_suggestions="""
    * Line charts showing churn rate trends over time.
    * Pie charts to visualize the reasons for customer churn.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High churn rates can lead to revenue loss and impact the company\'s bottom line.
    * Consistently high churn rates may indicate systemic issues that require immediate attention.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify at-risk accounts.
    * Analytics tools to analyze customer behavior and identify patterns leading to churn.
    """,
    integration_points="""
    * Integrate churn rate data with marketing automation platforms to target at-risk customers with personalized retention campaigns.
    * Link churn rate analysis with product development processes to address recurring issues leading to customer dissatisfaction.
    """,
    change_impact_analysis="""
    * Reducing churn rate can lead to increased customer lifetime value and long-term revenue growth.
    * However, investing in customer retention strategies may initially increase operational costs.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Churn Event", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Lost Sale", "Opportunity", "Product", "Quarterly Business Review", "Service Level Agreement", "Subscription"]
    }
)
