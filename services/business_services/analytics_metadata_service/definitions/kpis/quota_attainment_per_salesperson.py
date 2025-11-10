"""
Quota Attainment per Salesperson KPI

The percentage of the sales quota each salesperson has achieved, indicating individual performance and effectiveness.
"""

QUOTA_ATTAINMENT_PER_SALESPERSON = {
    "code": "QUOTA_ATTAINMENT_PER_SALESPERSON",
    "name": "Quota Attainment per Salesperson",
    "description": "The percentage of the sales quota each salesperson has achieved, indicating individual performance and effectiveness.",
    "formula": "(Total Sales by Salesperson / Sales Quota for Salesperson) * 100",
    "calculation_formula": "(Total Sales by Salesperson / Sales Quota for Salesperson) * 100",
    "category": "Sales Performance",
    "is_active": True,
    "kpi_definition": "The percentage of the sales quota each salesperson has achieved, indicating individual performance and effectiveness.",
    "expected_business_insights": "Indicates individual sales performance and effectiveness of sales targets.",
    "measurement_approach": "Measures the percentage of sales quota achieved by each salesperson.",
    "trend_analysis": """
    * Consistently increasing quota attainment may indicate a need to raise sales targets or a highly motivated sales team.
    * A decreasing trend could signal issues with sales strategy, market conditions, or individual performance.
    """,
    "diagnostic_questions": """
    * Are there specific products or regions where salespeople consistently struggle to meet their quotas?
    * How does the quota attainment of new hires compare to more experienced salespeople?
    """,
    "actionable_tips": """
    * Provide additional training and support for salespeople who consistently fall short of their quotas.
    * Regularly review and adjust quotas to ensure they are challenging but achievable based on market conditions.
    * Recognize and reward top performers to motivate the entire sales team.
    """,
    "visualization_suggestions": """
    * Line charts showing individual salesperson quota attainment over time.
    * Bar graphs comparing quota attainment across different sales territories or product lines.
    """,
    "risk_warnings": """
    * Consistently low quota attainment may lead to high turnover and demotivation among the sales team.
    * High quota attainment without proper support or resources may lead to burnout and decreased job satisfaction.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track individual sales performance and quota attainment.
    * Sales performance management platforms to set, track, and analyze sales quotas and performance.
    """,
    "integration_points": """
    * Integrate quota attainment data with compensation and incentive systems to align rewards with performance.
    * Link quota attainment with sales forecasting to adjust targets based on predicted market conditions.
    """,
    "change_impact_analysis": """
    * Improving quota attainment can lead to increased revenue and market share, but may also require additional resources and support.
    * Low quota attainment can impact overall sales team morale and the organization's ability to meet financial targets.
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Quota Plan", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
}
