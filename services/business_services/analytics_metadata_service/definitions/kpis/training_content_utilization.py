"""
Training Content Utilization KPI

The frequency with which sales reps use the training materials and resources provided.
"""

TRAINING_CONTENT_UTILIZATION = {
    "code": "TRAINING_CONTENT_UTILIZATION",
    "name": "Training Content Utilization",
    "description": "The frequency with which sales reps use the training materials and resources provided.",
    "formula": "(Number of Accesses to Training Content / Number of Training Materials Available) * 100",
    "calculation_formula": "(Number of Accesses to Training Content / Number of Training Materials Available) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The frequency with which sales reps use the training materials and resources provided.",
    "expected_business_insights": "Indicates the relevance and applicability of training content to the sales reps’ day-to-day activities.",
    "measurement_approach": "Measure of how frequently and extensively sales reps use the training materials provided.",
    "trend_analysis": """
    * Increasing utilization may indicate a positive response to the training content and improved sales performance.
    * Decreasing utilization could signal a need to reassess the relevance and effectiveness of the training materials.
    """,
    "diagnostic_questions": """
    * Are there specific training modules or resources that are being underutilized?
    * How does the utilization of training content correlate with sales performance and quota attainment?
    """,
    "actionable_tips": """
    * Regularly update and refresh training materials to keep them relevant and engaging.
    * Provide incentives or recognition for reps who demonstrate strong utilization of training resources.
    * Seek feedback from sales reps on the effectiveness and helpfulness of the training content.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of training content utilization over time.
    * Pie charts comparing the utilization rates of different training modules or resources.
    """,
    "risk_warnings": """
    * Low utilization may lead to missed sales opportunities and decreased productivity.
    * High utilization without corresponding improvements in sales performance may indicate a need for more effective training content.
    """,
    "tracking_tools": """
    * Learning management systems (LMS) to track and analyze the utilization of training materials.
    * Survey and feedback tools to gather insights from sales reps on the usefulness of the training content.
    """,
    "integration_points": """
    * Integrate training content utilization data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link utilization data with individual performance reviews and coaching sessions to address specific training needs.
    """,
    "change_impact_analysis": """
    * Improving utilization can lead to better sales performance and increased revenue.
    * However, over-reliance on training materials without practical application may not translate to actual sales results.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
