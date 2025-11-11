"""
Win/Loss Ratio KPI

The ratio of won sales to lost opportunities, helping to assess the competitiveness and effectiveness of the sales process.
"""

WINLOSS_RATIO = {
    "code": "WINLOSS_RATIO",
    "name": "Win/Loss Ratio",
    "description": "The ratio of won sales to lost opportunities, helping to assess the competitiveness and effectiveness of the sales process.",
    "formula": "Number of Sales Won / Number of Sales Lost",
    "calculation_formula": "Number of Sales Won / Number of Sales Lost",
    "category": "Sales Performance",
    "is_active": True,
    "kpi_definition": "The ratio of won sales to lost opportunities, helping to assess the competitiveness and effectiveness of the sales process.",
    "expected_business_insights": "Reflects the effectiveness of the sales process and competitive positioning.",
    "measurement_approach": "Compares the number of sales won to the number of sales lost.",
    "trend_analysis": """
    * An increasing win-loss ratio may indicate improved sales strategies or a stronger market position.
    * A decreasing ratio could signal increased competition or inefficiencies in the sales process.
    """,
    "diagnostic_questions": """
    * Are there specific sales tactics or approaches that have contributed to recent wins or losses?
    * How does our win-loss ratio compare with industry benchmarks or with our competitors?
    """,
    "actionable_tips": """
    * Provide additional sales training and resources to improve the effectiveness of the sales team.
    * Regularly review and update the sales process to adapt to changing market conditions and customer needs.
    * Implement a robust customer relationship management (CRM) system to better track and manage sales opportunities.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of win-loss ratio over time.
    * Stacked bar charts comparing win and loss percentages across different sales teams or regions.
    """,
    "risk_warnings": """
    * A consistently low win-loss ratio may indicate a need for significant changes in sales strategies or team composition.
    * High fluctuations in the win-loss ratio could point to instability in the sales process or market conditions.
    """,
    "tracking_tools": """
    * CRM software such as Salesforce or HubSpot for tracking and managing sales opportunities.
    * Sales performance analytics tools like InsightSquared or Clari for deeper insights into win-loss patterns.
    """,
    "integration_points": """
    * Integrate win-loss ratio data with sales forecasting systems to better predict future performance and resource needs.
    * Link with customer feedback platforms to understand the impact of wins and losses on overall customer satisfaction.
    """,
    "change_impact_analysis": """
    * An improved win-loss ratio can lead to increased revenue and market share, but may also require adjustments in sales strategies and resource allocation.
    * Conversely, a declining ratio may lead to decreased confidence from stakeholders and potential shifts in investment priorities.
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Lost Sale", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
}
