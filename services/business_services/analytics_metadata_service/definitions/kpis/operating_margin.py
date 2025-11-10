"""
Operating Margin KPI

A measure of what portion of a company's revenue is left over after paying for variable costs of production like wages and raw materials.
"""

OPERATING_MARGIN = {
    "code": "OPERATING_MARGIN",
    "name": "Operating Margin",
    "description": "A measure of what portion of a company's revenue is left over after paying for variable costs of production like wages and raw materials.",
    "formula": "Operating Income / Net Sales",
    "calculation_formula": "Operating Income / Net Sales",
    "category": "Sales Performance",
    "is_active": True,
    "kpi_definition": "A measure of what portion of a company's revenue is left over after paying for variable costs of production like wages and raw materials.",
    "expected_business_insights": "Highlights profitability after covering operating expenses, useful for operational efficiency analysis.",
    "measurement_approach": "Compares operating income to net sales.",
    "trend_analysis": """
    * Operating margin tends to increase when there is efficient cost management and pricing strategies.
    * A declining trend may indicate rising production costs or pricing pressures in the market.
    """,
    "diagnostic_questions": """
    * What are the main cost drivers impacting our operating margin?
    * How does our operating margin compare to industry benchmarks or competitors?
    """,
    "actionable_tips": """
    * Implement cost-saving measures such as lean production or renegotiating supplier contracts.
    * Regularly review pricing strategies to ensure they align with cost structures and market conditions.
    * Invest in technologies that can automate processes and reduce variable costs.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of operating margin over time.
    * Stacked bar charts comparing operating margin by product lines or business segments.
    """,
    "risk_warnings": """
    * A declining operating margin may lead to reduced profitability and financial instability.
    * High operating margins without corresponding investment in growth initiatives may limit long-term business expansion.
    """,
    "tracking_tools": """
    * Financial management software like QuickBooks or SAP for accurate tracking and analysis of cost and revenue data.
    * Business intelligence tools to identify cost-saving opportunities and optimize pricing strategies.
    """,
    "integration_points": """
    * Integrate operating margin analysis with budgeting and forecasting systems to align financial goals with operational performance.
    * Link with sales and marketing systems to understand the impact of pricing and promotions on operating margin.
    """,
    "change_impact_analysis": """
    * Improving operating margin can lead to increased profitability but may require changes in cost structures and pricing strategies.
    * Conversely, a declining operating margin can affect investment capacity and shareholder confidence.
    """,
    "metadata_": {"modules": ["SALES_PERFORMANCE"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_PERFORMANCE"],
    "module_code": "SALES_PERFORMANCE",
}
