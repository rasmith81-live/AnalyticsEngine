"""
Sales Coaching Effectiveness Rate KPI

The effectiveness of sales coaching programs provided by the sales enablement team in terms of improving sales skills and performance.
"""

SALES_COACHING_EFFECTIVENESS_RATE = {
    "code": "SALES_COACHING_EFFECTIVENESS_RATE",
    "name": "Sales Coaching Effectiveness Rate",
    "description": "The effectiveness of sales coaching programs provided by the sales enablement team in terms of improving sales skills and performance.",
    "formula": "(Post-Coaching Sales Performance - Pre-Coaching Sales Performance) / Pre-Coaching Sales Performance",
    "calculation_formula": "(Post-Coaching Sales Performance - Pre-Coaching Sales Performance) / Pre-Coaching Sales Performance",
    "category": "Sales Enablement",
    "is_active": True,
    "kpi_definition": "The effectiveness of sales coaching programs provided by the sales enablement team in terms of improving sales skills and performance.",
    "expected_business_insights": "Highlights the impact of coaching on sales results and identifies opportunities for further development.",
    "measurement_approach": "Evaluates the improvement in sales performance as a result of coaching sessions.",
    "trend_analysis": """
    * An increasing sales coaching effectiveness rate may indicate that the sales team is adopting and implementing the coaching feedback effectively.
    * A decreasing rate could signal a need for reevaluation of the coaching programs or a lack of engagement from the sales team.
    """,
    "diagnostic_questions": """
    * Are there specific sales skills or areas where the coaching seems to have the most impact?
    * How do the sales coaching effectiveness rates align with the actual sales performance metrics?
    """,
    "actionable_tips": """
    * Regularly gather feedback from the sales team to understand the effectiveness of the coaching programs.
    * Customize coaching programs to address specific skill gaps or challenges identified in the sales team.
    * Provide ongoing support and reinforcement of the coaching to ensure long-term impact on sales performance.
    """,
    "visualization_suggestions": """
    * Line charts showing the trend of sales coaching effectiveness rates over time.
    * Comparison bar charts to visualize the impact of coaching on different sales skills or performance metrics.
    """,
    "risk_warnings": """
    * A consistently low sales coaching effectiveness rate may lead to stagnant or declining sales performance.
    * High variability in the coaching effectiveness rate may indicate inconsistency in the coaching programs or their impact.
    """,
    "tracking_tools": """
    * Utilize sales performance management software to track the impact of coaching on individual sales team members.
    * Implement video coaching platforms to provide remote and personalized coaching to the sales team.
    """,
    "integration_points": """
    * Integrate sales coaching effectiveness data with individual sales performance metrics to understand the direct impact of coaching on results.
    * Link coaching effectiveness with employee development and training programs to create a holistic approach to skill improvement.
    """,
    "change_impact_analysis": """
    * Improving sales coaching effectiveness can lead to increased sales productivity and revenue generation.
    * However, a lack of improvement in coaching effectiveness may result in missed sales opportunities and decreased team morale.
    """,
    "metadata_": {"modules": ["SALES_ENABLEMENT"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Coaching Session", "Enablement Feedback", "Enablement Platform", "Partner Performance Scorecard", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]},
    "modules": ["SALES_ENABLEMENT"],
    "module_code": "SALES_ENABLEMENT",
}
