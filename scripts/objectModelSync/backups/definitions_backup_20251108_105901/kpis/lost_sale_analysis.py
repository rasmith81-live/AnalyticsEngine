"""
Lost Sale Analysis KPI

The evaluation of deals that were not won to understand the reasons behind the loss.
"""

from analytics_models import KPI

LOST_SALE_ANALYSIS = KPI(
    name="Lost Sale Analysis",
    code="LOST_SALE_ANALYSIS",
    category="Inside Sales",
    
    # Core Definition
    description="The evaluation of deals that were not won to understand the reasons behind the loss.",
    kpi_definition="The evaluation of deals that were not won to understand the reasons behind the loss.",
    expected_business_insights="Provides insights into obstacles within the sales process, offering opportunities for improvement.",
    measurement_approach="Identification of reasons for lost sales and the rate at which sales opportunities are lost.",
    
    # Formula
    formula="Variables vary; often a qualitative analysis",
    calculation_formula="Variables vary; often a qualitative analysis",
    
    # Analysis
    trend_analysis="""
    * An increasing lost sale analysis may indicate issues with the sales process, product quality, or market competition.
    * A decreasing analysis could signal improved sales strategies, product enhancements, or better customer relationship management.
    """,
    diagnostic_questions="""
    * Are there common reasons or patterns behind the lost sales? (e.g., pricing, product features, competitor actions)
    * How do our lost sales compare with industry benchmarks or historical data? Are there any emerging trends?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement regular win/loss analysis to gather feedback from lost opportunities and identify areas for improvement.
    * Provide additional sales training or resources to address common objections or concerns raised by potential customers.
    * Consider revising pricing strategies, product offerings, or sales approaches based on the insights gained from the lost sale analysis.
    """,
    visualization_suggestions="""
    * Funnel charts to visualize the stages where potential sales are being lost in the sales process.
    * Comparison charts to highlight the reasons for lost sales across different time periods or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Consistently high lost sale rates can impact revenue and market share, leading to long-term business implications.
    * Ignoring the reasons behind lost sales may result in continued inefficiencies and missed opportunities for improvement.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and analyze lost sales data and customer interactions.
    * Sales analytics tools to identify patterns and trends in lost sale data, enabling targeted improvements.
    """,
    integration_points="""
    * Integrate lost sale analysis with customer feedback systems to gain a comprehensive understanding of customer needs and preferences.
    * Link analysis with sales forecasting and inventory management systems to align production and sales efforts with market demand.
    """,
    change_impact_analysis="""
    * Improving the lost sale analysis can lead to more targeted sales efforts, increased customer satisfaction, and higher conversion rates.
    * However, changes in sales strategies or product offerings may require additional resources and could impact short-term sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES", "SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Competitive Analysis", "Deal", "Lost Sale", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
