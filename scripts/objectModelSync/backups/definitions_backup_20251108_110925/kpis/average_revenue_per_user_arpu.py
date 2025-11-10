"""
Average Revenue Per User (ARPU) KPI

The average revenue generated from each active customer or user.
"""

from analytics_models import KPI

AVERAGE_REVENUE_PER_USER_ARPU = KPI(
    name="Average Revenue Per User (ARPU)",
    code="AVERAGE_REVENUE_PER_USER_ARPU",
    category="Customer Retention",
    
    # Core Definition
    description="The average revenue generated from each active customer or user.",
    kpi_definition="The average revenue generated from each active customer or user.",
    expected_business_insights="Reflects the value each customer brings to the company, useful for forecasting and strategic planning.",
    measurement_approach="Calculates the average revenue generated per user or customer over a specific period.",
    
    # Formula
    formula="Total Revenue / Total Number of Users",
    calculation_formula="Total Revenue / Total Number of Users",
    
    # Analysis
    trend_analysis="""
    * ARPU tends to increase as customers become more engaged with the product or service, indicating positive performance.
    * A declining ARPU may signal increased competition, customer dissatisfaction, or a shift in customer behavior.
    """,
    diagnostic_questions="""
    * What factors contribute to fluctuations in ARPU, such as pricing changes, product offerings, or customer segmentation?
    * How does ARPU vary across different customer segments, and what can be done to increase it for underperforming segments?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement targeted upselling and cross-selling strategies to increase the average spend per customer.
    * Enhance the value proposition of the product or service to justify higher pricing and increase ARPU.
    * Focus on customer retention and loyalty programs to increase the lifetime value of each customer.
    """,
    visualization_suggestions="""
    * Line charts showing ARPU trends over time to identify seasonal or cyclical patterns.
    * Comparison bar charts to visualize ARPU differences between customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining ARPU can lead to reduced revenue and profitability if not addressed promptly.
    * High ARPU may indicate a reliance on a small number of high-value customers, posing a risk if they churn.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify upsell opportunities.
    * Business intelligence tools for analyzing customer data and identifying opportunities to increase ARPU.
    """,
    integration_points="""
    * Integrate ARPU data with marketing automation platforms to personalize offers and promotions based on customer spending habits.
    * Link ARPU with customer support systems to identify opportunities for upselling or cross-selling during customer interactions.
    """,
    change_impact_analysis="""
    * Increasing ARPU may lead to higher revenue and profitability, but could also result in customer pushback if not managed carefully.
    * Decreasing ARPU may indicate a need for cost-cutting measures, but could also signal a decline in customer satisfaction and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale"]
    }
)
