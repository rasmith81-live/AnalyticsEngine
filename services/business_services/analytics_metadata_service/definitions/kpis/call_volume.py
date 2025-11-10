"""
Call Volume KPI

The number of calls made by the inside sales team during a specific time period. It can help identify whether the team is making enough calls to generate leads and close deals.
"""

from analytics_models import KPI

CALL_VOLUME = KPI(
    name="Call Volume",
    code="CALL_VOLUME",
    category="Inside Sales",
    
    # Core Definition
    description="The number of calls made by the inside sales team during a specific time period. It can help identify whether the team is making enough calls to generate leads and close deals.",
    kpi_definition="The number of calls made by the inside sales team during a specific time period. It can help identify whether the team is making enough calls to generate leads and close deals.",
    expected_business_insights="Indicates the level of activity and potential customer outreach of the sales team.",
    measurement_approach="Number of inbound or outbound calls made by sales reps.",
    
    # Formula
    formula="Total Number of Calls Made",
    calculation_formula="Total Number of Calls Made",
    
    # Analysis
    trend_analysis="""
    * An increasing call volume may indicate a proactive sales team or a response to increased market opportunities.
    * A decreasing call volume could signal a lack of leads, decreased demand, or potential issues within the sales team.
    """,
    diagnostic_questions="""
    * Are there specific times or days when call volume tends to be higher or lower?
    * How does our call volume compare with industry benchmarks or with historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement call tracking software to monitor and analyze call volume trends.
    * Provide ongoing training and support to the inside sales team to improve call efficiency and effectiveness.
    * Consider adjusting call scripts or outreach strategies based on analysis of call volume and outcomes.
    """,
    visualization_suggestions="""
    * Line charts showing call volume over time to identify trends and patterns.
    * Bar graphs comparing call volume by individual sales team members to identify top performers and areas for improvement.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High call volume without corresponding sales may indicate inefficiencies in the sales process or product-market fit issues.
    * Low call volume may lead to missed opportunities and decreased revenue.
    """,
    tracking_tools="""
    * Customer Relationship Management (CRM) systems like Salesforce or HubSpot to track and analyze call volume and outcomes.
    * Call tracking software such as CallRail or CallTrackingMetrics to monitor and optimize call performance.
    """,
    integration_points="""
    * Integrate call volume data with lead management systems to better understand the quality of leads generated from calls.
    * Link call volume with sales performance metrics to identify correlations and opportunities for improvement.
    """,
    change_impact_analysis="""
    * Increasing call volume may lead to higher lead generation and sales, but it could also impact the workload and stress levels of the inside sales team.
    * Decreasing call volume may result in missed opportunities and reduced revenue, impacting overall sales performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["INSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Call", "Deal", "Lead", "Opportunity", "Outbound Call", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
