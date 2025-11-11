"""
Rep Attrition Rate KPI

The rate at which sales representatives leave the company.
"""

REP_ATTRITION_RATE = {
    "code": "REP_ATTRITION_RATE",
    "name": "Rep Attrition Rate",
    "description": "The rate at which sales representatives leave the company.",
    "formula": "(Number of Sales Reps Who Left / Average Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Who Left / Average Number of Sales Reps) * 100",
    "category": "Sales Operations",
    "is_active": True,
    "kpi_definition": "The rate at which sales representatives leave the company.",
    "expected_business_insights": "Shows the stability and satisfaction within the sales team, important for maintaining relationships and knowledge.",
    "measurement_approach": "Tracks the turnover rate of sales representatives.",
    "trend_analysis": """
    * A rising rep attrition rate may indicate dissatisfaction with compensation, work environment, or management.
    * A decreasing rate could signal improved employee engagement, better training, or more effective leadership.
    """,
    "diagnostic_questions": """
    * Are there common reasons cited by departing sales representatives?
    * How does our rep attrition rate compare with industry benchmarks or turnover rates in similar roles?
    """,
    "actionable_tips": """
    * Conduct exit interviews to understand the reasons for leaving and address any recurring issues.
    * Invest in ongoing training and development programs to enhance job satisfaction and career growth opportunities for sales representatives.
    * Regularly review and adjust compensation and benefits packages to remain competitive in the market.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend in rep attrition rate over time.
    * Pie charts to compare reasons for leaving among sales representatives.
    """,
    "risk_warnings": """
    * High rep attrition rates can lead to loss of sales productivity and revenue.
    * Frequent turnover may indicate underlying issues with company culture, management, or job satisfaction.
    """,
    "tracking_tools": """
    * Employee engagement and feedback platforms like Culture Amp or Officevibe to gather insights and feedback from the sales team.
    * Human resource management systems to track turnover rates and identify patterns or trends.
    """,
    "integration_points": """
    * Integrate rep attrition rate data with performance reviews and feedback systems to identify potential issues early on.
    * Link with recruitment and onboarding processes to streamline the hiring and training of new sales representatives.
    """,
    "change_impact_analysis": """
    * Reducing rep attrition can lead to a more stable and productive sales team, positively impacting overall sales performance and customer relationships.
    * However, addressing high attrition rates may require investment in training, benefits, and employee support programs, impacting operational costs.
    """,
    "metadata_": {"modules": ["SALES_OPERATIONS"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_OPERATIONS"],
    "module_code": "SALES_OPERATIONS",
}
