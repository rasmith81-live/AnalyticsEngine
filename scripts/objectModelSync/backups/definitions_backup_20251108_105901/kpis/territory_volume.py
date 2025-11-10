"""
Territory Volume KPI

The volume of sales within a defined sales territory, which can be used to assess market penetration and sales representative performance.
"""

from analytics_models import KPI

TERRITORY_VOLUME = KPI(
    name="Territory Volume",
    code="TERRITORY_VOLUME",
    category="Sales Performance",
    
    # Core Definition
    description="The volume of sales within a defined sales territory, which can be used to assess market penetration and sales representative performance.",
    kpi_definition="The volume of sales within a defined sales territory, which can be used to assess market penetration and sales representative performance.",
    expected_business_insights="Provides insights into regional market performance and potential for territorial adjustments.",
    measurement_approach="Assesses the total sales volume within a specific sales territory.",
    
    # Formula
    formula="Total Sales Volume per Territory",
    calculation_formula="Total Sales Volume per Territory",
    
    # Analysis
    trend_analysis="""
    * Increasing territory volume may indicate successful sales strategies or expanding market opportunities.
    * Decreasing volume could signal market saturation or ineffective sales representative performance.
    """,
    diagnostic_questions="""
    * Are there specific products or services that are driving the majority of sales within the territory?
    * How does the territory volume compare to historical data and industry benchmarks?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide targeted sales training and support to representatives in underperforming territories.
    * Explore new market segments or potential partnerships to expand territory opportunities.
    * Regularly review and adjust sales territories based on changing market dynamics.
    """,
    visualization_suggestions="""
    * Line charts showing territory volume over time to identify trends and seasonality.
    * Geospatial maps to visualize territory boundaries and sales distribution.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High territory volume may lead to potential resource strain and difficulty in maintaining customer service levels.
    * Low territory volume could indicate missed opportunities or ineffective sales strategies.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track sales activities and customer interactions within each territory.
    * Data analytics tools to identify patterns and opportunities within territory sales data.
    """,
    integration_points="""
    * Integrate territory volume data with sales forecasting systems to align resource allocation and inventory management.
    * Link territory volume with marketing analytics to understand the impact of promotional activities on sales performance.
    """,
    change_impact_analysis="""
    * Increasing territory volume may require adjustments in supply chain management and customer support to meet growing demand.
    * Decreasing volume could impact revenue projections and overall business growth if not addressed proactively.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_PERFORMANCE"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account Penetration", "Channel Market", "Market Segment", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Territory Assignment"]
    }
)
