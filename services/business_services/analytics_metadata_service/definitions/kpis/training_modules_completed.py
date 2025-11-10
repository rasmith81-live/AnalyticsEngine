"""
Training Modules Completed KPI

The number of training modules or courses completed by sales reps.
"""

TRAINING_MODULES_COMPLETED = {
    "code": "TRAINING_MODULES_COMPLETED",
    "name": "Training Modules Completed",
    "description": "The number of training modules or courses completed by sales reps.",
    "formula": "Total Number of Training Modules Completed",
    "calculation_formula": "Total Number of Training Modules Completed",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The number of training modules or courses completed by sales reps.",
    "expected_business_insights": "Indicates the breadth of knowledge and skills covered in sales training, contributing to comprehensive sales education.",
    "measurement_approach": "The total number of distinct training modules or courses completed by sales reps.",
    "trend_analysis": """
    * An increasing number of completed training modules may indicate a proactive approach to skill development and continuous learning among sales reps.
    * A decreasing trend could signal disengagement or lack of commitment to ongoing training, potentially impacting sales performance.
    """,
    "diagnostic_questions": """
    * Are there specific modules that are frequently left incomplete, and if so, why?
    * How does the completion rate of training modules correlate with sales performance and customer satisfaction?
    """,
    "actionable_tips": """
    * Provide incentives or recognition for sales reps who consistently complete training modules.
    * Offer a variety of training formats (e.g., online, in-person, role-playing) to cater to different learning preferences.
    * Regularly assess the relevance and effectiveness of existing training modules and update them as needed.
    """,
    "visualization_suggestions": """
    * Line charts showing the completion rate of training modules over time.
    * Pie charts comparing completion rates across different modules or sales teams.
    """,
    "risk_warnings": """
    * Low completion rates may lead to gaps in knowledge and skills, impacting sales effectiveness and customer interactions.
    * Inconsistent completion of training modules may indicate a lack of alignment with organizational goals and values.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) to track and manage the completion of training modules.
    * Survey tools to gather feedback from sales reps on the effectiveness and relevance of training modules.
    """,
    "integration_points": """
    * Integrate completion data with sales performance metrics to identify correlations between training and results.
    * Link completion rates with individual performance reviews and development plans for sales reps.
    """,
    "change_impact_analysis": """
    * Improving completion rates can lead to a more knowledgeable and skilled sales force, potentially increasing sales effectiveness and customer satisfaction.
    * However, a focus solely on completion rates may overlook the quality and application of the acquired knowledge and skills.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
