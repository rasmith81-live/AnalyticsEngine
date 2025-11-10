"""
Customer Engagement Score Post-Training KPI

The change in the score measuring how effectively sales reps engage customers after training.
"""

CUSTOMER_ENGAGEMENT_SCORE_POST_TRAINING = {
    "code": "CUSTOMER_ENGAGEMENT_SCORE_POST_TRAINING",
    "name": "Customer Engagement Score Post-Training",
    "description": "The change in the score measuring how effectively sales reps engage customers after training.",
    "formula": "Sum of Engagement Scores Post-Training / Number of Interactions",
    "calculation_formula": "Sum of Engagement Scores Post-Training / Number of Interactions",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The change in the score measuring how effectively sales reps engage customers after training.",
    "expected_business_insights": "Provides insight into the training’s impact on customer engagement skills and can highlight areas for further development.",
    "measurement_approach": "A measure of customer interaction and engagement levels with sales reps after they have undergone training.",
    "trend_analysis": """
    * An increasing customer engagement score post-training may indicate the effectiveness of the training program in improving sales reps' customer interaction skills.
    * A decreasing score could signal a need for additional or different training methods to enhance customer engagement.
    """,
    "diagnostic_questions": """
    * Are there specific customer segments or types of interactions that show the most significant changes in engagement scores post-training?
    * How do the post-training engagement scores compare with pre-training scores and industry benchmarks?
    """,
    "actionable_tips": """
    * Provide ongoing coaching and reinforcement of training concepts to ensure sustained improvement in customer engagement.
    * Use role-playing exercises and simulations to practice and refine customer engagement skills learned in training.
    * Collect feedback from customers to understand the impact of training on their perception of sales reps' engagement.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of customer engagement scores over time.
    * Comparison bar charts displaying pre-training and post-training engagement scores for different sales reps or teams.
    """,
    "risk_warnings": """
    * Low post-training engagement scores may lead to decreased sales performance and customer satisfaction.
    * Inconsistent or ineffective training may result in minimal improvement in customer engagement, impacting overall sales effectiveness.
    """,
    "tracking_tools": """
    * CRM systems with built-in customer engagement tracking and reporting capabilities.
    * Feedback and survey tools to gather customer feedback on sales reps' engagement post-training.
    """,
    "integration_points": """
    * Integrate customer engagement scores with performance management systems to align training efforts with individual sales rep development plans.
    * Link engagement scores with customer relationship management platforms to track the impact of improved engagement on customer retention and sales opportunities.
    """,
    "change_impact_analysis": """
    * Improving customer engagement scores can lead to increased customer loyalty and repeat business.
    * However, focusing solely on engagement scores may neglect other critical aspects of the sales process, such as conversion rates and deal size.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Lead", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
