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
                        79.67,
                        64.47,
                        61.52,
                        78.75,
                        64.6,
                        61.98,
                        75.3,
                        67.18,
                        64.23,
                        66.17,
                        79.28,
                        64.7
                ],
                "unit": "%"
        },
        "current": {
                "value": 64.7,
                "unit": "%",
                "change": -14.58,
                "change_percent": -18.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.99,
                "min": 61.52,
                "max": 79.67,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 20.81,
                        "percentage": 32.2
                },
                {
                        "category": "Category B",
                        "value": 7.99,
                        "percentage": 12.3
                },
                {
                        "category": "Category C",
                        "value": 10.49,
                        "percentage": 16.2
                },
                {
                        "category": "Category D",
                        "value": 2.96,
                        "percentage": 4.6
                },
                {
                        "category": "Other",
                        "value": 22.45,
                        "percentage": 34.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.081287",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Trainer-to-Trainee Ratio"
        }
    },
}
