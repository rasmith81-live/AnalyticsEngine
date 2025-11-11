"""
Post-Training Support Satisfaction KPI

The satisfaction of sales reps with the support they receive after completing training.
"""

POST_TRAINING_SUPPORT_SATISFACTION = {
    "code": "POST_TRAINING_SUPPORT_SATISFACTION",
    "name": "Post-Training Support Satisfaction",
    "description": "The satisfaction of sales reps with the support they receive after completing training.",
    "formula": "Average of Satisfaction Scores Collected from Post-Training Surveys",
    "calculation_formula": "Average of Satisfaction Scores Collected from Post-Training Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The satisfaction of sales reps with the support they receive after completing training.",
    "expected_business_insights": "Highlights the effectiveness and perceived value of post-training support, which can impact long-term training outcomes.",
    "measurement_approach": "The level of sales rep satisfaction with the support and resources provided after training.",
    "trend_analysis": """
    * Increasing satisfaction with post-training support may indicate a positive impact on sales performance and confidence.
    * Decreasing satisfaction could signal a need for improved or more personalized support strategies.
    """,
    "diagnostic_questions": """
    * Are there specific areas where sales reps feel they need more support after training?
    * How does the satisfaction level compare with the actual support provided, and are there any gaps?
    """,
    "actionable_tips": """
    * Implement regular check-ins or follow-up sessions to address any post-training challenges or questions.
    * Provide access to additional resources or mentors for ongoing support and guidance.
    * Collect feedback from sales reps to continuously improve and tailor post-training support to their needs.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of satisfaction levels over time.
    * Comparison bar charts to analyze satisfaction levels across different support strategies or resources.
    """,
    "risk_warnings": """
    * Low satisfaction with post-training support can lead to decreased motivation and performance among sales reps.
    * Consistently low satisfaction may indicate a need for a complete overhaul of the support system.
    """,
    "tracking_tools": """
    * CRM systems with feedback and survey capabilities to gather and analyze post-training support satisfaction data.
    * Learning management systems to track and monitor the utilization of post-training resources and support materials.
    """,
    "integration_points": """
    * Integrate post-training support satisfaction data with sales performance metrics to understand the impact on results.
    * Link with HR systems to identify any correlations between post-training support and employee retention or turnover.
    """,
    "change_impact_analysis": """
    * Improving post-training support satisfaction can lead to increased sales productivity and effectiveness.
    * Conversely, low satisfaction can result in higher turnover rates and a negative impact on the overall sales team morale.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Support Ticket", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
