"""
First Contact Resolution (FCR) KPI

The percentage of customer service issues resolved on the first interaction with the customer.
"""

from analytics_models import KPI

FIRST_CONTACT_RESOLUTION_FCR = KPI(
    name="First Contact Resolution (FCR)",
    code="FIRST_CONTACT_RESOLUTION_FCR",
    category="Customer Retention",
    
    # Core Definition
    description="The percentage of customer service issues resolved on the first interaction with the customer.",
    kpi_definition="The percentage of customer service issues resolved on the first interaction with the customer.",
    expected_business_insights="Indicates the efficiency and effectiveness of customer support, important for customer satisfaction.",
    measurement_approach="Tracks the percentage of customer inquiries or issues resolved on the first contact with no follow-up required.",
    
    # Formula
    formula="(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
    calculation_formula="(Number of Issues Resolved on First Contact / Total Number of Issues) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing FCR may indicate improved customer service training or more knowledgeable staff.
    * Decreasing FCR could signal a need for better problem-solving tools or increased workload on customer service representatives.
    """,
    diagnostic_questions="""
    * Are there common issues that are not being resolved on the first contact?
    * How does our FCR compare with industry benchmarks or customer satisfaction surveys?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in training programs to enhance the problem-solving skills of customer service representatives.
    * Implement a knowledge base or AI-powered chatbot to provide quick and accurate solutions to common customer issues.
    * Regularly review and update customer service scripts and protocols to ensure they align with customer needs.
    """,
    visualization_suggestions="""
    * Line charts showing FCR trends over time.
    * Pie charts comparing FCR rates for different types of customer service issues.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low FCR rates can lead to customer frustration and dissatisfaction.
    * Repeated failures to resolve issues on the first contact may indicate systemic problems in customer service operations.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track customer interactions and issue resolution.
    * Quality management systems to monitor and improve customer service processes.
    """,
    integration_points="""
    * Integrate FCR tracking with customer feedback systems to identify areas for improvement.
    * Link FCR data with employee performance evaluations to incentivize and reward high FCR rates.
    """,
    change_impact_analysis="""
    * Improving FCR can lead to higher customer satisfaction and loyalty, positively impacting long-term revenue.
    * However, focusing solely on FCR may lead to longer average handling times, potentially impacting overall customer service efficiency.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_RETENTION"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Product", "Service Level Agreement", "Support Ticket"]
    }
)
