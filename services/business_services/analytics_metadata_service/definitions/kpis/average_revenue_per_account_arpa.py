"""
Average Revenue Per Account (ARPA) KPI

The average revenue generated per account over a given time period, typically monthly or annually.
"""

from analytics_models import KPI

AVERAGE_REVENUE_PER_ACCOUNT_ARPA = KPI(
    name="Average Revenue Per Account (ARPA)",
    code="AVERAGE_REVENUE_PER_ACCOUNT_ARPA",
    category="Customer Success",
    
    # Core Definition
    description="The average revenue generated per account over a given time period, typically monthly or annually.",
    kpi_definition="The average revenue generated per account over a given time period, typically monthly or annually.",
    expected_business_insights="Helps in understanding revenue generation efficiency and identifying high-value customer segments.",
    measurement_approach="Measures the average revenue generated per account over a given period, often monthly or annually.",
    
    # Formula
    formula="Total Revenue / Total Number of Accounts",
    calculation_formula="Total Revenue / Total Number of Accounts",
    
    # Analysis
    trend_analysis="""
    * ARPA tends to increase over time as customer accounts grow and more revenue is generated.
    * A sudden decrease in ARPA could indicate customer churn or a shift towards lower-value accounts.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or industries that contribute more to ARPA?
    * How does our ARPA compare with industry benchmarks or changes in our product/service offerings?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Upsell and cross-sell strategies to increase revenue from existing accounts.
    * Target higher-value customer segments and tailor offerings to maximize revenue potential.
    * Implement pricing strategies to capture more value from each account without sacrificing customer satisfaction.
    """,
    visualization_suggestions="""
    * Line charts showing ARPA trends over time.
    * Pie charts to visualize the distribution of revenue across different customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Average Revenue Per Account may not reflect profitability if acquisition or servicing costs are high.
    * Over-reliance on a few high-value accounts can pose a risk if they are lost or reduce spending.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems to track account revenue and interactions.
    * Business Intelligence (BI) tools for analyzing customer data and identifying opportunities for revenue growth.
    """,
    integration_points="""
    * Integrate ARPA tracking with sales and marketing systems to align efforts towards higher-value accounts.
    * Link ARPA with customer support systems to ensure consistent service for high-value accounts.
    """,
    change_impact_analysis="""
    * Increasing ARPA may lead to higher overall revenue but could also strain resources if not managed effectively.
    * Decreasing ARPA may indicate a need to reevaluate customer targeting and product/service offerings to maintain overall revenue levels.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS", "SALES_OPERATIONS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Call", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Revenue Forecast", "Sale"]
    }
)
