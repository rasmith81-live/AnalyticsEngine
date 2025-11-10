"""
Year-Over-Year Growth KPI

The growth in sales or revenue when compared to the same period in the previous year.
"""

from analytics_models import KPI

YEAR_OVER_YEAR_GROWTH = KPI(
    name="Year-Over-Year Growth",
    code="YEAR_OVER_YEAR_GROWTH",
    category="Outside Sales",
    
    # Core Definition
    description="The growth in sales or revenue when compared to the same period in the previous year.",
    kpi_definition="The growth in sales or revenue when compared to the same period in the previous year.",
    expected_business_insights="Signals business health and the effectiveness of sales strategies over time.",
    measurement_approach="Calculates the percentage increase in sales or revenue from one year to the next.",
    
    # Formula
    formula="((This Year\'s Sales - Last Year\'s Sales) / Last Year\'s Sales) * 100",
    calculation_formula="((This Year\'s Sales - Last Year\'s Sales) / Last Year\'s Sales) * 100",
    
    # Analysis
    trend_analysis="""
    * Year-over-year growth may show a consistent upward trend, indicating healthy sales expansion.
    * Fluctuations in growth rates could signal seasonal or market-specific influences on sales performance.
    """,
    diagnostic_questions="""
    * What factors contributed to the increase or decrease in year-over-year growth?
    * Are there specific products or regions driving the growth, and what can be learned from their performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in targeted marketing and sales efforts to capitalize on growth opportunities.
    * Analyze customer feedback and market trends to identify new areas for expansion.
    * Implement sales training and development programs to maximize the potential of the sales team.
    """,
    visualization_suggestions="""
    * Line charts showing year-over-year growth by product category or geographic region.
    * Comparative bar graphs to visualize growth rates across different time periods.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Rapid growth may strain operational capacity and lead to service or quality issues.
    * Slow or negative growth could indicate market saturation or competitive challenges.
    """,
    tracking_tools="""
    * Customer relationship management (CRM) software to track and manage sales activities and customer interactions.
    * Business intelligence tools for in-depth analysis of sales data and performance metrics.
    """,
    integration_points="""
    * Integrate year-over-year growth data with financial reporting systems for comprehensive performance analysis.
    * Link sales growth metrics with inventory and supply chain management systems to ensure alignment with demand.
    """,
    change_impact_analysis="""
    * Positive growth can lead to increased revenue, market share, and overall business success.
    * Negative growth may necessitate strategic shifts, cost-cutting measures, or market repositioning.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
