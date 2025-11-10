"""
Sales Rep Soft Skills Improvement KPI

The enhancement of soft skills, such as communication and empathy, among sales reps after training.
"""

from analytics_models import KPI

SALES_REP_SOFT_SKILLS_IMPROVEMENT = KPI(
    name="Sales Rep Soft Skills Improvement",
    code="SALES_REP_SOFT_SKILLS_IMPROVEMENT",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The enhancement of soft skills, such as communication and empathy, among sales reps after training.",
    kpi_definition="The enhancement of soft skills, such as communication and empathy, among sales reps after training.",
    expected_business_insights="Signals the development of interpersonal skills crucial for sales success, potentially improving customer relationships.",
    measurement_approach="The advancement in soft skills such as communication, negotiation, and empathy, typically measured through assessments or feedback.",
    
    # Formula
    formula="Qualitative Assessment or Improvement Rating",
    calculation_formula="Qualitative Assessment or Improvement Rating",
    
    # Analysis
    trend_analysis="""
    * Improvement in soft skills may lead to better customer rapport and increased sales.
    * A decline in soft skills could result in decreased customer satisfaction and lower sales performance.
    """,
    diagnostic_questions="""
    * Are there specific soft skills that sales reps struggle with more than others?
    * How do customer feedback and satisfaction scores correlate with the enhancement of soft skills?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide ongoing coaching and practice opportunities for sales reps to improve their soft skills.
    * Incorporate soft skills training into regular sales meetings and performance evaluations.
    * Encourage role-playing exercises to help sales reps practice and refine their soft skills in a safe environment.
    """,
    visualization_suggestions="""
    * Line charts showing the progression of soft skills improvement over time.
    * Comparison bar charts displaying the soft skills levels of different sales reps or teams.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Poor soft skills can lead to negative customer experiences and potential loss of business.
    * Lack of improvement in soft skills may indicate a need for more targeted training and coaching methods.
    """,
    tracking_tools="""
    * Utilize customer relationship management (CRM) systems to track customer interactions and feedback related to soft skills.
    * Implement training and coaching platforms that offer personalized development plans for sales reps based on their soft skills assessments.
    """,
    integration_points="""
    * Integrate soft skills assessment results with performance evaluations to provide a comprehensive view of sales rep capabilities.
    * Align soft skills training with overall sales strategies and goals to ensure consistency and relevance.
    """,
    change_impact_analysis="""
    * Improving soft skills can lead to stronger customer relationships and increased customer lifetime value.
    * Conversely, a decline in soft skills may result in decreased customer retention and loyalty.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Customer Feedback", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
