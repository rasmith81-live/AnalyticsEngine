"""
Sales Efficiency KPI

The ratio of revenue generated to the cost of sales and marketing efforts.
"""

SALES_EFFICIENCY = {
    "code": "SALES_EFFICIENCY",
    "name": "Sales Efficiency",
    "description": "The ratio of revenue generated to the cost of sales and marketing efforts.",
    "formula": "Revenue Generated / Cost of Sales Activities",
    "calculation_formula": "Revenue Generated / Cost of Sales Activities",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The ratio of revenue generated to the cost of sales and marketing efforts.",
    "expected_business_insights": "Provides insights into the profitability and cost-effectiveness of the sales organization.",
    "measurement_approach": "Compares the revenue generated to the cost of sales-related activities.",
    "trend_analysis": """
    * Increasing sales efficiency may indicate improved targeting and effectiveness of sales and marketing efforts.
    * Decreasing sales efficiency could signal increased competition, market saturation, or inefficiencies in the sales process.
    """,
    "diagnostic_questions": """
    * What specific sales and marketing activities contribute most to revenue generation?
    * Are there any market or competitive factors impacting the cost-effectiveness of our sales efforts?
    """,
    "actionable_tips": """
    * Regularly review and optimize sales and marketing strategies to ensure maximum impact for the cost incurred.
    * Invest in training and development for sales teams to improve their effectiveness and efficiency.
    * Utilize customer relationship management (CRM) software to better track and manage sales activities and customer interactions.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of sales efficiency over time.
    * Pie charts comparing the proportion of revenue generated to the cost of different sales and marketing activities.
    """,
    "risk_warnings": """
    * Declining sales efficiency may lead to reduced profitability and financial performance.
    * High sales efficiency without corresponding revenue growth may indicate missed opportunities for investment and expansion.
    """,
    "tracking_tools": """
    * Sales analytics platforms like Tableau or Power BI to track and analyze sales efficiency metrics.
    * Marketing automation tools to streamline and optimize marketing efforts for better cost-effectiveness.
    """,
    "integration_points": """
    * Integrate sales efficiency data with financial reporting systems to understand its impact on overall profitability.
    * Link sales efficiency with customer relationship management (CRM) systems to identify the most cost-effective customer acquisition channels.
    """,
    "change_impact_analysis": """
    * Improving sales efficiency can lead to increased profitability and better resource allocation.
    * However, a singular focus on sales efficiency may neglect the quality of customer interactions and long-term customer relationships.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
}
