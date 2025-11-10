"""
Customer Onboarding Effectiveness KPI

The success rate and satisfaction level of new customers during the onboarding process.
"""

from analytics_models import KPI

CUSTOMER_ONBOARDING_EFFECTIVENESS = KPI(
    name="Customer Onboarding Effectiveness",
    code="CUSTOMER_ONBOARDING_EFFECTIVENESS",
    category="Customer Retention",
    
    # Core Definition
    description="The success rate and satisfaction level of new customers during the onboarding process.",
    kpi_definition="The success rate and satisfaction level of new customers during the onboarding process.",
    expected_business_insights="Reveals the efficacy of onboarding processes and can correlate with early-stage customer retention.",
    measurement_approach="Measures the success rate of new customers who become proficient with the product or service.",
    
    # Formula
    formula="(Number of Successfully Onboarded Customers / Total Number of New Customers) * 100",
    calculation_formula="(Number of Successfully Onboarded Customers / Total Number of New Customers) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer onboarding effectiveness may indicate improved onboarding processes or better alignment of customer expectations with the onboarding experience.
    * A decreasing effectiveness could signal issues with onboarding procedures, lack of personalized attention, or miscommunication during the onboarding process.
    """,
    diagnostic_questions="""
    * Are there specific stages in the onboarding process where customers tend to drop off or express dissatisfaction?
    * How does our customer onboarding satisfaction compare with industry benchmarks or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Personalize the onboarding experience to address individual customer needs and pain points.
    * Implement regular check-ins and feedback sessions during the onboarding process to address any concerns or issues promptly.
    * Provide comprehensive and easily accessible resources to guide customers through the onboarding journey.
    """,
    visualization_suggestions="""
    * Line charts showing the trend in customer onboarding satisfaction over time.
    * Stacked bar charts comparing satisfaction levels across different onboarding stages or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer onboarding effectiveness can lead to increased churn and negative word-of-mouth, impacting overall customer retention.
    * Consistently low satisfaction during onboarding may indicate systemic issues in the sales and customer success processes that need to be addressed.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track and manage the onboarding journey for each customer.
    * Survey and feedback tools to gather and analyze customer feedback during the onboarding process.
    """,
    integration_points="""
    * Integrate customer onboarding effectiveness with customer success platforms to ensure a seamless transition from onboarding to ongoing support.
    * Link onboarding data with sales performance metrics to understand the impact of effective onboarding on long-term customer value.
    """,
    change_impact_analysis="""
    * Improving customer onboarding effectiveness can lead to higher customer lifetime value and increased customer loyalty.
    * Conversely, a decline in onboarding satisfaction may result in reduced customer retention and negative impact on overall sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Product Adoption", "Product Usage", "Sales Process Workflow", "Service Level Agreement"]
    }
)
