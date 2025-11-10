"""
Average Order Value (AOV) KPI

The average value of orders received from key accounts.
"""

from analytics_models import KPI

AVERAGE_ORDER_VALUE_AOV = KPI(
    name="Average Order Value (AOV)",
    code="AVERAGE_ORDER_VALUE_AOV",
    category="Key Account Management",
    
    # Core Definition
    description="The average value of orders received from key accounts.",
    kpi_definition="The average value of orders received from key accounts.",
    expected_business_insights="Helps understand customer spending behaviors and evaluate pricing strategies.",
    measurement_approach="Measures the average dollar amount spent each time a customer places an order over a certain period.",
    
    # Formula
    formula="Total Revenue / Total Number of Orders",
    calculation_formula="Total Revenue / Total Number of Orders",
    
    # Analysis
    trend_analysis="""
    * Increasing average order value may indicate upselling or cross-selling success with key accounts.
    * Decreasing average order value could signal a shift in purchasing behavior or dissatisfaction with products or services.
    """,
    diagnostic_questions="""
    * Are there specific products or services that contribute significantly to the average order value?
    * How does the average order value compare to historical data or industry benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement targeted marketing campaigns to promote higher-value products or services to key accounts.
    * Offer bundled packages or discounts for larger orders to encourage higher average order values.
    * Provide personalized recommendations to key accounts based on their purchasing history and preferences.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of average order value over time.
    * Pareto charts to identify the most significant contributors to the average order value.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A consistently low average order value may indicate a lack of customer loyalty or satisfaction.
    * Over-reliance on a few high-value orders may pose a risk if those accounts are lost or reduce their purchasing volume.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track and analyze purchasing behavior of key accounts.
    * Business intelligence tools to identify patterns and opportunities for increasing average order value.
    """,
    integration_points="""
    * Integrate average order value data with sales performance metrics to understand the impact on overall revenue and profitability.
    * Link with inventory management systems to ensure availability of high-value products for key accounts.
    """,
    change_impact_analysis="""
    * Increasing average order value may lead to higher revenue and profitability, but could also require additional resources for personalized sales efforts.
    * Conversely, a declining average order value may indicate the need for product or service improvements to maintain customer satisfaction and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale"]
    }
)
