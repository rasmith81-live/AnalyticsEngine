"""
Behavioral Change Post-Training

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
    "full_kpi_definition": "Complete definition for Behavioral Change Post-Training to be added.",
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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Demo", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:43:23.058404"},
    "required_objects": [],
    "modules": ["SALES_TRAINING_COACHING"],
    "module_code": "SALES_TRAINING_COACHING",
    "sample_data": {
        "time_series": {
                "dates": [
                        "2024-12-15",
                        "2025-01-14",
                        "2025-02-13",
                        "2025-03-15",
                        "2025-04-14",
                        "2025-05-14",
                        "2025-06-13",
                        "2025-07-13",
                        "2025-08-12",
                        "2025-09-11",
                        "2025-10-11",
                        "2025-11-10"
                ],
                "values": [
                        393,
                        393,
                        356,
                        352,
                        393,
                        389,
                        363,
                        378,
                        367,
                        383,
                        359,
                        356
                ],
                "unit": "count"
        },
        "current": {
                "value": 356,
                "unit": "count",
                "change": -3,
                "change_percent": -0.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 373.5,
                "min": 352,
                "max": 393,
                "unit": "count"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 61.68,
                        "percentage": 17.3
                },
                {
                        "category": "Category B",
                        "value": 88.0,
                        "percentage": 24.7
                },
                {
                        "category": "Category C",
                        "value": 32.28,
                        "percentage": 9.1
                },
                {
                        "category": "Category D",
                        "value": 24.57,
                        "percentage": 6.9
                },
                {
                        "category": "Other",
                        "value": 149.47,
                        "percentage": 42.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:23.058404",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Behavioral Change Post-Training"
        }
    },
}
