"""
Activity Scorecard KPI

A comprehensive measure of sales activities, including calls, emails, meetings, and tasks completed.
"""

ACTIVITY_SCORECARD = {
    "code": "ACTIVITY_SCORECARD",
    "name": "Activity Scorecard",
    "description": "A comprehensive measure of sales activities, including calls, emails, meetings, and tasks completed.",
    "formula": "Sum of all sales activities completed / Total number of sales reps",
    "calculation_formula": "Sum of all sales activities completed / Total number of sales reps",
    "category": "Inside Sales",
    "is_active": True,
    "kpi_definition": "A comprehensive measure of sales activities, including calls, emails, meetings, and tasks completed.",
    "expected_business_insights": "Reveals sales rep productivity and effectiveness in managing and executing sales activities.",
    "measurement_approach": "Tracks metrics such as calls made, emails sent, meetings booked, and deals closed.",
    "trend_analysis": """
    * An increasing activity scorecard may indicate a proactive sales team or increased outreach efforts.
    * A decreasing scorecard could signal issues with sales team productivity or engagement.
    """,
    "diagnostic_questions": """
    * Are there specific sales activities that are consistently underperforming?
    * How does our activity scorecard compare with industry benchmarks or seasonal fluctuations?
    """,
    "actionable_tips": """
    * Implement sales activity tracking software to monitor and analyze individual and team performance.
    * Provide regular training and coaching to improve sales skills and increase activity effectiveness.
    * Establish clear activity goals and incentives to motivate the sales team.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of different sales activities over time.
    * Pie charts to compare the distribution of various sales activities within the team.
    """,
    "risk_warnings": """
    * Low activity scorecard may lead to missed sales opportunities and revenue loss.
    * High activity scorecard without corresponding results may indicate inefficiencies or ineffective sales strategies.
    """,
    "tracking_tools": """
    * CRM systems like Salesforce or HubSpot for tracking and managing sales activities.
    * Sales engagement platforms to automate and optimize outreach efforts.
    """,
    "integration_points": """
    * Integrate activity scorecard data with performance management systems to align individual goals with overall sales objectives.
    * Link sales activity data with customer relationship management systems to track the impact on customer interactions and conversions.
    """,
    "change_impact_analysis": """
    * Increasing sales activities may lead to higher customer acquisition but could also strain resources and increase costs.
    * Decreasing activities may improve efficiency but could also result in missed opportunities and reduced revenue.
    """,
    "metadata_": {"modules": ["INSIDE_SALES"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Call", "Email", "Meeting", "Partner Performance Scorecard", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["INSIDE_SALES"],
    "module_code": "INSIDE_SALES",
}
