"""
Sales Productivity KPI

The effectiveness of the sales team in generating revenue relative to their cost.
"""

SALES_PRODUCTIVITY = {
    "code": "SALES_PRODUCTIVITY",
    "name": "Sales Productivity",
    "description": "The effectiveness of the sales team in generating revenue relative to their cost.",
    "formula": "Total Revenue / Number of Sales Reps or Efforts",
    "calculation_formula": "Total Revenue / Number of Sales Reps or Efforts",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The effectiveness of the sales team in generating revenue relative to their cost.",
    "expected_business_insights": "Identifies the effectiveness of individual sales representatives and overall team performance.",
    "measurement_approach": "Revenue generated per sales representative or per sales effort.",
    "trend_analysis": """
    * Increasing sales productivity may indicate improved sales processes, better lead generation, or more effective sales training.
    * Decreasing productivity could signal issues with sales team motivation, market saturation, or ineffective sales strategies.
    """,
    "diagnostic_questions": """
    * What are the main factors contributing to the current level of sales productivity?
    * Are there specific sales territories, products, or customer segments that are underperforming in terms of productivity?
    """,
    "actionable_tips": """
    * Invest in sales training and coaching to improve the effectiveness of the sales team.
    * Implement or optimize sales automation tools to streamline processes and free up more time for actual selling activities.
    * Regularly review and update the sales compensation structure to ensure it incentivizes high productivity.
    """,
    "visualization_suggestions": """
    * Line charts showing sales productivity over time, segmented by individual sales reps or sales teams.
    * Pareto charts to identify the most and least productive sales activities or products.
    """,
    "risk_warnings": """
    * Low sales productivity can lead to missed revenue targets and decreased profitability.
    * High sales productivity without proper quality control can result in increased customer complaints and returns.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track sales activities and customer interactions.
    * Sales performance management tools to monitor and analyze individual and team productivity metrics.
    """,
    "integration_points": """
    * Integrate sales productivity data with marketing analytics to understand the impact of marketing efforts on sales outcomes.
    * Link sales productivity with customer satisfaction metrics to assess the overall impact of sales efforts on customer experience.
    """,
    "change_impact_analysis": """
    * Increasing sales productivity may lead to higher revenue and improved profitability, but it could also strain resources if not managed effectively.
    * Decreasing sales productivity can result in missed sales opportunities and decreased market share, impacting long-term business growth.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"],
    "module_code": "INSIDE_SALES",
}
