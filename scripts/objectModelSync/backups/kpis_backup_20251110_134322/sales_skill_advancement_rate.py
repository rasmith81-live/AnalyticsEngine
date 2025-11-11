"""
Sales Skill Advancement Rate KPI

The rate at which sales representatives improve their sales skills post-training.
"""

SALES_SKILL_ADVANCEMENT_RATE = {
    "code": "SALES_SKILL_ADVANCEMENT_RATE",
    "name": "Sales Skill Advancement Rate",
    "description": "The rate at which sales representatives improve their sales skills post-training.",
    "formula": "(Performance Metrics Post-Training - Performance Metrics Pre-Training) / Performance Metrics Pre-Training * 100",
    "calculation_formula": "(Performance Metrics Post-Training - Performance Metrics Pre-Training) / Performance Metrics Pre-Training * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The rate at which sales representatives improve their sales skills post-training.",
    "expected_business_insights": "Highlights the direct skill enhancements gained from training, which can lead to improved sales performance.",
    "measurement_approach": "The rate of improvement in specific sales skills following training, as measured by assessments or performance metrics.",
    "trend_analysis": """
    * Positive trend in sales skill advancement rate may indicate the effectiveness of the training program and coaching methods.
    * Negative trend could signal a need for reevaluation of the training content, coaching techniques, or individual performance issues.
    """,
    "diagnostic_questions": """
    * Are there specific sales skills that sales representatives struggle to improve post-training?
    * How does the sales skill advancement rate compare with industry benchmarks or with the performance of top-performing sales representatives?
    """,
    "actionable_tips": """
    * Provide ongoing coaching and mentorship to reinforce and apply newly acquired sales skills in real-world scenarios.
    * Customize training programs to address specific skill gaps identified through performance evaluations and feedback.
    * Implement regular practice sessions and role-playing exercises to ensure retention and application of learned sales skills.
    """,
    "visualization_suggestions": """
    * Line charts showing the progression of sales skill advancement rate over time.
    * Comparison bar charts displaying the improvement in sales skills for different sales representatives or teams.
    """,
    "risk_warnings": """
    * Low sales skill advancement rate may lead to missed sales opportunities and decreased revenue.
    * Failure to improve sales skills post-training could indicate a need for more comprehensive performance management and development strategies.
    """,
    "tracking_tools": """
    * Utilize sales performance management software to track and analyze individual sales skill advancement and identify areas for improvement.
    * Implement learning management systems to deliver and track the effectiveness of sales training programs.
    """,
    "integration_points": """
    * Integrate sales skill advancement rate with performance evaluation systems to align training and coaching efforts with individual development plans.
    * Link sales skill advancement data with customer relationship management (CRM) systems to measure the impact of improved sales skills on customer interactions and sales outcomes.
    """,
    "change_impact_analysis": """
    * Improving sales skill advancement rate can lead to increased sales effectiveness, customer satisfaction, and long-term revenue growth.
    * However, focusing solely on sales skill advancement without considering the quality of customer interactions may lead to short-term gains at the expense of long-term customer relationships.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Performance Scorecard", "Partner Training", "Performance Benchmark", "Performance Scorecard", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
