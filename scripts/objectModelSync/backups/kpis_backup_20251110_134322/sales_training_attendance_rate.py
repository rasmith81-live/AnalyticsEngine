"""
Sales Training Attendance Rate KPI

The percentage of eligible sales representatives who attend scheduled sales training sessions.
"""

SALES_TRAINING_ATTENDANCE_RATE = {
    "code": "SALES_TRAINING_ATTENDANCE_RATE",
    "name": "Sales Training Attendance Rate",
    "description": "The percentage of eligible sales representatives who attend scheduled sales training sessions.",
    "formula": "(Number of Reps Attending Training / Total Number of Reps Expected to Attend) * 100",
    "calculation_formula": "(Number of Reps Attending Training / Total Number of Reps Expected to Attend) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The percentage of eligible sales representatives who attend scheduled sales training sessions.",
    "expected_business_insights": "Reveals the commitment to professional development and potential correlations to sales performance.",
    "measurement_approach": "Measures the percentage of sales reps attending scheduled training sessions.",
    "trend_analysis": """
    * Increasing sales training attendance rate may indicate a more engaged and motivated sales team.
    * Decreasing attendance could signal a lack of interest in the training content or a need for more engaging training methods.
    """,
    "diagnostic_questions": """
    * Are there specific topics or areas of training that consistently have lower attendance?
    * How does the attendance rate vary between new hires and more experienced sales representatives?
    """,
    "actionable_tips": """
    * Offer incentives or rewards for attending training sessions to boost participation.
    * Provide more interactive and hands-on training experiences to increase engagement.
    * Regularly survey sales representatives to gather feedback on training content and delivery.
    """,
    "visualization_suggestions": """
    * Line charts showing attendance rates over time to identify trends and patterns.
    * Comparison bar charts to visualize attendance rates for different training topics or regions.
    """,
    "risk_warnings": """
    * Low attendance rates may lead to gaps in knowledge and skills among the sales team, impacting overall performance.
    * Consistently low attendance could indicate a need for reevaluation of training content and methods.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) to track and analyze attendance data for training sessions.
    * Survey and feedback tools to gather insights from sales representatives about their training experiences.
    """,
    "integration_points": """
    * Integrate attendance data with performance metrics to assess the impact of training on sales results.
    * Link attendance tracking with HR systems to identify any correlations between training participation and employee satisfaction or turnover.
    """,
    "change_impact_analysis": """
    * Improving attendance rates can lead to better-equipped sales representatives, potentially increasing sales performance and customer satisfaction.
    * However, increased attendance may also require additional resources for training delivery and content development.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
