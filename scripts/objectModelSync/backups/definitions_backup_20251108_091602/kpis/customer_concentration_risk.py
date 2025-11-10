"""
Customer Concentration Risk KPI

The level of risk associated with dependency on a limited number of customers for a significant percentage of revenue.
"""

from analytics_models import KPI

CUSTOMER_CONCENTRATION_RISK = KPI(
    name="Customer Concentration Risk",
    code="CUSTOMER_CONCENTRATION_RISK",
    category="Customer Retention",
    
    # Core Definition
    description="The level of risk associated with dependency on a limited number of customers for a significant percentage of revenue.",
    kpi_definition="The level of risk associated with dependency on a limited number of customers for a significant percentage of revenue.",
    expected_business_insights="Helps in risk assessment and encourages diversification of the customer base to ensure business stability.",
    measurement_approach="Evaluates the revenue dependency on a limited number of customers.",
    
    # Formula
    formula="Revenue from Top X Customers / Total Revenue",
    calculation_formula="Revenue from Top X Customers / Total Revenue",
    
    # Analysis
    trend_analysis="""
    * An increasing customer concentration risk may indicate a growing dependency on a small number of clients, which could lead to vulnerability if any of them are lost.
    * A decreasing risk may signal successful efforts to diversify the customer base and reduce reliance on a few key clients.
    """,
    diagnostic_questions="""
    * What percentage of our revenue comes from our top 5 customers?
    * Are there any specific industries or regions that our major customers belong to, and how does this impact our risk?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Diversify the customer base by targeting new industries or regions.
    * Implement strategies to increase customer retention and loyalty across all customer segments.
    * Develop contingency plans for potential loss of major customers to mitigate the impact on revenue.
    """,
    visualization_suggestions="""
    * Pie charts showing the revenue contribution from different customer segments.
    * Line graphs depicting the trend of revenue concentration over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High customer concentration risk can make the business vulnerable to economic downturns or industry-specific challenges.
    * Loss of a major customer can have a significant negative impact on revenue and profitability.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and analyze customer revenue contributions.
    * Data analytics tools to identify trends and patterns in customer revenue concentration.
    """,
    integration_points="""
    * Integrate customer concentration risk analysis with sales forecasting to anticipate potential revenue impacts.
    * Link customer concentration risk with customer satisfaction metrics to understand the relationship between customer dependency and loyalty.
    """,
    change_impact_analysis="""
    * Reducing customer concentration risk may require investment in sales and marketing efforts to target new customer segments.
    * Increased customer diversification can lead to improved revenue stability and reduced vulnerability to customer-specific challenges.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Revenue Forecast", "Sale", "Service Level Agreement"]
    }
)
