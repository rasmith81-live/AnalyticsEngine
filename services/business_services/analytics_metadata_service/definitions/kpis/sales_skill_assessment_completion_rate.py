"""
Sales Skill Assessment Completion Rate KPI

The percentage of sales team members who complete periodic skill assessments.
"""

SALES_SKILL_ASSESSMENT_COMPLETION_RATE = {
    "code": "SALES_SKILL_ASSESSMENT_COMPLETION_RATE",
    "name": "Sales Skill Assessment Completion Rate",
    "description": "The percentage of sales team members who complete periodic skill assessments.",
    "formula": "(Number of Completed Assessments / Total Number of Required Assessments) * 100",
    "calculation_formula": "(Number of Completed Assessments / Total Number of Required Assessments) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The percentage of sales team members who complete periodic skill assessments.",
    "expected_business_insights": "Measures the level of engagement with professional development and identification of skill gaps.",
    "measurement_approach": "Tracks the percentage of sales reps who have completed mandatory skill assessments.",
    "trend_analysis": """
    * Increasing completion rates may indicate a focus on continuous learning and development within the sales team.
    * Decreasing completion rates could signal disengagement, lack of motivation, or a need for more engaging assessment methods.
    """,
    "diagnostic_questions": """
    * Are there specific skills or topics where completion rates are consistently lower?
    * How do completion rates compare across different sales team segments (e.g., new hires vs. tenured employees)?
    """,
    "actionable_tips": """
    * Offer incentives or recognition for completing assessments to boost motivation.
    * Provide additional resources or training to address areas where completion rates are low.
    * Regularly communicate the importance of skill assessments and how they contribute to individual and team success.
    """,
    "visualization_suggestions": """
    * Line charts showing completion rates over time to identify trends and seasonality.
    * Pie charts to compare completion rates across different assessment topics or categories.
    """,
    "risk_warnings": """
    * Low completion rates may lead to gaps in knowledge and skills within the sales team, impacting overall performance.
    * Consistently high completion rates without corresponding performance improvements may indicate ineffective or irrelevant assessments.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) with built-in assessment modules for easy tracking and analysis.
    * Survey and assessment tools that provide real-time feedback and insights into completion rates and engagement.
    """,
    "integration_points": """
    * Integrate skill assessment data with performance reviews to identify correlations between completion rates and sales results.
    * Link assessment completion with individual development plans and training programs to create a seamless learning experience.
    """,
    "change_impact_analysis": """
    * Improving completion rates can lead to a more knowledgeable and skilled sales team, potentially impacting sales performance and customer satisfaction.
    * However, an overemphasis on completion rates alone may lead to "checkbox" mentality and superficial learning, affecting the quality of skill development.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
