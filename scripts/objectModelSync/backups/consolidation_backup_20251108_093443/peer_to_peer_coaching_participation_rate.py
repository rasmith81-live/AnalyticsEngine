"""
Peer-to-Peer Coaching Participation Rate KPI

The percentage of sales team members who participate in peer-to-peer coaching sessions.
"""

from analytics_models import KPI

PEER_TO_PEER_COACHING_PARTICIPATION_RATE = KPI(
    name="Peer-to-Peer Coaching Participation Rate",
    code="PEER_TO_PEER_COACHING_PARTICIPATION_RATE",
    category="Sales Enablement",
    
    # Core Definition
    description="The percentage of sales team members who participate in peer-to-peer coaching sessions.",
    kpi_definition="The percentage of sales team members who participate in peer-to-peer coaching sessions.",
    expected_business_insights="Signals the level of team collaboration and knowledge sharing, contributing to the overall skill advancement of the sales team.",
    measurement_approach="Tracks the percentage of sales reps participating in peer-to-peer coaching sessions.",
    
    # Formula
    formula="(Number of Sales Reps Participating in Coaching / Total Number of Sales Reps) * 100",
    calculation_formula="(Number of Sales Reps Participating in Coaching / Total Number of Sales Reps) * 100",
    
    # Analysis
    trend_analysis="""
    * Increasing participation rate may indicate a positive shift in team collaboration and knowledge sharing.
    * Decreasing participation could signal disengagement or lack of buy-in from the sales team.
    """,
    diagnostic_questions="""
    * Are there specific topics or areas where peer-to-peer coaching sessions are more popular or less popular?
    * How does the participation rate correlate with sales performance or team satisfaction?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Encourage senior or high-performing team members to lead coaching sessions to increase interest and engagement.
    * Provide incentives or recognition for active participation in coaching sessions.
    * Regularly solicit feedback from sales team members to understand their preferences and needs for coaching topics.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of participation rate over time.
    * Pie charts to compare participation rates across different coaching topics or leaders.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low participation rates may lead to missed opportunities for knowledge sharing and skill development.
    * Consistently low participation could indicate deeper issues with team dynamics or coaching effectiveness.
    """,
    tracking_tools="""
    * Collaboration platforms like Slack or Microsoft Teams to facilitate communication and scheduling for coaching sessions.
    * Survey tools to gather feedback and preferences from sales team members regarding coaching topics and formats.
    """,
    integration_points="""
    * Integrate participation rate data with individual sales performance metrics to identify correlations and opportunities for improvement.
    * Link coaching participation with employee development plans and performance reviews to align coaching with career growth.
    """,
    change_impact_analysis="""
    * Increasing participation can lead to improved sales performance and team cohesion, but may require additional resources for coaching support.
    * Low participation rates can impact overall team morale and knowledge sharing, potentially affecting the entire sales organization\'s performance.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_ENABLEMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Coaching Session", "Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)
