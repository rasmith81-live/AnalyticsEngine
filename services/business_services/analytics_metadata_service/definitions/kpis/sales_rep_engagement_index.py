"""
Sales Rep Engagement Index KPI

A composite measure of how engaged sales reps are with their work and training.
"""

SALES_REP_ENGAGEMENT_INDEX = {
    "code": "SALES_REP_ENGAGEMENT_INDEX",
    "name": "Sales Rep Engagement Index",
    "description": "A composite measure of how engaged sales reps are with their work and training.",
    "formula": "Composite Score from Engagement Surveys",
    "calculation_formula": "Composite Score from Engagement Surveys",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "A composite measure of how engaged sales reps are with their work and training.",
    "expected_business_insights": "Provides insight into the overall engagement and motivation of the sales team, which can be influenced by training and development initiatives.",
    "measurement_approach": "A composite score measuring sales rep involvement, enthusiasm, and commitment to their roles.",
    "trend_analysis": """
    * An increasing Sales Rep Engagement Index may indicate a positive shift in the sales team's motivation and productivity.
    * A decreasing index could signal disengagement, potential turnover, or dissatisfaction with training and coaching programs.
    """,
    "diagnostic_questions": """
    * Are there specific training modules or coaching methods that are receiving lower engagement from sales reps?
    * How does the Sales Rep Engagement Index compare with industry benchmarks or with historical data?
    """,
    "actionable_tips": """
    * Regularly solicit feedback from sales reps to understand their training and coaching needs.
    * Provide personalized coaching and training plans to address individual development areas and keep sales reps engaged.
    * Implement recognition and rewards programs to acknowledge and incentivize active participation in training and coaching activities.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of the Sales Rep Engagement Index over time.
    * Pie charts to visualize the distribution of engagement levels across different training and coaching programs.
    """,
    "risk_warnings": """
    * Low engagement may lead to decreased sales performance and missed targets.
    * Disengagement could also result in increased turnover and recruitment costs.
    """,
    "tracking_tools": """
    * Employee engagement platforms like Officevibe or 15Five to gather feedback and measure engagement levels.
    * Learning management systems (LMS) to track participation and completion rates of training modules.
    """,
    "integration_points": """
    * Integrate the Sales Rep Engagement Index with performance management systems to identify correlations between engagement and sales results.
    * Link engagement data with HR systems to understand the impact of engagement on turnover and retention.
    """,
    "change_impact_analysis": """
    * Improving the Sales Rep Engagement Index can lead to higher sales productivity and improved customer satisfaction.
    * Conversely, low engagement may result in missed sales opportunities and a negative impact on the overall sales team morale.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Lead", "Partner Training", "Prospect Engagement", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
