"""
Product Return Rate KPI

The percentage of products that are returned by customers over a certain period of time.
"""

from analytics_models import KPI

PRODUCT_RETURN_RATE = KPI(
    name="Product Return Rate",
    code="PRODUCT_RETURN_RATE",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of products that are returned by customers over a certain period of time.",
    kpi_definition="The percentage of products that are returned by customers over a certain period of time.",
    expected_business_insights="Provides insight into product satisfaction and potential issues with product quality or expectations.",
    measurement_approach="Measures the percentage of sold products that are returned by customers.",
    
    # Formula
    formula="(Number of Products Returned / Number of Products Sold) * 100",
    calculation_formula="(Number of Products Returned / Number of Products Sold) * 100",
    
    # Analysis
    trend_analysis="""
    * A rising product return rate may indicate quality issues or customer dissatisfaction.
    * A decreasing rate can signal improved product quality or better customer service.
    """,
    diagnostic_questions="""
    * Are there specific products that are consistently being returned?
    * What are the primary reasons cited by customers for returning products?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Enhance product quality control measures to reduce the likelihood of returns.
    * Implement a more lenient return policy to improve customer satisfaction and reduce returns.
    * Provide better product information and customer support to minimize the chances of returns due to misunderstandings.
    """,
    visualization_suggestions="""
    * Pie charts showing the distribution of returns by product category.
    * Trend line graphs to visualize the change in return rates over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High return rates can lead to increased operational costs and reduced profitability.
    * Consistently high return rates may indicate systemic issues that need to be addressed.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track reasons for returns and customer feedback.
    * Quality management systems to monitor and improve product quality.
    """,
    integration_points="""
    * Integrate return rate data with product development to address recurring issues.
    * Link return rate tracking with customer support systems to identify and resolve customer concerns.
    """,
    change_impact_analysis="""
    * Reducing return rates can lead to cost savings and improved customer satisfaction.
    * However, changes in return rates may also impact inventory management and production planning.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Product", "Product Adoption", "Product Usage"]
    }
)
