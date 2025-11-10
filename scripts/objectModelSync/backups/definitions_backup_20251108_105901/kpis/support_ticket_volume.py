"""
Support Ticket Volume KPI

The number of customer support tickets or inquiries received over a certain period of time.
"""

from analytics_models import KPI

SUPPORT_TICKET_VOLUME = KPI(
    name="Support Ticket Volume",
    code="SUPPORT_TICKET_VOLUME",
    category="Customer Success",
    
    # Core Definition
    description="The number of customer support tickets or inquiries received over a certain period of time.",
    kpi_definition="The number of customer support tickets or inquiries received over a certain period of time.",
    expected_business_insights="Provides insight into product issues, customer needs, and the workload of the support team.",
    measurement_approach="Measures the number of support tickets or inquiries received by the customer support team within a given timeframe.",
    
    # Formula
    formula="Total Number of Support Tickets Received",
    calculation_formula="Total Number of Support Tickets Received",
    
    # Analysis
    trend_analysis="""
    * An increasing support ticket volume may indicate product or service issues that need to be addressed.
    * A decreasing volume could signal improved product quality or customer education leading to fewer inquiries.
    """,
    diagnostic_questions="""
    * Are there specific products or services that are generating a disproportionate number of support tickets?
    * How does our support ticket volume compare with industry benchmarks or with previous periods?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in product or service improvements based on common support ticket themes.
    * Provide additional customer education or resources to address recurring support ticket topics.
    * Implement proactive customer outreach to address potential support issues before they become tickets.
    """,
    visualization_suggestions="""
    * Line charts showing support ticket volume over time to identify trends and patterns.
    * Pie charts to visualize the distribution of support tickets by product or service category.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High support ticket volume can lead to customer frustration and dissatisfaction.
    * Chronic support ticket issues may indicate underlying product or service quality problems.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems to track and manage support tickets.
    * Help desk software to streamline ticket resolution processes and identify common issues.
    """,
    integration_points="""
    * Integrate support ticket data with product development teams to address recurring issues.
    * Link support ticket volume with customer satisfaction metrics to understand the impact on overall customer experience.
    """,
    change_impact_analysis="""
    * Reducing support ticket volume can lead to cost savings and improved customer satisfaction.
    * However, a sudden decrease in support ticket volume may also indicate a decline in customer engagement or feedback, which could impact product development and innovation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Lead", "Opportunity", "Sales Team", "Support Ticket"]
    }
)
