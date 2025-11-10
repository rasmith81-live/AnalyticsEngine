"""
Sales Confidence Increase KPI

A metric that tracks the increase in sales reps' confidence after training and coaching interventions.
"""

from analytics_models import KPI

SALES_CONFIDENCE_INCREASE = KPI(
    name="Sales Confidence Increase",
    code="SALES_CONFIDENCE_INCREASE",
    category="Sales Training and Coaching",
    
    # Core Definition
    description="A metric that tracks the increase in sales reps\' confidence after training and coaching interventions.",
    kpi_definition="A metric that tracks the increase in sales reps\' confidence after training and coaching interventions.",
    expected_business_insights="Can indicate the psychological impact of training on sales performance and readiness to engage with customers.",
    measurement_approach="The change in self-reported confidence levels of sales reps following training.",
    
    # Formula
    formula="(Average Confidence Level Post-Training - Average Confidence Level Pre-Training) / Average Confidence Level Pre-Training * 100",
    calculation_formula="(Average Confidence Level Post-Training - Average Confidence Level Pre-Training) / Average Confidence Level Pre-Training * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing sales confidence may indicate the effectiveness of training and coaching interventions.
    * A decreasing confidence level could signal a need for reevaluation of training methods or individual coaching approaches.
    """,
    diagnostic_questions="""
    * Are there specific areas or topics where sales reps consistently show lower confidence levels?
    * How do the confidence levels of top-performing sales reps compare to those who are struggling?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide personalized coaching and training to address individual sales reps\' areas of low confidence.
    * Implement regular feedback sessions to reinforce positive behaviors and build confidence.
    * Create a supportive and collaborative team environment to boost overall confidence levels.
    """,
    visualization_suggestions="""
    * Line charts tracking the average confidence levels over time for the entire sales team or specific individuals.
    * Radar charts comparing confidence levels across different sales competencies or skills.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low confidence levels can lead to decreased motivation and performance among sales reps.
    * Consistently low confidence across the team may indicate systemic issues in training or coaching methods.
    """,
    tracking_tools="""
    * Utilize sales performance management software to track and analyze individual sales reps\' confidence levels.
    * Implement video coaching platforms to provide personalized feedback and support for sales reps.
    """,
    integration_points="""
    * Integrate sales confidence data with performance management systems to identify correlations between confidence levels and sales results.
    * Link confidence tracking with customer relationship management (CRM) systems to understand the impact on customer interactions and outcomes.
    """,
    change_impact_analysis="""
    * Increasing sales confidence can lead to higher motivation, improved customer interactions, and ultimately, increased sales performance.
    * However, overly confident sales reps may need additional monitoring to ensure they maintain professionalism and accuracy in their interactions.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_TRAINING_COACHING"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"]
    }
)
