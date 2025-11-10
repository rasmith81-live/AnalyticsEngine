"""
E-learning Completion Rates KPI

The percentage of online training modules successfully completed by sales reps.
"""

E_LEARNING_COMPLETION_RATES = {
    "code": "E_LEARNING_COMPLETION_RATES",
    "name": "E-learning Completion Rates",
    "description": "The percentage of online training modules successfully completed by sales reps.",
    "formula": "(Number of E-learning Modules Completed / Total Number of E-learning Modules Assigned) * 100",
    "calculation_formula": "(Number of E-learning Modules Completed / Total Number of E-learning Modules Assigned) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The percentage of online training modules successfully completed by sales reps.",
    "expected_business_insights": "Reflects the level of engagement and commitment to self-paced online sales training among the sales team.",
    "measurement_approach": "The percentage of assigned e-learning modules that sales reps successfully complete.",
    "trend_analysis": """
    * Completion rates may show an initial spike as sales reps engage with new training materials, followed by a gradual decline as the novelty wears off.
    * An upward trend in completion rates could indicate improved content relevance or increased motivation among sales reps, while a downward trend may suggest disengagement or dissatisfaction with the training modules.
    """,
    "diagnostic_questions": """
    * Are there specific modules or topics with consistently low completion rates?
    * How does the completion rate compare across different sales teams or regions?
    """,
    "actionable_tips": """
    * Regularly update and refresh training content to maintain sales reps' interest and relevance to their roles.
    * Provide incentives or recognition for high completion rates to motivate sales reps to engage with e-learning modules.
    * Implement a mentorship or coaching program to support sales reps in applying the knowledge gained from e-learning in their day-to-day activities.
    """,
    "visualization_suggestions": """
    * Line charts showing completion rates over time to identify trends and patterns.
    * Pie charts comparing completion rates across different modules or teams to pinpoint areas for improvement.
    """,
    "risk_warnings": """
    * Low completion rates may indicate a lack of knowledge retention or application in real sales scenarios.
    * High completion rates without corresponding improvements in sales performance could suggest that the training content is not effectively addressing the needs of the sales team.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) with built-in analytics to track completion rates and identify areas for improvement.
    * Interactive e-learning platforms that offer engaging and interactive content to increase completion rates.
    """,
    "integration_points": """
    * Integrate completion rate data with sales performance metrics to assess the impact of training on actual sales results.
    * Link completion rates with individual performance reviews to identify training needs and opportunities for development.
    """,
    "change_impact_analysis": """
    * Improving completion rates can lead to better knowledge retention, increased sales effectiveness, and ultimately, higher revenue.
    * However, a focus solely on completion rates may neglect the quality and applicability of the training content, leading to limited impact on actual sales performance.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
