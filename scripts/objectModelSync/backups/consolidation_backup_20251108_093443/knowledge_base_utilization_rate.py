"""
Knowledge Base Utilization Rate KPI

The usage rate of a self-service knowledge base by customers for problem-solving.
"""

from analytics_models import KPI

KNOWLEDGE_BASE_UTILIZATION_RATE = KPI(
    name="Knowledge Base Utilization Rate",
    code="KNOWLEDGE_BASE_UTILIZATION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The usage rate of a self-service knowledge base by customers for problem-solving.",
    kpi_definition="The usage rate of a self-service knowledge base by customers for problem-solving.",
    expected_business_insights="Indicates the effectiveness of self-service resources in providing timely and relevant assistance to customers.",
    measurement_approach="Measures how often customers use the self-help resources available in the knowledge base.",
    
    # Formula
    formula="Number of Customer Interactions with Knowledge Base / Total Number of Customer Support Interactions",
    calculation_formula="Number of Customer Interactions with Knowledge Base / Total Number of Customer Support Interactions",
    
    # Analysis
    trend_analysis="""
    * An increasing knowledge base utilization rate may indicate a growing customer preference for self-service support and a positive shift towards more efficient problem-solving.
    * A decreasing rate could signal that the knowledge base content is outdated or not meeting customer needs, leading to negative performance shifts in customer satisfaction and support efficiency.
    """,
    diagnostic_questions="""
    * Are there specific topics or articles within the knowledge base that are frequently accessed by customers?
    * How does the knowledge base utilization rate correlate with customer support ticket volume or resolution times?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update and expand the knowledge base content to address common customer issues and questions.
    * Promote the knowledge base as a primary resource for problem-solving through targeted customer communications and support channels.
    * Collect and analyze feedback from customers regarding the knowledge base usability and content relevance to make continuous improvements.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of knowledge base utilization rate over time.
    * Pie charts illustrating the distribution of knowledge base utilization across different categories or topics.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A low knowledge base utilization rate may indicate a lack of customer awareness or trust in the self-service support option, leading to increased support costs and customer dissatisfaction.
    * High utilization without corresponding resolution rates could indicate that the knowledge base content is not effectively addressing customer issues, risking customer frustration and churn.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) systems with integrated knowledge base functionality to track customer interactions and knowledge base usage.
    * Analytics tools like Google Analytics or Mixpanel to monitor and analyze knowledge base traffic and user behavior.
    """,
    integration_points="""
    * Integrate knowledge base utilization data with customer satisfaction surveys and feedback collection systems to understand the impact on overall customer experience.
    * Link knowledge base usage metrics with employee performance evaluations to incentivize and reward effective knowledge base utilization in customer support interactions.
    """,
    change_impact_analysis="""
    * Improving the knowledge base utilization rate can lead to reduced support costs and increased customer satisfaction, positively impacting overall customer success metrics.
    * Conversely, a declining utilization rate may lead to higher support costs and decreased customer satisfaction, affecting customer retention and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Knowledge Base", "Product", "Product Usage", "Service Level Agreement", "Support Ticket"]
    }
)
