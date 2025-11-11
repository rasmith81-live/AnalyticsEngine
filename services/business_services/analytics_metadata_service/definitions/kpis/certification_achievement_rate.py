"""
Certification Achievement Rate

The proportion of sales reps who achieve certification if applicable, through the training program.
"""

CERTIFICATION_ACHIEVEMENT_RATE = {
    "code": "CERTIFICATION_ACHIEVEMENT_RATE",
    "name": "Certification Achievement Rate",
    "description": "The proportion of sales reps who achieve certification if applicable, through the training program.",
    "formula": "(Number of Sales Reps Achieving Certification / Number of Sales Reps Enrolled in the Certification Program) * 100",
    "calculation_formula": "(Number of Sales Reps Achieving Certification / Number of Sales Reps Enrolled in the Certification Program) * 100",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Certification Achievement Rate to be added.",
    "trend_analysis": """



    * An increasing certification achievement rate may indicate the effectiveness of the training program in preparing sales reps.
    * A decreasing rate could signal a need for program adjustments or changes in the sales team composition.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas of the training program where sales reps struggle to achieve certification?
    * How does the certification achievement rate compare with industry benchmarks or with different cohorts of sales reps?
    
    
    
    """,
    "actionable_tips": """



    * Provide additional support and resources for sales reps who are struggling to achieve certification.
    * Regularly review and update the training program to ensure it aligns with the evolving needs and challenges of the sales team.
    * Implement mentorship or coaching programs to help sales reps prepare for certification.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the certification achievement rate over time.
    * Comparison bar charts to visualize the differences in certification achievement among different groups of sales reps.
    
    
    
    """,
    "risk_warnings": """



    * A consistently low certification achievement rate may indicate a need for a more comprehensive review of the training program.
    * High variability in certification achievement rates among different sales reps may point to inconsistencies in the training or coaching process.
    
    
    
    """,
    "tracking_tools": """



    * Learning management systems (LMS) to track and manage sales reps' progress in the training program.
    * Coaching and feedback tools to provide personalized support for sales reps aiming for certification.
    
    
    
    """,
    "integration_points": """



    * Integrate certification achievement data with performance management systems to identify correlations between certification and sales success.
    * Link certification achievement with individual development plans to ensure ongoing improvement and career growth for sales reps.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving the certification achievement rate can lead to a more skilled and knowledgeable sales force, potentially increasing overall sales performance.
    * Conversely, a declining certification achievement rate may lead to decreased confidence and motivation among the sales team.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Certification", "Customer Advocacy Program", "Loyalty Program", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:32.679042"},
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
                        63.6,
                        76.27,
                        75.51,
                        58.72,
                        74.27,
                        63.94,
                        66.64,
                        69.53,
                        64.83,
                        74.81,
                        67.93,
                        68.46
                ],
                "unit": "%"
        },
        "current": {
                "value": 68.46,
                "unit": "%",
                "change": 0.53,
                "change_percent": 0.8,
                "trend": "stable"
        },
        "statistics": {
                "average": 68.71,
                "min": 58.72,
                "max": 76.27,
                "unit": "%"
        },
        "breakdown": [
                {
                        "category": "Direct Sales",
                        "value": 20.84,
                        "percentage": 30.4
                },
                {
                        "category": "Channel Sales",
                        "value": 16.21,
                        "percentage": 23.7
                },
                {
                        "category": "Online Sales",
                        "value": 6.9,
                        "percentage": 10.1
                },
                {
                        "category": "Enterprise Sales",
                        "value": 4.65,
                        "percentage": 6.8
                },
                {
                        "category": "Other",
                        "value": 19.86,
                        "percentage": 29.0
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:11.431307",
                "data_points": 12,
                "kpi_type": "percentage",
                "kpi_name": "Certification Achievement Rate"
        }
    },
}
