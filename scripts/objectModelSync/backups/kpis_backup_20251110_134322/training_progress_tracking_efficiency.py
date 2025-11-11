"""
Training Progress Tracking Efficiency KPI

How effectively the sales training team tracks the progress of sales reps through training programs.
"""

TRAINING_PROGRESS_TRACKING_EFFICIENCY = {
    "code": "TRAINING_PROGRESS_TRACKING_EFFICIENCY",
    "name": "Training Progress Tracking Efficiency",
    "description": "How effectively the sales training team tracks the progress of sales reps through training programs.",
    "formula": "(Total Number of Completed Training Assignments / Total Number of Assigned Training Tasks) * 100",
    "calculation_formula": "(Total Number of Completed Training Assignments / Total Number of Assigned Training Tasks) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "How effectively the sales training team tracks the progress of sales reps through training programs.",
    "expected_business_insights": "Reveals the effectiveness of the training curriculum and potential bottlenecks in the learning process.",
    "measurement_approach": "Considers metrics like the average time taken for employees to complete training modules and the rate of overdue training assignments.",
    "trend_analysis": """
    * Increasing training progress tracking efficiency may indicate a more structured and effective training program.
    * Decreasing efficiency could signal a lack of engagement or understanding among sales reps, or a need for better tracking tools.
    """,
    "diagnostic_questions": """
    * Are there specific training modules or topics where sales reps tend to progress more slowly?
    * How does the progress tracking efficiency compare with the actual performance improvement of sales reps post-training?
    """,
    "actionable_tips": """
    * Implement automated tracking systems to reduce manual data entry and improve accuracy.
    * Regularly review and update training materials to ensure relevance and engagement.
    * Provide incentives for sales reps to complete training modules in a timely manner.
    """,
    "visualization_suggestions": """
    * Line charts showing the average time taken to complete each training module over time.
    * Comparison bar charts displaying the progress tracking efficiency for different sales teams or regions.
    """,
    "risk_warnings": """
    * Low progress tracking efficiency may lead to gaps in knowledge and skills among sales reps, impacting overall performance.
    * Inaccurate tracking could result in misinformed decisions regarding training program improvements.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) with built-in progress tracking and reporting features.
    * CRM platforms that integrate with training progress tracking to provide a comprehensive view of sales rep performance.
    """,
    "integration_points": """
    * Integrate progress tracking data with performance management systems to align training progress with sales targets and goals.
    * Link progress tracking with coaching and mentoring programs to provide personalized support based on individual training needs.
    """,
    "change_impact_analysis": """
    * Improving training progress tracking efficiency can lead to better-prepared sales reps, potentially increasing sales performance and customer satisfaction.
    * However, overly stringent tracking methods may lead to disengagement and resistance among sales reps, impacting overall morale and retention.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
