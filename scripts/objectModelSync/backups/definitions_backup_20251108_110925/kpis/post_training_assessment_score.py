"""
Post-Training Assessment Score KPI

The average scores of sales reps on assessments administered after training completion.
"""

from analytics_models import KPI

POST_TRAINING_ASSESSMENT_SCORE = KPI(
    name="Post-Training Assessment Score",
    code="POST_TRAINING_ASSESSMENT_SCORE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The average scores of sales reps on assessments administered after training completion.",
    kpi_definition="The average scores of sales reps on assessments administered after training completion.",
    expected_business_insights="Reflects the immediate understanding and retention of training material, guiding future training content adjustments.",
    measurement_approach="Average score achieved by sales reps on assessments conducted after training completion.",
    
    # Formula
    formula="Sum of Assessment Scores / Number of Assessments Administered",
    calculation_formula="Sum of Assessment Scores / Number of Assessments Administered",
    
    # Analysis
    trend_analysis="""
    * Increasing post-training assessment scores may indicate the effectiveness of the training program and improved knowledge retention among sales reps.
    * Decreasing scores could signal a need for reevaluation of the training content, delivery methods, or individual coaching needs.
    """,
    diagnostic_questions="""
    * Are there specific areas or topics where sales reps consistently score lower on post-training assessments?
    * How do the post-training assessment scores correlate with actual sales performance and quota attainment?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide ongoing coaching and reinforcement of training materials to ensure long-term retention and application of knowledge.
    * Customize training programs to address specific knowledge gaps identified through post-training assessments.
    * Implement mentorship programs or peer-to-peer learning initiatives to support continuous learning and skill development.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of average assessment scores over time to visualize improvements or declines.
    * Comparison bar charts to highlight the performance of different sales teams or individuals in post-training assessments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently low post-training assessment scores may indicate a need for more comprehensive training programs or individual coaching interventions.
    * High variability in scores across different sales teams or regions could signal inconsistent training delivery or support.
    """,
    tracking_tools="""
    * Learning management systems (LMS) to track and analyze post-training assessment scores across the sales organization.
    * Assessment and survey tools to gather feedback from sales reps on the effectiveness of training programs and areas for improvement.
    """,
    integration_points="""
    * Integrate post-training assessment data with sales performance metrics to identify correlations between training effectiveness and actual results.
    * Link assessment scores with individual development plans and performance reviews to drive continuous improvement and skill enhancement.
    """,
    change_impact_analysis="""
    * Improving post-training assessment scores can lead to increased sales productivity, higher customer satisfaction, and improved revenue generation.
    * On the other hand, declining scores may result in missed sales opportunities, decreased confidence among sales reps, and potential turnover.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
