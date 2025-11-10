"""
Sales Growth Year-to-Date (YTD) KPI

The increase in sales revenue from the beginning of the current fiscal year up to the present date, compared against the same period in the prior year.
"""

from analytics_models import KPI

SALES_GROWTH_YEAR_TO_DATE_YTD = KPI(
    name="Sales Growth Year-to-Date (YTD)",
    code="SALES_GROWTH_YEAR_TO_DATE_YTD",
    category="Sales Performance",
    
    # Core Definition
    description="The increase in sales revenue from the beginning of the current fiscal year up to the present date, compared against the same period in the prior year.",
    kpi_definition="The increase in sales revenue from the beginning of the current fiscal year up to the present date, compared against the same period in the prior year.",
    expected_business_insights="Provides a snapshot of sales performance and trends within the current year.",
    measurement_approach="Measures the cumulative sales revenue growth since the beginning of the year.",
    
    # Formula
    formula="(Current YTD Sales - Previous YTD Sales) / Previous YTD Sales",
    calculation_formula="(Current YTD Sales - Previous YTD Sales) / Previous YTD Sales",
    
    # Analysis
    trend_analysis="""
    * Sales growth tends to follow seasonal patterns, with higher performance during certain times of the year.
    * Changes in market conditions, such as new competitors or economic downturns, can significantly impact sales growth.
    """,
    diagnostic_questions="""
    * What factors have historically driven sales growth during certain periods?
    * How does our sales growth compare to industry averages and benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in targeted marketing and promotional campaigns during peak sales periods.
    * Regularly analyze and adjust pricing strategies to maximize revenue.
    * Explore new sales channels or geographic markets to expand customer reach.
    """,
    visualization_suggestions="""
    * Line charts showing year-over-year sales growth by month or quarter.
    * Comparative bar graphs illustrating sales growth performance against industry averages.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on a small number of key clients or products can make sales growth vulnerable to sudden changes.
    * Rapid sales growth may strain operational capacity and lead to service or quality issues.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage customer interactions and sales opportunities.
    * Business intelligence and analytics tools to identify sales trends and opportunities for growth.
    """,
    integration_points="""
    * Integrate sales growth data with financial systems to understand the impact on revenue and profitability.
    * Link sales growth metrics with inventory and supply chain systems to ensure adequate stock levels to meet demand.
    """,
    change_impact_analysis="""
    * Increasing sales growth may require additional investment in sales and marketing resources.
    * Significant changes in sales growth can impact cash flow and working capital requirements.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
