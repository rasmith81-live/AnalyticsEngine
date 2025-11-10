"""
Negotiation-to-Close Ratio KPI

The ratio comparing the number of negotiations to the successfully closed deals.
"""

NEGOTIATION_TO_CLOSE_RATIO = {
    "code": "NEGOTIATION_TO_CLOSE_RATIO",
    "name": "Negotiation-to-Close Ratio",
    "description": "The ratio comparing the number of negotiations to the successfully closed deals.",
    "formula": "Number of Deals Closed / Number of Negotiations Conducted * 100",
    "calculation_formula": "Number of Deals Closed / Number of Negotiations Conducted * 100",
    "category": "Outside Sales",
    "is_active": True,
    "kpi_definition": "The ratio comparing the number of negotiations to the successfully closed deals.",
    "expected_business_insights": "Reveals the effectiveness and efficiency of the negotiation process and the sales team’s ability to close deals.",
    "measurement_approach": "Compares the number of negotiations conducted to the number of deals closed.",
    "trend_analysis": """
    * An increasing negotiation-to-close ratio may indicate improved sales tactics or a stronger market position.
    * A decreasing ratio could signal challenges in closing deals or increased competition.
    """,
    "diagnostic_questions": """
    * Are there specific products or services that consistently have a higher negotiation-to-close ratio?
    * How does our negotiation-to-close ratio compare with industry benchmarks or with our competitors?
    """,
    "actionable_tips": """
    * Provide additional negotiation training and resources for sales representatives.
    * Regularly review and adjust pricing strategies to ensure competitiveness.
    * Implement customer relationship management (CRM) systems to track and manage negotiations more effectively.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of negotiation-to-close ratio over time.
    * Scatter plots to identify any correlation between negotiation-to-close ratio and sales volume.
    """,
    "risk_warnings": """
    * A consistently low negotiation-to-close ratio may lead to missed revenue opportunities.
    * A high ratio could indicate a lack of negotiation skills or ineffective sales strategies.
    """,
    "tracking_tools": """
    * CRM software with negotiation tracking capabilities, such as Salesforce or HubSpot.
    * Sales performance analytics tools to identify patterns and opportunities for improvement, like Tableau or Power BI.
    """,
    "integration_points": """
    * Integrate negotiation-to-close ratio data with sales forecasting systems to better predict future performance.
    * Link with customer relationship management platforms to understand the impact of negotiations on customer satisfaction and retention.
    """,
    "change_impact_analysis": """
    * Improving the negotiation-to-close ratio can lead to increased revenue and customer satisfaction.
    * However, overly aggressive negotiation tactics may negatively impact customer relationships and long-term loyalty.
    """,
    "metadata_": {"modules": ["OUTSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Opportunity", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["OUTSIDE_SALES"],
    "module_code": "OUTSIDE_SALES",
}
