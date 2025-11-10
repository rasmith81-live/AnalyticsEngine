"""
Client Lifetime Value KPI

The predicted net profit attributed to the entire future relationship with a new client.
"""

from analytics_models import KPI

CLIENT_LIFETIME_VALUE = KPI(
    name="Client Lifetime Value",
    code="CLIENT_LIFETIME_VALUE",
    category="Outside Sales",
    
    # Core Definition
    description="The predicted net profit attributed to the entire future relationship with a new client.",
    kpi_definition="The predicted net profit attributed to the entire future relationship with a new client.",
    expected_business_insights="Assists in determining the long-term value of customers and informs strategies for customer retention and profitability.",
    measurement_approach="Calculates the total net profit attributed to a customer throughout the business relationship.",
    
    # Formula
    formula="(Average Sale per Customer * Number of Repeat Transactions * Average Retention Time) - Initial Cost of Customer Acquisition",
    calculation_formula="(Average Sale per Customer * Number of Repeat Transactions * Average Retention Time) - Initial Cost of Customer Acquisition",
    
    # Analysis
    trend_analysis="""
    * Increasing client lifetime value over time may indicate successful upselling or cross-selling strategies.
    * A decreasing trend could signal declining customer retention or satisfaction levels.
    """,
    diagnostic_questions="""
    * What factors contribute to the increase or decrease in client lifetime value?
    * How does our client lifetime value compare to industry benchmarks or competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Focus on building long-term relationships with clients through personalized communication and exceptional service.
    * Implement loyalty programs or incentives to encourage repeat purchases and customer retention.
    * Regularly review and optimize pricing strategies to maximize customer lifetime value.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of client lifetime value over time.
    * Pareto charts to identify the most valuable clients contributing to overall lifetime value.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low client lifetime value may indicate a high churn rate and the need for improved customer retention strategies.
    * Over-reliance on a small number of high-value clients can pose a risk if they are lost.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage client interactions and relationships.
    * Data analytics tools to analyze customer behavior and identify opportunities to increase lifetime value.
    """,
    integration_points="""
    * Integrate client lifetime value tracking with sales and marketing systems to align efforts towards maximizing long-term value.
    * Link with customer support platforms to ensure consistent and personalized service for high-value clients.
    """,
    change_impact_analysis="""
    * Improving client lifetime value can lead to increased revenue and profitability.
    * However, focusing solely on short-term gains may negatively impact customer satisfaction and long-term brand reputation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Lost Sale", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
