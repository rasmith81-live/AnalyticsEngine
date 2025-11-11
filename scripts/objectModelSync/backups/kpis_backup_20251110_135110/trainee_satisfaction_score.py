"""
Trainee Satisfaction Score

A metric that assesses the satisfaction level of sales trainees with the training program.
"""

TRAINEE_SATISFACTION_SCORE = {
    "code": "TRAINEE_SATISFACTION_SCORE",
    "name": "Trainee Satisfaction Score",
    "description": "A metric that assesses the satisfaction level of sales trainees with the training program.",
    "formula": "Average of Satisfaction Scores Collected from Training Participants",
    "calculation_formula": "Average of Satisfaction Scores Collected from Training Participants",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Trainee Satisfaction Score to be added.",
    "trend_analysis": """


    * Trainee satisfaction scores may show an initial increase as new training methods or materials are introduced, followed by a plateau or decline as the novelty wears off.
    * Long-term trends may reveal fluctuations based on changes in sales management, leadership, or company culture.
    
    
    """,
    "diagnostic_questions": """


    * What specific aspects of the training program are contributing to high or low satisfaction scores?
    * How do trainee satisfaction scores correlate with sales performance or retention rates?
    
    
    """,
    "actionable_tips": """


    * Regularly gather feedback from trainees to identify areas for improvement in the training program.
    * Implement mentorship or coaching programs to provide ongoing support and guidance to sales trainees.
    * Customize training materials and methods to better align with the learning styles and preferences of the trainees.
    
    
    """,
    "visualization_suggestions": """


    * Line charts to track changes in satisfaction scores over time.
    * Comparative bar charts to analyze satisfaction scores across different training modules or instructors.
    
    
    """,
    "risk_warnings": """


    * Consistently low satisfaction scores may lead to decreased motivation and performance among sales trainees.
    * High variability in satisfaction scores could indicate inconsistency in the quality of training delivery.
    
    
    """,
    "tracking_tools": """


    * Survey and feedback tools to collect and analyze trainee satisfaction data.
    * Learning management systems (LMS) to track trainee progress and engagement with training materials.
    
    
    """,
    "integration_points": """


    * Integrate trainee satisfaction scores with performance management systems to identify correlations between satisfaction and sales results.
    * Link satisfaction scores with individual coaching or development plans to address specific areas of improvement.
    
    
    """,
    "change_impact_analysis": """


    * Improving trainee satisfaction scores can lead to higher engagement, retention, and ultimately, better sales performance.
    * However, focusing solely on satisfaction scores without considering sales outcomes may lead to a disconnect between training effectiveness and business results.
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Advocacy Program", "Loyalty Program", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Service Level Agreement", "Training Program"], "last_validated": "2025-11-10T13:49:33.728268"},
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
                        86.5,
                        76.7,
                        86.9,
                        80.1,
                        82.7,
                        79.1,
                        85.1,
                        77.4,
                        81.2,
                        81.5,
                        80.3,
                        84.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 84.6,
                "unit": "score",
                "change": 4.3,
                "change_percent": 5.4,
                "trend": "stable"
        },
        "statistics": {
                "average": 81.84,
                "min": 76.7,
                "max": 86.9,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Category A",
                        "value": 17.64,
                        "percentage": 20.9
                },
                {
                        "category": "Category B",
                        "value": 10.86,
                        "percentage": 12.8
                },
                {
                        "category": "Category C",
                        "value": 10.78,
                        "percentage": 12.7
                },
                {
                        "category": "Category D",
                        "value": 11.64,
                        "percentage": 13.8
                },
                {
                        "category": "Other",
                        "value": 33.68,
                        "percentage": 39.8
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:43:25.075293",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Trainee Satisfaction Score"
        }
    },
}
