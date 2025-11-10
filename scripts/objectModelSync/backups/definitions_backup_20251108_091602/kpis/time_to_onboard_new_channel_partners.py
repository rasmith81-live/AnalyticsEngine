"""
Time to Onboard New Channel Partners KPI

The time taken to onboard new channel partners from initial contact to first sale.
"""

from analytics_models import KPI

TIME_TO_ONBOARD_NEW_CHANNEL_PARTNERS = KPI(
    name="Time to Onboard New Channel Partners",
    code="TIME_TO_ONBOARD_NEW_CHANNEL_PARTNERS",
    category="Channel Sales",
    
    # Core Definition
    description="The time taken to onboard new channel partners from initial contact to first sale.",
    kpi_definition="The time taken to onboard new channel partners from initial contact to first sale.",
    expected_business_insights="Highlights the efficiency of the onboarding process and informs strategies to accelerate partner ramp-up time.",
    measurement_approach="Measures the average time required to recruit, train, and enable new partners to become productive.",
    
    # Formula
    formula="Average Number of Days from Partner Agreement to First Sale",
    calculation_formula="Average Number of Days from Partner Agreement to First Sale",
    
    # Analysis
    trend_analysis="""
    * Decreasing time to onboard new channel partners may indicate improved onboarding processes or increased demand for partnership.
    * An increasing time to onboard new channel partners could signal inefficiencies in the onboarding process or a decline in interest from potential partners.
    """,
    diagnostic_questions="""
    * What are the common bottlenecks in the onboarding process for new channel partners?
    * How does our time to onboard new channel partners compare with industry benchmarks or with our competitors?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Streamline the onboarding process by providing comprehensive training and support materials for new channel partners.
    * Invest in technology solutions that can automate and expedite the onboarding process, such as partner relationship management (PRM) software.
    * Regularly review and update the onboarding process based on feedback from new channel partners to identify and address any pain points.
    """,
    visualization_suggestions="""
    * Line charts showing the average time to onboard new channel partners over time.
    * Comparison bar charts displaying the time to onboard new channel partners for different regions or product lines.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Lengthy onboarding processes may result in potential partners seeking out competitors with faster onboarding procedures.
    * Rapidly increasing time to onboard new channel partners may indicate a need for immediate attention to prevent a negative impact on sales.
    """,
    tracking_tools="""
    * Utilize customer relationship management (CRM) systems to track and manage the onboarding process for new channel partners.
    * Implement collaboration tools such as Slack or Microsoft Teams to facilitate communication and coordination during the onboarding process.
    """,
    integration_points="""
    * Integrate the onboarding process with sales and marketing systems to ensure seamless transition from onboarding to sales activities.
    * Link the onboarding process with customer support systems to provide immediate assistance to new channel partners as they begin their sales activities.
    """,
    change_impact_analysis="""
    * Improving the time to onboard new channel partners can lead to increased sales revenue and market expansion.
    * Conversely, a prolonged onboarding process may result in missed sales opportunities and decreased market competitiveness.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Lost Sale", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement"]
    }
)
