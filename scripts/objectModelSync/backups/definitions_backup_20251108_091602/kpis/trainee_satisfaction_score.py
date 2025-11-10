"""
Trainee Satisfaction Score KPI

A metric that assesses the satisfaction level of sales trainees with the training program.
"""

from analytics_models import KPI

TRAINEE_SATISFACTION_SCORE = KPI(
    name="Trainee Satisfaction Score",
    code="TRAINEE_SATISFACTION_SCORE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="A metric that assesses the satisfaction level of sales trainees with the training program.",
    kpi_definition="A metric that assesses the satisfaction level of sales trainees with the training program.",
    expected_business_insights="Provides insight into the perceived value and quality of training from the perspective of the participants.",
    measurement_approach="Average score given by sales reps regarding their satisfaction with training sessions.",
    
    # Formula
    formula="Average of Satisfaction Scores Collected from Training Participants",
    calculation_formula="Average of Satisfaction Scores Collected from Training Participants",
    
    # Analysis
    trend_analysis="""
    * Trainee satisfaction scores may show an initial increase as new training methods or materials are introduced, followed by a plateau or decline as the novelty wears off.
    * Long-term trends may reveal fluctuations based on changes in sales management, leadership, or company culture.
    """,
    diagnostic_questions="""
    * What specific aspects of the training program are contributing to high or low satisfaction scores?
    * How do trainee satisfaction scores correlate with sales performance or retention rates?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly gather feedback from trainees to identify areas for improvement in the training program.
    * Implement mentorship or coaching programs to provide ongoing support and guidance to sales trainees.
    * Customize training materials and methods to better align with the learning styles and preferences of the trainees.
    """,
    visualization_suggestions="""
    * Line charts to track changes in satisfaction scores over time.
    * Comparative bar charts to analyze satisfaction scores across different training modules or instructors.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently low satisfaction scores may lead to decreased motivation and performance among sales trainees.
    * High variability in satisfaction scores could indicate inconsistency in the quality of training delivery.
    """,
    tracking_tools="""
    * Survey and feedback tools to collect and analyze trainee satisfaction data.
    * Learning management systems (LMS) to track trainee progress and engagement with training materials.
    """,
    integration_points="""
    * Integrate trainee satisfaction scores with performance management systems to identify correlations between satisfaction and sales results.
    * Link satisfaction scores with individual coaching or development plans to address specific areas of improvement.
    """,
    change_impact_analysis="""
    * Improving trainee satisfaction scores can lead to higher engagement, retention, and ultimately, better sales performance.
    * However, focusing solely on satisfaction scores without considering sales outcomes may lead to a disconnect between training effectiveness and business results.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer Advocacy Program", "Loyalty Program", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"]
    }
)
