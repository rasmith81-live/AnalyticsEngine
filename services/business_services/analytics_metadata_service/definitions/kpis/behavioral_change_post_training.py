"""
Behavioral Change Post-Training KPI

The extent to which sales reps alter their sales techniques and behaviors after training.
"""

BEHAVIORAL_CHANGE_POST_TRAINING = {
    "code": "BEHAVIORAL_CHANGE_POST_TRAINING",
    "name": "Behavioral Change Post-Training",
    "description": "The extent to which sales reps alter their sales techniques and behaviors after training.",
    "formula": "(Number of Sales Reps Demonstrating Desired Behaviors Post-Training / Total Number of Sales Reps) * 100",
    "calculation_formula": "(Number of Sales Reps Demonstrating Desired Behaviors Post-Training / Total Number of Sales Reps) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "kpi_definition": "The extent to which sales reps alter their sales techniques and behaviors after training.",
    "expected_business_insights": "Provides insight into the effectiveness of training in changing sales behaviors to align with best practices.",
    "measurement_approach": "Measures the degree to which sales reps alter their sales behaviors and strategies following training.",
    "trend_analysis": """
    * Increasing behavioral change post-training may indicate effective training programs and coaching methods.
    * Decreasing behavioral change post-training could signal a need for more targeted and impactful training content.
    """,
    "diagnostic_questions": """
    * Are there specific sales techniques or behaviors that sales reps struggle to adopt after training?
    * How do the post-training behavioral changes align with the desired sales outcomes and goals?
    """,
    "actionable_tips": """
    * Provide ongoing reinforcement and support for newly learned sales techniques through regular coaching and feedback.
    * Customize training content to address specific challenges or gaps in sales reps' adoption of new behaviors.
    """,
    "visualization_suggestions": """
    * Line charts showing the percentage of sales reps exhibiting behavioral changes over time.
    * Comparison bar charts illustrating the differences in sales techniques and behaviors before and after training.
    """,
    "risk_warnings": """
    * Low levels of behavioral change post-training may lead to stagnant sales performance and missed revenue targets.
    * Resistance to change among sales reps could indicate deeper cultural or organizational issues that hinder training effectiveness.
    """,
    "tracking_tools": """
    * CRM systems with performance tracking capabilities to monitor and analyze the adoption of new sales techniques.
    * Sales enablement platforms to deliver targeted content and resources for reinforcing post-training behavioral changes.
    """,
    "integration_points": """
    * Integrate behavioral change data with performance management systems to align training efforts with sales goals and objectives.
    * Link post-training behavioral changes with customer relationship management to measure the impact on customer interactions and outcomes.
    """,
    "change_impact_analysis": """
    * Improving behavioral change post-training can lead to increased sales effectiveness and revenue generation.
    * However, resistance to change may impact team dynamics and overall sales culture, requiring careful change management strategies.
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Demo", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"]},
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
}
