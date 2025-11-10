"""
Partner Lead Responsiveness KPI

The speed with which channel partners follow up on leads provided by the company.
"""

from analytics_models import KPI

PARTNER_LEAD_RESPONSIVENESS = KPI(
    name="Partner Lead Responsiveness",
    code="PARTNER_LEAD_RESPONSIVENESS",
    category="Channel Sales",
    
    # Core Definition
    description="The speed with which channel partners follow up on leads provided by the company.",
    kpi_definition="The speed with which channel partners follow up on leads provided by the company.",
    expected_business_insights="Indicates partner efficiency in lead management and can predict conversion success rates.",
    measurement_approach="Tracks the speed at which partners follow up on leads provided by the company.",
    
    # Formula
    formula="Average Time Taken by Partners to Follow Up on Leads",
    calculation_formula="Average Time Taken by Partners to Follow Up on Leads",
    
    # Analysis
    trend_analysis="""
    * Increasing partner lead responsiveness may indicate better alignment between partners and the company\'s sales goals.
    * Decreasing responsiveness could signal a lack of motivation or engagement from channel partners.
    """,
    diagnostic_questions="""
    * Are there specific regions or partners that consistently show higher or lower lead responsiveness?
    * How does the lead responsiveness compare with industry benchmarks or competitors\' performance?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Provide regular training and support to channel partners on lead management and follow-up best practices.
    * Implement lead tracking systems to monitor partner responsiveness and provide timely feedback and incentives.
    * Establish clear communication channels and expectations with partners regarding lead follow-up.
    """,
    visualization_suggestions="""
    * Line charts showing lead responsiveness over time for different partners or regions.
    * Pie charts to compare the distribution of leads and the corresponding follow-up rates among partners.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low partner lead responsiveness can result in missed sales opportunities and revenue loss.
    * Consistently high responsiveness from a few partners may indicate an over-reliance on a small group, posing a risk to overall sales performance.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) software to track and manage leads provided to partners.
    * Lead management platforms to automate lead distribution and follow-up tracking.
    """,
    integration_points="""
    * Integrate lead responsiveness data with sales performance metrics to understand the impact on overall revenue generation.
    * Link lead management systems with marketing automation tools to ensure seamless lead handoff and follow-up.
    """,
    change_impact_analysis="""
    * Improving partner lead responsiveness can lead to increased sales efficiency and revenue growth.
    * However, a sudden change in responsiveness may also impact the quality of leads and the overall sales pipeline.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["CHANNEL_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Channel Conflict", "Channel Deal", "Channel Market", "Channel Partner", "Deal", "Lead", "Lead Qualification", "Opportunity", "Partner Agreement", "Partner Incentive", "Partner Performance Scorecard", "Partner Portal", "Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
