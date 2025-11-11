"""
Win-Loss Analysis Completion Rate KPI

The percentage of closed deals that are followed by a win-loss analysis to understand the reasons behind the outcome.
"""

WIN_LOSS_ANALYSIS_COMPLETION_RATE = {
    "code": "WIN_LOSS_ANALYSIS_COMPLETION_RATE",
    "name": "Win-Loss Analysis Completion Rate",
    "description": "The percentage of closed deals that are followed by a win-loss analysis to understand the reasons behind the outcome.",
    "formula": "(Number of Completed Win-Loss Analyses / Total Number of Sales Opportunities) * 100",
    "calculation_formula": "(Number of Completed Win-Loss Analyses / Total Number of Sales Opportunities) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The percentage of closed deals that are followed by a win-loss analysis to understand the reasons behind the outcome.",
    "expected_business_insights": "Provides insights into the thoroughness and dedication of the sales team towards understanding the reasons behind wins and losses, which can drive strategic improvements.",
    "measurement_approach": "Considers the number of completed win-loss analyses compared to the total number of sales opportunities that could potentially be analyzed.",
    "trend_analysis": """
    * An increasing win-loss analysis completion rate may indicate a proactive approach to understanding customer needs and market dynamics.
    * A decreasing rate could signal complacency or a lack of emphasis on learning from lost deals.
    """,
    "diagnostic_questions": """
    * Are there specific sales teams or individuals with consistently high or low win-loss analysis completion rates?
    * What are the common reasons for not conducting a win-loss analysis after a deal is closed?
    """,
    "actionable_tips": """
    * Implement a standardized process for conducting win-loss analysis after every closed deal.
    * Provide training and resources to sales teams on how to effectively conduct and utilize win-loss analysis.
    * Create incentives for completing win-loss analysis, such as recognition or rewards for valuable insights gained.
    """,
    "visualization_suggestions": """
    * Stacked bar charts comparing win-loss analysis completion rates by sales team or individual.
    * Trend line graphs showing the change in completion rates over time.
    """,
    "risk_warnings": """
    * A low win-loss analysis completion rate may result in missed opportunities for learning and improvement.
    * Not conducting win-loss analysis can lead to a lack of understanding of customer needs and competitive positioning.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) systems with built-in win-loss analysis tracking capabilities.
    * Sales enablement platforms that facilitate and automate the win-loss analysis process.
    """,
    "integration_points": """
    * Integrate win-loss analysis completion data with sales performance metrics to identify correlations between analysis completion and sales success.
    * Link win-loss analysis insights with product development and marketing strategies to align offerings with customer needs and market demands.
    """,
    "change_impact_analysis": """
    * Improving the win-loss analysis completion rate can lead to a better understanding of customer preferences and needs, potentially increasing sales effectiveness.
    * However, an increased focus on win-loss analysis may require additional time and resources from sales teams, impacting their overall productivity.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Competitive Analysis", "Deal", "Enablement Feedback", "Enablement Platform", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
