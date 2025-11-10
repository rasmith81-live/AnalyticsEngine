"""
Knowledge Retention Rate KPI

The percentage of training information and skills retained by sales reps over time.
"""

from analytics_models import KPI

KNOWLEDGE_RETENTION_RATE = KPI(
    name="Knowledge Retention Rate",
    code="KNOWLEDGE_RETENTION_RATE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The percentage of training information and skills retained by sales reps over time.",
    kpi_definition="The percentage of training information and skills retained by sales reps over time.",
    expected_business_insights="Indicates the long-term effectiveness of training and potential needs for reinforcement or refresher courses.",
    measurement_approach="The percentage of training content that sales reps can recall and demonstrate understanding of after a certain period.",
    
    # Formula
    formula="(Number of Correct Responses in Follow-up Assessments / Total Number of Assessment Questions) * 100",
    calculation_formula="(Number of Correct Responses in Follow-up Assessments / Total Number of Assessment Questions) * 100",
    
    # Analysis
    trend_analysis="""
    * Knowledge retention rate may initially increase after training but gradually decline over time without reinforcement.
    * Positive trends may indicate effective coaching and ongoing support, while negative trends could signal a need for refresher training or improved coaching techniques.
    """,
    diagnostic_questions="""
    * Are there specific training modules or skills that sales reps struggle to retain?
    * How do our knowledge retention rates compare with industry benchmarks or best practices?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement spaced repetition techniques to reinforce training material at regular intervals.
    * Encourage peer-to-peer knowledge sharing and mentoring to solidify learning through teaching.
    * Provide ongoing coaching and support to help sales reps apply and retain new knowledge and skills.
    """,
    visualization_suggestions="""
    * Line charts showing knowledge retention rates over time for different training modules.
    * Comparison bar charts to visualize retention rates across different sales teams or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low knowledge retention rates can lead to decreased sales performance and missed opportunities.
    * Inconsistent retention may indicate a need for improved training content or delivery methods.
    """,
    tracking_tools="""
    * Learning management systems (LMS) with built-in assessment and tracking features to monitor knowledge retention.
    * Interactive e-learning platforms that offer quizzes, simulations, and interactive exercises to reinforce learning.
    """,
    integration_points="""
    * Integrate knowledge retention data with performance management systems to correlate retention with sales results.
    * Link retention rates with individual coaching and development plans to tailor support based on specific needs.
    """,
    change_impact_analysis="""
    * Improving knowledge retention can lead to more effective sales conversations and higher customer satisfaction.
    * However, investing in retention strategies may require allocating resources and time away from other sales activities.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Customer", "Deal", "Knowledge Base", "Lead", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
