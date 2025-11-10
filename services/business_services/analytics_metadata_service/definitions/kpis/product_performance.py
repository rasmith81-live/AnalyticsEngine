"""
Product Performance KPI

The sales success of individual products or services, which helps in analyzing which items are performing well and which are not.
"""

from analytics_models import KPI

PRODUCT_PERFORMANCE = KPI(
    name="Product Performance",
    code="PRODUCT_PERFORMANCE",
    category="Sales Performance",
    
    # Core Definition
    description="The sales success of individual products or services, which helps in analyzing which items are performing well and which are not.",
    kpi_definition="The sales success of individual products or services, which helps in analyzing which items are performing well and which are not.",
    expected_business_insights="Enables product-specific insights and decision-making to optimize product portfolios.",
    measurement_approach="Assesses sales figures, market reception, and profitability per product.",
    
    # Formula
    formula="Varies Depending on Specific Product Metrics Analyzed",
    calculation_formula="Varies Depending on Specific Product Metrics Analyzed",
    
    # Analysis
    trend_analysis="""
    * Identifying which products or services are consistently top performers over time.
    * Analyzing the trend of underperforming products to determine if there are common factors contributing to their lack of success.
    """,
    diagnostic_questions="""
    * Are there specific products or services that consistently outperform others?
    * What factors contribute to the success or failure of individual products or services?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Regularly review and update product or service offerings based on performance data.
    * Invest in marketing and promotional efforts for underperforming products to boost sales.
    * Consider adjusting pricing or packaging for products based on their performance.
    """,
    visualization_suggestions="""
    * Pareto charts to identify the most significant contributors to overall sales performance.
    * Line graphs to track the performance of individual products or services over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Over-reliance on a few top-performing products may lead to vulnerability if their sales decline.
    * Ignoring underperforming products may result in missed opportunities for improvement or innovation.
    """,
    tracking_tools="""
    * CRM systems to track customer preferences and purchasing behavior for different products or services.
    * Market research tools to gather insights on consumer trends and preferences.
    """,
    integration_points="""
    * Integrate product performance data with inventory management systems to ensure adequate stock levels for top-performing items.
    * Link product performance with marketing and sales systems to align promotional efforts with successful products.
    """,
    change_impact_analysis="""
    * Improving the performance of underperforming products can lead to increased overall sales and revenue.
    * Shifting focus away from top-performing products may impact short-term sales but could lead to long-term diversification and stability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Market", "Customer Success Manager", "Market Segment", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Product", "Product Adoption", "Product Usage", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
