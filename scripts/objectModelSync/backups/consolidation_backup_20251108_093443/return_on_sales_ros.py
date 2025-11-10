"""
Return on Sales (ROS) KPI

A measure of the company's operational efficiency calculated as the ratio of operating profit to net sales.
"""

from analytics_models import KPI

RETURN_ON_SALES_ROS = KPI(
    name="Return on Sales (ROS)",
    code="RETURN_ON_SALES_ROS",
    category="Inside Sales",
    
    # Core Definition
    description="A measure of the company\'s operational efficiency calculated as the ratio of operating profit to net sales.",
    kpi_definition="A measure of the company\'s operational efficiency calculated as the ratio of operating profit to net sales.",
    expected_business_insights="Provides insight into the profitability of sales, assessing how much profit is generated from sales revenue.",
    measurement_approach="Net profit as a percentage of sales revenue.",
    
    # Formula
    formula="Net Profit / Sales Revenue",
    calculation_formula="Net Profit / Sales Revenue",
    
    # Analysis
    trend_analysis="""
    * A rising return on sales may indicate improved operational efficiency or increased demand for the company\'s products/services.
    * A decreasing return on sales could signal declining profitability or challenges in maintaining sales levels.
    """,
    diagnostic_questions="""
    * What specific operational changes have contributed to the trend in return on sales?
    * How does the return on sales compare with industry benchmarks or competitors\' performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement cost-saving measures to improve operating profit margins.
    * Focus on sales strategies that target higher-margin products or services.
    * Invest in technology and process improvements to streamline operations and reduce costs.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of return on sales over time.
    * Comparative bar charts displaying return on sales for different product lines or business segments.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * A declining return on sales may indicate potential financial challenges or inefficiencies in the company\'s operations.
    * High return on sales without corresponding growth in net sales could signal pricing or market saturation issues.
    """,
    tracking_tools="""
    * Financial analysis software to track and analyze return on sales data.
    * Enterprise resource planning (ERP) systems to integrate sales and financial data for comprehensive analysis.
    """,
    integration_points="""
    * Integrate return on sales analysis with sales forecasting and budgeting processes for more accurate financial planning.
    * Link return on sales with customer relationship management (CRM) systems to understand the impact of sales activities on profitability.
    """,
    change_impact_analysis="""
    * Improving return on sales can lead to increased profitability and financial stability for the company.
    * Conversely, a declining return on sales may require cost-cutting measures that could impact employee morale and operational capabilities.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
