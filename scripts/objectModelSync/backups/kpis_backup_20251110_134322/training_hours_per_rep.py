"""
Training Hours per Rep KPI

The total number of hours each sales representative spends in training.
"""

TRAINING_HOURS_PER_REP = {
    "code": "TRAINING_HOURS_PER_REP",
    "name": "Training Hours per Rep",
    "description": "The total number of hours each sales representative spends in training.",
    "formula": "Total Training Hours Completed / Number of Sales Reps",
    "calculation_formula": "Total Training Hours Completed / Number of Sales Reps",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The total number of hours each sales representative spends in training.",
    "expected_business_insights": "Reflects the depth and intensity of training efforts, indicating the time investment in sales rep development.",
    "measurement_approach": "The total number of training hours completed by each sales rep over a given period.",
    "trend_analysis": """
    * Training hours per rep may increase over time as new products, services, or sales techniques are introduced.
    * A decrease in training hours could indicate a lack of investment in ongoing development or a need for more efficient training methods.
    """,
    "diagnostic_questions": """
    * Are there specific areas or skills that sales reps consistently require more training in?
    * How do our training hours per rep compare with industry standards or benchmarks?
    """,
    "actionable_tips": """
    * Implement regular skills assessments to identify areas where reps need additional training.
    * Utilize e-learning platforms to provide flexible and ongoing training opportunities.
    * Encourage mentorship and peer-to-peer learning to supplement formal training programs.
    """,
    "visualization_suggestions": """
    * Line charts showing training hours per rep over time to identify trends and patterns.
    * Bar graphs comparing training hours by department, region, or product line to pinpoint areas needing more focus.
    """,
    "risk_warnings": """
    * Low training hours per rep may lead to decreased sales effectiveness and missed opportunities.
    * High training hours without corresponding improvements in performance may indicate ineffective training methods or lack of retention.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) to track and manage training programs and progress.
    * Video conferencing and virtual training tools for remote or distributed sales teams.
    """,
    "integration_points": """
    * Integrate training hours data with sales performance metrics to assess the impact of training on results.
    * Link training hours with employee development plans and performance reviews for a holistic approach to talent management.
    """,
    "change_impact_analysis": """
    * Increasing training hours may initially impact productivity but can lead to long-term improvements in sales performance.
    * Decreasing training hours may result in short-term cost savings but could lead to decreased competitiveness and employee satisfaction.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
