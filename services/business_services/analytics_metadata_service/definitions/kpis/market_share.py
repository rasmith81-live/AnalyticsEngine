"""
Market Share KPI

The percentage of market share held by the company within the key accounts.
"""

MARKET_SHARE = {
    "code": "MARKET_SHARE",
    "name": "Market Share",
    "description": "The percentage of market share held by the company within the key accounts.",
    "formula": "(Company's Sales Revenue / Total Market Sales Revenue) * 100",
    "calculation_formula": "(Company's Sales Revenue / Total Market Sales Revenue) * 100",
    "category": "Key Account Management",
    "is_active": True,
    "kpi_definition": "The percentage of market share held by the company within the key accounts.",
    "expected_business_insights": "Reveals the company's position and competitive strength within the industry.",
    "measurement_approach": "Compares a company's sales revenue to the total sales revenue of the competitive market.",
    "trend_analysis": """
    * Increasing market share within key accounts may indicate successful sales strategies and customer retention.
    * A decreasing market share could signal competitive pressures or dissatisfaction among key accounts.
    """,
    "diagnostic_questions": """
    * What factors have contributed to the recent changes in market share within key accounts?
    * How does our market share compare with competitors within the same key accounts?
    """,
    "actionable_tips": """
    * Regularly assess customer needs and preferences to tailor offerings and maintain market share.
    * Provide exceptional customer service and support to solidify relationships and prevent attrition.
    * Implement targeted marketing and promotional campaigns to increase brand visibility and appeal within key accounts.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of market share percentage over time.
    * Pie charts comparing the distribution of market share among different key accounts.
    """,
    "risk_warnings": """
    * Decreasing market share may lead to reduced revenue and profitability.
    * Loss of market share within key accounts can indicate vulnerability to competitive threats.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software to track and manage interactions with key accounts.
    * Market intelligence tools to gather insights on competitor activities and market trends.
    """,
    "integration_points": """
    * Integrate market share data with sales performance metrics to identify correlations and opportunities for improvement.
    * Link market share analysis with customer feedback systems to understand the impact of customer satisfaction on market share.
    """,
    "change_impact_analysis": """
    * Increasing market share can lead to higher revenue and potentially lower customer acquisition costs.
    * However, aggressive tactics to gain market share may impact profitability and long-term customer relationships.
    """,
    "metadata_": {"modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Channel Market", "Customer", "Key Account", "Key Account Manager", "Market Segment", "Renewal Management", "Sale"]},
    "modules": ["KEY_ACCOUNT_MANAGEMENT", "SALES_DEVELOPMENT", "SALES_PERFORMANCE", "SALES_STRATEGY"],
    "module_code": "KEY_ACCOUNT_MANAGEMENT",
}
