"""
Training Feedback Responsiveness

The speed and quality of how sales training providers respond to and act on trainee feedback.
"""

TRAINING_FEEDBACK_RESPONSIVENESS = {
    "code": "TRAINING_FEEDBACK_RESPONSIVENESS",
    "name": "Training Feedback Responsiveness",
    "description": "The speed and quality of how sales training providers respond to and act on trainee feedback.",
    "formula": "Time Taken to Implement Changes Post-Feedback",
    "calculation_formula": "Time Taken to Implement Changes Post-Feedback",
    "category": "Sales Training and Coaching",
    "is_active": True,
    "full_kpi_definition": "Complete definition for Training Feedback Responsiveness to be added.",
    "trend_analysis": """



    * Increased responsiveness to training feedback may indicate a positive shift in the quality of sales training being provided.
    * Decreasing responsiveness could signal a decline in the effectiveness of the sales training program or a lack of attention to trainee feedback.
    
    
    
    """,
    "diagnostic_questions": """



    * Are there specific areas of the sales training program where feedback responsiveness is consistently low?
    * How do trainees perceive the impact of their feedback on the training content and delivery?
    
    
    
    """,
    "actionable_tips": """



    * Implement regular feedback collection mechanisms to ensure timely and comprehensive responses to trainee input.
    * Train sales managers and trainers on how to effectively analyze and act on feedback to continuously improve the training program.
    * Encourage open communication channels between trainees and training providers to address feedback in real-time.
    
    
    
    """,
    "visualization_suggestions": """



    * Line charts showing the trend of responsiveness over time.
    * Comparison bar charts to highlight differences in responsiveness across different training modules or providers.
    
    
    
    """,
    "risk_warnings": """



    * Poor responsiveness to feedback can lead to disengagement and reduced effectiveness of the sales training program.
    * Consistently low responsiveness may indicate a systemic issue in the training provider's ability to adapt and improve.
    
    
    
    """,
    "tracking_tools": """



    * Feedback management software to streamline the collection, analysis, and response to trainee feedback.
    * Training evaluation platforms that provide insights into the impact of feedback on training outcomes.
    
    
    
    """,
    "integration_points": """



    * Integrate feedback responsiveness data with sales performance metrics to understand the correlation between training improvements and sales results.
    * Link feedback responsiveness with employee development systems to identify training needs and opportunities for individual improvement.
    
    
    
    """,
    "change_impact_analysis": """



    * Improving feedback responsiveness can lead to a more engaged and skilled sales team, positively impacting overall sales performance.
    * On the other hand, a decline in responsiveness may result in decreased employee satisfaction and retention.
    
    
    
    """,
    "metadata_": {"modules": ["SALES_TRAINING_COACHING"], "source": "kpidepot.com", "import_date": "2025-11-07", "required_objects": ["Customer Feedback", "Deal", "Enablement Feedback", "Lead", "Opportunity", "Partner Training", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Training Program"], "last_validated": "2025-11-10T13:49:33.740174"},
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
                        420.24,
                        355.35,
                        318.09,
                        330.14,
                        307.79,
                        350.86,
                        337.99,
                        391.07,
                        371.64,
                        306.26,
                        419.69,
                        390.2
                ],
                "unit": "units"
        },
        "current": {
                "value": 390.2,
                "unit": "units",
                "change": -29.49,
                "change_percent": -7.0,
                "trend": "stable"
        },
        "statistics": {
                "average": 358.28,
                "min": 306.26,
                "max": 420.24,
                "unit": "units"
        },
        "breakdown": [
                {
                        "category": "Segment A",
                        "value": 85.24,
                        "percentage": 21.8
                },
                {
                        "category": "Segment B",
                        "value": 98.14,
                        "percentage": 25.2
                },
                {
                        "category": "Segment C",
                        "value": 49.66,
                        "percentage": 12.7
                },
                {
                        "category": "Segment D",
                        "value": 42.19,
                        "percentage": 10.8
                },
                {
                        "category": "Other",
                        "value": 114.97,
                        "percentage": 29.5
                }
        ],
        "metadata": {
                "generated_date": "2025-11-10T13:51:13.847043",
                "data_points": 12,
                "kpi_type": "metric",
                "kpi_name": "Training Feedback Responsiveness"
        }
    },
}
