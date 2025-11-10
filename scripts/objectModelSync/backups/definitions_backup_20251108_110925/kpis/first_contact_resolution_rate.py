"""
First Contact Resolution Rate KPI

The percentage of customer support issues resolved during the first interaction with a customer.
"""

from analytics_models import KPI

FIRST_CONTACT_RESOLUTION_RATE = KPI(
    name="First Contact Resolution Rate",
    code="FIRST_CONTACT_RESOLUTION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The percentage of customer support issues resolved during the first interaction with a customer.",
    kpi_definition="The percentage of customer support issues resolved during the first interaction with a customer.",
    expected_business_insights="Assesses the efficiency of customer support operations and their impact on customer satisfaction.",
    measurement_approach="Tracks the percentage of customer inquiries or issues that are resolved during the first interaction with support.",
    
    # Formula
    formula="(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
    calculation_formula="(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing first contact resolution rate may indicate improved training and knowledge among customer support staff.
    * A decreasing rate could signal a need for process improvements or changes in customer support protocols.
    """,
    diagnostic_questions="""
    * Are there common reasons why customer support interactions require multiple contacts to resolve?
    * How does our first contact resolution rate compare with industry benchmarks or customer expectations?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in ongoing training and development for customer support teams to enhance their problem-solving abilities.
    * Implement a knowledge base or self-service options for customers to address common issues without the need for direct support.
    * Analyze customer support interactions to identify recurring issues and develop proactive solutions.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of first contact resolution rate over time.
    * Pie charts to illustrate the percentage of different types of issues resolved on the first contact.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low first contact resolution rate can lead to customer frustration and dissatisfaction.
    * Repeated contacts for the same issue may indicate underlying product or service problems that need to be addressed.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with robust ticketing and case management capabilities.
    * Analytics tools to track and analyze customer support interactions and resolution rates.
    """,
    integration_points="""
    * Integrate first contact resolution rate data with customer satisfaction surveys to understand the impact of support interactions on overall satisfaction.
    * Link with sales and marketing systems to identify patterns in customer issues and proactively address them.
    """,
    change_impact_analysis="""
    * Improving first contact resolution rate can lead to higher customer satisfaction and loyalty, impacting long-term customer retention and revenue.
    * However, focusing solely on speed of resolution may impact the depth of support provided, potentially affecting overall customer experience.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION", "CUSTOMER_SUCCESS", "OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Support Ticket"],
        "replaces": ["FIRST_CONTACT_RESOLUTION_FCR"]}
)
