"""
Sales Team Morale Post-Training KPI

The overall morale and motivation of the sales team following training interventions.
"""

SALES_TEAM_MORALE_POST_TRAINING = {
    "code": "SALES_TEAM_MORALE_POST_TRAINING",
    "name": "Sales Team Morale Post-Training",
    "description": "The overall morale and motivation of the sales team following training interventions.",
    "formula": "Qualitative Assessment or Morale Survey Scores",
    "calculation_formula": "Qualitative Assessment or Morale Survey Scores",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The overall morale and motivation of the sales team following training interventions.",
    "expected_business_insights": "Can signal the impact of training on team cohesion and motivation, affecting overall sales performance.",
    "measurement_approach": "The overall mood and spirit of the sales team after participating in training sessions.",
    "trend_analysis": """
    * Increasing morale post-training may indicate a positive impact on sales performance and productivity.
    * Decreasing morale could signal a lack of effectiveness in the training program or other underlying issues within the sales team.
    """,
    "diagnostic_questions": """
    * Are there specific aspects of the training program that received particularly positive or negative feedback from the sales team?
    * How does the current morale compare to previous periods, and what factors may have contributed to any changes?
    """,
    "actionable_tips": """
    * Implement regular feedback sessions to understand the impact of training on morale and address any concerns or issues promptly.
    * Recognize and reward improvements in performance or attitude following training to reinforce positive morale.
    """,
    "visualization_suggestions": """
    * Line charts showing morale levels over time to identify trends and correlations with specific training interventions.
    * Bar graphs comparing morale before and after different training programs to assess their effectiveness.
    """,
    "risk_warnings": """
    * Low morale can lead to decreased productivity, increased turnover, and ultimately, lower sales performance.
    * Consistently high morale without corresponding improvements in sales performance may indicate a disconnect between training and real-world application.
    """,
    "tracking_tools": """
    * Employee engagement platforms like Officevibe or TINYpulse to regularly assess and monitor morale levels.
    * Training management systems to track the impact of specific training programs on morale and performance.
    """,
    "integration_points": """
    * Integrate morale data with sales performance metrics to understand the direct impact of training on results.
    * Link morale assessments with individual performance reviews to identify areas for improvement and development.
    """,
    "change_impact_analysis": """
    * Improving morale can lead to increased motivation, collaboration, and ultimately, higher sales figures.
    * However, solely focusing on morale without addressing underlying issues or skill gaps may not lead to sustainable performance improvements.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
