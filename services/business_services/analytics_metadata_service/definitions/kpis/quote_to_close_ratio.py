"""
Quote to Close Ratio KPI

The percentage of quotes given to prospects that result in closed sales.
"""

QUOTE_TO_CLOSE_RATIO = {
    "code": "QUOTE_TO_CLOSE_RATIO",
    "name": "Quote to Close Ratio",
    "description": "The percentage of quotes given to prospects that result in closed sales.",
    "formula": "(Number of Closed Sales / Number of Quotes Given) * 100",
    "calculation_formula": "(Number of Closed Sales / Number of Quotes Given) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The percentage of quotes given to prospects that result in closed sales.",
    "expected_business_insights": "Indicates the effectiveness of pricing strategies and the proposal process.",
    "measurement_approach": "The percentage of quotes that result in closed sales.",
    "trend_analysis": """
    * An increasing quote to close ratio may indicate improved sales effectiveness or a stronger market demand for the product or service.
    * A decreasing ratio could signal issues in the sales process, pricing, or product competitiveness.
    """,
    "diagnostic_questions": """
    * Are there specific sales representatives or teams with consistently higher or lower quote to close ratios?
    * How does our quote to close ratio compare with industry benchmarks or with different customer segments?
    """,
    "actionable_tips": """
    * Provide sales training and coaching to improve sales techniques and negotiation skills.
    * Review pricing strategies and product positioning to ensure competitiveness in the market.
    * Implement a lead scoring system to prioritize high-quality leads and improve conversion rates.
    """,
    "visualization_suggestions": """
    * Line charts showing the quote to close ratio over time to identify trends and seasonality.
    * Pie charts comparing quote to close ratios for different sales teams or product categories.
    """,
    "risk_warnings": """
    * A consistently low quote to close ratio can lead to missed revenue opportunities and decreased sales performance.
    * An excessively high ratio may indicate underpricing or missed opportunities for upselling or cross-selling.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track and analyze the entire sales process from lead generation to closing.
    * Sales performance analytics tools to identify areas for improvement and track the impact of sales initiatives.
    """,
    "integration_points": """
    * Integrate quote to close ratio data with marketing analytics to understand the quality of leads generated and the effectiveness of marketing campaigns.
    * Link with customer feedback systems to understand how the sales process impacts customer satisfaction and retention.
    """,
    "change_impact_analysis": """
    * Improving the quote to close ratio can lead to increased revenue and better sales team morale, but may also require investment in training and resources.
    * A declining ratio can impact overall sales performance, revenue targets, and the organization's competitive position in the market.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Deal", "Opportunity", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES", "KEY_ACCOUNT_MANAGEMENT", "OUTSIDE_SALES", "SALES_DEVELOPMENT", "SALES_OPERATIONS", "SALES_PERFORMANCE", "SALES_STRATEGY"],
    "module_code": "INSIDE_SALES",
}
