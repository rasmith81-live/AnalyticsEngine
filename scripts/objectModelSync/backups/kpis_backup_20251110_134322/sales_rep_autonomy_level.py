"""
Sales Rep Autonomy Level KPI

The level of independence and decision-making granted to sales reps as a result of effective training.
"""

SALES_REP_AUTONOMY_LEVEL = {
    "code": "SALES_REP_AUTONOMY_LEVEL",
    "name": "Sales Rep Autonomy Level",
    "description": "The level of independence and decision-making granted to sales reps as a result of effective training.",
    "formula": "Qualitative Assessment or Autonomy Level Rating",
    "calculation_formula": "Qualitative Assessment or Autonomy Level Rating",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The level of independence and decision-making granted to sales reps as a result of effective training.",
    "expected_business_insights": "Indicates the effectiveness of training in preparing reps for autonomous decision-making and action in sales scenarios.",
    "measurement_approach": "The degree to which sales reps operate independently after receiving training, often based on self-reporting or managerial assessment.",
    "trend_analysis": """
    * Increasing sales rep autonomy may indicate improved training effectiveness and confidence in decision-making.
    * Decreasing autonomy could signal a lack of trust in sales reps or ineffective training methods.
    """,
    "diagnostic_questions": """
    * Are sales reps consistently making decisions without needing approval or guidance?
    * How does the level of autonomy impact sales performance and customer satisfaction?
    """,
    "actionable_tips": """
    * Provide ongoing coaching and support to ensure sales reps are equipped to make independent decisions.
    * Establish clear guidelines and boundaries for decision-making to balance autonomy with organizational goals.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of sales rep autonomy over time.
    * Stacked bar charts comparing autonomy levels across different sales teams or regions.
    """,
    "risk_warnings": """
    * Too much autonomy without proper training can lead to poor decision-making and negative customer experiences.
    * Too little autonomy can result in disengaged sales reps and missed opportunities for innovation.
    """,
    "tracking_tools": """
    * CRM systems with activity tracking and performance metrics to monitor the impact of autonomy on sales outcomes.
    * Training and development platforms to assess the effectiveness of training programs in building autonomy.
    """,
    "integration_points": """
    * Integrate sales rep autonomy data with performance evaluations to understand the correlation between autonomy and results.
    * Link autonomy levels with customer feedback and satisfaction scores to gauge the impact on customer experience.
    """,
    "change_impact_analysis": """
    * Increasing autonomy can lead to faster decision-making and more agile responses to customer needs.
    * Decreasing autonomy may result in a more controlled sales process but could stifle creativity and innovation.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Assessment", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
