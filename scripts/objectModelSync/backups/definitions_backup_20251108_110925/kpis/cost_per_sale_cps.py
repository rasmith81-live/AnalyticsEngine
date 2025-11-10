"""
Cost Per Sale (CPS) KPI

The average cost incurred to make a single sale, including marketing, sales personnel, and other related expenses.
"""

from analytics_models import KPI

COST_PER_SALE_CPS = KPI(
    name="Cost Per Sale (CPS)",
    code="COST_PER_SALE_CPS",
    category="Sales Performance",
    
    # Core Definition
    description="The average cost incurred to make a single sale, including marketing, sales personnel, and other related expenses.",
    kpi_definition="The average cost incurred to make a single sale, including marketing, sales personnel, and other related expenses.",
    expected_business_insights="Helps in analyzing the efficiency of sales processes and effectiveness of sales strategies.",
    measurement_approach="Includes costs directly related to the selling process divided by the number of sales made.",
    
    # Formula
    formula="Total Sales Costs / Number of Sales Made",
    calculation_formula="Total Sales Costs / Number of Sales Made",
    
    # Analysis
    trend_analysis="""
    * Increasing cost per sale may indicate rising marketing or sales expenses without a proportional increase in revenue.
    * Decreasing cost per sale could signal improved efficiency in the sales process or reduced marketing costs.
    """,
    diagnostic_questions="""
    * Are there specific sales channels or campaigns that have significantly higher or lower cost per sale?
    * How does our cost per sale compare with industry averages or benchmarks for similar products or services?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement lead scoring and qualification processes to focus sales efforts on high-potential leads.
    * Regularly review and optimize marketing and advertising spend to ensure cost-effectiveness.
    * Provide sales teams with training and tools to improve their efficiency and effectiveness.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of cost per sale over time.
    * Pareto charts to identify the most significant contributors to overall cost per sale.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High cost per sale can lead to reduced profitability and competitiveness in the market.
    * Significant fluctuations in cost per sale may indicate instability or inefficiency in sales and marketing operations.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems to track and analyze sales and marketing expenses.
    * Marketing automation platforms to optimize campaign performance and cost-effectiveness.
    """,
    integration_points="""
    * Integrate cost per sale analysis with financial reporting to understand its impact on overall profitability.
    * Link cost per sale data with customer relationship management systems to assess the relationship between cost and customer acquisition.
    """,
    change_impact_analysis="""
    * Reducing cost per sale may lead to increased sales volume but could also impact the quality of leads and customer relationships.
    * Increasing cost per sale to improve lead quality or customer experience may result in lower immediate profitability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Lost Sale", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
