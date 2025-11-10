"""
Training Attendance Rate KPI

The percentage of mandated training sessions that sales reps attend.
"""

TRAINING_ATTENDANCE_RATE = {
    "code": "TRAINING_ATTENDANCE_RATE",
    "name": "Training Attendance Rate",
    "description": "The percentage of mandated training sessions that sales reps attend.",
    "formula": "(Number of Attendees / Total Number of Trainees Expected) * 100",
    "calculation_formula": "(Number of Attendees / Total Number of Trainees Expected) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The percentage of mandated training sessions that sales reps attend.",
    "expected_business_insights": "Shows the level of engagement with and commitment to mandatory or optional training programs.",
    "measurement_approach": "The percentage of sales reps who attend scheduled training sessions.",
    "trend_analysis": """
    * Training attendance rate may show an initial increase as new training initiatives are introduced, followed by a plateau or decline as the novelty wears off.
    * An upward trend in attendance rate could indicate improved engagement and buy-in from sales reps, while a downward trend may signal disengagement or dissatisfaction with the training content.
    """,
    "diagnostic_questions": """
    * Are there specific training sessions that consistently have lower attendance rates, and if so, what factors may be contributing to this?
    * How does the attendance rate for mandated training sessions compare with voluntary or optional training opportunities, and what insights can be gained from this comparison?
    """,
    "actionable_tips": """
    * Offer incentives or rewards for consistent attendance at training sessions to boost participation.
    * Regularly solicit feedback from sales reps on the quality and relevance of training content, and make adjustments based on their input.
    * Provide flexible training options such as virtual sessions or self-paced modules to accommodate different learning styles and schedules.
    """,
    "visualization_suggestions": """
    * Line charts to track attendance rates over time and identify any recurring patterns or fluctuations.
    * Bar graphs comparing attendance rates across different training topics or facilitators to pinpoint areas of high and low engagement.
    """,
    "risk_warnings": """
    * Low training attendance rates may lead to gaps in knowledge and skills among the sales team, impacting their ability to effectively sell products or services.
    * Consistently low attendance could indicate broader issues with the training program or a lack of perceived value in the content, requiring a reevaluation of the training approach.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) to track attendance, deliver training content, and gather feedback from participants.
    * Survey and assessment tools to measure the effectiveness of training sessions and identify areas for improvement.
    """,
    "integration_points": """
    * Integrate training attendance data with sales performance metrics to identify any correlations between training participation and sales outcomes.
    * Link attendance tracking with individual performance reviews to recognize and reward consistent participation in training activities.
    """,
    "change_impact_analysis": """
    * Improving training attendance rates can lead to better-equipped sales reps, potentially resulting in increased sales, customer satisfaction, and retention.
    * However, a heavy focus on attendance numbers alone may overlook the quality and effectiveness of the training content, so a balanced approach is necessary.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
