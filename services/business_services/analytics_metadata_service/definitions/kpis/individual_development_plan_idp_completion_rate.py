"""
Individual Development Plan (IDP) Completion Rate KPI

The percentage of sales reps who complete their IDPs within the planned timeframe.
"""

INDIVIDUAL_DEVELOPMENT_PLAN_IDP_COMPLETION_RATE = {
    "code": "INDIVIDUAL_DEVELOPMENT_PLAN_IDP_COMPLETION_RATE",
    "name": "Individual Development Plan (IDP) Completion Rate",
    "description": "The percentage of sales reps who complete their IDPs within the planned timeframe.",
    "formula": "(Number of IDPs Completed / Total Number of IDPs Assigned) * 100",
    "calculation_formula": "(Number of IDPs Completed / Total Number of IDPs Assigned) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The percentage of sales reps who complete their IDPs within the planned timeframe.",
    "expected_business_insights": "Reveals the degree to which sales reps are following through with their development goals and the effectiveness of IDPs.",
    "measurement_approach": "The percentage of sales reps who complete their personalized development plans within a specified timeframe.",
    "trend_analysis": """
    * An increasing IDP completion rate may indicate a more engaged and proactive sales team.
    * A decreasing rate could signal disengagement, lack of motivation, or ineffective coaching and training.
    """,
    "diagnostic_questions": """
    * Are there common reasons why sales reps are not completing their IDPs on time?
    * How does the IDP completion rate correlate with sales performance and overall job satisfaction?
    """,
    "actionable_tips": """
    * Provide clear expectations and guidance for creating and completing IDPs.
    * Offer regular coaching and support to help sales reps identify and achieve their development goals.
    * Incorporate IDP progress into performance evaluations and recognition programs.
    """,
    "visualization_suggestions": """
    * Line charts showing the IDP completion rate over time for individual sales reps and the team as a whole.
    * Comparison bar graphs to visualize completion rates across different sales territories or product lines.
    """,
    "risk_warnings": """
    * A low IDP completion rate may lead to decreased individual and team performance, as well as higher turnover.
    * Consistently high completion rates without corresponding improvements in sales performance could indicate a lack of meaningful development in the IDPs.
    """,
    "tracking_tools": """
    * Performance management software with IDP tracking and reporting capabilities.
    * Coaching and mentoring platforms to facilitate ongoing support and feedback for sales reps.
    """,
    "integration_points": """
    * Integrate IDP completion data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link IDP progress with learning and development systems to ensure alignment with broader training initiatives.
    """,
    "change_impact_analysis": """
    * Improving the IDP completion rate can lead to more skilled and motivated sales reps, potentially driving higher revenue and customer satisfaction.
    * However, focusing solely on completion rates without considering the quality and relevance of the IDPs may result in superficial development and limited impact on sales outcomes.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Plan", "Deal", "Lead", "Opportunity", "Partner Training", "Quota Plan", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
