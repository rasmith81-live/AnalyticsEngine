"""
Net Revenue Retention (NRR) KPI

The percentage of revenue retained from existing customers after accounting for churned and downgraded customers.
"""

from analytics_models import KPI

NET_REVENUE_RETENTION_NRR = KPI(
    name="Net Revenue Retention (NRR)",
    code="NET_REVENUE_RETENTION_NRR",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of revenue retained from existing customers after accounting for churned and downgraded customers.",
    kpi_definition="The percentage of revenue retained from existing customers after accounting for churned and downgraded customers.",
    expected_business_insights="Indicates the financial health related to customer retention and the impact of upsells, cross-sells, and churn.",
    measurement_approach="Calculates the percentage of recurring revenue retained from existing customers over a given period.",
    
    # Formula
    formula="((Starting MRR + Expansion Revenue - Churned Revenue) / Starting MRR) * 100",
    calculation_formula="((Starting MRR + Expansion Revenue - Churned Revenue) / Starting MRR) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing NRR may indicate successful upselling or cross-selling efforts with existing customers.
    * A decreasing NRR could signal increased competition or dissatisfaction among the customer base.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or product lines that are driving the changes in NRR?
    * How does our NRR compare with industry benchmarks or with our historical performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Focus on delivering exceptional customer service to retain existing customers.
    * Regularly review and update pricing strategies to ensure they align with customer value perceptions.
    * Implement customer loyalty programs to incentivize repeat purchases and increase retention.
    """,
    visualization_suggestions="""
    * Line charts showing NRR trends over time.
    * Stacked bar graphs comparing NRR by customer segment or product category.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining NRR may lead to reduced overall revenue and profitability.
    * High NRR without corresponding customer acquisition efforts may indicate limited growth potential.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and identify retention opportunities.
    * Business intelligence tools for in-depth analysis of customer behavior and preferences.
    """,
    integration_points="""
    * Integrate NRR tracking with sales and marketing systems to align retention efforts with customer acquisition strategies.
    * Link NRR data with customer feedback and satisfaction surveys to gain a comprehensive view of customer sentiment.
    """,
    change_impact_analysis="""
    * Improving NRR can lead to increased customer lifetime value and overall business sustainability.
    * However, aggressive retention strategies may impact short-term profitability if not balanced with acquisition efforts.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Expansion Opportunity", "Revenue Forecast", "Sale", "Subscription"]
    }
)
