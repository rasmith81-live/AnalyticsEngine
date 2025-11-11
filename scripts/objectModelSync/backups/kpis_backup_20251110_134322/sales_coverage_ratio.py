"""
Sales Coverage Ratio KPI

The ratio of sales representatives to the potential market or number of accounts, indicating potential market reach.
"""

SALES_COVERAGE_RATIO = {
    "code": "SALES_COVERAGE_RATIO",
    "name": "Sales Coverage Ratio",
    "description": "The ratio of sales representatives to the potential market or number of accounts, indicating potential market reach.",
    "formula": "Number of Sales Representatives / Number of Accounts or Sales Territories",
    "calculation_formula": "Number of Sales Representatives / Number of Accounts or Sales Territories",
    "category": "Sales Development",
    "is_active": True,
    "kpi_definition": "The ratio of sales representatives to the potential market or number of accounts, indicating potential market reach.",
    "expected_business_insights": "Indicates the adequacy of sales force size and informs staffing decisions.",
    "measurement_approach": "Compares the number of sales representatives to the number of potential sales or accounts.",
    "trend_analysis": """
    * An increasing sales coverage ratio may indicate a growing sales team or expansion into new markets.
    * A decreasing ratio could signal a need for more sales representatives to effectively cover the potential market.
    """,
    "diagnostic_questions": """
    * How does the current sales coverage ratio align with our sales strategy and target market segments?
    * Are there specific regions or customer segments that are underrepresented in our current sales coverage?
    """,
    "actionable_tips": """
    * Regularly assess and adjust the sales coverage ratio based on changes in the potential market and customer demand.
    * Invest in sales training and development to ensure existing representatives can effectively cover the potential market.
    * Utilize sales territory mapping and optimization tools to maximize the efficiency of sales coverage.
    """,
    "visualization_suggestions": """
    * Map visualizations showing the geographical distribution of sales representatives compared to the potential market.
    * Line charts tracking the sales coverage ratio over time to identify any significant shifts or trends.
    """,
    "risk_warnings": """
    * A low sales coverage ratio may result in missed opportunities and decreased market penetration.
    * An excessively high ratio could lead to inefficiencies and decreased effectiveness of individual sales representatives.
    """,
    "tracking_tools": """
    * Customer relationship management (CRM) software with territory management features to optimize sales coverage.
    * Geospatial analytics tools to visualize and analyze the distribution of potential customers relative to sales representatives.
    """,
    "integration_points": """
    * Integrate sales coverage data with customer relationship management systems to align sales efforts with customer needs and preferences.
    * Link sales coverage metrics with sales performance data to assess the impact of coverage on actual sales results.
    """,
    "change_impact_analysis": """
    * Increasing the sales coverage ratio may lead to higher customer acquisition but could also require additional resources and support.
    * Decreasing the ratio may reduce costs but could limit the organization's ability to reach new customers and expand market share.
    """,
    "metadata_": {"modules": ["SALES_DEVELOPMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Channel Market", "Market Segment", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_DEVELOPMENT"],
    "module_code": "SALES_DEVELOPMENT",
}
