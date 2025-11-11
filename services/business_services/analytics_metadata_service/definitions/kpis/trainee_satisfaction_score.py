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
                        84.0,
                        86.0,
                        81.8,
                        90.4,
                        89.8,
                        83.8,
                        89.1,
                        84.5,
                        89.0,
                        80.2,
                        85.8,
                        81.6
                ],
                "unit": "score"
        },
        "current": {
                "value": 81.6,
                "unit": "score",
                "change": -4.2,
                "change_percent": -4.9,
                "trend": "stable"
        },
        "statistics": {
                "average": 85.5,
                "min": 80.2,
                "max": 90.4,
                "unit": "score"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 14.03,
                        "percentage": 17.2
                },
                {
                        "category": "Segment B",
                        "value": 21.01,
                        "percentage": 25.7
                },
                {
                        "category": "Segment C",
                        "value": 11.08,
                        "percentage": 13.6
                },
                {
                        "category": "Segment D",
                        "value": 10.46,
                        "percentage": 12.8
                },
                {
                        "category": "Other",
                        "value": 25.02,
                        "percentage": 30.7
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.811919",
                "data_points": 12,
                "kpi_type": "score",
                "kpi_name": "Trainee Satisfaction Score"
        }
    },
}
