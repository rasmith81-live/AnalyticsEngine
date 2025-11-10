"""
Customer Success Manager (CSM) Ratio KPI

The ratio of customers to customer success managers, indicating the level of personalized attention provided.
"""

from analytics_models import KPI

CUSTOMER_SUCCESS_MANAGER_CSM_RATIO = KPI(
    name="Customer Success Manager (CSM) Ratio",
    code="CUSTOMER_SUCCESS_MANAGER_CSM_RATIO",
    category="Customer Success",
    
    # Core Definition
    description="The ratio of customers to customer success managers, indicating the level of personalized attention provided.",
    kpi_definition="The ratio of customers to customer success managers, indicating the level of personalized attention provided.",
    expected_business_insights="Provides insight into the scalability of the customer success team and the level of attention provided to customers.",
    measurement_approach="Measures the number of customers or accounts managed by a single customer success manager.",
    
    # Formula
    formula="Total Number of Customers / Number of Customer Success Managers",
    calculation_formula="Total Number of Customers / Number of Customer Success Managers",
    
    # Analysis
    trend_analysis="""
    * An increasing CSM ratio may indicate a growing customer base without a proportional increase in customer success managers, potentially leading to decreased personalized attention.
    * A decreasing ratio could signal improved efficiency in customer success management, but it could also mean that customer success managers are spread too thin to provide adequate support.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or product lines that require more attention from customer success managers?
    * How does our CSM ratio compare to industry standards or benchmarks for similar companies?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement customer segmentation to prioritize high-value customers for more personalized attention.
    * Invest in training and development for customer success managers to improve their efficiency and effectiveness.
    * Consider hiring additional customer success managers to maintain a healthy ratio as the customer base grows.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of the CSM ratio over time.
    * Bar graphs comparing the CSM ratio across different customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A high CSM ratio may lead to decreased customer satisfaction and retention.
    * An excessively low ratio could result in increased operational costs without a proportional improvement in customer success.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify areas for improvement.
    * Workflow automation tools to streamline routine tasks and free up time for more personalized customer engagement.
    """,
    integration_points="""
    * Integrate the CSM ratio with sales and marketing systems to align customer success efforts with overall business objectives.
    * Link the ratio with customer feedback and satisfaction metrics to understand the impact of customer success efforts on overall customer experience.
    """,
    change_impact_analysis="""
    * An improved CSM ratio can lead to higher customer lifetime value and increased referrals, but it may also require additional investment in customer success resources.
    * A declining ratio could result in decreased customer retention and negative word-of-mouth, impacting overall sales and revenue.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account Manager", "Sales Representative", "Service Level Agreement"]
    }
)
