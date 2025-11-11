"""
Coaching Quality Rating KPI

A measure of the quality of coaching sessions based on feedback from sales reps.
"""

COACHING_QUALITY_RATING = {
    "code": "COACHING_QUALITY_RATING",
    "name": "Coaching Quality Rating",
    "description": "A measure of the quality of coaching sessions based on feedback from sales reps.",
    "formula": "Average of Coaching Quality Scores Collected from Feedback Surveys",
    "calculation_formula": "Average of Coaching Quality Scores Collected from Feedback Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "A measure of the quality of coaching sessions based on feedback from sales reps.",
    "expected_business_insights": "Provides insight into the effectiveness of sales coaches and may indicate areas for improvement in coaching.",
    "measurement_approach": "A score representing the perceived quality of coaching sessions, typically assessed through feedback surveys.",
    "trend_analysis": """
    * An increasing coaching quality rating may indicate more effective coaching techniques being implemented by sales managers.
    * A decreasing rating could signal a decline in the effectiveness of coaching sessions or a lack of engagement from sales reps.
    """,
    "diagnostic_questions": """
    * Are there specific areas or topics where sales reps consistently rate coaching sessions lower?
    * How does the coaching quality rating compare with sales performance metrics such as conversion rates or average deal size?
    """,
    "actionable_tips": """
    * Implement regular feedback sessions with sales reps to understand their needs and preferences for coaching.
    * Provide training for sales managers on effective coaching techniques and communication skills.
    * Encourage peer-to-peer coaching and knowledge sharing among the sales team.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of coaching quality ratings over time.
    * Radar charts comparing different aspects of coaching quality (e.g., communication, motivation, skill development).
    """,
    "risk_warnings": """
    * Low coaching quality ratings may lead to decreased motivation and performance among sales reps.
    * Consistently low ratings could indicate a need for a complete overhaul of coaching strategies and techniques.
    """,
    "tracking_tools": """
    * Coaching and feedback platforms like Refract or LevelEleven to track coaching sessions and feedback from sales reps.
    * Performance management systems that integrate coaching quality ratings with sales performance data for a comprehensive view.
    """,
    "integration_points": """
    * Integrate coaching quality ratings with performance reviews and goal setting to align coaching efforts with individual development plans.
    * Link coaching quality data with sales training programs to identify areas where additional training or resources may be needed.
    """,
    "change_impact_analysis": """
    * Improving coaching quality can lead to increased sales performance and overall team effectiveness.
    * Conversely, a decline in coaching quality may result in missed sales opportunities and decreased team morale.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Customer Feedback", "Enablement Feedback", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
