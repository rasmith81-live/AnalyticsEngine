"""
Profit Margin KPI

The percentage of revenue that turns into profit after accounting for all expenses, taxes, and interest.
"""

PROFIT_MARGIN = {
    "code": "PROFIT_MARGIN",
    "name": "Profit Margin",
    "description": "The percentage of revenue that turns into profit after accounting for all expenses, taxes, and interest.",
    "formula": "Net Income / Revenue",
    "calculation_formula": "Net Income / Revenue",
    "category": "Sales Performance",
    "is_active": True,
    "kpi_definition": "The percentage of revenue that turns into profit after accounting for all expenses, taxes, and interest.",
    "expected_business_insights": "Reveals the percentage of revenue that translates into profit, critical for overall financial health assessment.",
    "measurement_approach": "Takes into account net income divided by revenue.",
    "trend_analysis": """
    * Increasing profit margin over time may indicate improved cost management or pricing strategies.
    * A decreasing margin could signal rising expenses, pricing pressure, or declining sales.
    """,
    "diagnostic_questions": """
    * What are the main cost drivers that impact our profit margin?
    * How does our profit margin compare to industry benchmarks or competitors?
    """,
    "actionable_tips": """
    * Regularly review and optimize pricing strategies to maintain healthy margins.
    * Focus on cost control measures such as reducing waste, improving operational efficiency, or renegotiating supplier contracts.
    * Explore opportunities for upselling or cross-selling to increase revenue without significantly impacting costs.
    """,
    "visualization_suggestions": """
    * Line charts showing profit margin trends over time.
    * Pareto charts to identify the most significant cost drivers impacting margin.
    """,
    "risk_warnings": """
    * Declining profit margins can lead to financial instability and reduced investment capacity.
    * Excessively high margins may indicate pricing strategies that could alienate customers or attract regulatory scrutiny.
    """,
    "tracking_tools": """
    * Financial management software like QuickBooks or Xero for detailed expense tracking and analysis.
    * Business intelligence tools to identify patterns and correlations between expenses, revenue, and profit margin.
    """,
    "integration_points": """
    * Integrate profit margin analysis with sales and marketing systems to understand the impact of pricing and promotions on profitability.
    * Link with supply chain and procurement systems to optimize costs and reduce expenses.
    """,
    "change_impact_analysis": """
    * Improving profit margin can lead to increased financial stability and investment opportunities.
    * However, aggressive margin improvement may impact customer loyalty and brand perception if not managed carefully.
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Key Account", "Key Account Manager", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
}
