"""
Sales by Region KPI

The amount of sales generated in each geographic region.
"""

SALES_BY_REGION = {
    "code": "SALES_BY_REGION",
    "name": "Sales by Region",
    "description": "The amount of sales generated in each geographic region.",
    "formula": "Revenue attributed to each region",
    "calculation_formula": "Revenue attributed to each region",
    "category": "Sales Operations",
    "is_active": True,
    "kpi_definition": "The amount of sales generated in each geographic region.",
    "expected_business_insights": "Indicates regional market performance and potential for expansion.",
    "measurement_approach": "Measures revenue generated in different geographical regions.",
    "trend_analysis": """
    * Sales in certain regions may show consistent growth, indicating potential market opportunities.
    * Declining sales in a specific region could signal changing customer preferences or increased competition.
    """,
    "diagnostic_questions": """
    * Are there specific products or services that perform better in certain regions?
    * How do regional economic conditions or cultural factors impact sales performance?
    """,
    "actionable_tips": """
    * Customize marketing and sales strategies to better align with regional preferences and needs.
    * Invest in market research to understand regional dynamics and tailor offerings accordingly.
    * Empower regional sales teams with the autonomy to adapt tactics to local market conditions.
    """,
    "visualization_suggestions": """
    * Map visualizations to show sales distribution across different regions.
    * Line charts to track sales trends in each region over time.
    """,
    "risk_warnings": """
    * Over-reliance on a single region for sales may expose the business to significant risk in case of economic downturns or other disruptions.
    * Ignoring regional sales performance may lead to missed opportunities for growth and expansion.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) systems to track regional sales activities and customer interactions.
    * Geospatial analytics tools to analyze demographic and economic data for targeted regional strategies.
    """,
    "integration_points": """
    * Integrate regional sales data with inventory management systems to ensure adequate stock levels in high-demand areas.
    * Link regional sales performance with financial reporting to assess overall business profitability by region.
    """,
    "change_impact_analysis": """
    * Improving sales in certain regions may lead to increased revenue and market share, but could also require additional resources for expansion.
    * Declining sales in key regions may impact overall business performance and require strategic shifts in resource allocation.
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["SALES_BY_REGIONAREA"]},
    "modules": ["SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE"],
    "module_code": "SALES_DEVELOPMENT",
}
