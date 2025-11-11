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
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Demo", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.666238"},
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
                        57.97,
                        55.1,
                        54.1,
                        56.04,
                        63.29,
                        49.7,
                        46.79,
                        62.91,
                        63.03,
                        57.87,
                        49.11,
                        58.26
                ],
                "unit": "%"
        },
        "current": {
                "value": 58.26,
                "unit": "%",
                "change": 9.15,
                "change_percent": 18.6,
                "trend": "stable"
        },
        "statistics": {
                "average": 56.18,
                "min": 46.79,
                "max": 63.29,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 16.2,
                        "percentage": 27.8
                },
                {
                        "category": "Channel Sales",
                        "value": 7.9,
                        "percentage": 13.6
                },
                {
                        "category": "Online Sales",
                        "value": 5.99,
                        "percentage": 10.3
                },
                {
                        "category": "Enterprise Sales",
                        "value": 3.7,
                        "percentage": 6.4
                },
                {
                        "category": "Other",
                        "value": 24.47,
                        "percentage": 42.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.408205",
                "data_points": 12,
                "kpi_type": "count",
                "kpi_name": "Behavioral Change Post-Training"
        }
    },
}
