"""
Customer Lifetime Value (CLV) KPI

The predicted net profit attributed to the entire future relationship with a customer.
"""

from analytics_models import KPI

CUSTOMER_LIFETIME_VALUE_CLV = KPI(
    name="Customer Lifetime Value (CLV)",
    code="CUSTOMER_LIFETIME_VALUE_CLV",
    category="Customer Retention",
    
    # Core Definition
    description="The predicted net profit attributed to the entire future relationship with a customer.",
    kpi_definition="The predicted net profit attributed to the entire future relationship with a customer.",
    expected_business_insights="Helps in understanding the long-term value of customers and informs customer relationship management strategies.",
    measurement_approach="Calculates the total revenue a business can expect from a single customer over the course of their relationship.",
    
    # Formula
    formula="(Annual Revenue per Customer * Customer Relationship in Years) - Initial Acquisition Cost",
    calculation_formula="(Annual Revenue per Customer * Customer Relationship in Years) - Initial Acquisition Cost",
    
    # Analysis
    trend_analysis="""
    * Increasing customer lifetime value may indicate successful upselling or cross-selling efforts.
    * A decreasing CLV could signal declining customer satisfaction or loyalty.
    """,
    diagnostic_questions="""
    * What factors contribute to the calculation of CLV for our organization?
    * Are there specific customer segments with significantly higher or lower CLV?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Focus on improving customer satisfaction and loyalty to increase CLV.
    * Implement targeted marketing and personalized offers to maximize customer lifetime value.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of CLV over time.
    * Pareto charts to identify the most valuable customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Ignoring declining CLV can lead to customer churn and revenue loss.
    * Over-reliance on short-term sales tactics may negatively impact long-term CLV.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and behavior.
    * Analytics tools to analyze customer data and predict future purchasing behavior.
    """,
    integration_points="""
    * Integrate CLV tracking with sales and marketing systems to align efforts with high-value customer segments.
    * Link CLV with customer support systems to ensure a consistent experience for high CLV customers.
    """,
    change_impact_analysis="""
    * Increasing CLV may require investment in customer experience and relationship-building initiatives.
    * Decreasing CLV can impact revenue forecasts and overall business performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Quarterly Business Review", "Revenue Forecast", "Sale"]
    }
)
