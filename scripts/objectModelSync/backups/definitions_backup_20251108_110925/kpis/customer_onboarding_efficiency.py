"""
Customer Onboarding Efficiency KPI

Measurement of the speed and effectiveness of the process that gets new customers or clients acclimated to the company's products or services.
"""

from analytics_models import KPI

CUSTOMER_ONBOARDING_EFFICIENCY = KPI(
    name="Customer Onboarding Efficiency",
    code="CUSTOMER_ONBOARDING_EFFICIENCY",
    category="Key Account Management",
    
    # Core Definition
    description="Measurement of the speed and effectiveness of the process that gets new customers or clients acclimated to the company\'s products or services.",
    kpi_definition="Measurement of the speed and effectiveness of the process that gets new customers or clients acclimated to the company\'s products or services.",
    expected_business_insights="Indicates efficiency of the onboarding process and its effect on customer satisfaction and time to value.",
    measurement_approach="Assesses the time and resources required to onboard a new customer.",
    
    # Formula
    formula="Total Onboarding Time for All Customers / Number of Customers Onboarded",
    calculation_formula="Total Onboarding Time for All Customers / Number of Customers Onboarded",
    
    # Analysis
    trend_analysis="""
    * An increasing customer onboarding efficiency may indicate improved processes or better alignment with customer needs.
    * A decreasing efficiency could signal issues with training, product complexity, or organizational changes.
    """,
    diagnostic_questions="""
    * Are there specific stages in the onboarding process where customers tend to get stuck or require additional support?
    * How does our customer onboarding efficiency compare with industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Streamline onboarding processes by automating repetitive tasks or providing self-service resources.
    * Invest in training and support resources to ensure customers are well-equipped to use the products or services effectively.
    * Regularly gather feedback from new customers to identify areas for improvement in the onboarding process.
    """,
    visualization_suggestions="""
    * Flowcharts or process maps to visualize the customer onboarding journey and identify bottlenecks.
    * Time-series line charts to track the efficiency of onboarding over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer onboarding efficiency can lead to customer frustration and increased churn rates.
    * Complex or lengthy onboarding processes may deter potential customers from making a purchase.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track customer interactions and progress through the onboarding process.
    * Customer feedback and survey tools to gather insights on the onboarding experience.
    """,
    integration_points="""
    * Integrate customer onboarding data with sales and marketing systems to understand the impact of onboarding on customer acquisition and retention.
    * Link onboarding efficiency with customer support systems to ensure a seamless transition from onboarding to ongoing assistance.
    """,
    change_impact_analysis="""
    * Improving customer onboarding efficiency can lead to higher customer satisfaction and retention rates.
    * However, rapid changes in onboarding processes may require additional resources and could impact initial sales velocity.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["KEY_ACCOUNT_MANAGEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Product", "Renewal Management", "Sales Process Workflow"]
    }
)
