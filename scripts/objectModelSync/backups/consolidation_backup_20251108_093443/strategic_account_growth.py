"""
Strategic Account Growth KPI

The year-over-year revenue growth for key strategic accounts, indicating account managers' success in growing accounts.
"""

from analytics_models import KPI

STRATEGIC_ACCOUNT_GROWTH = KPI(
    name="Strategic Account Growth",
    code="STRATEGIC_ACCOUNT_GROWTH",
    category="Key Account Management",
    
    # Core Definition
    description="The year-over-year revenue growth for key strategic accounts, indicating account managers\' success in growing accounts.",
    kpi_definition="The year-over-year revenue growth for key strategic accounts, indicating account managers\' success in growing accounts.",
    expected_business_insights="Indicates the effectiveness of strategic account management in generating additional revenue.",
    measurement_approach="Calculates the percentage growth in revenue from strategic accounts over a specific period.",
    
    # Formula
    formula="(Current Period Revenue from Strategic Account - Previous Period Revenue from Strategic Account) / Previous Period Revenue from Strategic Account * 100",
    calculation_formula="(Current Period Revenue from Strategic Account - Previous Period Revenue from Strategic Account) / Previous Period Revenue from Strategic Account * 100",
    
    # Analysis
    trend_analysis="""
    * Consistent year-over-year growth may indicate effective account management strategies and strong customer relationships.
    * Fluctuations in growth rates could be influenced by changes in market conditions, customer needs, or competitive landscape.
    """,
    diagnostic_questions="""
    * What specific actions or initiatives have contributed to the growth in strategic accounts?
    * Are there any external factors or market shifts that have impacted the revenue growth in key accounts?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update account plans to align with evolving customer needs and market dynamics.
    * Invest in training and development for account managers to enhance their strategic account management skills.
    * Implement a customer feedback mechanism to continuously assess satisfaction and identify opportunities for growth.
    """,
    visualization_suggestions="""
    * Line charts showing revenue growth trends for individual strategic accounts over time.
    * Pareto charts to identify the top contributing accounts to overall growth.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on a few key accounts for growth may pose a risk if those accounts experience downturns.
    * Failure to adapt to changing customer needs and market trends could result in stagnant or declining growth rates.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track interactions and opportunities with key accounts.
    * Data analytics tools to identify patterns and insights within the revenue growth data.
    """,
    integration_points="""
    * Integrate strategic account growth data with sales forecasting to align resources and strategies for future growth.
    * Link account growth metrics with customer satisfaction surveys to understand the relationship between growth and customer experience.
    """,
    change_impact_analysis="""
    * Increased strategic account growth can positively impact overall sales performance and contribute to the company\'s bottom line.
    * However, rapid growth in key accounts may require additional resources and support to maintain service levels and customer satisfaction.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Renewal Management", "Revenue Forecast", "Sale", "Sales Representative", "Strategic Initiative", "Strategic Review"]
    }
)
