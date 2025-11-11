"""
Sales Team Collaboration Index KPI

A measure of the effectiveness of collaboration within the sales team, which could include cross-functional initiatives.
"""

SALES_TEAM_COLLABORATION_INDEX = {
    "code": "SALES_TEAM_COLLABORATION_INDEX",
    "name": "Sales Team Collaboration Index",
    "description": "A measure of the effectiveness of collaboration within the sales team, which could include cross-functional initiatives.",
    "formula": "Collaborative Activities Score / Total Number of Opportunities for Collaboration",
    "calculation_formula": "Collaborative Activities Score / Total Number of Opportunities for Collaboration",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "A measure of the effectiveness of collaboration within the sales team, which could include cross-functional initiatives.",
    "expected_business_insights": "Indicates how well the sales team works together and shares knowledge, potentially impacting team success.",
    "measurement_approach": "Assesses the degree of collaboration and communication among sales team members.",
    "trend_analysis": """
    * An increasing Sales Team Collaboration Index may indicate improved cross-functional initiatives and better alignment within the sales team.
    * A decreasing index could signal breakdowns in communication, lack of teamwork, or siloed behavior within the sales team.
    """,
    "diagnostic_questions": """
    * Are there specific sales projects or initiatives where collaboration has been particularly effective or ineffective?
    * How does our Sales Team Collaboration Index compare with industry benchmarks or best practices?
    """,
    "actionable_tips": """
    * Implement regular cross-functional meetings to align on goals and strategies.
    * Encourage open communication and knowledge sharing within the sales team.
    * Utilize collaboration tools and technologies to facilitate teamwork and information exchange.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of the Sales Team Collaboration Index over time.
    * Stacked bar charts comparing collaboration levels across different sales projects or teams.
    """,
    "risk_warnings": """
    * Low Sales Team Collaboration Index can lead to missed opportunities, duplicated efforts, and internal conflicts.
    * Ineffective collaboration may result in poor customer experience and lost sales.
    """,
    "tracking_tools": """
    * Collaboration platforms like Microsoft Teams or Slack for seamless communication and file sharing.
    * Project management tools such as Asana or Trello to track and manage cross-functional initiatives.
    """,
    "integration_points": """
    * Integrate the Sales Team Collaboration Index with performance management systems to align individual goals with team collaboration efforts.
    * Link collaboration metrics with customer relationship management (CRM) systems to understand the impact on customer interactions and sales outcomes.
    """,
    "change_impact_analysis": """
    * Improving the Sales Team Collaboration Index can lead to better customer engagement, increased sales productivity, and higher overall team morale.
    * Conversely, a low index may result in missed sales opportunities, decreased employee satisfaction, and potential turnover.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
