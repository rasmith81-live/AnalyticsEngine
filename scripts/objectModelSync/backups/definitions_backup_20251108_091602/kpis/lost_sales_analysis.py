"""
Lost Sales Analysis KPI

A review of lost sales opportunities to determine common factors or reasons for not winning the business.
"""

from analytics_models import KPI

LOST_SALES_ANALYSIS = KPI(
    name="Lost Sales Analysis",
    code="LOST_SALES_ANALYSIS",
    category="Outside Sales",
    
    # Core Definition
    description="A review of lost sales opportunities to determine common factors or reasons for not winning the business.",
    kpi_definition="A review of lost sales opportunities to determine common factors or reasons for not winning the business.",
    expected_business_insights="Provides insights into reasons for lost sales, helping improve sales strategies and product offerings.",
    measurement_approach="Involves qualitative and quantitative assessment of lost sales opportunities.",
    
    # Formula
    formula="No Standard Formula - This KPI is typically a combination of various metrics and qualitative assessments.",
    calculation_formula="No Standard Formula - This KPI is typically a combination of various metrics and qualitative assessments.",
    
    # Analysis
    trend_analysis="""
    * An increasing number of lost sales due to pricing issues may indicate a need to reevaluate pricing strategies or offer more competitive pricing.
    * A decrease in lost sales related to product availability could signal improvements in inventory management or supplier relationships.
    """,
    diagnostic_questions="""
    * Are there common objections or reasons cited by potential customers for not choosing our products/services?
    * How do our lost sales compare to competitors, and what factors differentiate our offerings?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide additional sales training to address common objections and improve sales techniques.
    * Conduct market research to understand customer needs and preferences better, allowing for more targeted sales approaches.
    * Implement a customer feedback system to gather insights on why sales opportunities are being lost.
    """,
    visualization_suggestions="""
    * Pie charts showing the distribution of lost sales reasons.
    * Trend line graphs to track changes in lost sales reasons over time.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently losing sales due to the same reasons may indicate a need for significant changes in product offerings or sales strategies.
    * Ignoring common reasons for lost sales can lead to continued revenue loss and market share erosion.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze reasons for lost sales.
    * Sales analytics tools to identify patterns and trends in lost sales data.
    """,
    integration_points="""
    * Integrate lost sales analysis with customer feedback systems to gain a comprehensive understanding of customer preferences and objections.
    * Link lost sales data with sales performance metrics to identify areas for improvement in the sales process.
    """,
    change_impact_analysis="""
    * Addressing common reasons for lost sales can lead to increased revenue and market share.
    * However, changes in sales strategies or product offerings may require initial investment and could impact short-term profitability.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Assessment", "Call", "Competitive Analysis", "Lost Sale", "Quarterly Business Review", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Strategic Review"]
    }
)
