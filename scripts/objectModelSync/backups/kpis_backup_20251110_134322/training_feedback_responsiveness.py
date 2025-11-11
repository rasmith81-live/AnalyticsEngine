"""
Training Feedback Responsiveness KPI

The speed and quality of how sales training providers respond to and act on trainee feedback.
"""

TRAINING_FEEDBACK_RESPONSIVENESS = {
    "code": "TRAINING_FEEDBACK_RESPONSIVENESS",
    "name": "Training Feedback Responsiveness",
    "description": "The speed and quality of how sales training providers respond to and act on trainee feedback.",
    "formula": "Time Taken to Implement Changes Post-Feedback",
    "calculation_formula": "Time Taken to Implement Changes Post-Feedback",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The speed and quality of how sales training providers respond to and act on trainee feedback.",
    "expected_business_insights": "Shows the commitment to continuous improvement in training based on participant input, impacting future training quality.",
    "measurement_approach": "The speed and extent to which training organizers act on feedback provided by trainees.",
    "trend_analysis": """
    * Increased responsiveness to training feedback may indicate a positive shift in the quality of sales training being provided.
    * Decreasing responsiveness could signal a decline in the effectiveness of the sales training program or a lack of attention to trainee feedback.
    """,
    "diagnostic_questions": """
    * Are there specific areas of the sales training program where feedback responsiveness is consistently low?
    * How do trainees perceive the impact of their feedback on the training content and delivery?
    """,
    "actionable_tips": """
    * Implement regular feedback collection mechanisms to ensure timely and comprehensive responses to trainee input.
    * Train sales managers and trainers on how to effectively analyze and act on feedback to continuously improve the training program.
    * Encourage open communication channels between trainees and training providers to address feedback in real-time.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of responsiveness over time.
    * Comparison bar charts to highlight differences in responsiveness across different training modules or providers.
    """,
    "risk_warnings": """
    * Poor responsiveness to feedback can lead to disengagement and reduced effectiveness of the sales training program.
    * Consistently low responsiveness may indicate a systemic issue in the training provider's ability to adapt and improve.
    """,
    "tracking_tools": """
    * Feedback management software to streamline the collection, analysis, and response to trainee feedback.
    * Training evaluation platforms that provide insights into the impact of feedback on training outcomes.
    """,
    "integration_points": """
    * Integrate feedback responsiveness data with sales performance metrics to understand the correlation between training improvements and sales results.
    * Link feedback responsiveness with employee development systems to identify training needs and opportunities for individual improvement.
    """,
    "change_impact_analysis": """
    * Improving feedback responsiveness can lead to a more engaged and skilled sales team, positively impacting overall sales performance.
    * On the other hand, a decline in responsiveness may result in decreased employee satisfaction and retention.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Feedback", "Deal", "Enablement Feedback", "Lead", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
