"""
Year-over-Year (YoY) Sales Growth KPI

The increase in sales revenue compared to the same period in the previous year.
"""

YEAR_OVER_YEAR_YOY_SALES_GROWTH = {
    "code": "YEAR_OVER_YEAR_YOY_SALES_GROWTH",
    "name": "Year-over-Year (YoY) Sales Growth",
    "description": "The increase in sales revenue compared to the same period in the previous year.",
    "formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "calculation_formula": "((Current Year Sales - Previous Year Sales) / Previous Year Sales) * 100",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "The increase in sales revenue compared to the same period in the previous year.",
    "expected_business_insights": "Shows business growth and can indicate the effectiveness of current sales strategies and market conditions.",
    "measurement_approach": "The growth rate of sales compared to the previous year.",
    "trend_analysis": """
    * Year-over-year sales growth tends to show seasonal fluctuations, with certain periods of the year consistently outperforming others.
    * A consistent upward trend in year-over-year sales growth may indicate successful product launches, market expansion, or improved sales strategies.
    """,
    "diagnostic_questions": """
    * What factors contributed to the increase or decrease in year-over-year sales growth during specific periods?
    * How does the year-over-year sales growth compare to industry averages and competitors' performance?
    """,
    "actionable_tips": """
    * Invest in targeted marketing campaigns to capitalize on peak sales periods and drive year-over-year growth.
    * Regularly assess and adjust pricing strategies to maximize revenue and stimulate sales growth.
    * Provide sales teams with ongoing training and support to enhance their ability to close deals and drive revenue growth.
    """,
    "visualization_suggestions": """
    * Line charts showing year-over-year sales growth by month or quarter to visualize seasonal trends.
    * Comparative bar charts to highlight year-over-year growth rates for different product categories or customer segments.
    """,
    "risk_warnings": """
    * A decline in year-over-year sales growth may indicate market saturation, increased competition, or shifts in customer preferences.
    * Rapid growth in year-over-year sales may strain operational capacity, leading to fulfillment and customer service challenges.
    """,
    "tracking_tools": """
    * Customer Relationship Management (CRM) software to track and analyze sales performance and customer behavior.
    * Business Intelligence (BI) tools to identify patterns and correlations that contribute to year-over-year sales growth.
    """,
    "integration_points": """
    * Integrate year-over-year sales growth data with marketing analytics to evaluate the effectiveness of promotional efforts.
    * Link sales growth metrics with inventory management systems to ensure adequate stock levels to support increased demand.
    """,
    "change_impact_analysis": """
    * Improving year-over-year sales growth can lead to increased profitability and market share, but may require additional resources and investments.
    * A decline in year-over-year sales growth can impact cash flow, profitability, and overall business performance.
    """,
    "metadata_": {"modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_STRATEGY"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"], "replaces": ["YEAR_OVER_YEAR_GROWTH"]},
    "modules": ["INSIDE_SALES", "OUTSIDE_SALES", "SALES_STRATEGY"],
    "module_code": "INSIDE_SALES",
}
