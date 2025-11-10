"""
Customer Lifetime Profitability KPI

The total profit a company expects to earn over the entirety of its business relationship with a customer.
"""

from analytics_models import KPI

CUSTOMER_LIFETIME_PROFITABILITY = KPI(
    name="Customer Lifetime Profitability",
    code="CUSTOMER_LIFETIME_PROFITABILITY",
    category="Outside Sales",
    
    # Core Definition
    description="The total profit a company expects to earn over the entirety of its business relationship with a customer.",
    kpi_definition="The total profit a company expects to earn over the entirety of its business relationship with a customer.",
    expected_business_insights="Allows for evaluation of customer relationships and informs decisions on customer service and retention investments.",
    measurement_approach="Calculates the total profit a company expects to earn over the entire business relationship with a customer.",
    
    # Formula
    formula="Sum of Customer’s Lifetime Value - Sum of Customer’s Lifetime Costs",
    calculation_formula="Sum of Customer’s Lifetime Value - Sum of Customer’s Lifetime Costs",
    
    # Analysis
    trend_analysis="""
    * Increasing customer lifetime profitability may indicate successful upselling or cross-selling efforts.
    * Decreasing profitability could signal customer dissatisfaction or increased competition impacting repeat business.
    """,
    diagnostic_questions="""
    * What factors contribute to the increase or decrease in customer lifetime profitability?
    * How does our customer lifetime profitability compare to industry benchmarks or customer segments?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Focus on building long-term customer relationships through personalized service and tailored solutions.
    * Regularly review customer feedback and adjust strategies to meet evolving needs and expectations.
    * Implement loyalty programs to encourage repeat purchases and increase customer lifetime value.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer lifetime profitability over time.
    * Pareto charts to identify the most profitable customers and prioritize retention efforts.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on a small number of high-profit customers can pose a risk if their business is lost.
    * Ignoring declining profitability may lead to customer churn and revenue loss.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track customer interactions and preferences.
    * Business intelligence tools for analyzing customer data and identifying opportunities for increasing profitability.
    """,
    integration_points="""
    * Integrate customer profitability data with sales and marketing systems to align efforts with high-value customers.
    * Link profitability metrics with customer service platforms to ensure consistent experience across all touchpoints.
    """,
    change_impact_analysis="""
    * Improving customer lifetime profitability may require investment in customer service and relationship management.
    * Decreasing profitability can impact overall revenue and long-term business sustainability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
