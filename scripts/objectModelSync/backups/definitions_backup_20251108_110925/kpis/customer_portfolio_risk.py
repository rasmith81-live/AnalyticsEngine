"""
Customer Portfolio Risk KPI

A measure of the risk associated with the customer portfolio, indicating the potential for churn or dissatisfaction.
"""

from analytics_models import KPI

CUSTOMER_PORTFOLIO_RISK = KPI(
    name="Customer Portfolio Risk",
    code="CUSTOMER_PORTFOLIO_RISK",
    category="Customer Success",
    
    # Core Definition
    description="A measure of the risk associated with the customer portfolio, indicating the potential for churn or dissatisfaction.",
    kpi_definition="A measure of the risk associated with the customer portfolio, indicating the potential for churn or dissatisfaction.",
    expected_business_insights="Helps in proactively managing and mitigating risks associated with the customer base.",
    measurement_approach="Assesses the potential risk within the customer portfolio, considering factors such as churn risk and payment delinquency.",
    
    # Formula
    formula="Sum of Risk Scores Assigned to Each Customer / Total Number of Customers",
    calculation_formula="Sum of Risk Scores Assigned to Each Customer / Total Number of Customers",
    
    # Analysis
    trend_analysis="""
    * Increasing customer portfolio risk may indicate a higher likelihood of churn or dissatisfaction among customers.
    * Decreasing risk could signal improved customer satisfaction and loyalty, leading to lower churn rates.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or industries that contribute more to the overall portfolio risk?
    * How do customer feedback and satisfaction scores correlate with changes in the customer portfolio risk?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement proactive customer success strategies to address potential churn risks and improve overall satisfaction.
    * Leverage data analytics to identify at-risk customers and personalize retention efforts.
    * Invest in customer relationship management (CRM) tools to better track and manage customer interactions and feedback.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer portfolio risk over time.
    * Pie charts to visualize the distribution of risk across different customer segments or industries.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High customer portfolio risk may lead to increased customer churn and negative word-of-mouth, impacting future sales and revenue.
    * Persistent high risk levels could indicate systemic issues in customer management and require immediate attention.
    """,
    tracking_tools="""
    * Customer success platforms like Gainsight or Totango for tracking and managing customer satisfaction and retention efforts.
    * Data analytics tools such as Tableau or Power BI for deeper insights into customer behavior and risk factors.
    """,
    integration_points="""
    * Integrate customer portfolio risk data with sales and marketing systems to align customer retention efforts with sales strategies.
    * Link risk analysis with customer support systems to ensure a coordinated approach in addressing customer concerns and issues.
    """,
    change_impact_analysis="""
    * Reducing customer portfolio risk can lead to higher customer lifetime value and improved overall sales performance.
    * However, investing in customer retention efforts may require additional resources and could impact short-term profitability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account Risk", "Churn Event", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Subscription"]
    }
)
