"""
Territory Penetration Rate KPI

The rate at which the outside sales team is able to penetrate or cover the allocated sales territory.
"""

TERRITORY_PENETRATION_RATE = {
    "code": "TERRITORY_PENETRATION_RATE",
    "name": "Territory Penetration Rate",
    "description": "The rate at which the outside sales team is able to penetrate or cover the allocated sales territory.",
    "formula": "(Number of Customers in Territory / Total Market Potential in Territory) * 100",
    "calculation_formula": "(Number of Customers in Territory / Total Market Potential in Territory) * 100",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The rate at which the outside sales team is able to penetrate or cover the allocated sales territory.",
    "expected_business_insights": "Reveals the effectiveness of sales strategies in capturing market share within a designated sales area.",
    "measurement_approach": "Accounts for the number of customers engaged within a specific sales territory compared to the total identified market potential.",
    "trend_analysis": """
    * Increasing territory penetration rate may indicate successful expansion into new markets or improved sales strategies.
    * Decreasing rate could signal increased competition or ineffective territory management.
    """,
    "diagnostic_questions": """
    * Are there specific regions within the territory that are consistently underperforming?
    * How does our territory penetration rate compare with industry benchmarks or with previous performance?
    """,
    "actionable_tips": """
    * Provide additional training and resources to the sales team to better understand and address the needs of different regions within the territory.
    * Regularly review and adjust territory boundaries based on market changes and sales performance.
    * Implement a customer relationship management (CRM) system to track and manage sales activities within the territory.
    """,
    "visualization_suggestions": """
    * Heat maps to visually represent the coverage and performance within the sales territory.
    * Line charts showing the territory penetration rate over time to identify trends and patterns.
    """,
    "risk_warnings": """
    * Low territory penetration rate may result in missed sales opportunities and reduced market share.
    * High turnover or dissatisfaction among the sales team can negatively impact territory coverage and penetration.
    """,
    "tracking_tools": """
    * Geographic information system (GIS) software to analyze and visualize territory data.
    * CRM platforms with territory management features to track and optimize sales activities within the territory.
    """,
    "integration_points": """
    * Integrate territory penetration rate with sales performance metrics to understand the relationship between coverage and actual sales results.
    * Link territory data with marketing and lead generation systems to align sales efforts with potential opportunities.
    """,
    "change_impact_analysis": """
    * Improving territory penetration rate can lead to increased sales and market share, but may require additional resources and investment in sales activities.
    * Conversely, a declining territory penetration rate can impact overall revenue and market presence, affecting the organization's growth and competitiveness.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account Penetration", "Channel Market", "Customer", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Territory Assignment"]},
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
}
