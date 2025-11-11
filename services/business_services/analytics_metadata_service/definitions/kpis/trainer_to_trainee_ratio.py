"""
Trainer-to-Trainee Ratio

The ratio of trainers to trainees, affecting the quality and attention given during training.
"""

TRAINER_TO_TRAINEE_RATIO = {
    "code": "TRAINER_TO_TRAINEE_RATIO",
    "name": "Trainer-to-Trainee Ratio",
    "description": "The ratio of trainers to trainees, affecting the quality and attention given during training.",
    "formula": "Number of Trainers / Number of Trainees",
    "calculation_formula": "Number of Trainers / Number of Trainees",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Trainer-to-Trainee Ratio to be added.",
    "trend_analysis": """



    * An increasing trainer-to-trainee ratio may indicate a lack of resources or a growing demand for training.
    * A decreasing ratio could suggest improved resource allocation or a decline in training needs.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas or departments with consistently higher trainer-to-trainee ratios?
    * How does our current trainer-to-trainee ratio compare with industry standards or best practices?
    
    
    
    """,
    "actionable_tips": """



    * Invest in additional trainers or coaching resources to maintain a balanced ratio.
    * Implement technology-enabled training solutions to scale coaching efforts without significantly increasing the trainer-to-trainee ratio.
    * Regularly assess and adjust the ratio based on changing training needs and organizational growth.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the historical trend of trainer-to-trainee ratios over time.
    * Stacked bar graphs comparing trainer-to-trainee ratios across different departments or teams.
    
    
    
    """,
    "risk_warnings": """



    * A high trainer-to-trainee ratio may lead to decreased training effectiveness and individual attention.
    * A low ratio could indicate underutilization of training resources and potential inefficiencies.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) with reporting capabilities to track and analyze training resource allocation.
    * Coaching and mentoring software to facilitate virtual or remote coaching sessions, optimizing the trainer-to-trainee ratio.
    
    
    
    """,
    "integration_points": """



    * Integrate trainer-to-trainee ratio data with performance management systems to correlate training effectiveness with business outcomes.
    * Link coaching and training data with HR systems to align resource allocation with employee development plans and career paths.
    
    
    
    """,
    "change_impact_analysis": """



    * Changes in the trainer-to-trainee ratio can impact the overall skill development and performance of the workforce.
    * Optimizing the ratio may lead to improved sales performance, customer satisfaction, and employee retention.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Partner Training", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"], "last_validated": "2025-11-10T13:49:33.729950"},
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
                        61.71,
                        63.01,
                        67.7,
                        64.98,
                        63.6,
                        79.83,
                        72.79,
                        70.4,
                        64.28,
                        72.23,
                        74.38,
                        70.64
                ],
                "unit": "%"
        },
        "current": {
                "value": 70.64,
                "unit": "%",
                "change": -3.74,
                "change_percent": -5.0,
                "trend": "increasing"
        },
        "statistics": {
                "average": 68.8,
                "min": 61.71,
                "max": 79.83,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 12.46,
                        "percentage": 17.6
                },
                {
                        "category": "Segment B",
                        "value": 16.59,
                        "percentage": 23.5
                },
                {
                        "category": "Segment C",
                        "value": 7.69,
                        "percentage": 10.9
                },
                {
                        "category": "Segment D",
                        "value": 4.34,
                        "percentage": 6.1
                },
                {
                        "category": "Other",
                        "value": 29.56,
                        "percentage": 41.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.817131",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Trainer-to-Trainee Ratio"
        }
    },
}
