"""
Deal Size Growth KPI

The change in average size or value of sales deals over time.
"""

DEAL_SIZE_GROWTH = {
    "code": "DEAL_SIZE_GROWTH",
    "name": "Deal Size Growth",
    "description": "The change in average size or value of sales deals over time.",
    "formula": "(Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size * 100",
    "calculation_formula": "(Current Period Average Deal Size - Previous Period Average Deal Size) / Previous Period Average Deal Size * 100",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The change in average size or value of sales deals over time.",
    "expected_business_insights": "Indicates the effectiveness of sales strategies and customer willingness to invest more in the company's offerings.",
    "measurement_approach": "Calculates the percentage change in the average size of deals over time.",
    "trend_analysis": """
    * Increasing deal size growth may indicate successful upselling or cross-selling strategies.
    * Decreasing deal size growth could signal increased competition or pricing pressure.
    """,
    "diagnostic_questions": """
    * What factors have contributed to the recent changes in deal size growth?
    * Are there specific customer segments or product lines driving the fluctuations in deal size?
    """,
    "actionable_tips": """
    * Implement targeted sales training to improve upselling and cross-selling techniques.
    * Conduct pricing analysis to ensure competitiveness without sacrificing profitability.
    """,
    "visualization_suggestions": """
    * Line charts showing deal size growth over time.
    * Comparison bar charts to visualize deal size growth by customer segment or product category.
    """,
    "risk_warnings": """
    * Significant fluctuations in deal size growth may impact revenue forecasts and financial planning.
    * Consistently declining deal size growth could indicate a need for strategic reevaluation of sales tactics.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and analyze customer purchasing patterns.
    * Business intelligence tools for in-depth sales performance analysis and trend identification.
    """,
    "integration_points": """
    * Integrate deal size growth data with sales pipeline management to align sales strategies with changing deal sizes.
    * Link deal size growth with customer feedback systems to understand the impact of sales strategies on customer satisfaction.
    """,
    "change_impact_analysis": """
    * Increasing deal size growth may lead to higher revenue and improved sales team motivation.
    * Decreasing deal size growth could impact sales team morale and require adjustments to sales targets and incentives.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Deal", "Deal", "Key Account", "Key Account Manager", "Lead", "Opportunity", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
