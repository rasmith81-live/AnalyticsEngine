"""
Partner Profitability KPI

A measure of the net profit a channel partner generates for the company, indicating the financial success of the partnership.
"""

from analytics_models import KPI

PARTNER_PROFITABILITY = KPI(
    name="Partner Profitability",
    code="PARTNER_PROFITABILITY",
    category="Channel Sales",
    
    # Core Definition
    description="A measure of the net profit a channel partner generates for the company, indicating the financial success of the partnership.",
    kpi_definition="A measure of the net profit a channel partner generates for the company, indicating the financial success of the partnership.",
    expected_business_insights="Assesses the financial success of the channel program and informs strategies for improving partner profitability.",
    measurement_approach="Measures the net profit attributed to channel partner sales after accounting for all related expenses.",
    
    # Formula
    formula="(Total Revenue from Partners - Total Costs Associated with Partners) / Total Revenue from Partners * 100",
    calculation_formula="(Total Revenue from Partners - Total Costs Associated with Partners) / Total Revenue from Partners * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing partner profitability may indicate successful sales strategies and strong customer relationships.
    * Decreasing profitability could signal issues with pricing, competition, or changes in customer demand.
    """,
    diagnostic_questions="""
    * What factors contribute to the profitability of our channel partners?
    * Are there specific products or services that are more profitable for our partners?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide training and support to help partners effectively market and sell high-margin products.
    * Regularly review and adjust partner commission structures to align with company goals and market conditions.
    * Implement incentive programs to encourage partners to focus on selling more profitable products or services.
    """,
    visualization_suggestions="""
    * Line charts showing partner profitability over time to identify trends and seasonal variations.
    * Pie charts to compare the contribution of different products or services to overall partner profitability.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Declining partner profitability may lead to disengagement or seeking partnerships with competitors.
    * Over-reliance on a small number of highly profitable products or services may create vulnerability to market changes.
    """,
    tracking_tools="""
    * Channel management software to track partner performance and profitability in real-time.
    * Customer relationship management (CRM) systems to analyze customer behavior and preferences, helping partners focus on more profitable opportunities.
    """,
    integration_points="""
    * Integrate partner profitability data with sales and marketing systems to identify opportunities for improving partner performance.
    * Link partner profitability with inventory and supply chain management to ensure partners have access to profitable products in a timely manner.
    """,
    change_impact_analysis="""
    * Improving partner profitability can lead to increased revenue and market share for the company.
    * However, changes in partner profitability may also impact relationships with other channel partners and overall market competitiveness.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Customer Success Manager", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Partnership", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
