"""
Partner Recruitment Rate KPI

The rate at which new channel partners are recruited over a specific period, which indicates the expansion of the channel network.
"""

from analytics_models import KPI

PARTNER_RECRUITMENT_RATE = KPI(
    name="Partner Recruitment Rate",
    code="PARTNER_RECRUITMENT_RATE",
    category="Channel Sales",
    
    # Core Definition
    description="The rate at which new channel partners are recruited over a specific period, which indicates the expansion of the channel network.",
    kpi_definition="The rate at which new channel partners are recruited over a specific period, which indicates the expansion of the channel network.",
    expected_business_insights="Indicates the attractiveness of the partner program and informs recruitment strategy effectiveness.",
    measurement_approach="Measures the success rate of bringing new partners into the channel program.",
    
    # Formula
    formula="(Number of New Partners Acquired / Number of Partners Targeted) * 100",
    calculation_formula="(Number of New Partners Acquired / Number of Partners Targeted) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing partner recruitment rate may indicate successful marketing and sales efforts to attract new partners.
    * A decreasing rate could signal market saturation or ineffective partner onboarding processes.
    """,
    diagnostic_questions="""
    * What specific strategies or channels have been most effective in recruiting new partners?
    * Are there any common barriers or challenges that potential partners face during the recruitment process?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Offer comprehensive training and support to new partners to ensure their success and commitment.
    * Regularly review and update the partner recruitment process to streamline and improve efficiency.
    * Implement referral programs or incentives to encourage existing partners to refer new potential partners.
    """,
    visualization_suggestions="""
    * Line charts showing the monthly or quarterly trend of partner recruitment rate.
    * Pie charts to compare the contribution of different channels or strategies to partner recruitment.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Rapid partner recruitment without proper vetting can lead to poor-quality partnerships and negative impact on brand reputation.
    * A declining partner recruitment rate may indicate a need for reevaluation of the overall channel strategy and approach.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage partner leads and conversions.
    * Partner Relationship Management (PRM) platforms to streamline partner onboarding and management processes.
    """,
    integration_points="""
    * Integrate partner recruitment data with sales performance metrics to understand the impact of new partners on overall sales.
    * Link partner recruitment with marketing analytics to assess the effectiveness of different marketing channels in attracting potential partners.
    """,
    change_impact_analysis="""
    * An increase in partner recruitment rate can lead to expanded market reach and potentially higher sales volume.
    * However, rapid expansion without proper support and resources can strain internal operations and customer service capabilities.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Customer Advocacy Program", "Customer Success Manager", "Expansion Opportunity", "Loyalty Program", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
