"""
Training Effectiveness KPI

The percentage of sales reps who rate the training and coaching as effective. A higher rating indicates effective training and coaching.
"""

TRAINING_EFFECTIVENESS = {
    "code": "TRAINING_EFFECTIVENESS",
    "name": "Training Effectiveness",
    "description": "The percentage of sales reps who rate the training and coaching as effective. A higher rating indicates effective training and coaching.",
    "formula": "Composite Score from Effectiveness Surveys and Performance Improvements",
    "calculation_formula": "Composite Score from Effectiveness Surveys and Performance Improvements",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The percentage of sales reps who rate the training and coaching as effective. A higher rating indicates effective training and coaching.",
    "expected_business_insights": "Evaluates the overall success of training programs in enhancing sales rep skills and performance.",
    "measurement_approach": "A composite measure of how well training meets its objectives, often assessed through feedback, assessments, and performance metrics.",
    "trend_analysis": """
    * An increasing percentage of sales reps rating the training and coaching as effective may indicate a positive shift in performance and skill development.
    * A decreasing percentage could signal a decline in the quality of training and coaching, leading to potential negative impacts on sales performance.
    """,
    "diagnostic_questions": """
    * Are there specific areas of the training and coaching program that receive consistently lower ratings?
    * How do the ratings for training and coaching correlate with actual sales performance and targets?
    """,
    "actionable_tips": """
    * Regularly solicit feedback from sales reps to identify areas for improvement in the training and coaching program.
    * Provide additional resources and support for sales reps who may require extra assistance in implementing the training and coaching content.
    * Implement a mentorship program to pair experienced sales reps with those who may benefit from additional guidance and support.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of the percentage of sales reps rating the training and coaching as effective over time.
    * Comparative bar charts displaying the effectiveness ratings across different sales teams or regions.
    """,
    "risk_warnings": """
    * A consistently low percentage of sales reps rating the training and coaching as effective may lead to decreased motivation and performance.
    * Failure to address issues with training and coaching effectiveness could result in increased turnover and recruitment costs.
    """,
    "tracking_tools": """
    * Utilize survey and feedback tools to gather and analyze ratings and comments from sales reps regarding the training and coaching program.
    * Implement learning management systems (LMS) to track the completion and effectiveness of training modules and coaching sessions.
    """,
    "integration_points": """
    * Integrate training and coaching effectiveness data with sales performance metrics to identify correlations and areas for improvement.
    * Link feedback from sales reps regarding training and coaching to performance management and development plans.
    """,
    "change_impact_analysis": """
    * Improving the effectiveness of training and coaching can lead to increased sales productivity and revenue generation.
    * Conversely, a decline in training and coaching effectiveness may result in missed sales opportunities and reduced customer satisfaction.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer Feedback", "Enablement Feedback", "Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
