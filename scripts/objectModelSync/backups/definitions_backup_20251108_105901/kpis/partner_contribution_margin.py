"""
Partner Contribution Margin KPI

A measure of how much each channel partner contributes to covering the company's fixed costs after variable costs are subtracted.
"""

from analytics_models import KPI

PARTNER_CONTRIBUTION_MARGIN = KPI(
    name="Partner Contribution Margin",
    code="PARTNER_CONTRIBUTION_MARGIN",
    category="Channel Sales",
    
    # Core Definition
    description="A measure of how much each channel partner contributes to covering the company\'s fixed costs after variable costs are subtracted.",
    kpi_definition="A measure of how much each channel partner contributes to covering the company\'s fixed costs after variable costs are subtracted.",
    expected_business_insights="Evaluates the financial value added by partners after accounting for direct costs associated with sales.",
    measurement_approach="Measures the profit margin that is attributable to channel partner sales.",
    
    # Formula
    formula="(Total Revenue from Partners - Variable Costs Attributable to Partners) / Total Revenue from Partners * 100",
    calculation_formula="(Total Revenue from Partners - Variable Costs Attributable to Partners) / Total Revenue from Partners * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing partner contribution margin may indicate improved efficiency in the channel partner network or better pricing strategies.
    * Decreasing margin could signal rising variable costs, ineffective pricing, or a decline in sales volume.
    """,
    diagnostic_questions="""
    * Are there specific channel partners that consistently contribute more or less to covering fixed costs?
    * How does our partner contribution margin compare with industry benchmarks or historical performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide channel partners with training and support to improve their sales effectiveness and reduce variable costs.
    * Regularly review pricing strategies to ensure they align with market conditions and partner capabilities.
    * Implement incentive programs to encourage channel partners to focus on high-margin products or services.
    """,
    visualization_suggestions="""
    * Line charts showing partner contribution margin over time to identify trends and seasonality.
    * Pie charts to compare the contribution margin of different channel partners or regions.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low partner contribution margin may lead to increased reliance on company-owned sales channels, impacting overall profitability.
    * Highly variable contribution margins across partners may indicate inconsistent performance or potential issues with partner management.
    """,
    tracking_tools="""
    * Channel management software to track and analyze partner performance and contribution margin.
    * Financial management systems to accurately allocate fixed and variable costs to each channel partner.
    """,
    integration_points="""
    * Integrate partner contribution margin analysis with sales and marketing systems to identify opportunities for improved partner performance.
    * Link contribution margin data with supply chain and inventory management systems to ensure efficient cost allocation.
    """,
    change_impact_analysis="""
    * Increasing partner contribution margin may lead to higher overall profitability but could require additional investment in partner support and resources.
    * Decreasing margin may impact the company\'s ability to cover fixed costs and maintain profitability, potentially leading to strategic shifts in the channel partner network.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
