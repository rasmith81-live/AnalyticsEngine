"""
Partner-Centric Productivity KPI

The productivity of channel partners, often measured in revenue per partner or deals closed per partner.
"""

from analytics_models import KPI

PARTNER_CENTRIC_PRODUCTIVITY = KPI(
    name="Partner-Centric Productivity",
    code="PARTNER_CENTRIC_PRODUCTIVITY",
    category="Channel Sales",
    
    # Core Definition
    description="The productivity of channel partners, often measured in revenue per partner or deals closed per partner.",
    kpi_definition="The productivity of channel partners, often measured in revenue per partner or deals closed per partner.",
    expected_business_insights="Highlights how effectively partners are utilizing company support to achieve sales goals.",
    measurement_approach="Assesses the efficiency of partners in generating revenue relative to the support and resources provided.",
    
    # Formula
    formula="Total Revenue from Partners / Total Costs of Partner Support and Resources",
    calculation_formula="Total Revenue from Partners / Total Costs of Partner Support and Resources",
    
    # Analysis
    trend_analysis="""
    * Increasing revenue per partner may indicate successful enablement and support programs.
    * Decreasing deals closed per partner could signal a lack of engagement or alignment with the partner channel.
    """,
    diagnostic_questions="""
    * Are there specific partners consistently driving high revenue, and what can be learned from their approach?
    * How does our partner-centric productivity compare with industry benchmarks or with top-performing partners in our network?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in partner training and enablement to improve their sales capabilities.
    * Align partner incentives with desired sales behaviors to drive better performance.
    * Regularly communicate with partners to understand their challenges and provide necessary support.
    """,
    visualization_suggestions="""
    * Line charts showing revenue per partner over time to identify trends and patterns.
    * Pie charts comparing deals closed per partner to visualize the distribution of performance across the partner network.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low partner-centric productivity can lead to missed sales opportunities and revenue loss.
    * Over-reliance on a few high-performing partners can create vulnerability if they disengage or underperform.
    """,
    tracking_tools="""
    * Partner relationship management (PRM) software to track partner performance and engagement.
    * Sales enablement platforms to provide partners with necessary resources and training materials.
    """,
    integration_points="""
    * Integrate partner-centric productivity data with CRM systems to understand the full customer journey and partner involvement.
    * Link partner performance with incentive and compensation systems to drive desired behaviors.
    """,
    change_impact_analysis="""
    * Improving partner-centric productivity can lead to increased market coverage and customer reach.
    * However, changes in partner engagement and incentives may impact the overall sales strategy and resource allocation.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer", "Deal", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Product", "Revenue Forecast", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)
