"""
Sales Onboarding Feedback Score KPI

The average feedback score from new sales reps about the onboarding and training process.
"""

from analytics_models import KPI

SALES_ONBOARDING_FEEDBACK_SCORE = KPI(
    name="Sales Onboarding Feedback Score",
    code="SALES_ONBOARDING_FEEDBACK_SCORE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="The average feedback score from new sales reps about the onboarding and training process.",
    kpi_definition="The average feedback score from new sales reps about the onboarding and training process.",
    expected_business_insights="Provides insights into the effectiveness and satisfaction with the onboarding experience, which can influence future program design.",
    measurement_approach="Average feedback score provided by new sales reps about the onboarding process.",
    
    # Formula
    formula="Average of Feedback Scores Collected from New Sales Reps",
    calculation_formula="Average of Feedback Scores Collected from New Sales Reps",
    
    # Analysis
    trend_analysis="""
    * Increasing feedback scores may indicate a more effective onboarding process and better training materials.
    * Decreasing scores could signal issues with the onboarding program or a lack of support for new sales reps.
    """,
    diagnostic_questions="""
    * Are there specific aspects of the onboarding process that new sales reps consistently rate poorly?
    * How does the feedback score compare with industry benchmarks or with feedback from more tenured sales reps?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly update onboarding materials to reflect changes in products, processes, or market conditions.
    * Provide mentors or coaches for new sales reps to offer ongoing support and guidance beyond initial training.
    * Collect feedback from new sales reps at multiple points during the onboarding process to identify and address issues in real-time.
    """,
    visualization_suggestions="""
    * Line charts showing the average feedback score over time to track improvements or declines.
    * Pie charts comparing feedback scores for different training modules or aspects of the onboarding process.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low feedback scores may lead to higher turnover among new sales reps and increased recruitment costs.
    * Consistently poor feedback could indicate a need for a complete overhaul of the onboarding program.
    """,
    tracking_tools="""
    * Feedback collection and analysis tools like SurveyMonkey or Qualtrics to gather and interpret new sales rep feedback.
    * Learning management systems (LMS) to deliver and track onboarding materials and assessments.
    """,
    integration_points="""
    * Integrate feedback scores with performance management systems to identify correlations between onboarding experience and subsequent sales performance.
    * Link feedback data with HR systems to track the impact of onboarding on employee retention and satisfaction.
    """,
    change_impact_analysis="""
    * Improving the onboarding feedback score can lead to higher sales productivity and better customer interactions.
    * Conversely, a poor onboarding experience may result in lost sales opportunities and damage to the company\'s reputation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer Feedback", "Customer Onboarding", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]
    }
)
