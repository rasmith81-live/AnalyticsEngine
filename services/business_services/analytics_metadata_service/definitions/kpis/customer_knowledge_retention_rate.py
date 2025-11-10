"""
Customer Knowledge Retention Rate KPI

The rate at which customers retain the knowledge or training provided by the company over time.
"""

from analytics_models import KPI

CUSTOMER_KNOWLEDGE_RETENTION_RATE = KPI(
    name="Customer Knowledge Retention Rate",
    code="CUSTOMER_KNOWLEDGE_RETENTION_RATE",
    category="Customer Success",
    
    # Core Definition
    description="The rate at which customers retain the knowledge or training provided by the company over time.",
    kpi_definition="The rate at which customers retain the knowledge or training provided by the company over time.",
    expected_business_insights="Assesses the effectiveness of educational content and its impact on product usage and satisfaction.",
    measurement_approach="Measures the extent to which customers retain important information or skills after education or training initiatives.",
    
    # Formula
    formula="(Number of Correct Responses in Follow-Up Assessments / Total Number of Responses) * 100",
    calculation_formula="(Number of Correct Responses in Follow-Up Assessments / Total Number of Responses) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing customer knowledge retention rate may indicate improved training programs or better customer engagement.
    * A decreasing rate could signal changes in the customer base, shifts in product complexity, or ineffective training methods.
    """,
    diagnostic_questions="""
    * Are there specific areas of training where customers consistently struggle to retain knowledge?
    * How does our customer knowledge retention rate compare with industry benchmarks or with different customer segments?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement interactive and engaging training methods to improve knowledge retention.
    * Regularly assess and update training materials to ensure relevance and effectiveness.
    * Provide ongoing support and resources for customers to reinforce and apply their knowledge.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of customer knowledge retention rate over time.
    * Comparison charts to analyze retention rates across different training modules or customer segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low customer knowledge retention can lead to increased support costs and customer dissatisfaction.
    * Inconsistent knowledge retention may indicate a need for better alignment between training and customer needs.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and analyze customer engagement with training materials.
    * Customer relationship management (CRM) software to monitor customer feedback and support interactions related to training.
    """,
    integration_points="""
    * Integrate customer knowledge retention data with product development to improve user experience and product usability.
    * Link retention rate with customer feedback systems to identify areas for improvement in training and support.
    """,
    change_impact_analysis="""
    * Improving customer knowledge retention can lead to higher customer satisfaction and loyalty.
    * Conversely, a decline in retention rate may impact overall customer experience and brand perception.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CUSTOMER_SUCCESS"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Deal", "Knowledge Base", "Lead", "Opportunity", "Partner Training", "Sales Training Program", "Training Program"]
    }
)
