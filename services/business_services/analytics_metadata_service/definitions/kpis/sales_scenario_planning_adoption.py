"""
Sales Scenario Planning Adoption KPI

The adoption rate of scenario planning exercises by the sales team to prepare for different sales situations.
"""

SALES_SCENARIO_PLANNING_ADOPTION = {
    "code": "SALES_SCENARIO_PLANNING_ADOPTION",
    "name": "Sales Scenario Planning Adoption",
    "description": "The adoption rate of scenario planning exercises by the sales team to prepare for different sales situations.",
    "formula": "(Number of Sales Reps Using Scenario Planning / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Using Scenario Planning / Total Number of Sales Reps) * 100",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The adoption rate of scenario planning exercises by the sales team to prepare for different sales situations.",
    "expected_business_insights": "Indicates the preparedness of the sales team for various market conditions and customer interactions.",
    "measurement_approach": "Evaluates the uptake of scenario planning practices within the sales team.",
    "trend_analysis": """
    * An increasing adoption rate of scenario planning may indicate a proactive and forward-thinking sales team.
    * A decreasing adoption rate could signal a lack of preparation for different sales situations and potential missed opportunities.
    """,
    "diagnostic_questions": """
    * Are there specific sales scenarios where the team consistently struggles or feels unprepared?
    * How does the adoption rate of scenario planning compare with the overall sales performance?
    """,
    "actionable_tips": """
    * Provide training and resources to help the sales team understand the importance and benefits of scenario planning.
    * Encourage collaboration and knowledge sharing among the sales team to develop effective strategies for different sales situations.
    * Incorporate scenario planning into regular sales meetings and performance evaluations to reinforce its importance.
    """,
    "visualization_suggestions": """
    * Line charts showing the adoption rate of scenario planning over time.
    * Comparison charts displaying the adoption rate across different sales teams or regions.
    """,
    "risk_warnings": """
    * Low adoption of scenario planning may lead to missed sales opportunities and ineffective responses to customer needs.
    * Resistance to scenario planning could indicate a cultural or organizational barrier that hinders sales effectiveness.
    """,
    "tracking_tools": """
    * CRM systems with built-in scenario planning modules to integrate planning with sales activities.
    * Sales enablement platforms that offer scenario planning templates and best practices for the sales team.
    """,
    "integration_points": """
    * Integrate scenario planning adoption with sales performance metrics to understand its impact on overall sales effectiveness.
    * Link scenario planning with customer relationship management systems to align strategies with customer needs and preferences.
    """,
    "change_impact_analysis": """
    * Improving scenario planning adoption can lead to better sales performance and customer satisfaction, but may require initial investment in training and resources.
    * Low adoption of scenario planning can result in reactive sales strategies, potentially impacting customer relationships and revenue generation.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Enablement Feedback", "Enablement Platform", "Product Adoption", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
